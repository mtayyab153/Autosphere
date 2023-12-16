CREATE TABLE `new_table` (
    `PersonID` int,
    `LastName` varchar(255),
    `FirstName` varchar(255),
    `Address` varchar(255),
    `City` varchar(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `new_table` (`PersonID`, `LastName`, `FirstName`, `Address`, `City`) VALUES
(1, 'Doe', 'Joe', 'Address 1', 'Islamabad'),
(2, 'Root', 'Joe', 'Address 2', 'Rawalpindi'),
(3, 'Curran', 'Sam', 'Address 3', 'Karachi'),
(4, 'Archer', 'Jofra', 'Address 4', 'Peshawar'),
(5, 'Cummins', 'Pat', 'Address 5', 'Mardan'),
(6, 'Okeefe', 'Kerry', 'Address 6', 'Nowshera'),
(7, 'Akram', 'Wasim', 'Address 7', 'Sialkot');