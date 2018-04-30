using Newtonsoft.Json;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace FontEnd {
    class User {
        String userAlias;
        String emailAddress;
        String loginID;

        public string UserAlias { get => userAlias; set => userAlias = value; }
        public string EmailAddress { get => emailAddress; set => emailAddress = value; }
        public string LoginID { get => loginID; set => loginID = value; }


    }
    class Team {
        String teamName;
        String leaderName;
        ArrayList memberList;

        public Team(String _teamName, String _teamLeaderName) {
            TeamName = _teamName;
            LeaderName = _teamLeaderName;
            MemberList = new ArrayList();
        }

        public string TeamName { get => teamName; set => teamName = value; }
        public string LeaderName { get => leaderName; set => leaderName = value; }
        public ArrayList MemberList { get => memberList; set => memberList = value; }


        public void AddTeamMember(String _userName) {
            MemberList.Add(_userName);
        }

        public String JsonSerialization() {
            return JsonConvert.SerializeObject(this);
        }
    }
}
