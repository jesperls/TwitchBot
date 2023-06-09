drop table if exists users;
CREATE TABLE IF NOT EXISTS users (
    username varchar(64) default null,
    points int default 0,
    online_status boolean default 0,
    unique (username)
);
CREATE TABLE IF NOT EXISTS commands (
    command varchar(64) default null,
    response TEXT default null,
    unique (command)
);