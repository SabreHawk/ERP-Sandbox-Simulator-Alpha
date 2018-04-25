using System;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;

namespace FontEnd {
    class RequestManager {
        private NetworkCommunication refNetworkCommunication;
        public RequestManager(ref NetworkCommunication _nc) {
            refNetworkCommunication = _nc;
        }
        public LoginRep RequestLogin(LoginReq _i) {
            try {
                String tmp_s = refNetworkCommunication.RequestService(_i.JsonSerialization());
                return new LoginRep(tmp_s);
            } catch (Exception e) {
                Console.WriteLine("Exception : " + e);
                return new LoginRep(false,"Exception");
            }
        }

        public LogoutRep RequestLogout(LogoutReq _i) {
            try {
                return new LogoutRep(refNetworkCommunication.RequestService(_i.JsonSerialization()));
            } catch (Exception e) {
                Console.WriteLine("Exception : " + e);
                return new LogoutRep(false, "Exception");
            }
        }

        public RegisterRep RequestRegister(RegisterReq _i) {
            try {
                String EmailPattern = @"^([A-Za-z0-9]{1}[A-Za-z0-9_]*)@([A-Za-z0-9_]+)[.]([A-Za-z0-9_]*)$";
                if (Regex.IsMatch(_i.UserName.Trim(), EmailPattern)) {
                    return new RegisterRep(refNetworkCommunication.RequestService(_i.JsonSerialization()));
                } else {
                    throw new Exception("ERROR Email Address");
                }
            } catch (Exception e) {
                Console.WriteLine("Exception : " + e);
                return new RegisterRep(false, "Exception");
            }
        }
    }
}
