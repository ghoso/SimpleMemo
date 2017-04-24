drop table if exists memos;
create table memos (
       id integer primary key autoincrement,
       title string not null,
       text string not null
       );
