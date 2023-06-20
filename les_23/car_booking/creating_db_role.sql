create role car_book_user createrole createdb password 'car_book_user_password';
create database car_booking_db owner car_book_user encoding 'utf-8';