using System;
using System.Collections.Generic;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using System.Text;
using System.Threading;

namespace FontEnd {
    
    class NetworkCommunication {
        IPAddress serverAddress;
        int serverPort;
        IPEndPoint serverEndPoint;
        public NetworkCommunication(String _ip, int _port) {
            serverPort = _port;
            serverAddress = IPAddress.Parse(_ip);
            serverEndPoint = new IPEndPoint(serverAddress, serverPort);
        }

        public String RequestService(String _r) {
            try {
                Socket clientRequestSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                clientRequestSocket.Connect(serverEndPoint);
                clientRequestSocket.Send(Encoding.UTF8.GetBytes(_r));
                byte[] buffer = new byte[1024 * 1024];
                int msgLen = clientRequestSocket.Receive(buffer);
                String recMsg = Encoding.UTF8.GetString(buffer, 0, msgLen);
                clientRequestSocket.Close();
                return recMsg;
            } catch (Exception e) {
                Console.WriteLine("Exception : " + e);
                return e.ToString();
            }

        }
        //public Reply SendRequest(Request _r) {
        //    RequestInfo tmp_rInfo = new RequestInfo(_r,serverEndPoint);
        //    Thread childThread = new Thread(new ThreadStart(tmp_rInfo.SendRequest));
        //    childThread.Start();
        //    childThread.Join();
        //    return tmp_rInfo.GetReply();
        //}
    }

    //class RequestInfo {
    //    private Request request;
    //    private IPEndPoint serverEndPoint;
    //    private Reply reply;
    //    public RequestInfo(Request _r,IPEndPoint _p) {
    //        request = _r;
    //        serverEndPoint = _p;
    //    }
    //    public void SetRequest(Request _r) {
    //        this.request = _r;
    //    }
    //    public void SendRequest() {
    //        Socket clientRequestSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
    //        clientRequestSocket.Connect(serverEndPoint);
    //        clientRequestSocket.Send(Encoding.UTF8.GetBytes(request.getMessage()));
    //        byte[] buffer = new byte[1024 * 1024];
    //        int msgLen = clientRequestSocket.Receive(buffer);
    //        String recMsg = Encoding.UTF8.GetString(buffer, 0, msgLen);
    //        clientRequestSocket.Close();
    //        reply = new Reply(recMsg);
    //    }

    //    public Reply GetReply() {
    //        return reply;
    //    }
    //}
}
