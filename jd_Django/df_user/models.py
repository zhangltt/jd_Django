# coding=utf-8
from django.db import models

# Create your models here.

# CREATE TABLE `php41_user` (
#   `user_id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键id',
#   `user_name` varchar(32) NOT NULL COMMENT '会员名称',
#   `user_email` varchar(64) NOT NULL DEFAULT '' COMMENT '邮箱',
#   `user_pwd` char(32) NOT NULL COMMENT '密码',
#   `openid` char(32) NOT NULL DEFAULT '' COMMENT 'qq登录的openid信息',
#   `user_sex` enum('男','女','保密') NOT NULL DEFAULT '男' COMMENT '性别',
#   `user_weight` smallint(6) NOT NULL DEFAULT '0' COMMENT '体重',
#   `user_height` decimal(5,2) NOT NULL DEFAULT '0.00' COMMENT '身高',
#   `user_logo` varchar(128) NOT NULL DEFAULT '' COMMENT '头像',
#   `user_tel` char(11) NOT NULL DEFAULT '' COMMENT '手机',
#   `user_identify` char(18) NOT NULL DEFAULT '' COMMENT '身份号码',
#   `user_check` enum('0','1') NOT NULL DEFAULT '0' COMMENT '是否激活, 0:未激活  1:已激活',
#   `user_check_code` char(32) NOT NULL DEFAULT '' COMMENT '邮箱验证激活码',
#   `add_time` int(11) NOT NULL COMMENT '注册时间',
#   `is_del` enum('0','1') NOT NULL DEFAULT '0' COMMENT '是否删除, 0:正常  1:被删除',
#   PRIMARY KEY (`user_id`),
#   KEY `user_name` (`user_name`),
#   KEY `user_tel` (`user_tel`)
# ) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='会员表';

class python41_user(models.Model):
    user_name = models.CharField(max_length=32)# 会员名称
    nick_name = models.CharField(max_length=32,default='')# 昵称
    user_email = models.CharField(max_length=64,default='')# '邮箱'
    user_pwd = models.CharField(max_length=40)# '密码',
    openid =models.CharField(max_length=32,default='')#'qq登录的openid信息',
    user_sex = models.BooleanField(default=False)#'男' COMMENT '性别',
    user_weight = models.DecimalField(max_digits=5,decimal_places=2,default=0)#'体重',
    user_height = models.DecimalField(max_digits=5,decimal_places=2,default=0)# '身高',
    user_logo = models.ImageField(upload_to='user_logo')#'头像',
    user_tel = models.CharField(max_length=20,default='')#手机',
    user_identify = models.CharField(max_length=20,default='')#'身份号码',
    user_check = models.CharField(max_length=10, default='0')#'是否激活, 0:未激活  1:已激活',
    user_check_code = models.CharField(max_length=32,default='')#'邮箱验证激活码',
    add_time = models.DateTimeField(auto_now_add=True)#注册时间',
    isDelete = models.BooleanField(default=False)

class UserAddress(models.Model):
    consignee = models.CharField(max_length=32,default='')# 收货人
    address = models.CharField(max_length=300,default='')# 收货地址
    iphone = models.CharField(max_length=20,default='')# 手机
    default_addr = models.BooleanField(default=False)# 默认地址(选择为True,否则为Fales)
    uid = models.ForeignKey(python41_user)# 关联用户id
