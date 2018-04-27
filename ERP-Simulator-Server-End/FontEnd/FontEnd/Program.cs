using System;
using Newtonsoft.Json;

namespace FontEnd {
    class Program {
        static void Main(string[] args) {
            /*
            NetworkCommunication myNC = new NetworkCommunication("127.0.0.1", 8828);
            RequestManager rManager = new RequestManager(ref myNC);
            //Test RegisterReq & RegisterRep
            RegisterReq tmp_reg_q = new RegisterReq("myhawk@outlook.com", "123456");
            tmp_reg_q.ExtraInfo = "test Extra";
            RegisterRep tmp_reg_p = rManager.RequestRegister(tmp_reg_q);
            Console.WriteLine("#Test Register Function");
            Console.WriteLine(tmp_reg_q.JsonSerialization());
            Console.WriteLine(tmp_reg_q.Type);
            Console.WriteLine(tmp_reg_q.UserName);
            Console.WriteLine(tmp_reg_q.UserPwd);
            Console.WriteLine(tmp_reg_q.ExtraInfo);
            Console.WriteLine();
            Console.WriteLine(tmp_reg_p.JsonSerialization());
            Console.WriteLine(tmp_reg_p.IsSuccessful);
            Console.WriteLine(tmp_reg_p.ExtraInfo);
            //Test LoginReq & LoginRep
            LoginReq tmp_q = new LoginReq("myhawk@outlook.com", "123456");
            LoginRep tmp_p = rManager.RequestLogin(tmp_q);
            Console.WriteLine("#Test Login Function");
            Console.WriteLine(tmp_q.JsonSerialization());
            Console.WriteLine(tmp_q.Type);
            Console.WriteLine(tmp_q.UserName);
            Console.WriteLine(tmp_q.UserPwd);
            Console.WriteLine(tmp_q.ExtraInfo);
            Console.WriteLine();
            Console.WriteLine(tmp_p.JsonSerialization());
            Console.WriteLine(tmp_p.IsSuccessful);
            Console.WriteLine(tmp_p.LoginID);
            Console.WriteLine(tmp_p.ExtraInfo);

            //Test LogoutReq & LogoutRep
            LogoutReq tmp_o_q = new LogoutReq(tmp_p.LoginID);
            LogoutRep tmp_o_p = rManager.RequestLogout(tmp_o_q);
            Console.WriteLine("# Test LogoutReq & LougoutRep");
            Console.WriteLine(tmp_o_q.JsonSerialization());
            Console.WriteLine(tmp_o_q.Type);
            Console.WriteLine(tmp_o_q.LoginID);
            Console.WriteLine(tmp_o_q.ExtraInfo);
            Console.WriteLine();
            Console.WriteLine(tmp_o_p.JsonSerialization());
            Console.WriteLine(tmp_o_p.IsSuccessful);
            Console.WriteLine(tmp_o_p.ExtraInfo);
            Console.ReadKey();
            */

            GameInfo tmpGameInfo = new GameInfo("newGame", new GameDate(2018, 4, 5, 19, 40), 4, true, "123", new GameDate(2018, 4, 3, 12, 40), new GameDate(2018, 4, 3, 12, 40));
            Console.WriteLine(tmpGameInfo.JsonSerialization());
            Console.ReadKey();
        }
    }
}
