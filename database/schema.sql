CREATE DATABASE train_booking_db;

USE train_booking_db;

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    departure VARCHAR(100) NOT NULL,
    arrival VARCHAR(100) NOT NULL,
    seats INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL
);
