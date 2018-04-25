using System;
using Newtonsoft.Json;
namespace FontEnd {
    //abstract class Message {
    //    protected String header;
    //    protected String content;
    //    protected String extraInfo;
    //    protected bool illegal;

    //    public Message() {
    //    }
    //    public Message(String _h, String _c, String _e) {
    //        header = _h;
    //        content = _c;
    //        extraInfo = _e;
    //    }
    //    public Message(String _h, String _c) {
    //        header = _h;
    //        content = _c;
    //        extraInfo = "";
    //    }
    //    public Message(String _r) {
    //        String[] tmp_c = _r.Split(new char[] { ':' });
    //        this.header = tmp_c[0];
    //        this.content = tmp_c[1];
    //        this.extraInfo = tmp_c[2];
    //    }

    //    public Message(bool _h, String _c, String _e) {
    //        if (_h) {
    //            header = "True";
    //        } else {
    //            header = "False";
    //        }
    //        content = _c;
    //        extraInfo = _e;
    //    }
    //    public string Header {
    //        get => header;
    //        set {
    //            header = value;
    //            foreach (String tmp_str in MessageList.messageName) {
    //                if (tmp_str == header) {
    //                    illegal = true;
    //                    break;
    //                }
    //            }
    //        }
    //    }
    //    public String Content {
    //        get => content;
    //        set => content = value;
    //    }
    //    public string ExtraInfo {
    //        get => extraInfo;
    //        set => extraInfo = value;
    //    }
    //    public bool Illegal {
    //        get => illegal;
    //    }

    //    public String getMessage() {
    //        return this.header + ":" + this.content + ":" + this.extraInfo;
    //    }
    //}
    //class Request : Message {
    //    public Request() : base() {

    //    }
    //    public Request(String _h, String _c, String _e) : base(_h, _c, _e) {
    //        illegal = false;
    //        foreach (String tmp_str in MessageList.messageName) {
    //            if (tmp_str == header) {
    //                illegal = true;
    //                break;
    //            }
    //        }
    //    }
    //    public Request(String _h, String _c) : base(_h, _c) {
    //        illegal = false;
    //        foreach (String tmp_str in MessageList.messageName) {
    //            if (tmp_str == header) {
    //                illegal = true;
    //                break;
    //            }
    //        }
    //    }

    //    public Request(String _c) : base(_c) {
    //        illegal = false;
    //        foreach (String tmp_str in MessageList.messageName) {
    //            if (tmp_str == header) {
    //                illegal = true;
    //                break;
    //            }
    //        }
    //    }
    //}
    //class Reply : Message {
    //    public Reply() : base() {

    //    }
    //    public Reply(String _h, String _c, String _e) : base(_h, _c, _e) {
    //        if (_h == "True" || _h == "False") {
    //            this.illegal = true;
    //        } else {
    //            this.illegal = false;
    //        }
    //    }
    //    public Reply(String _c) : base(_c) {
    //        if (this.Header == "True" || this.Header == "False") {
    //            this.illegal = true;
    //        } else {
    //            this.illegal = false;
    //        }
    //    }



    //}
    class MessageList {
        public const String Login = "login";
        public const String Logout = "logout";
        public const String Register = "register";
        public static String[] messageName = { Login, Logout, Register };
    }

    abstract class RequestInfo {
        protected String type;
        protected String extraInfo;
        public RequestInfo() {

        }
        public RequestInfo(String _type) {
            type = _type;
            extraInfo = "";
        }

        public string ExtraInfo { get => extraInfo; set => extraInfo = value; }
        public string Type { get => type; }
        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }
    class LoginReq : RequestInfo {
        private String userName;
        private String userPwd;
        public LoginReq() : base() {
            type = MessageList.Login;
        }
        public LoginReq(String _jsonS) {
            LoginReq tmp_l = JsonConvert.DeserializeObject<LoginReq>(_jsonS);
            type = MessageList.Login;
            userName = tmp_l.UserName;
            userPwd = tmp_l.UserPwd;
        }
        public LoginReq(String _n, String _p) : base(MessageList.Login) {
            userName = _n;
            userPwd = _p;
        }
        public string UserName { get => userName; set => userName = value; }
        public string UserPwd { get => userPwd; set => userPwd = value; }

    }
    class LogoutReq : RequestInfo {
        String loginID;
        public LogoutReq() {
            type = MessageList.Logout;
        }
        public LogoutReq(String _id) : base(MessageList.Logout) {
            loginID = _id;
        }
        public string LoginID { get => loginID; set => loginID = value; }
    }
    class RegisterReq : RequestInfo {
        String userName;
        String userPwd;
        public RegisterReq() {
            type = MessageList.Register;
        }
        public RegisterReq(String _n, String _p) : base(MessageList.Register) {
            UserName = _n;
            UserPwd = _p;
        }

        public string UserName { get => userName; set => userName = value; }
        public string UserPwd { get => userPwd; set => userPwd = value; }
    }

    abstract class ReplyInfo {
        private Boolean isSuccessful;
        private String extraInfo;
        public ReplyInfo() {
        }
        public ReplyInfo(Boolean _b,String _e) {
            isSuccessful = _b;
            extraInfo = _e;
        }
        public bool IsSuccessful { get => isSuccessful; set => isSuccessful = value; }
        public String ExtraInfo { get => extraInfo; set => extraInfo = value; }
        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }
    class LoginRep: ReplyInfo {
        private String loginID;
        public LoginRep():base() {

        }
        public LoginRep(Boolean _b, String _e="") : base(_b, _e) {
            LoginID = "";
        }
        public LoginRep(String _jsonS) {
            LoginRep tmp_l = JsonConvert.DeserializeObject<LoginRep>(_jsonS);
            IsSuccessful = tmp_l.IsSuccessful;
            LoginID = tmp_l.LoginID;
            ExtraInfo = tmp_l.ExtraInfo;
        }
        public String LoginID { get => loginID; set => loginID = value; }
    }
    class LogoutRep : ReplyInfo {
        public LogoutRep() : base() {

        }
        public LogoutRep(Boolean _b, String _e) : base(_b, _e) {

        }
        public LogoutRep(String _jsonS) {
            LogoutRep tmp_l = JsonConvert.DeserializeObject<LogoutRep>(_jsonS);
            IsSuccessful = tmp_l.IsSuccessful;
            ExtraInfo = tmp_l.ExtraInfo;
        }
    }
    class RegisterRep : ReplyInfo {
        public RegisterRep() : base() {

        }
        public RegisterRep(Boolean _b,String _e) : base(_b, _e) {

        }
        public RegisterRep(String _jsonS) {
            RegisterRep tmp_l = JsonConvert.DeserializeObject<RegisterRep>(_jsonS);
            IsSuccessful = tmp_l.IsSuccessful;
            ExtraInfo = tmp_l.ExtraInfo;
        }
    }
}