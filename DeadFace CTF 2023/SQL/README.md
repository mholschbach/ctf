# Category SQL

Originally I didn't want to start with this category at all, but once I had started the environment, loaded the database and solved the first challenge, I couldn't stop.

## Setup a MariaDB plus phpmyadmin environment

I used [docker-compose](docker-compose.yml) to start an environment with MariaDB and PHPMyAdmin. Use "root:notSecureChangeMe" for login to http://localhost:808, create a database aurora with utf8_general_ci and then import the [aurora database dump](https://tinyurl.com/ytsdav3b) ([local copy](aurora.zip)).

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
> Starypax (street name STAR) is a controlled substance and is in high demand on the Dark Web. DEADFACE might leverage this database to find out which patients currently carry STAR.
>
> How many patients in the Aurora database have an active prescription for Starypax as of Oct 20, 2023? And whose prescription expires first?
>
> Submit the flag as flag{#_firstname lastname}.

### Solution
The first statement returned the drug_id 26 for Starypax, the second returned a sorted by expiration list of seven prescriptions. The next to expire was for patient_id 10042. (Yes, I was avoiding JOIN statements as long as possible).

```sql
SELECT * FROM drugs WHERE drugs.drug_name LIKE "%Starypax%"
SELECT * FROM `prescriptions`
where drug_id=26 and expiration>'2023-10-20' ORDER BY `prescriptions`.`expiration` DESC
SELECT * FROM `aurora`.`patients` WHERE `patient_id` = 10042

flag{7_Renae Allum}
```

## Transaction Approved 100

### Challenge
> Turbo Tactical wants you to determine how many credit cards are still potentially at risk of being used by DEADFACE. How many credit cards in the Aurora database are NOT expired as of Oct 2023?
>
> Submit the flag as flag{#}.

### Solution
Only one statement needed. (I wasn't expecting that each card_number was only used for one billing)
```sql
SELECT distinct card_num FROM `billing` where exp>'2023-10' ORDER BY `billing`.`exp` ASC; 
SELECT COUNT(card_num) FROM `billing` where exp>'2023-10' ORDER BY `billing`.`exp` ASC;

flag{8785}
```
   
## Genovex Profits 100

### Challenge
> Genovex, a pharmaceutical company, is concerned that DEADFACE will target their company based on how much money they made this year on prescriptions at the Aurora Health pharmacy. How much money did Genovex make in 2023 based on the Aurora database?
> 
> Submit the dollar value as the flag. Example: flag{$1234.56}
> 
> Note: Round to the nearest hundredths.

### Solution
This challenge took me a long time. I thought the refill column needed to be included, but would 3 refills mean a drug was ordered 3 or 4 times? Refills in the context of prescription wasn't familiar for me used to German Health Care, but a question to the CTF moderators helped.

```sql
select sum(drugs.cost) from drugs
join suppliers on suppliers.supplier_id=drugs.supplier_id
join prescriptions on prescriptions.drug_id=drugs.drug_id
where suppliers.supplier_name="Genovex" and prescriptions.date_prescribed LIKE "2023%"; 

flag{$19249.88}
```

## City Hoard 100

### Challenge
> Aurora is asking for help in determining which city has the facility with the largest inventory of Remizide based on the Aurora database.
> 
> Submit the flag as flag{city}.

### Solution
```sql
SELECT * FROM drugs WHERE drugs.drug_name LIKE "%Remizide%"; 
SELECT * FROM `inventory` JOIN facilities on inventory.facility_id=facilities.facility_id
where inventory.drug_id=13 ORDER BY `inventory`.`qty` DESC; 

flag{Miami}
```

##    Order Up 125

### Challenge
> Dr. Flegg prescribed Automeda to a patient in June 2023. What is the order number for this prescription?
> 
> Submit the flag as flag{order_num}.

### Solution
This was one of the SQL challenges I solved last and I was using JOIN now. The table returns five rows, but only one is for Automeda.
```sql
select prescriptions.prescription_id, drugs.drug_name, orders.order_id, orders.order_num from prescriptions
join staff on staff.staff_id=prescriptions.doctor_id
join drugs on drugs.drug_id=prescriptions.drug_id
join orders on orders.prescription_id=prescriptions.prescription_id
where prescriptions.date_prescribed like "2023-06%" and staff.last_name like "%Flegg%";

flag{DYP8AXK3QG9OTPWB}
```

## Counting STARs 150
    
### Challenge
> We know DEADFACE is trying to get their hands on STAR, so it makes sense that they will try to target the doctor who prescribes the most STAR from the Aurora database. Provide the first and last name and the type of doctor (position name) that prescribed the most STAR from the database.
> 
> Submit the flag as flag{FirstName LastName Position}.
> 
> For example: flag{John Doe Podiatrist}

### Solution
I got to the solution in three steps. First the drug_id 26, then the doctor_id 1957, which is the staff_id for the third statement:
```sql
SELECT * FROM drugs WHERE drugs.drug_name LIKE "%Starypax%"
SELECT doctor_id, count(doctor_id) FROM `prescriptions` where drug_id=26 group by doctor_id ORDER BY `count(doctor_id)` DESC
SELECT positions_assigned.position_assigned_id, staff.staff_id, staff.first_name, staff.last_name, positions.position_name
FROM `positions_assigned`
join staff on staff.staff_id = positions_assigned.staff_id
join positions on positions.position_id = positions_assigned.position_id
WHERE staff.staff_id = 1957; 

flag{Alisa MacUchadair Dermatologist}
```

## Clean up on aisle 5 300

### Challenge
> Based on Ghost Town conversations, DEADFACE is going to try to compromise an Aurora Health pharmacy to get their hands on STAR. Turbo Tactical wants to provide security personnel at Aurora with information about which facility, aisle, and bin contains the most STAR, since it is likely what DEADFACE will target.
> 
> Provide the facility_id, aisle, and bin where the most STAR is kept in the city DEADFACE is targeting. Submit the flag as flag{facility_id-aisle-bin}.
> 
> Example: flag{123-4-8}

### Solution
I couldn't find anything on aisle or bin in the database... then a look into the [System Design Specification](https://tinyurl.com/3z7zf9y9) ([local copy](System%20Design%20Specification.pdf)) explained the column locator A11B44 is "aisle 11 bin 44":
```sql
SELECT * FROM `inventory` join facilities on facilities.facility_id=inventory.facility_id
where drug_id=26 and city like "%Phoe%" ORDER BY `inventory`.`qty` DESC; 

flag{412-11-44}
```

## SHAttered Dreams 400

### Challenge
> DEADFACE is on the brink of selling a patient's credit card details from the Aurora database to a dark web buyer. Investigate Ghost Town for potential leads on the victim's identity.
> 
> Submit the flag as flag{Firstname Lastname}. Example: flag{John Smith}.

### Solution
This challenge required additional information from Ghost Town, which can be found here https://ghosttown.deadface.io/t/we-got-a-potential-buyer/107/7 and below:

```pre
"I’ll let him know! I told him to put this SHA1 hash in the notes of the transaction so we have a record of what was sold: 911d1fc5930fa5025dbc2d3953c94de9e4773584"
"Awesome. How are you coming up with that SHA1? The patient_id?"
"No I’m actually including almost the full billing and patient data. I’m just concatenating the following: 
    card number
    expiration
..."
```

```sql
SELECT sha(concat(billing.card_num, billing.exp, billing.ccv, billing.patient_id,
                  patients.first_name, patients.last_name, patients.middle, patients.sex, patients.email,
                  patients.street, patients.city, patients.state, patients.zip, patients.dob)) as sha,
                  patients.first_name, patients.last_name
FROM `billing`
join patients on patients.patient_id=billing.patient_id having sha like "%911d1%";

flag{Berton Luchetti}
```



