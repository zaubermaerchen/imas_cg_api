DROP TABLE IF EXISTS `idol`;
CREATE TABLE `idol` (
  `id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(256) NOT NULL DEFAULT '',
  `type` int(11) NOT NULL DEFAULT '0',
  `rarity` int(11) NOT NULL DEFAULT '0',
  `cost` int(11) NOT NULL DEFAULT '0',
  `offense` int(11) NOT NULL DEFAULT '0',
  `defense` int(11) NOT NULL DEFAULT '0',
  `max_offense` int(11) NOT NULL DEFAULT '0',
  `max_defense` int(11) NOT NULL DEFAULT '0',
  `skill_name` varchar(256) NOT NULL DEFAULT '',
  `skill_id` int(11) NOT NULL DEFAULT '0',
  `hash` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FULLTEXT INDEX `name_index` (`name`),
  KEY `idol_idx1` (`type`,`rarity`)
) ENGINE=Mroonga DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `skill`;
CREATE TABLE `skill` (
  `id` int(11) NOT NULL,
  `target_unit` int(11) NOT NULL DEFAULT '0',
  `target_member` int(11) NOT NULL DEFAULT '0',
  `target_type` int(11) NOT NULL DEFAULT '0',
  `target_num` int(11) NOT NULL DEFAULT '-1',
  `target_param` int(11) NOT NULL DEFAULT '0',
  `skill_value_id` int(11) NOT NULL DEFAULT '0',
  `comment` varchar(256) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `skill_value`;
CREATE TABLE `skill_value` (
  `id` int(11) NOT NULL,
  `value1` int(11) NOT NULL DEFAULT '0',
  `value2` int(11) NOT NULL DEFAULT '0',
  `value3` int(11) NOT NULL DEFAULT '0',
  `value4` int(11) NOT NULL DEFAULT '0',
  `value5` int(11) NOT NULL DEFAULT '0',
  `value6` int(11) NOT NULL DEFAULT '0',
  `value7` int(11) NOT NULL DEFAULT '0',
  `value8` int(11) NOT NULL DEFAULT '0',
  `value9` int(11) NOT NULL DEFAULT '0',
  `value10` int(11) NOT NULL DEFAULT '0',
  `value11` int(11) NOT NULL DEFAULT '0',
  `value12` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DROP TABLE IF EXISTS `cartoon`;
DROP TABLE IF EXISTS `idol_name`;

CREATE TABLE `idol_name` (
  `name` varchar(255) PRIMARY KEY
) ENGINE=Mroonga DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='default_tokenizer "TokenDelimit"';

CREATE TABLE `cartoon` (
  `id` int(11) NOT NULL DEFAULT '0' PRIMARY KEY,
  `title` varchar(256) NOT NULL DEFAULT '',
  `date` date NOT NULL DEFAULT '0000-00-00',
  `idols` text COMMENT 'flags "COLUMN_VECTOR", type "idol_name"',
  `comment` varchar(256) NOT NULL DEFAULT '',
  `thumbnail_hash` char(32) DEFAULT NULL,
  FULLTEXT INDEX `title_index` (`title`),
  FULLTEXT INDEX `idols_index` (`idols`) COMMENT 'table "idol_name"'
) ENGINE=Mroonga DEFAULT CHARSET=utf8mb4;