CREATE TABLE `NEWS`.`group` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name`);


CREATE TABLE `NEWS`.`group_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `group_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `group_permissions_id_uniq`,
  CONSTRAINT `fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `NEWS`.`group` (`id`));


CREATE TABLE `NEWS`.`user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username`);


CREATE TABLE `NEWS`.`user_groups` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `group_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_groups_id_uniq`,
  CONSTRAINT `fk_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `NEWS`.`group` (`id`),
  CONSTRAINT `fk_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `NEWS`.`user` (`id`));


CREATE TABLE `NEWS`.`news` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(50) NOT NULL,
  `image` VARCHAR(100) NOT NULL,
  `short_text` LONGTEXT NOT NULL,
  `text` LONGTEXT NOT NULL,
  `pubtime` DATETIME NOT NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `NEWS`.`comments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `text` LONGTEXT NOT NULL,
  `pubtime` DATETIME NOT NULL,
  `new_id` INT(11) NOT NULL,
  `user_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_comments_new_news_id`
    FOREIGN KEY (`new_id`)
    REFERENCES `NEWS`.`news` (`id`),
  CONSTRAINT `fk_comments_user_id_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `NEWS`.`user` (`id`));


CREATE TABLE `NEWS`.`admin_log` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT(5) UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT(11) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_auth_user_id`,
  CONSTRAINT `fk_admin_log_user_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `NEWS`.`user` (`id`));


CREATE TABLE `NEWS`.`session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME NOT NULL,
  PRIMARY KEY (`session_key`));


CREATE TABLE `NEWS`.`main_emailconfirm` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `token` VARCHAR(36) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_main_emailconfirm_user__auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `NEWS`.`user` (`id`));
