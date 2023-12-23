using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Lab4
{
    public class WrapOperationsInTaskImplementation
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

        private static void StartClient(string host, int id)
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

            Connect(socket_information).Wait();

            Send(socket_information, HttpHandler.GetRequestString(socket_information.host_name, socket_information.endpoint_path)).Wait();

            Receive(socket_information).Wait();

            Console.WriteLine(socket_information.response_content);

            client.Shutdown(SocketShutdown.Both);
            client.Close();
        }

        private static Task Connect(SocketInformation socket_information)
        {
            socket_information.socket.BeginConnect(socket_information.remote_end_point, ConnectCallback, socket_information);
            return Task.FromResult(socket_information.connect_done.WaitOne());
        }

        private static void ConnectCallback(IAsyncResult ar)
        {
            var socket_information = (SocketInformation)ar.AsyncState;
            var clientSocket = socket_information.socket;
            var clientId = socket_information.client_id;
            var hostname = socket_information.host_name;

            clientSocket.EndConnect(ar);

            Console.WriteLine("{0}) Socket connected to {1} ({2})", clientId, hostname, clientSocket.RemoteEndPoint);

            socket_information.connect_done.Set();
        }

        private static Task Send(SocketInformation socket_information, string data)
        {
            var byteData = Encoding.ASCII.GetBytes(data);

            socket_information.socket.BeginSend(byteData, 0, byteData.Length, 0, SendCallback, socket_information);

            return Task.FromResult(socket_information.send_done.WaitOne());
        }

        private static void SendCallback(IAsyncResult ar)
        {
            var socket_information = (SocketInformation)ar.AsyncState;
            var clientSocket = socket_information.socket;
            var clientId = socket_information.client_id;

            var bytesSent = clientSocket.EndSend(ar);
            Console.WriteLine("{0}) Sent {1} bytes to server.", clientId, bytesSent);

            socket_information.send_done.Set();
        }

        private static Task Receive(SocketInformation socket_information)
        {
            socket_information.socket.BeginReceive(socket_information.receive_buffer, 0, SocketInformation.size_of_buffer, 0, ReceiveCallback, socket_information);

            return Task.FromResult(socket_information.receive_done.WaitOne());
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
