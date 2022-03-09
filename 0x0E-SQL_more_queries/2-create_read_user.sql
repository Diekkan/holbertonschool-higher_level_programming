-- creates DATABASE
-- and user with CREATE DATABASE and GRANT
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
