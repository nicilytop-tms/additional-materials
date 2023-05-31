create role blog_user nocreatedb createrole login;
alter user blog_user with password 'blog_password';
create database blog owner blog_user encoding 'utf-8';