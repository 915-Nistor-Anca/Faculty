using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Threading;

namespace Lab4
{
    public class SocketInformation
    {
        public Socket socket = null;
        public const int size_of_buffer = 512;
        public byte[] receive_buffer = new byte[size_of_buffer];
        public StringBuilder response_content = new StringBuilder();
        public IPEndPoint remote_end_point;
        public ManualResetEvent connect_done = new ManualResetEvent(false);
        public ManualResetEvent send_done = new ManualResetEvent(false);
        public ManualResetEvent receive_done = new ManualResetEvent(false);
        public int client_id;
        public string host_name;
        public string endpoint_path;
    }
}
