# Category Boo!-sint

## The Wizard 175

### Challenge
>We intercepted a photo intended to be received by a suspected agent working with the Zorglaxians - or so it seems.
>
>We're still decompiling the data, but we think the photo was taken nearby to where the agent was supposed to meet the Zorglaxians.
>
>Can you find the location of the photo while our team works on decrypting the accompanying message?
>
>We need the entire street address, city and abbreviated state or district of where it was taken to send our agents to investigate with the local authorities.
>
>\# = Number
>XX = State abbreviation
>All spaces are underscores
>
>flag format: NICC{#_Street_Address_City_XX}

### Solution
Started with an image search to find this: https://washington.org/visit-dc/where-to-find-street-murals-washington-dc

```pre
NICC{950_24th_Street_NW_Washington_DC}
```

## just go live 372

### Challenge
>Can you seem to find our flag on our service where we stream?
>
>Be careful, things aren't as they seem!

## Lunch with the wizard 586

### Challenge
>Great work finding the location of the photo!
>
>While you were getting the location of the photo, we were able to decrypt the message.
>
>Meet me for lunch. I'll be at my hotel nearby where the queen sits watching the snowy court.
>
>Get us the name of the hotel and the restaurant so we can get there. It might be too late to see them, but we may be able to recover tapes, audio, or other evidence from the scene to figure out their plans.
>
>Time's running out - so make sure you get it right when you send it to us... there aren't a lot of chances to mess this up.
>
>flag format: NICC{The-Hotel-Name_Restaurant-Name}
>
>NOTE: Only use the first part of the restaurant's name. After that seems to be a description that was recently added. Example: If it was at the holiday_inn and the restaurant was Sunshine a burger and bourbon car, you would write: NICC{The-Holiday-Inn_Sunshine}. Note, this is not correct and probably doesn't exist.

### Solution
Starting with the address from *The Wizard* here: https://www.google.com/maps/place/950+24th+St+NW,+Washington,+DC+20052,+USA/@38.9018708,-77.0542021,17z/data=!4m6!3m5!1s0x89b7b7b3ee92881b:0x9fe40fbfef88ed23!8m2!3d38.9022321!4d-77.0517613!16s%2Fg%2F12hkk9r2x?entry=ttu

And then found two streets nearby "Queen Annes Ln" and "Snows Ct". The hotel and restaurant were right there.
```pre
NICC{The-River-Inn_Matera} 
```

## reading the fine print 716

### Challenge
>It's really important to pay attention to the rules of engagement, especially when the stakes are so high.

### Solution
Read it afterwards, the #rules in the discord contained a hidden link.

## Where we're going... 745

### Challenge
>If we're going to explore the universe like the Zorglax, we're going to need a way to get there. I bet there's some geniuses out there who have already figured it out. I heard someone say last November that there was a breakthrough in spacetime propulsion out of Florida of all places. I can't speak for other nations, but I know the US has some real geniuses who have probably already figured it out. I just hope that they patent it so that they get the credit they deserve. If you see anything, can you tell me the unique id so I can look it up? Make sure to give it to me exactly as it appears, wrapped in NICC{} of course.
>
>flag format: NICC{HO-wever-IT-might-appear}

### Solution
Read it afterwards, search for U.S. patents around the time of November 2023. Research is done by the University of Central Florida.

## fake-news 999

### Challenge
>New Jersey is famous for a specific cryptid from the pines. Though it commonly goes by one name, there is another name that it is known by first.
>
>Despite hailing from New Jersey since the mid 1700s, there wasn't a lot of news about it from within the state - but what did exist spoke of it by its original name. When you're that close to its birthplace, you'd put respect on its name, too.
>
>Even more interesting, the cryptid had a "Legion" in the late 1800s within New Jersey - led by an owly man who lived to be one of the oldest men in the Pines.
>
>Twelve years before you could turn to this man in his 80s as your source for information about the cryptid, he was indicted for a crime.
>
>Find his first name, nickname, last name, what he stole, and the pension he was awarded but would be taken away from him if he tried to take it.
>
>Flag format is NICC{firstname_nickname_lastname_whathestole_$pension} <- Yes, include the dollar sign.

### Solution
I read and search quite a lot, found the Jersey Devil but nothing about the owly man.

