create_table_user_info = """CREATE TABLE `account_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `usr_name` char(20) NOT NULL,
  `pwd_md5` char(40) NOT NULL,
  PRIMARY KEY (`id`)
);"""
