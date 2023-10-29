# Category forensics

## Don't stick me there! 50

### Challenge
>I woke up after a night out and I'm hurting uh... everywhere... I think I left my phone at one of the bars we were at last night. Thankfully, I was able to see the last photo I took through the cloud.
>
>Can you help me find my phone? I need to know the name of the bar and when the photo was taken.
>
>flagformat: NICC{Bar_Name-HH:MM:SS}

### Solution
The EXIF information from the picture included the GPS position 40° 42' 33.02" N  73° 56' 14.04" W and the time the picture was created.
A google maps search led to the place
```
NICC{The_Anchored_Inn-03:47:12}
``

## abducted 399

### Challenge
>I was going to just give you this flag, but the alien mothership downloaded it and deleted it from my computer!
>
>We managed to get a snapshot of their mothership before it got away but it's in some weird proprietary format, can you find the flag they stole?

### Solution
I don't like challenges where you have to download gigabytes.

## I Have Become Death

### Challenge
>Oh boy... Things are becoming hectic and it is stressing me out.
>
>My computer seems to be haunted as it prevents me from starting up my computer.
>
>Thankfully, after multiple resets - it stopped. I checked the logs and it is in these weird folders named after COD maps. Can you discover which file, with its extension, and the time, keep as is, it was executed?
>
>Flag Format: NICC{nameOfFile.extension_00:00}


## Halloween Masks Are Overrated

### Challenge
> My friend who is into aliens, has been acting weird lately.
>
>Ever since he learned about some weird technique musicians used in the 1980s, he has been losing his mind.
>
>The last message he sent me was this image of an alien mask, it might one of the masks from his big halloween mask collection.
>
>Can see if there is anything in this image he sent me?

### Solution
I used binwalk to extract flag.mp3 from the given jpg. And I reversed the mp3 with audacity and was able to hear three differnt voices. But not able to separate the voices or understand them.

## Like Clockwork

### Challenge
>It happens every year, just like clockwork. The campus is packed until the first set of exams. Then it gets a little less crowded. This case might be different though.
>
>Anna Circoh says she saw the owner looking panicked and sweaty. Well, sweatier than normal anyway. Then the alert went out about the UFO over newark. He hit a few keys and then left his laptop behind, running away from campus. Anna grabbed it in case he comes back, but I think something deeper is happening.
>
>I've never seen someone leave a laptop behind, though. It's strange, too - because this laptop seems wiped clean! What student here has an empty laptop? Mine's filled with half working programs and at least 12 revisions to the last essay I had to write. Seriously, not even a game on here.
>
>We had our team take an image of it, but with all of the commotion due to, well, everything, we can't spare the time to figure out what the deal is.
>
>Can you give this a thorough once over to see if there's anything to it?
>
>Flag format: Flag will be exactly as you see it.

### Solution
I don't like challenges where you have to download gigabytes.

## Down the Wormhole

### Challenge
>An explosive chase with a UFO led us to a wormhole!
>
>Make sure you have your bases covered before you head in and find the secrets hiding inside!

### Solution
Using exiftool you found this comment in the wormhole.jpg: cGFzc3dvcmQ6IGRpZ2dpbmdkZWVwZXI=, which decodes to "password: diggingdeeper".

Using the wormhole.jpg with the password diggingdeeper and this URL: https://futureboy.us/stegano/decinput.html provided this:

After diving through the wormhole, you find yourself in front of a rabbit hole. What secrets lie inside?

https://niccgetsspooky.xyz/r/a/b/b/i/t/h/o/l/e/rabbit-hole.svg

After download the huge rabbit-hole.svg file, its content contained a large baseNN encoded text. Remove everything else and base32 -d this part gives a file, that was gzip of secrets666.zip.bz2. From there I used this shell script:

```shell
#!/bin/bash

NUM=666

while
    echo $NUM
    
    gunzip secrets${NUM}.zip.bz2.gz
    bunzip2 secrets${NUM}.zip.bz2
    unzip secrets${NUM}.zip
    rm secrets${NUM}.zip
    
    NUM="$((NUM-1))"
    [ "$NUM" -gt -1 ]
do :; done
```

At the end was a flag.txt file with this content
```pre
NICC{TH3-UF0S-4R3-UP-N0T-D0WN-50-WHY-4R3-Y0U-D0WN-H3R3}
```



