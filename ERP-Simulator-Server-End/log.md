# Coding Log

* 2018/04/03 21:46 - Zhiquan Wang
  * Summary : Modularize MD5 Manager & Modify Database Operation In Class UserManager.py
  * Attention : Uncompleted
  * Details :  
    1.  Transform class CreatePwdMd5 into a static function create_md5 as a general method (All Operation Of Generate A MD5 Code Can Use This Method)
    2.  Add a private member variable into class UserManger ,which is a reference object - DbManager From ServerSystem.(!!!All Operations About Database Should Be Addressed In This DbManager Reference ,Rather than Generate A New DbManager Object)
* 2018/04/04 11:44 - Zhiquan Wang
  * Summary : Consummate Class User Manager & Add methods into DbManager
  * Details : 
    1. Modify Method : register_user() - Move 'insert_user_info' operation into ref_db_manager
    2. Modify Method : login() - Query user_id which matches the user_name and password from database,if exist user_id login and add user_id into active_list else return false
* 2018/04/04 19:14 - Zhiquan.Wang
  * Summary : Consummate Class User Manager & ActiveUser & ServerNetWork
  * Attention : Untested
  * Detials :
    1. Modify Method (Class User Manager) : login() - delete param : id when add active user into active_list
    2. Modify Class ActiveUser :Delelte member:ip & add method :get_id()
    3. Modify Class ServerNetwork : Simplify Method launch_server & __address_requset()
* 2018/04/09 11：27 - Simin.Zhan
  * Summary : Consummate dbcmd.py
  * Attention : Untested
  * Detials : 
  * 1. Add create_table_factory_info & create_table_production_line_info

2018/04/04 19:14 - Zhiquan.Wang

- Summary : Add GameManager.py Game.py & Modify UserManager.py & Modify Logging Message 
- Attention : tested
- Detials :
  1. Modify Method (Class User Manager) : trans active_user.id to login_id