using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Lab4
{
    public class AsyncAwaitMechanismImplementation
    {
        private static List<string> hosts;
        private static List<Task> tasks;

        public static void Run(List<string> hostnames)
        {
            hosts = hostnames;
            tasks = new List<Task>();
            for (var i = 0; i < hosts.Count; i++)
            {
                tasks.Add(Task.Factory.StartNew(InitiateConnection, i));
            }
            Task.WaitAll(tasks.ToArray());
        }

        private static void InitiateConnection(object idObject)
        {
            var id = (int)idObject;
            StartClient(hosts[id], id);
        }

        private static async void StartClient(string host, int id)
        {
            var ipHostInfo = Dns.GetHostEntry(host.Split('/')[0]);
            var ipAddress = ipHostInfo.AddressList[0];
            var remoteEndpoint = new IPEndPoint(ipAddress, HttpHandler.http_port);

            var client = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            var socket_information = new SocketInformation
            {
                socket = client,
                host_name = host.Split('/')[0],
                endpoint_path = host.Contains("/") ? host.Substring(host.IndexOf("/")) : "/",
                remote_end_point = remoteEndpoint,
                client_id = id
            };

            await Connect(socket_information);

            
            await Send(socket_information, HttpHandler.GetRequestString(socket_information.host_name, socket_information.endpoint_path));

            
            await Receive(socket_information);

            Console.WriteLine(socket_information.response_content);

            client.Shutdown(SocketShutdown.Both);
            client.Close();
        }

        private static async Task Connect(SocketInformation socket_information)
        {
            socket_information.socket.BeginConnect(socket_information.remote_end_point, ConnectCallback, socket_information);
            await Task.FromResult<object>(socket_information.connect_done.WaitOne());
        }

        private static void ConnectCallback(IAsyncResult ar)
        {
            var state = (SocketInformation)ar.AsyncState;
            var clientSocket = state.socket;
            var clientID = state.client_id;
            var hostname = state.host_name;

            clientSocket.EndConnect(ar);

            Console.WriteLine("{0}. Socket is connected to {1} ({2}).", clientID, hostname, clientSocket.RemoteEndPoint);

            state.connect_done.Set();
        }

        private static async Task Send(SocketInformation socketinfo, string data)
        {
            var byteData = Encoding.ASCII.GetBytes(data);

            socketinfo.socket.BeginSend(byteData, 0, byteData.Length, 0, SendCallback, socketinfo);
            await Task.FromResult<object>(socketinfo.send_done.WaitOne());
        }

        private static void SendCallback(IAsyncResult ar)
        {
            var state = (SocketInformation)ar.AsyncState;
            var clientSocket = state.socket;
            var clientID = state.client_id;

            var bytesSent = clientSocket.EndSend(ar);
            Console.WriteLine("{0}. Sent {1} bytes to the server.", clientID, bytesSent);

            state.send_done.Set();
        }

        private static async Task Receive(SocketInformation socket_information)
        {
            socket_information.socket.BeginReceive(socket_information.receive_buffer, 0, SocketInformation.size_of_buffer, 0, ReceiveCallback, socket_information);
            await Task.FromResult<object>(socket_information.receive_done.WaitOne());
        }

        private static void ReceiveCallback(IAsyncResult ar)
        {
            var socket_information = (SocketInformation)ar.AsyncState;
            var clientSocket = socket_information.socket;

            try
            {
                var bytesRead = clientSocket.EndReceive(ar);

                socket_information.response_content.Append(Encoding.ASCII.GetString(socket_information.receive_buffer, 0, bytesRead));

                if (!HttpHandler.ResponseHeaderFullyObtained(socket_information.response_content.ToString()))
                {
                    clientSocket.BeginReceive(socket_information.receive_buffer, 0, SocketInformation.size_of_buffer, 0, ReceiveCallback, socket_information);
                }
                else
                {
                    var responseBody = HttpHandler.GetResponseBody(socket_information.response_content.ToString());

                    if (responseBody.Length < HttpHandler.GetContentLength(socket_information.response_content.ToString()))
                    {
                        clientSocket.BeginReceive(socket_information.receive_buffer, 0, SocketInformation.size_of_buffer, 0, ReceiveCallback, socket_information);
                    }
                    else
                    {
                        socket_information.receive_done.Set();
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    }
}
