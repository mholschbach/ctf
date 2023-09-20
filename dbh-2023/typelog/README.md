# typelog
> Wir haben hier diese Datei auf dem Gerät gefunden, tuen uns aber schwer etwas damit anzufangen. Aus zuverlässigen Quellen wissen wir, dass die Besitzerin Engländerin ist, zum Zeitpunkt als die Datei entstand jedoch mit einem Deutschen kommunizierte.

## Challenge
Given is the file [type.log](type.log) and the description text, indicating that a German text was probably written using an English keyboard layout.

## Solution
The given file contains a long list of "events" in chronological order, which appear to be positions of an on-screen keyboard together with the touch "down" and release "up" information. I don't know if the backspace was pressed harder than average, but it was the most frequently pressed key.

My first version of [solver.py](solver.py) used the matplotlib to just print a line between the "down" and "up" pairs. From there I identified which axis should be mirrored and what the approximate distances between the on-screen keys were.

Next I added the function printlayout to print the keyboard layout a bit below where all the lines were printed. That was promising: the letter e was often pressed, the letter y never and the spacebar was also identifiable. I don't know if the backspace was pressed harder than average, but it was the most frequently pressed key.

I thought about an automatic matching of the line positions to the nearest key, but decided to start manually first and then pulled through. For this the final solution draws a group of ten lines with their order of precedence and I wrote the keys down by hand:

> die flagge
> f#fue#er 
> di#iese #
> (...)
> setzt werd
> e#en.#.

The # is representing the backspace and fortunately the englishwoman never mistyped, but deleted and wrote the same letter again.

To get the flag you needed all 39 lines and then had to follow the instructions on how to create the flag.
