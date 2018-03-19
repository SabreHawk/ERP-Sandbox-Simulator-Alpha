create_account_info_table = """CREATE TABLE `account_info` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `account` char(20) NOT NULL,
  `pwd_md5` char(40) NOT NULL,
  PRIMARY KEY (`id`)
);"""
