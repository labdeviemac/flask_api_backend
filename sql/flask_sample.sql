CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `surname` varchar(255),
  `age` int,
  `birthdate` date,
  `created_at` date,
  `users_id` int
);

CREATE TABLE `states` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `state_name` varchar(255),
  `state_shortname` varchar(255)
);

ALTER TABLE `users` ADD FOREIGN KEY (`users_id`) REFERENCES `states` (`id`);
