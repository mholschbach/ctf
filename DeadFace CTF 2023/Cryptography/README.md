# Category Cryptography

## Coin Code 10

### Challenge
> We found this image of a coin that belongs to a member of DEADFACE. The image has something to do with the encoded message. We believe the message indicates who this DEADFACE actor wants to target next. Figure out who the target is.
> 
> Submit the flag as flag{Target Name} (e.g., flag{Bob's Auto})
> 
> The encoded message reads: Fwpl lsjywl xgj ew oadd tw Smjgjs Hzsjes.

### Solution
Use the message with CyberChef and ROT13 Brute Force. You can also take a look at the provided picture of the [coin](https://tinyurl.com/2k239ux9).

[CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'')&input=RndwbCBsc2p5d2wgeGdqIGV3IG9hZGQgdHcgU21qZ2pzIEh6c2plcy4)

Amount =  8: Next target for me will be Aurora Pharma.
```pre
flag{Aurora Pharma}
```

## Letter Soup 10

### Challenge
> We believe we have ran into one of the newest members of DEADFACE while they were waiting for the train. The member seemed to have gotten spooked and stood up suddenly to jump on the train right before the doors shut. They seemed to have gotten away, but dropped this innocent looking word search. I believe this member might be actually a courier for DEADFACE. Let’s solve the word search to decode the mystery message. We believe the message might tell us their next move.
> 
> Submit the flag as flag{TARGETNAME} (e.g., flag{THISISTHEANSWER})
>
> [Deadface_Word_Search.png](https://tinyurl.com/mr2yufep)

### Solution
I crossed out the letters of all the given words and then entered the remaining letters:
[CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'')&input=bXNobmh6aXNoanJtbGhhb2x5enpvcHVscHVhb2x6YnU)

Amount = 19: flagasblackfeathersshineinthesun

```pre
flag{asblackfeathersshineinthesun}
```

## B1Tz and B0Tz 25

### Challenge
> Yet another message was left at the scene. Perhaps they think they are giving us a lesson…either way report back to us what this says but dont give us guesses! Make sure you check your work!
> 
> Submit Flag as flag{hiddenmessage}

### Solution
First convert from binary with
[CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)&input=MDExMDAxMDAgMDExMDExMTEgMDExMDExMTAgMDExMTAxMDAgMDAxMDAwMDAgMDExMDAxMTAgMDExMDExMTEgMDExMTAwMTAgMDExMDAxMTEgMDExMDAxMDEgMDExMTAxMDAgMDAxMDAwMDAgMDExMTAxMDAgMDExMDEwMDAgMDExMDAxMDEgMDAxMDAwMDAgMDExMDAwMTAgMDExMDAwMDEgMDExMTAwMTEgMDExMDEwMDEgMDExMDAwMTEgMDExMTAwMTEgMDAxMDAwMDEgMDAxMDAwMDAgMDExMDAwMTAgMDExMTAxMDEgMDExMTAxMDAgMDAxMDAwMDAgMDExMTEwMDEgMDExMDExMTEgMDExMTAxMDEgMDAxMDAwMDAgMDExMDAxMDAgMDExMDEwMDEgMDExMDAxMDAgMDExMDAxMDAgMDExMDExMTAgMDExMTAxMDAgMDAxMDAwMDAgMDExMTAxMDAgMDExMDEwMDAgMDExMDEwMDEgMDExMDExMTAgMDExMDEwMTEgMDAxMDAwMDAgMDExMDEwMDEgMDExMTAxMDAgMDAxMDAwMDAgMDExMTAxMTEgMDExMDExMTEgMDExMTAxMDEgMDExMDExMDAgMDExMDAxMDAgMDAxMDAwMDAgMDExMDAwMTAgMDExMDAxMDEgMDAxMDAwMDAgMDExMTAxMDAgMDExMDEwMDAgMDExMDAwMDEgMDExMTAxMDAgMDAxMDAwMDAgMDExMDAxMDEgMDExMDAwMDEgMDExMTAwMTEgMDExMTEwMDEgMDAxMDAwMDAgMDExMDAxMDAgMDExMDEwMDEgMDExMDAxMDAgMDAxMDAwMDAgMDExMTEwMDEgMDExMDExMTEgMDExMTAxMDEgMDAxMTExMTEgMDAxMDAwMDAgMDEwMDEwMDAgMDEwMDAwMDEgMDEwMDEwMDAgMDEwMDAwMDEgMDEwMDEwMDAgMDEwMDAwMDEgMDEwMDEwMDAgMDEwMDAwMDEgMDEwMDEwMDAgMDEwMDAwMDEgMDAxMDAwMDAgMDEwMTAwMTEgMDExMDEwMDEgMDExMDExMDAgMDExMDExMDAgMDExMTEwMDEgMDAxMDAwMDAgMDEwMTAxMDAgMDExMTAxMDEgMDExMTAwMTAgMDExMDAwMTAgMDExMDExMTEgMDExMTAwMTEgMDAxMDAwMDEgMDAxMDAwMDAgMDEwMDExMDEgMDExMDExMTEgMDExMTAwMTAgMDExMDAxMDEgMDAxMDAwMDAgMDEwMDExMDAgMDExMDEwMDEgMDExMDEwMTEgMDExMDAxMDEgMDAxMDAwMDAgMDEwMTAxMDAgMDExMTAxMDEgMDExMTAwMTAgMDExMDAwMTAgMDExMDExMTEgMDAxMDAwMDAgMDEwMTAxMDAgMDEwMDAwMDEgMDEwMDAwMTEgMDEwMDEwMTEgMDEwMTEwMDEgMDAxMDAwMDEgMDAxMDAwMDEgMDAxMDAwMDEgMDAxMDAwMDEgMDAxMDAwMDAgMDEwMDAxMTEgMDExMDExMTEgMDAxMDAwMDAgMDExMDAwMDEgMDExMDEwMDAgMDExMDAxMDEgMDExMDAwMDEgMDExMDAxMDAgMDAxMDAwMDAgMDExMDAwMDEgMDExMDExMTAgMDExMDAxMDAgMDAxMDAwMDAgMDEwMTAwMTAgMDEwMDExMTEgMDEwMTAxMDAgMDAxMDAwMDAgMDAwMDEwMTAgMDAxMTAxMTEgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMTAgMDEwMDAxMDEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAxMDAgMDAxMDAwMDAgMDAxMTAxMTEgMDEwMDAwMTAgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMTEgMDAxMDAwMDAgMDAxMTAxMTAgMDEwMDAxMDEgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAwMDEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAwMDEgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMDEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAwMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAwMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMDEgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAwMTAgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMTEgMDAxMDAwMDAgMDAxMTAxMTEgMDEwMDAxMDAgMDAwMDEwMTA)

Take the last line of the output and "Go ahead and ROT":
[CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')ROT13_Brute_Force(true,true,false,100,0,true,'')&input=NzMgNzkgNkUgNzQgN0IgNzMgNzkgNzYgNjMgNzYgNjcgNkUgNjEgNzEgNjUgNzIgNjkgNzIgNjUgNjYgNzIgNzYgNjcgN0Q)

Amount = 13: flag{flipitandreverseit}

No need to flip and reverse:
```pre
flag{flipitandreverseit}
```

## Refill on Soup 75

### Challenge
> How could we have missed this?? There were TWO word searches stuck together that the DEADFACE courier dropped. We’ve already solved the first one, but maybe solving this second word search will help us uncover the secret message they’re trying to covertly relay to the other members of DEADFACE. Hopefully, THIS will tell us how they plan to execute their next move.
> 
> Submit the flag as flag{TARGETNAME} (e.g., flag{THISISTHEANSWER})
>
> [Deadface_Word_Search_Part_2.png](https://tinyurl.com/yc2bvkwp)

### Solution
I crossed out the letters of all the given words and then entered the remaining letters in
[CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'')&input=bnZhdmFvbHNoemFzcHVsbXZ5YW9sbXNobmh1emRseWFvaGFudmx6cHV6cGtsYW9saXloanJsYXp6YXZ3bnF3a2RkZXZ3emx6dGpudGh4c2tlYWR2dWNidnRybGhzd2VlYmdiZHRoaHphb2xmbXNmaGp5dnp6)

Amount = 19: **gotothelastlinefortheflaganswerthatgoesinsidethebracketsstop**gjpdwwxopsesmcgmaqldxtwonvuomkealpxxuzuw

Take only the last line of the remaining letters:
[CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'')&input=aHphb2xmbXNmaGp5dnp6)

Amount = 19: astheyflyacross

The default setting for ROT13 Brute Force in CyberChef only outputs the first 100 characters, otherwise you could have already seen the solution.

```pre
flag{astheyflyacroos}
```

## HAM JAM 75

### Challenge
> It seems as if there is an upcoming hack that the rest of DEADFACE is planning, but someone didn't seem to get the memo. So, instead of risking meeting up to share the date, one of them has used a ham radio to send a message we managed to intercept.
>
> We also identified some chatter associated with the coded message, but we have not been able to figure it out. It’s possible there might be clues left on their message board?
>
> Submit the flag as flag{Month-Day#}. Example: flag{DECEMBER-10}.

### Solution

Using the [WAV](https://tinyurl.com/3v7vfejx) file with https://morsecode.world/international/decoder/audio-decoder-adaptive.html will give you "T H E K E Y I S H A C K T H E P L A N E T".

You can find a discussion in Ghost Town, which mentions "HAM": https://ghosttown.deadface.io/t/rendezvous-lets-goooooo/127/6

I then used https://products.aspose.app/barcode/de/recognize#/recognized to read the bar code: "YEOOFIIGEHRJBMTJYYUSKPMOIK"

A scrambled text together with a password can always indicate Vigenere encryption:
[CyberChef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('HACKTHEPLANET')&input=WUVPT0ZJSUdFSFJKQk1USllZVVNLUE1PSUs)

REMEMBERTHEFIFTHOFNOVEMBER

```pre
flag{NOVEMBER-5}
```

## Color Me Impressed

## Off Again On Again

## Halloween +1

## Up in the Air 250

### Challenge
>We found this unencrypted file that was shared between two members of DEADFACE, We haven't been able to understand what it means just yet but perhaps you can? Its supposed to be some sort of message or password to something but it just looks like nonsense.
>
>Submit Flag as flag{H1DD3NM355@G3}

### Solution
A359 an Airbus 359, B767 a Boeing 767, DH8C a Dash 8? And MSNs are the serial numbers for aircraft.

I used different web sites to find the registration number, https://www.flightradar24.com/data/aircraft/ was one of them. For the planes that Flightradar didn't know about I used an ordinary web search, which sometimes provided multiple registration strings.

I started to fill this table. Char:6 meant the six character of the registration, and ASCII:456 to convert the 4th to 6th character (which were numbers). I tried Octal, Decimal and Hex. After a few failed submissions, I saw the leetspeak: B18PH@RM@5UX

```pre
Look4Reg                                                        Char    Oct    Dec  Hex
T:A359 MSN:102 Char:6 ASCII:-               A7-ANB (F-WZFY)     B (Y)
T:E190 MSN:19000171 Char:4 ASCII:-          B-3120              1
T:B767 MSN:29451 Char:- ASCII:456           N66056                      056=.   8   V
T:AT75 MSN:0680 Char:2 ASCII:-              RP-C6638            P
T:AT45 MSN:0649 Char:1 ASCII:-              HK-5199             H
T:B767 MSN:29459 Char:- ASCII:456           N76064                      064=4   @   d
T:E170 MSN:17000053 Char:5 ASCII:-          N638RW              R
T:A388 MSN:177 Char:5 ASCII:-               D-AIMN              M
T:B767 MSN:34080 Char:- ASCII:678           19-46064                    064=4   @   d
T:B767 MSN:29448 Char:- ASCII:456           N59053                      053=+   5   S
T:DH8C MSN:373 Char:4 ASCII:                C-FUQY C-GFQL       U (F)
T:SF34 MSN:340B-164 Char:5 ASCII:-          SE-KXG              X

flag{B18PH@RM@5UX}
```


## Reflections

## Slothy
