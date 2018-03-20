#!/usr/bin/python3
import pymysql
import dbcmd
db_ip = "localhost"
db_usr = "root"
db_pwd = "0000"
db_name = "erp_system_manager"
db = pymysql.connect(db_ip,db_usr,db_pwd,db_name);
cursor = db.cursor()
tmp_sql = dbcmd.create_table_account_info;
cursor.execute(tmp_sql)
print("created table successfull.")
# disconnect from server
db.close()




