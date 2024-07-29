TABLE_INFO = '''
CREATE TABLE `zkyc_indicator_newest_info_dt` (
  `region_name` varchar(50) DEFAULT NULL COMMENT '地区名称{绍兴市/越城区/柯桥区/上虞区/新昌县/诸暨市/嵊州市}',
  `indicator_name` varchar(50) DEFAULT NULL COMMENT '指标名称',
  `indicator_value` varchar(50) DEFAULT NULL COMMENT '指标值',
  `unit` varchar(50) DEFAULT NULL COMMENT '单位',
  `update_frequency_name` varchar(50) DEFAULT NULL COMMENT '更新频率',
  `date` varchar(50) DEFAULT NULL COMMENT '创建日期'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='绍兴市指标统计表每日最新数据'
CREATE TABLE `zkyc_event_info_dt` (
  `id` varchar(50) NOT NULL COMMENT '事件ID',
  `source` varchar(5) DEFAULT NULL COMMENT '渠道id',
  `source_name` varchar(10) DEFAULT NULL COMMENT '渠道名称',
  `type_name` varchar(50) DEFAULT NULL,
  `sup_type_code` varchar(50) DEFAULT NULL COMMENT '类型码',
  `sup_type_name` varchar(50) DEFAULT NULL COMMENT '类型名称',
  `sub_type_name` varchar(50) DEFAULT NULL,
  `description` varchar(2000) DEFAULT NULL COMMENT '描述',
  `district` varchar(50) DEFAULT NULL COMMENT '区县码',
  `district_name` varchar(50) DEFAULT NULL COMMENT '区县名称{越城区/柯桥区/上虞区/新昌县/诸暨市/嵊州市}',
  `town_name` varchar(50) DEFAULT NULL COMMENT '镇/街道名称',
  `community_name` varchar(50) DEFAULT NULL COMMENT '社区名称',
  `address` varchar(100) DEFAULT NULL COMMENT '地址',
  `is_urgent` varchar(50) DEFAULT NULL COMMENT '是否紧急{0,1}',
  `distribute_dest` varchar(50) DEFAULT NULL,
  `report_time` datetime DEFAULT NULL COMMENT '上报时间',
  `completion_time` datetime DEFAULT NULL COMMENT '办结时间',
  `is_overdue` varchar(50) DEFAULT NULL,
  `state_code` varchar(50) DEFAULT NULL COMMENT '处理状态码',
  `state_name` varchar(50) DEFAULT NULL COMMENT '处理状态{已办结/办理中/待受理/null}',
  `title` varchar(2000) DEFAULT NULL COMMENT '事件标题',
  `dt` varchar(50) NOT NULL COMMENT '日期',
  PRIMARY KEY (`id`,`dt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='绍兴市事件基础信息表'
'''
