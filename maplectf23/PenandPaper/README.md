# Pen and Paper
> A sweet classical cipher. Why use a computer when I have a pen and paper?
> NOTE: please wrap the flag in maple{...}

## Challenge
You get the [ciphertext](ciphertext.txt) and a [python script](source.py).

## Solution
After taking a look at the [source.py](source.py) the *generate_keystream* function indicated a fancy encryption, so let's take a closer look. I modified the *source.py* (available in [printfrequencies.py](printfrequencies.py) to use a simplified key and print the derived keystream. With a line break after 13 elements you easily identify the pattern and the repition after 13 lines:

```
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0,
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 1,
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 1, 2,
4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 1, 2, 3,
5, 6, 7, 8, 9, 10, 11, 12, 0, 1, 2, 3, 4,
6, 7, 8, 9, 10, 11, 12, 0, 1, 2, 3, 4, 5,
7, 8, 9, 10, 11, 12, 0, 1, 2, 3, 4, 5, 6,
8, 9, 10, 11, 12, 0, 1, 2, 3, 4, 5, 6, 7,
9, 10, 11, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8,
10, 11, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
11, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
...
```
We now know that the keystream only uses those 13 values that were chosen by random in the original *generate_key* function and we can start a frequency analysis. We only need to distinguish for each encrypted character which of the 13 positions of the original *key* was used for encryption and the simplified key set in [printfrequencies.py](printfrequencies.py) comes handy again:

```python
if isinstance(indices[i], int):
            encrypted.append(ALPHABET[(keystream[i] + indices[i]) % 26])
            frequencies[keystream[i]][indices[i]] += 1
```

I used the ouput of the frequency table to identify the likely shift of the alphabet. Take a look at letter frequency [^1] for more information. Fairly simple to find are the three vocals a, e and i, which are exactly 3 letters apart in the alphabet. For the first line, the counted values of 12, 16 and 17 could represent those letters and a shift to the right of 14 steps is needed to move the letter a to the first position of the array. Other helpful frequencies to look for are the very rare occurance of the letter z and the higher frequencies of the adjacent letters r,s and t.

```
[7, 4, 0, 6, 10, 9, 4, 0, 0, 0, 5, 0, 12, 0, 9, 5, 16, 2, 3, 3, 17, 0, 1, 5, 1, 9],
14->                                   a            e            i     
[3, 8, 5, 12, 0, 1, 4, 3, 5, 8, 7, 0, 10, 6, 24, 2, 0, 0, 0, 2, 2, 10, 0, 7, 2, 12],
5->        i                                                        a            e
[13, 10, 5, 2, 0, 0, 4, 0, 7, 0, 5, 4, 12, 5, 0, 5, 18, 0, 1, 6, 4, 10, 5, 4, 0, 10],
18->                       a            e            i
[5, 16, 0, 0, 2, 3, 9, 6, 6, 0, 9, 3, 13, 6, 1, 0, 1, 3, 0, 12, 2, 7, 4, 9, 6, 1],
7->  i                                                       a           e
[6, 8, 0, 2, 1, 0, 8, 0, 11, 2, 9, 4, 21, 3, 3, 2, 7, 0, 0, 6, 3, 13, 12, 7, 0, 8],
18->                      a            e           i
[11, 14, 5, 1, 0, 1, 0, 0, 4, 1, 6, 5, 13, 2, 7, 4, 8, 0, 1, 8, 2, 12, 10, 5, 0, 14],
18->                       a            e           i
[3, 14, 0, 1, 6, 0, 8, 6, 2, 0, 7, 7, 14, 2, 2, 1, 0, 3, 0, 12, 1, 3, 0, 16, 3, 8],
7->  i                                                       a            e
[1, 13, 3, 7, 4, 12, 0, 0, 8, 3, 9, 5, 4, 0, 11, 9, 11, 2, 0, 1, 1, 5, 0, 13, 2, 9],
3->  e            i                                                        a
[4, 2, 11, 7, 4, 0, 9, 13, 13, 5, 1, 1, 0, 1, 1, 14, 0, 6, 4, 10, 1, 4, 13, 7, 0, 0],
11->                                              a            e            i
[11, 5, 1, 8, 13, 18, 3, 0, 1, 0, 5, 1, 9, 1, 5, 1, 13, 1, 4, 4, 12, 0, 2, 6, 1, 5],
14->                                    a            e            i
[1, 8, 3, 11, 1, 3, 5, 11, 0, 1, 6, 1, 15, 11, 6, 0, 8, 12, 7, 1, 4, 0, 0, 4, 0, 9],
1->        e            i                                                        a
[0, 3, 5, 9, 8, 6, 1, 9, 7, 12, 4, 1, 1, 0, 3, 0, 12, 0, 4, 2, 22, 2, 4, 2, 14, 0],
10->                                               a            e            i
[5, 3, 0, 16, 9, 9, 4, 2, 2, 0, 3, 0, 12, 2, 9, 8, 6, 2, 6, 6, 7, 0, 1, 3, 5, 12]
14->                                   a           e           i
```

I replaced the *generate_key()* function in the [solve.py](solve.py) script as follows:

```python
def generate_key():
    #return [random.randint(0, 26) for _ in range(13)]
    return [ 14, 5, 18, 7, 18, 18, 7, 3, 11, 14, 1, 10, 14]
```

and was able to read the message in cleartext. The value to use for the flag was part of this sentence *"THE FLAG YOU ARE LOOKING FOR IS VIGENEREWITHATWIST."*

I was unsure at the beginning whether it was really an English text, because there were too many long words. So I used the *solve.py* script incrementally with each guessed value of the key. The confirmation was when I saw some meaningful words or at least parts thereof.

[^1]: https://en.wikipedia.org/wiki/Letter_frequency
