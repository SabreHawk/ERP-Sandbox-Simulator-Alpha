# Coding Log

* 2018/04/03 21:46 - Zhiquan Wang
  * Summary : Modularize MD5 Manager & Modify Database Operation In Class UserManager.py
  * Attention : Uncompleted
  * Details :  
    1.  Transform class CreatePwdMd5 into a static function create_md5 as a general method (All Operation Of Generate A MD5 Code Can Use This Method)
    2. Add a private member variable into class UserManger ,which is a reference object - DbManager From ServerSystem.(!!!All Operations About Database Should Be Addressed In This DbManager Reference ,Rather than Generate A New DbManager Object)
* ​