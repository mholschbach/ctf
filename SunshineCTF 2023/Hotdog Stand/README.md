# Hotdog Stand
> In the not-so-distant future, robots have taken over the fast-food industry. Infiltrate the robot hotdog stand to find out whatjobs still remain.

## Challenge
You are given the URL https://hotdog.web.2023.sunshinectf.games

## Solution
The web site shows a form where you can enter a *Robot ID* and an *Access Code*. The five mentions of *Robot* and the wellcoming *Humans, this interface isn't for you!* made look for the robots.txt

```
User-agent: *
Disallow: /configs/
Disallow: /backups/
Disallow: /hotdog-database/
```

By accessing */hotdog-database/* a *robot_data.db* was downloaded, which turned out to be a sqlite3 database:

```
sqlite3 robot_data.db

sqlite> .tables
credentials       customer_reviews  menu_items        robot_logs
sqlite> .dump credentials
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE credentials(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   username TEXT NOT NULL,
   password TEXT NOT NULL,
   role TEXT
);
INSERT INTO credentials VALUES(1,'hotdogstand','slicedpicklesandonions','admin');
COMMIT;
```

Then use *hotdogstand* with *slicedpicklesandonions* on the web page and you receive the token *sun{5l1c3d_p1cKl35_4nd_0N10N2}*

