drop table if exists users;
CREATE TABLE IF NOT EXISTS users (
    username varchar(64) default null,
    points int default 0,
    online_status boolean default 0,
    watchtime int default 0,
    last_message text default null,
    unique (username)
);
drop table if exists commands;
CREATE TABLE IF NOT EXISTS commands (
    command varchar(64) default null,
    response TEXT default null,
    unique (command)
);