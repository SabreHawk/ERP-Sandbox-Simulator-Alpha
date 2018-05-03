using System;
using Newtonsoft.Json;
namespace FontEnd {
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

    abstract class ReplyInfo {
        private Boolean isSuccessful;
        private String extraInfo;
        public ReplyInfo() {
        }
        public ReplyInfo(Boolean _b, String _e) {
            isSuccessful = _b;
            extraInfo = _e;
        }
        public bool IsSuccessful { get => isSuccessful; set => isSuccessful = value; }
        public String ExtraInfo { get => extraInfo; set => extraInfo = value; }
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

    class LoginRep : ReplyInfo {
        private String loginID;
        public LoginRep() : base() {

        }
        public LoginRep(Boolean _b, String _e = "") : base(_b, _e) {
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

    class RegisterRep : ReplyInfo {
        public RegisterRep() : base() {

        }
        public RegisterRep(Boolean _b, String _e) : base(_b, _e) {

        }
        public RegisterRep(String _jsonS) {
            RegisterRep tmp_l = JsonConvert.DeserializeObject<RegisterRep>(_jsonS);
            IsSuccessful = tmp_l.IsSuccessful;
            ExtraInfo = tmp_l.ExtraInfo;
        }
    }
    class CreateGameReq : RequestInfo {
        String gameName;
        GameInfo gameInfo;
        GameRule gameRule;
        public CreateGameReq() : base() {

        }
        public CreateGameReq(String _game_name, GameInfo _gInfo, GameRule _gRule) {
            GameName = _game_name;
            GameInfo = _gInfo;
            GameRule = _gRule;
        }

        public GameInfo GameInfo { get => gameInfo; set => gameInfo = value; }
        public GameRule GameRule { get => gameRule; set => gameRule = value; }
        public string GameName { get => gameName; set => gameName = value; }
    }

    class CreateGameRep : ReplyInfo {
        String gameID;

        public CreateGameRep() : base() {

        }
        public CreateGameRep(bool _b, String _e) : base(_b, _e) {

        }
        public CreateGameRep(String _jsonS) {
            CreateGameRep tmp_p = JsonConvert.DeserializeObject<CreateGameRep>(_jsonS);
            IsSuccessful = tmp_p.IsSuccessful;
            GameID = tmp_p.GameID;
            ExtraInfo = tmp_p.ExtraInfo;
        }
        public string GameID { get => gameID; set => gameID = value; }
    }
    
   
   
 
}