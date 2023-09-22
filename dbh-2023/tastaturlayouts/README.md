# tastaturlayouts
> Ein Freundin von mir experimentiert gerne mit verschiedenen Tastaturlayouts. Leider scheint sie das falsche Tastaturlayout ausgewählt zu haben, denn die Nachricht die sie mir geschickt hat ergibt keinen Sinn..

## Challenge
Given is the file [email.txt](email.txt) and the description text.

## Solution
You can use a tool like CyberChef or a simple script like [solve.py](solve.py). Guessing the first letters is quite easy, you can use a frequency analysis or assume that "KX>[" will become "DBH{" and "hb." will become "ich" and continue from there. At least until the flag itself starts.

## Challenge Assessment
And there lies my issue with this challenge:
Up to the beginning of the flag all the necessary replacements of lower and upper case letters matched perfectly to a US english keyboard (not the whole layout, just the single keyboard keys) and lower case is replaced with lower case and the corresponding upper case with upper case:

| original key | replacement key |
| :-: | :-: |
| . > | h H |
| y Y | f F |
| n N | e E |
| l L | ; : |

and exactly that no longer remains valid for the flag part of the challenge:

| original key | replacement key |
| :-: | :-: |
| 1 | 5 | 
| ! | 1 |

and there are further replacements which collide, when a challenge is called tastaturlayout:

| original key | replacement key |
| :-: | :-: |
| 4 **$** | 0 **)** |
| **6** ^ | **0** ) |

