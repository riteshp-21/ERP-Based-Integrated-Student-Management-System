-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: student_erp_db
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exam_recordstb`
--

DROP TABLE IF EXISTS `exam_recordstb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_recordstb` (
  `exam_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `semester` int DEFAULT NULL,
  `subject` varchar(50) DEFAULT NULL,
  `marks` int DEFAULT NULL,
  `grade` varchar(5) DEFAULT NULL,
  `result` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`exam_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `exam_recordstb_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student_mastertb` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_recordstb`
--

LOCK TABLES `exam_recordstb` WRITE;
/*!40000 ALTER TABLE `exam_recordstb` DISABLE KEYS */;
/*!40000 ALTER TABLE `exam_recordstb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fee_detailstb`
--

DROP TABLE IF EXISTS `fee_detailstb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fee_detailstb` (
  `fee_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `fee_type` varchar(50) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `receipt_no` varchar(50) DEFAULT NULL,
  `payment_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`fee_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `fee_detailstb_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student_mastertb` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fee_detailstb`
--

LOCK TABLES `fee_detailstb` WRITE;
/*!40000 ALTER TABLE `fee_detailstb` DISABLE KEYS */;
INSERT INTO `fee_detailstb` VALUES (1,1,'Tuition Fee',50000.00,'2026-02-07','RCPT001','Paid');
/*!40000 ALTER TABLE `fee_detailstb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hostel_allocationtb`
--

DROP TABLE IF EXISTS `hostel_allocationtb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hostel_allocationtb` (
  `hostel_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `hostel_name` varchar(50) DEFAULT NULL,
  `room_no` varchar(10) DEFAULT NULL,
  `allocation_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`hostel_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `hostel_allocationtb_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student_mastertb` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostel_allocationtb`
--

LOCK TABLES `hostel_allocationtb` WRITE;
/*!40000 ALTER TABLE `hostel_allocationtb` DISABLE KEYS */;
/*!40000 ALTER TABLE `hostel_allocationtb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_mastertb`
--

DROP TABLE IF EXISTS `student_mastertb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_mastertb` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  `admission_date` date DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_mastertb`
--

LOCK TABLES `student_mastertb` WRITE;
/*!40000 ALTER TABLE `student_mastertb` DISABLE KEYS */;
INSERT INTO `student_mastertb` VALUES (1,'Ritesh Ramdas Pokharkar','2003-05-21','Male','MCA',2,'test@gmail.com','9999999999','2026-02-07');
/*!40000 ALTER TABLE `student_mastertb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userstb`
--

DROP TABLE IF EXISTS `userstb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userstb` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userstb`
--

LOCK TABLES `userstb` WRITE;
/*!40000 ALTER TABLE `userstb` DISABLE KEYS */;
/*!40000 ALTER TABLE `userstb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-07 15:32:43
