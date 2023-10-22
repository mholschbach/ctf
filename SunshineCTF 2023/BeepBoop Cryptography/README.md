# BeepBoop Cryptography
> Help! My IOT device has gone sentient! All I wanted to know was the meaning of 42! It's also waving its arms up and down, and I... oh no! It's free! AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA Automated Challenge Instructions Detected failure in challenge upload. Original author terminated. Please see attached file BeepBoop for your flag... human.

## Challenge
You are given the file [BeepBoop](BeepBoop).

## Solution
*beep* and *boop* could be a binary encoding, let's start with cyberchef [^1].

[^1]: https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':'beep'%7D,'0',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'boop'%7D,'1',true,false,true,false)Remove_whitespace(true,false,true,false,false,false)From_Binary('None',8)ROT13(true,true,false,13)&input=YmVlcCBiZWVwIGJlZXAgYmVlcCBib29wIGJlZXAgYm9vcCBiZWVwIGJlZXAgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBiZWVwIGJvb3AgYm9vcCBiZWVwIGJvb3AgYmVlcCBiZWVwIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBiZWVwIGJlZXAgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJvb3AgYm9vcCBiZWVwIGJvb3AgYm9vcCBiZWVwIGJvb3AgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYm9vcCBiZWVwIGJvb3AgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBiZWVwIGJvb3AgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJvb3AgYm9vcCBiZWVwIGJvb3AgYmVlcCBiZWVwIGJvb3AgYm9vcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBiZWVwIGJlZXAgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYm9vcCBib29wIGJvb3AgYmVlcCBiZWVwIGJvb3AgYm9vcCBiZWVwIGJlZXAgYm9vcCBib29wIGJvb3AgYmVlcCBib29wIGJvb3AgYm9vcCBiZWVwIGJlZXAgYm9vcCBiZWVwIGJlZXAgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYm9vcCBiZWVwIGJvb3AgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYm9vcCBiZWVwIGJvb3AgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBiZWVwIGJvb3AgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJvb3AgYm9vcCBiZWVwIGJvb3AgYmVlcCBiZWVwIGJvb3AgYm9vcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBiZWVwIGJlZXAgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYm9vcCBib29wIGJvb3AgYmVlcCBiZWVwIGJvb3AgYm9vcCBiZWVwIGJlZXAgYm9vcCBib29wIGJvb3AgYmVlcCBib29wIGJvb3AgYm9vcCBiZWVwIGJlZXAgYm9vcCBiZWVwIGJlZXAgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYm9vcCBiZWVwIGJvb3AgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYm9vcCBiZWVwIGJvb3AgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBiZWVwIGJvb3AgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJvb3AgYm9vcCBiZWVwIGJvb3AgYmVlcCBiZWVwIGJvb3AgYm9vcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYmVlcCBib29wIGJvb3AgYmVlcCBiZWVwIGJlZXAgYmVlcCBib29wIGJlZXAgYm9vcCBib29wIGJlZXAgYm9vcCBib29wIGJvb3AgYmVlcCBiZWVwIGJvb3AgYm9vcCBiZWVwIGJlZXAgYm9vcCBib29wIGJvb3AgYmVlcCBib29wIGJvb3AgYm9vcCBiZWVwIGJlZXAgYm9vcCBiZWVwIGJlZXAgYm9vcCBib29wIGJvb3AgYm9vcCBib29wIGJlZXAgYm9vcA