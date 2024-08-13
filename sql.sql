CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(10),
    password VARCHAR(255),
    status VARCHAR(50)
);

INSERT INTO Users (user_id, username, first_name, last_name, gender, password, status)
VALUES
(1, 'jdoe', 'John', 'Doe', 'Male', 'password123', 1),
(2, 'asmith', 'Alice', 'Smith', 'Female', 'securePass456', 0),
(3, 'bwhite', 'Bob', 'White', 'Male', 'pass789', 1),
(4, 'jwilson', 'James', 'Wilson', 'Male', 'randomPass1', 1),
(5, 'mjones', 'Mary', 'Jones', 'Female', 'randomPass2', 0),
(6, 'kking', 'Kevin', 'King', 'Male', 'randomPass3', 1),
(7, 'lmartin', 'Laura', 'Martin', 'Female', 'randomPass4', 0),
(8, 'cclark', 'Charles', 'Clark', 'Male', 'randomPass5', 1),
(9, 'ewalker', 'Elizabeth', 'Walker', 'Female', 'randomPass6', 1),
(10, 'pmoore', 'Paul', 'Moore', 'Male', 'randomPass7', 0),
(11, 'dthomas', 'David', 'Thomas', 'Male', 'randomPass8', 1),
(12, 'rtaylor', 'Rachel', 'Taylor', 'Female', 'randomPass9', 1),
(13, 'mbrown', 'Michael', 'Brown', 'Male', 'randomPass10', 0),
(14, 'kharris', 'Katherine', 'Harris', 'Female', 'randomPass11', 1),
(15, 'rgonzalez', 'Robert', 'Gonzalez', 'Male', 'randomPass12', 0),
(16, 'mlee', 'Megan', 'Lee', 'Female', 'randomPass13', 1),
(17, 'tlopez', 'Thomas', 'Lopez', 'Male', 'randomPass14', 1),
(18, 'sgarcia', 'Sarah', 'Garcia', 'Female', 'randomPass15', 0),
(19, 'jyoung', 'Joshua', 'Young', 'Male', 'randomPass16', 1),
(20, 'rallen', 'Rebecca', 'Allen', 'Female', 'randomPass17', 1),
(21, 'kmartinez', 'Kyle', 'Martinez', 'Male', 'randomPass18', 0),
(22, 'ashaw', 'Anna', 'Shaw', 'Female', 'randomPass19', 1),
(23, 'jwarren', 'Jacob', 'Warren', 'Male', 'randomPass20', 1),
(24, 'vcarter', 'Victoria', 'Carter', 'Female', 'randomPass21', 0),
(25, 'blong', 'Brandon', 'Long', 'Male', 'randomPass22', 1),
(26, 'mperez', 'Melissa', 'Perez', 'Female', 'randomPass23', 1),
(27, 'zreed', 'Zachary', 'Reed', 'Male', 'randomPass24', 0),
(28, 'jmorris', 'Jessica', 'Morris', 'Female', 'randomPass25', 1),
(29, 'tbell', 'Tyler', 'Bell', 'Male', 'randomPass26', 1),
(30, 'jward', 'Jennifer', 'Ward', 'Female', 'randomPass27', 0),
(31, 'jdavis', 'John', 'Davis', 'Male', 'randomPass28', 1),
(32, 'alewiss', 'Ashley', 'Lewis', 'Female', 'randomPass29', 1),
(33, 'rturner', 'Ryan', 'Turner', 'Male', 'randomPass30', 0),
(34, 'mgomez', 'Michelle', 'Gomez', 'Female', 'randomPass31', 1),
(35, 'hparker', 'Henry', 'Parker', 'Male', 'randomPass32', 1),
(36, 'sjames', 'Samantha', 'James', 'Female', 'randomPass33', 0),
(37, 'cfoster', 'Christopher', 'Foster', 'Male', 'randomPass34', 1),
(38, 'lrogers', 'Lily', 'Rogers', 'Female', 'randomPass35', 1),
(39, 'wwatson', 'William', 'Watson', 'Male', 'randomPass36', 0),
(40, 'abrooks', 'Amber', 'Brooks', 'Female', 'randomPass37', 1),
(41, 'jdiaz', 'Jason', 'Diaz', 'Male', 'randomPass38', 1),
(42, 'lrichards', 'Lauren', 'Richards', 'Female', 'randomPass39', 0),
(43, 'hbennett', 'Harrison', 'Bennett', 'Male', 'randomPass40', 1),
(44, 'csanders', 'Chloe', 'Sanders', 'Female', 'randomPass41', 1),
(45, 'sturner', 'Sean', 'Turner', 'Male', 'randomPass42', 0),
(46, 'mcollins', 'Mia', 'Collins', 'Female', 'randomPass43', 1),
(47, 'jsimmons', 'Jack', 'Simmons', 'Male', 'randomPass44', 1),
(48, 'alewis', 'Ava', 'Lewis', 'Female', 'randomPass45', 0),
(49, 'bstevens', 'Benjamin', 'Stevens', 'Male', 'randomPass46', 1),
(50, 'emarshall', 'Emily', 'Marshall', 'Female', 'randomPass47', 1),
(51, 'tbaker', 'Thomas', 'Baker', 'Male', 'randomPass48', 0),
(52, 'hyoung', 'Hannah', 'Young', 'Female', 'randomPass49', 1),
(53, 'jwilliams', 'James', 'Williams', 'Male', 'randomPass50', 1),
(54, 'lscott', 'Lily', 'Scott', 'Female', 'randomPass51', 0),
(55, 'ajackson', 'Andrew', 'Jackson', 'Male', 'randomPass52', 1),
(56, 'sroberts', 'Sophia', 'Roberts', 'Female', 'randomPass53', 1),
(57, 'jmartin', 'Jonathan', 'Martin', 'Male', 'randomPass54', 0),
(58, 'ncole', 'Natalie', 'Cole', 'Female', 'randomPass55', 1),
(59, 'rphillips', 'Richard', 'Phillips', 'Male', 'randomPass56', 1),
(60, 'kgreen', 'Kaitlyn', 'Green', 'Female', 'randomPass57', 0),
(61, 'echavez', 'Ethan', 'Chavez', 'Male', 'randomPass58', 1),
(62, 'mnelson', 'Madison', 'Nelson', 'Female', 'randomPass59', 1),
(63, 'fsmith', 'Frank', 'Smith', 'Male', 'randomPass60', 0),
(64, 'klee', 'Kimberly', 'Lee', 'Female', 'randomPass61', 1),
(65, 'bthompson', 'Brandon', 'Thompson', 'Male', 'randomPass62', 1),
(66, 'mgonzalez', 'Maria', 'Gonzalez', 'Female', 'randomPass63', 0),
(67, 'tjackson', 'Tyler', 'Jackson', 'Male', 'randomPass64', 1),
(68, 'pnelson', 'Pamela', 'Nelson', 'Female', 'randomPass65', 1),
(69, 'ggonzalez', 'Gabriel', 'Gonzalez', 'Male', 'randomPass66', 0),
(70, 'mmartinez', 'Madison', 'Martinez', 'Female', 'randomPass67', 1),
(71, 'arodriguez', 'Alexander', 'Rodriguez', 'Male', 'randomPass68', 1),
(72, 'hlee', 'Hailey', 'Lee', 'Female', 'randomPass69', 0),
(73, 'nlopez', 'Noah', 'Lopez', 'Male', 'randomPass70', 1),
(74, 'jclark', 'Jasmine', 'Clark', 'Female', 'randomPass71', 1),
(75, 'msmith', 'Matthew', 'Smith', 'Male', 'randomPass72', 0),
(76, 'kparker', 'Katherine', 'Parker', 'Female', 'randomPass73', 1),
(77, 'nwilson', 'Nathan', 'Wilson', 'Male', 'randomPass74', 1);

SELECT * FROM Users;

SELECT COUNT(*) from Users;

SELECT * FROM Users WHERE gender = 'Male';

SELECT COUNT(*) FROM Users WHERE gender = 'Male';

SELECT * FROM Users WHERE first_name LIKE 'b%';

select * from Users WHERE user_id >= 60;

SELECT * FROM Users WHERE user_id BETWEEN 10 AND 20;

SELECT * FROM Users WHERE first_name IN ('john', 'michael', 'david');

SELECT * FROM Users WHERE user_id BETWEEN 10 AND 20 ORDER BY user_id DESC LIMIT 3;


-- UPDATEUsers

UPDATE Users SET status = 0 WHERE first_name = 'Rebecca';

UPDATE Users SET status = 1 where user_id BETWEEN 1 and 10;

SELECT * FROM Users WHERE user_id BETWEEN 1 AND 10;

SELECT * FROM Users WHERE status = 1;

SELECT max(user_id), username, first_name FROM Users;

SELECT SUM(status) FROM Users;

SELECT AVG(user_id) FROM Users;