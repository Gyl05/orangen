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

INSERT INTO `user` (username, password) values ('root', 'e10adc3949ba59abbe56e057f20f883e');


CREATE TABLE `sites` (
    `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '站点id',
    `sitename` varchar(32) NOT NULL DEFAULT '' COMMENT '站点名称',
    `uri` varchar(128) COMMENT '站点url',
    `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00' COMMENT '创建时间',
    `visit_num` int unsigned DEFAULT 0 COMMENT '访问次数',
    PRIMARY KEY (`id`),
    UNIQUE KEY `sitename` (`sitename`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='站点收藏表';

-- 出现:在终端里使用中文字符会看不到的bug 
INSERT INTO `sites` (`id`, `sitename`, `uri`, `create_time`, `visit_num`) VALUES
	(2, 'python文档', 'https://docs.python.org/zh-cn/3/library', '2022-11-04 15:26:44', 0),
	(3, 'k8s中文文档', 'https://kubernetes.io/#', '2022-11-04 15:32:50', 0),
	(4, 'redis index page', 'https://redis.io/', '2022-11-04 15:34:03', 0),
	(5, 'StackOverflow', 'https://stackoverflow.co/', '1970-01-01 00:00:00', 0),
	(7, 'aiomysql', 'https://aiomysql.readthedocs.io/en/latest/', '1970-01-01 00:00:00', 0),
	(9, '蜀黍啊 守护最好的二次元', 'https://bilibili.com', '2022-11-07 15:47:33', 0),
	(10, '衡水老白干', 'https://bilibili.com', '2022-11-07 17:39:46', 0),
	(11, 'redis sentinel', 'https://redis.io/docs/management/sentinel/', '2022-11-07 17:52:55', 0);
