using System;
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
}
