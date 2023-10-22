# Category SQL

## Setup a MariaDB plus phpmyadmin environment

I used [docker-compose](docker-compose.yml) to start an environment with MariaDB and PHPMyAdmin. Use "root:notSecureChangeMe" for login to http://localhost:808, create a database aurora with utf8_general_ci and then import the [aurora database dump](aurora.zip).

## Aurora Compromise 10

### Challenge
> DEADFACE has taken responsibility for a partial database hack on a pharmacy tied to Aurora Pharmaceuticals. The hacked data consists of patient data, staff data, and information on drugs and prescriptions. We’ve managed to get a hold of the hacked data. Provide the first and last name of the patient that lives on a street called Hansons Terrace.
>
> Submit the flag as: flag{First Last}.

### Solution
```sql
SELECT first_name, last_name FROM `patients` WHERE street LIKE '%Hansons Terrace%'; 
Sandor Beyer

flag{Sandor Beyer}
```
    
## Foreign Keys 10

### Challenge
> How many foreign keys are described in the design of the inventory table?
>
> Submit the flag as flag{#}.

### Solution
Two constraints fk_inventory_drug_id and fk_inventory_facility_id are defined for the table inventory. 
See the *CREATE TABLE ìnventory` statement or http://localhost:8080/index.php?route=/table/relation&db=aurora&table=inventory

```sql
flag{2}
```

## Credit Compromise 15

### Challenge
> How many credit cards were exposed in the Aurora database hack?
>
> Submit the flag as flag{#}.

### Solution
I wanted to be sure that every card_num is only counted once, so I tried both statements:

```sql
SELECT DISTINCT card_num FROM `billing`;
SELECT COUNT(card_num) FROM `billing`;

flag{10391}
```
    
## Starypax 50

### Challenge
>Starypax (street name STAR) is a controlled substance and is in high demand on the Dark Web. DEADFACE might leverage this database to find out which patients currently carry STAR.
>
>How many patients in the Aurora database have an active prescription for Starypax as of Oct 20, 2023? And whose prescription expires first?
>
>Submit the flag as flag{#_firstname lastname}.

### Solution
The first statement returned the drug_id 26 for Starypax, the second returned a sorted by expiration list of seven prescriptions. The next to expire was for patient_id 10042. (Yes, I was avoiding JOIN statements as long as possible).

```sql
SELECT * FROM drugs WHERE drugs.drug_name LIKE "%Starypax%"
SELECT * FROM `prescriptions` where drug_id=26 and expiration>'2023-10-20' ORDER BY `prescriptions`.`expiration` DESC
SELECT * FROM `aurora`.`patients` WHERE `patient_id` = 10042

flag{7_Renae Allum}
```

## Transaction Approved 100

### Challenge

### Solution
   
## Genovex Profits 100

### Challenge

### Solution

## City Hoard 100

### Challenge

### Solution

##    Order Up 125

### Challenge

### Solution

## Counting STARs 150
    
### Challenge

### Solution

## Clean up on aisle 5 300

### Challenge

### Solution

## SHAttered Dreams 400

### Challenge

### Solution
