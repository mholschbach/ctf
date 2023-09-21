# FeO
> Mit FeO kannst du deine Dateien sehr sicher verschlüsseln! Die Flag wurde damit verschlüsselt.

## Challenge
Given are the binary [FeO](FeO) and an encrypted file [flag.txt.enc](flag.txt.enc).

## Solution
This was actually the first challenge I was able to solve using Ghidra. It took me much more time to find all the information than the short description suggests:

Use Ghidra to open the FeO binary and start the decompilation with ghidra's CodeBrowser.

In Ghidra's Symbol Tree windows look for Namespaces->FeO->FeO->main and double click on main to display the decompiled main function in the right most window.

Then double click on the generate_key function and take a closer look in Ghidra's Listing window with all the assembler instructions. You will find multiple entries of the form

```
ESI,0x76
ESI,0x33
...
ESI,0x21
```
and when you put all of the hex values together you get the string "v3ry_53cur3_k3y!". Looked promising, but this was not the key. Take another look at the generate_key function and you will find a while(true) loop which XORs with 0x55, which gav

Back to the main function and double click on the encrypt_file function, scroll a bit down to find the call of the encrypt function in line 170 and double click on the encrypt function. Scroll down to line 83 beginning with block_modes::traits::BlockMode and hover of the new_from_slices string in this line. From there I took the information that AES128 in CBC mode was used for encryption and I had to find an IV now. In Ghidra's Listing window of the encrypt function you will find multiple entries of the form

```
MOV byte ptr [RSP + local_9c0],0x56
MOV byte ptr [RSP + local_9bf],0x6d
...
MOV byte ptr [RSP + local_9b1],0x48
```
and when you put all of the hex values together you get the string "VmYq3t6w9z4B6E9H". A simple validation if you found enough ASCII values: How many bytes are necessary for the key and IV if AES128 is used?

For the last step I used CyberChef and put everything together to decrypt the [flag](https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'Hex','string':'23%2066%2027%202c%200a%2060%2066%2036%2020%2027%2066%200a%203e%2066%202c%2074'%7D,%7B'option':'Latin1','string':'VmYq3t6w9z4B6E9H'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=syLs9GhQBrGC/no/dofVDnQaxuLVq%2BncYz79NaShKnBdw4fJojDB4dZ1F8W8Pf1c).
