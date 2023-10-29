# Category crypto

## What have we found here... 50

### Challenge
>As the sun dipped below the horizon, casting long shadows across the barren landscape, I stood alone at the edge of the world. The map had brought me here, to this remote and desolate place, in pursuit of a mystery that had captivated the world's greatest minds.
>
>A cryptic message had been found on the ground, a message from the cosmos itself, or so it seemed. It hinted at the existence of extraterrestrial life, hidden within the depths of space. The message, a series of seemingly random characters, held secrets that could change everything we knew about the universe.
>
>My task was to decipher it, to unlock its hidden meaning. The characters appeared to be encoded in a complex language, something that I cannot seem to figure out. The key to understanding lay within those symbols, like a cosmic puzzle waiting to be solved.
>
>As I gazed up at the starry night sky, seeing the Leo Minor constellation in the sky, I knew that the fate of humanity rested on my ability to decode this enigmatic message, to uncover the truth hidden within the stars.

### Solution
```shell
base64 -d found_notes.txt > base64.jpeg
NICC{just_chillin}
```

## If the key fits... 257

### Challenge
>I am trying to escape this 64-story horror house and the only way to escape is by finding the flag in this text file! Can you help me crack into the file and get the flag? The only hint I get is this random phrase: MWwwdjM1eW1tM3RyMWNrM3Q1ISEh

### Solution
The string MWwwdjM1eW1tM3RyMWNrM3Q1ISEh equals 1l0v35ymm3tr1ck3t5!!! when it is base64decode. The encrypted file starts with an header that points to a proprietary software AESCrypt: https://www.aescrypt.com/download/

Use this software to decrypt and you get the flag:
```pre
NICC{1-4m-k3yn0ugh!}
```

## making contact 709

### Challenge
>The aliens have sent us a clue on how to make contact with them! A crate appeared mysteriously underneath the NJIT clock tower containing two artifacts. We convinced a freshman to grab it for us while the rest of the campus was going nuts.
>
>The first was a comic book about strange adventures written by a King. The second is a scrap of paper with the text "TNPIOEKNOPYZNUNZFKGUKFHEIRCU".
>
>The aliens seem to really love these comics and have been following them since they released a few years ago. They especially love one of the main characters and his motto.
>
>Who knows, they could be using this motto as a way to acclimate to earth culture? The motto could be the method and key to everything? If you manage to crack this code you should be able to contact the aliens!
>
>format: NICC{solution here} or nicc{solutionhere}

### Solution
The difficult part was to find out that Tom King wrote a comic series called Strange Adventures. And a Mr. Terrific for whom "Fair Play" is a credo to live by. Playfair is also an encryption algorithm.
Using an online decrypter like this one https://de.planetcalc.com/7751/, you receive 
STRANGESTADVENTUREEVERGMAILX back. To really get the flag, you needed to send an email to strangestadventureever@gmail.com and received a reply from the Alien Visitor:

```pre
Ayyyyyy yo its me the aliens. Here's your flag: nicc{p4Z87d7L4c}
```

## strange monuments 750

### Challenge
>Indiana is searching for alien artifacts deep in the jungle. He's following a winding river, and in order to not get lost he has charted its flow with the equation y^2 = x^3 + 7586x + 9001 (mod 46181).
>
>Every point on the river's flow represents the site where an alien monument has been reported. Indiana starts at the monument location denoted on his chart with the point (20305,32781).
>
>He follows the flow of the river from that monument and passes many others. However, he loses count due to some snakes that he had to run from! Indiana is now at the monument marked with the point (39234,12275) on his chart.
>
>How many monuments did Indiana pass in total?

### Solution
A nice ECC challenge with Indy! The solution lies in point multiplication on the given curve. Looking for N with N times 20305 equals 39234. I found this online tool https://asecuritysite.com/ecc/ecc_points_mult but for N>20 it was useless. The [sourcecode](solve_strangemonuments.py) instead was usable:

```shell
python3 solve_strangemonuments.py | grep 39234
3000P	(39234,12275)   	Point is on curve

The flag NICC{3000} wasn't correct, but "How many monuments did Indiana pass in total?" lead to:
NICC{2999}
```

## I don't speak Zorglax 991

### Challenge
>... I have no idea what this says. You'll need to figure it out for me. I'm 100% sure that there is a secret message in there, but I don't even know what I'm looking at.
>
>flag format: NICC{whateveryoufind}

### Solution
I wasn't interested to work with the PDF by hand.

## the spooky sentence## String Theory 1000

### Challenge
>It is Halloween night when an eerie green fog rolls in. You are heading back home after having to work the holiday shift at the detective's office. Traveling down the highway, you notice the fog gets thicker as you go. When you can barely see ahead, you notice what appears to be lit windows in the distance but, in a color, you can only think of as bright irradiated mountain dew.
>
>At this instance a deathly girlish scream is heard and you pullover to investigate. You walk up to the mansion and peer into the glowing window, it looks like there are brown splotches all over the inner room. When you open the front door a wall of smell washes over you. It smells like blood. Under the chandelier in front of you is a gigantic green machine spewing green smoke. Suddenly the door slams shut and now you realize it is locked. It starts to feel hard to breathe, this smoke is different from the fog outside.
>
>You desperately try to find a way out, even pulling out your service pistol and trying to break the window with it.
>
>The glass won't break from a simple tap, now even more desperate, you shoot the glass, but it does nothing as it is bulletproof.
>
>At this point you finally realize this is a trap and pass out from the smoke. When you wake up you are in a chair contraption and cannot move anything, darkness is around you with just a weathered note in front of you.
>
>It says:
>
>    "THE_WORDS_MUST_BE_SPOKEN"
>
>Hidden on the bottom in small writing is this string :
>
>    16237b1843709ffff16caa1ae00bece4
>
>The code is very spooky, it gives you the chills.
>
>A voice is heard again, whispering to the void:
>
>    "Do this task and you shall be free."
>
>Enclose what is found as follows NICC{FOUND_FLAG_HERE}.

### Solution
Was about finding a sentence that produced the given hash value.
