# Category bin

## String Theory 50

### Challenge
>I recieved this very weird [email](openme) that only contained a file called "openme", it looks like an executable.
>
>Can you see if there is anything weird in this file?

### Solution
Even a hint to use Ghidra was later given, but nothing beats *strings* in this challenge:

```shell
strings openme | grep NICC
NICC{leaky_data_huh}
```

## Across the Hex

### Challenge
>Who doesn't love a good spooky time crossword?
>
>This [crossword](crossword.bin) has the following words:
>
>    spooky hacker alien ghost pumpkin nicc ctf cybersecurity
>
>The letts can be a mix of uppercase, lowercase, basic 1337 text, raw hex, and basic 1337 text in raw hex.
>
>Easy, right?
>
>The crossword has a width of 16 and a word will never cross the boundary of the width.
>
>The key is the sequence of all correct letters in the crossword file based on the letter position in the file. All raw hex letters are uppercase.
>
>Remember words can be horizontal, vertical, or diagonal and can also be backwards.
>
>How many characters can a byte represent when viewed in raw hex?
>
>The words must be continuous, ex. 0 must not appear in between characters if there is no o in the word. Words that start with a single hex char always start as follows 0x0F for example in no case should a word use random memory before. ex if the word is Fail "\x0F" + "ail" is a possibility while "\x3F" + "ail" is not. This applies for reverse order aswell.
>
>Enclose what is found as follows NICC{FOUND_FLAG_HERE}.

### Solution
I tried to find the given words in a hexdump of the crossword.bin, but without any luck.
```pre
spooky 73 70 6f 6f 6b 79
SPOOKY 53 50 4f 4f 4b 59
5 0    35    30

using this search string in less
/53|75|50|70|4f|6f|4b|6b|59|79|35|30
```
