CREATE TABLE Authors (
    author_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    birthdate DATE
);

CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INT,
    published_year INT,
    genre VARCHAR(100),
    price DECIMAL(10, 2),

);

CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20)
);


INSERT INTO Authors ( first_name, last_name, birthdate)
VALUES
( 'George', 'Kuranchie', '1903-06-25');



INSERT INTO Books ( title, author_id, published_year, genre, price)
VALUES

( 'Animal Farm', 1, 1945, 'Agric', 19);



INSERT INTO Customers ( first_name, last_name, email, phone)
VALUES
( 'Iris', 'Anan', 'iris@gmail.com', '09988776655');


SELECT * FROM Books;
SELECT * FROM Authors;
SELECT * FROM Customers;
