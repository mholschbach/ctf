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

### Solution

## I don't speak Zorglax 991

### Challenge

### Solution

## the spooky sentence## String Theory 1000

### Challenge

### Solution
