


DROP DATABASE IF EXISTS company;

CREATE DATABASE IF NOT EXISTS company CHARACTER SET utf8;

USE company;




DROP TABLE IF EXISTS `t_dept`;

CREATE TABLE `t_dept` (
  `deptno` INT(11) NOT NULL,
  `dname` VARCHAR(20) DEFAULT NULL,
  `loc` VARCHAR(40) DEFAULT NULL,
  PRIMARY KEY (`deptno`),
  KEY `index_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;


LOCK TABLES `t_dept` WRITE;

INSERT INTO `t_dept` VALUES (10,'董事部','江东'),(20,'公关部','四川'),(30,'武统部','咸阳'),(40,'财务部','洛阳');

UNLOCK TABLES;



DROP TABLE IF EXISTS `t_employees`;

CREATE TABLE `t_employees` (
  `empno` INT(11) NOT NULL,
  `ename` VARCHAR(20) DEFAULT NULL,
  `job` VARCHAR(40) DEFAULT NULL,
  `MGR` INT(11) DEFAULT NULL,
  `hiredate` DATE DEFAULT NULL,
  `sal` DOUBLE(10,2) DEFAULT NULL,
  `comm` DOUBLE(10,2) DEFAULT NULL,
  `deptno` INT(11) DEFAULT NULL,
  PRIMARY KEY (`empno`),
  KEY `fk_deptno` (`deptno`),
  CONSTRAINT `fk_deptno` FOREIGN KEY (`deptno`) REFERENCES `t_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;


LOCK TABLES `t_employees` WRITE;

INSERT INTO `t_employees` VALUES (7369,'周瑜','高级公关',7566,'1981-03-21',1800.00,NULL,20),(7499,'张飞','武装教习',7698,'1982-03-21',2600.00,300.00,30),(7521,'关二爷','武装副司令',7698,'1983-03-21',2250.00,500.00,30),(7566,'孙权','经理',7839,'1981-03-21',3975.00,NULL,10),(7654,'黄忠','武装司令',7698,'1981-03-21',2250.00,1400.00,30),(7698,'刘备','经理',7839,'1984-03-21',3850.00,NULL,10),(7782,'曹操','经理',7839,'1985-03-21',3450.00,NULL,10),(7788,'许褚','武装上将',7782,'1981-03-21',4000.00,NULL,30),(7839,'汉献帝','董事长',NULL,'1981-03-21',6000.00,NULL,10),(7844,'魏延','武装上将',7698,'1989-03-21',2500.00,0.00,30),(7876,'黄盖','人事专员',7566,'1998-03-21',2100.00,NULL,20),(7902,'荀彧','分析员',7782,'2005-03-12',4000.00,NULL,20),(7934,'甘宁','中级公关',7782,'1981-03-21',2300.00,NULL,20),(7952,'马超','武装大校',7698,'2001-03-21',2750.00,0.00,30),(7953,'吕布','武装教习',7698,'2001-03-21',2750.00,0.00,30);

UNLOCK TABLES;

SELECT *
FROM t_employees
WHERE deptno=30;,

SELECT ename 姓名, empno 编号,deptno 部门编号,job 工作
FROM t_employees
WHERE job="经理";

SELECT *
FROM t_employees
WHERE comm>sal;

SELECT *
FROM t_employees
WHERE comm>sal*0.6;


SELECT *
FROM t_employees
WHERE deptno=10 AND job="经理" OR deptno=20 AND job="分析员";

SELECT *
FROM t_employees
WHERE (deptno=10 AND job="经理" OR deptno=20 AND job="分析员" ) OR 
job NOT IN ("经理","武装上将") AND sal>=3000;

SELECT *
FROM t_employees
WHERE comm IS NULL OR comm<1000;

SELECT *
FROM t_employees
WHERE ename LIKE "___";

SELECT *
FROM t_employees
WHERE hiredate LIKE "2%";

SELECT *
FROM t_employees
ORDER BY empno ASC;

SELECT *
FROM t_employees
ORDER BY sal DESC,hiredate ASC;

SELECT deptno,AVG(sal)
FROM t_employees
GROUP BY deptno;


SELECT deptno,COUNT(empno) 
FROM t_employees
GROUP BY deptno;


SELECT job,MAX(sal),MIN(sal),COUNT(empno)
FROM t_employees
GROUP BY job;

