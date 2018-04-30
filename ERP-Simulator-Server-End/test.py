import Message
import json
import GameInfoPackage.Team

if __name__ == '__main__':
    # s = '{"LoginID":"","IsSuccessful":true,"ExtraInfo":""}'
    # tmp_l = Message.LoginRep(json_info=s)
    # print(tmp_l.msg_suc)
    # print(tmp_l.login_id)
    # print(tmp_l.extra_info)
    # print(tmp_l.__dict__())
    # print(tmp_l.to_json())

    # s = '{"TeamName":"123","LeaderName":"name","MemberList":["455","member 2"]}'
    # tmp_team = GameInfoPackage.Team.Team(json_info=s)
    # print(tmp_team.to_json())
    # print(tmp_team.team_name)
    # print(tmp_team.leader_name)
    # print(tmp_team.member_list)
    tmp_list = [1, 2, 3, 4, 5]
    print(tmp_list)
    tmp_list.count(6)
    print(tmp_list)
