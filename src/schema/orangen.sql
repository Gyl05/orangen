CREATE DATABASE `orangen`;

USE `orangen`;

CREATE TABLE `user` (
    `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '用户id',
    `username` varchar(64) NOT NULL DEFAULT '' COMMENT '用户账号',
    `password` varchar(32) NOT NULL DEFAULT '' COMMENT '用户密码',
    `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00' COMMENT '创建时间',
    `update_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00' COMMENT '活跃时间',
    `state` tinyint unsigned NOT NULL DEFAULT 1 COMMENT '状态',
    PRIMARY KEY (`id`),
    UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

INSERT INTO `user` (username, password) values ('root', '123456');


CREATE TABLE `sites` (
    `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '站点id',
    `sitename` varchar(32) NOT NULL DEFAULT '' COMMENT '站点名称',
    `uri` varchar(128) COMMENT '站点url',
    `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00' COMMENT '创建时间',
    `visit_num` int unsigned DEFAULT 0 COMMENT '访问次数',
    PRIMARY KEY (`id`),
    UNIQUE KEY `sitename` (`sitename`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='站点收藏表';