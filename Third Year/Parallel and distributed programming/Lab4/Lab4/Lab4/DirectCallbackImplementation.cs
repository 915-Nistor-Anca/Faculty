using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading;

namespace Lab4
{
    public class DirectCallbackImplementation
    {
        private static List<string> hosts;

        public static void Run(List<string> hostnames)
        {
            hosts = hostnames;
            for (var i = 0; i < hosts.Count; i++) InitiateConnection(i);
        }

        private static void InitiateConnection(object idObject)
        {
            var id = (int)idObject;
            StartClient(hosts[id], id);
            Thread.Sleep(2000);
        }



        private static void StartClient(string host, int id)
        {
            var host_information = Dns.GetHostEntry(host.Split('/')[0]);
            var ip_address = host_information.AddressList[0];
            var remoteEndpoint = new IPEndPoint(ip_address, HttpHandler.http_port);
            var client = new Socket(ip_address.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            var socket_information = new SocketInformation
            {
                socket = client,
                host_name = host.Split('/')[0],
                endpoint_path = host.Contains("/") ? host.Substring(host.IndexOf("/")) : "/",
                remote_end_point = remoteEndpoint,
                client_id = id
            };

            socket_information.socket.BeginConnect(socket_information.remote_end_point, OnConnect, socket_information);
        }



        private static void OnConnect(IAsyncResult ar)
        {
            var socket_information = (SocketInformation)ar.AsyncState;
            var clientSocket = socket_information.socket;
            var clientID = socket_information.client_id;
            var hostname = socket_information.host_name;

            clientSocket.EndConnect(ar);
            Console.WriteLine("{0}. Socket is connected to {1} ({2}).", clientID, hostname, clientSocket.RemoteEndPoint);

            var byteData = Encoding.ASCII.GetBytes(HttpHandler.GetRequestString(socket_information.host_name, socket_information.endpoint_path));
            socket_information.socket.BeginSend(byteData, 0, byteData.Length, 0, OnSend, socket_information);
        }



        private static void OnSend(IAsyncResult ar)
        {
            var socket_information = (SocketInformation)ar.AsyncState;
            var clientSocket = socket_information.socket;
            var clientID = socket_information.client_id;

            var bytesSent = clientSocket.EndSend(ar);
            Console.WriteLine("{0}. Sent {1} bytes to server.", clientID, bytesSent);
            socket_information.socket.BeginReceive(socket_information.receive_buffer, 0, SocketInformation.size_of_buffer, 0, OnReceive, socket_information);
        }



        private static void OnReceive(IAsyncResult ar)
        {
            var socket_information = (SocketInformation)ar.AsyncState;
            var clientSocket = socket_information.socket;
            var clientID = socket_information.client_id;

            try
            {
                var bytesRead = clientSocket.EndReceive(ar);
                socket_information.response_content.Append(Encoding.ASCII.GetString(socket_information.receive_buffer, 0, bytesRead));

                if (!HttpHandler.ResponseHeaderFullyObtained(socket_information.response_content.ToString()))
                {
                    clientSocket.BeginReceive(socket_information.receive_buffer, 0, SocketInformation.size_of_buffer, 0, OnReceive, socket_information);
                }
                else
                {
                    var responseBody = HttpHandler.GetResponseBody(socket_information.response_content.ToString());
                    var contentLength = HttpHandler.GetContentLength(socket_information.response_content.ToString());
                    if (responseBody.Length < contentLength)
                    {
                        clientSocket.BeginReceive(socket_information.receive_buffer, 0, SocketInformation.size_of_buffer, 0, OnReceive, socket_information);
                    }
                    else
                    {
                        Console.WriteLine(socket_information.response_content);
                        clientSocket.Shutdown(SocketShutdown.Both);
                        clientSocket.Close();
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
