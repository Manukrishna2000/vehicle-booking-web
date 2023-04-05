-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 05, 2023 at 03:35 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vehicle`
--

-- --------------------------------------------------------

--
-- Table structure for table `addvehicle`
--

CREATE TABLE `addvehicle` (
  `v_id` int(25) NOT NULL,
  `vehicle_name` varchar(100) NOT NULL,
  `model` varchar(50) NOT NULL,
  `specification` varchar(300) NOT NULL,
  `price` varchar(30) NOT NULL,
  `photo` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addvehicle`
--

INSERT INTO `addvehicle` (`v_id`, `vehicle_name`, `model`, `specification`, `price`, `photo`) VALUES
(11, 'Mercedes-Benz', ' A-Class Benz 2021', 'The Mercedes-Benz A-Class has 1 Diesel Engine and 1 Petrol Engine on offer. The Diesel engine is 2143 cc while the Petrol engine is 1595 cc . It is available with Automatic transmission.Depending upon the variant and fuel type the A-Class has a mileage of 15.5 to 20.0 kmpl & Ground clearance of A-Cl', '25.95 lakhs', '/static/vehicles/front-left-side-47.jpg'),
(13, 'Mercedes-Benz', 'Mercedes-Benz GLA', 'The Mercedes-Benz GLA has 1 Diesel Engine and 1 Petrol Engine on offer. The Diesel engine is 1950 cc while the Petrol engine is 1332 cc . It is available with Automatic transmission.Depending upon the variant and fuel type the GLA has a mileage of . The GLA is a 5 seater 4 cylinder car and has lengt', '48.90 Lakh', '/static/vehicles/front-left-side-47.webp'),
(14, 'Mercedes-Benz ', 'Mercedes-Benz C-Class', 'C-Class Specs, Features and Price The Mercedes-Benz C-Class has 1 Diesel Engine and 1 Petrol Engine on offer. The Diesel engine is 1993 cc while the Petrol engine is 1496 cc . It is available with Automatic transmission.Depending upon the variant and fuel type the C-Class has a mileage of . The C-Cl', '61.45 Lakh', '/static/vehicles/front-left-side-47 (2).jpg');

-- --------------------------------------------------------

--
-- Table structure for table `booked`
--

CREATE TABLE `booked` (
  `slno` int(10) NOT NULL,
  `username` varchar(25) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `date` varchar(25) NOT NULL,
  `time` varchar(25) NOT NULL,
  `model` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `zipcode` int(10) NOT NULL,
  `city` varchar(50) NOT NULL,
  `status` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booked`
--

INSERT INTO `booked` (`slno`, `username`, `name`, `email`, `phone`, `date`, `time`, `model`, `address`, `zipcode`, `city`, `status`) VALUES
(1, 'manu', 'Manu', 'manukrishnaap@gmail.com', '8943432234', '11/23/2022', '09:58', 'A-Class Benz 2021 ', 'nit', 673601, 'calicut', 'complete'),
(2, 'jishnu', 'Jishnu', 'jishnu@gmail.com', '9048335993', '2022-11-25', '10:08', 'Mercedes-Benz C-Class ', 'Kairali house', 673601, 'Kozhikode', 'complete'),
(4, 'manu', 'Manu', 'manukrishnaap@gmail.com', '8943432234', '2022-11-28', '10:56', 'Mercedes-Benz GLA ', 'nit', 673601, 'calicut', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `type`) VALUES
('a', 'Manu@3467', 'user'),
('admin', 'admin', 'admin'),
('jishnu', 'Jishnu@3467', 'user'),
('manu', 'Manu@3467', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `address` varchar(50) NOT NULL,
  `zipcode` int(10) NOT NULL,
  `city` varchar(50) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`name`, `email`, `phone`, `address`, `zipcode`, `city`, `username`, `password`) VALUES
('manu', 'manu@gmail.com', '8943397231', 'a', 123456, 'a', 'a', 'Manu@3467'),
('Jishnu', 'jishnu@gmail.com', '9048335993', 'Kairali house', 673601, 'Kozhikode', 'jishnu', 'Jishnu@3467'),
('Manu', 'manukrishnaap@gmail.com', '8943432234', 'nit', 673601, 'calicut', 'manu', 'Manu@3467');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addvehicle`
--
ALTER TABLE `addvehicle`
  ADD PRIMARY KEY (`v_id`);

--
-- Indexes for table `booked`
--
ALTER TABLE `booked`
  ADD PRIMARY KEY (`slno`),
  ADD UNIQUE KEY `model` (`model`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addvehicle`
--
ALTER TABLE `addvehicle`
  MODIFY `v_id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `booked`
--
ALTER TABLE `booked`
  MODIFY `slno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
