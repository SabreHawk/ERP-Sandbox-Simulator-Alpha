import Message
import json

if __name__ == '__main__':
    s = '{"LoginID":"","IsSuccessful":true,"ExtraInfo":""}'
    tmp_l = Message.LoginRep(json_info=s)
    print(tmp_l.msg_suc)
    print(tmp_l.login_id)
    print(tmp_l.extra_info)
    print(tmp_l.__dict__())
    print(tmp_l.to_json())
