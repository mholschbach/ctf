# secure-login
> AES-GCM ist Authenticated Encryption. Damit sind meine Login-Tokens kryptographisch sicher!

## Challenge
Given is an archive [files.tar.gz}(files.tar.gz) of a flask application and the description text.

## Solution
I didn't solve this challenge during the CTF. But here is an explanation how a wrong usage of AES-GCM leads to a serios weekness although AES-GCM itself is a strong encryption scheme and therefore used in many applications.

### AES-CBC
If you take a look at [^1] you see that the output of AES in CBC mode is always a multiple of the block size and each line is almost completly different from the other lines. On top of that you would not reuse the initialisation vector IV multiple times. If you enable the "AES decrypt" module, you will see that output and input match after decryption.

### AES-GCM
At [^2] you see that AES in Galois/Counter Mode outputs a ciphertext with the same length as the cleartext and an additional tag of 16 bytes. Further interesting observation is that the ciphertext is only extended for each additional input character - only if you reuse the IV of course. Decryption works as shown in [^3] and you can not modify the ciphertext without producing a decryption error.

#### And why is it different in the application?

Because the implementer used python functions, which did not care about the tag. See [AESGCM.py](AESGCM.py) for details.

In my opinion this is a clear deficiency of the library! If you select AES in GCM mode then the library should prevent you from using the encrypt() resp decrypt() functions and remind you to use the encrypt_and_digest() resp. decrypt_and_verify() functions instead.

[^1]: https://gchq.github.io/CyberChef/#recipe=Fork('%5C%5Cn','%5C%5Cn',false)AES_Encrypt(%7B'option':'Latin1','string':'onequickbrownfox'%7D,%7B'option':'Latin1','string':'somerandomstring'%7D,'CBC','Raw','Hex',%7B'option':'Hex','string':''%7D)AES_Decrypt(%7B'option':'Latin1','string':'onequickbrownfox'%7D,%7B'option':'Latin1','string':'somerandomstring'%7D,'CBC','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D/disabled)&input=YQphZAphZG0KYWRtaQphZG1pbgphZG1pbjE
[^2]: https://gchq.github.io/CyberChef/#recipe=Fork('%5C%5Cn','%5C%5Cn',false)AES_Encrypt(%7B'option':'Latin1','string':'onequickbrownfox'%7D,%7B'option':'Latin1','string':'somerandomstring'%7D,'GCM','Raw','Hex',%7B'option':'Hex','string':''%7D)&input=YQphZAphZG0KYWRtaQphZG1pbgphZG1pbjE
[^3]: https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'Latin1','string':'onequickbrownfox'%7D,%7B'option':'Latin1','string':'somerandomstring'%7D,'GCM','Hex','Raw',%7B'option':'Hex','string':'253b9f77822aba0feb111b9b6d74569b'%7D,%7B'option':'Hex','string':''%7D)&input=Yjc3NjQ0YjEzNGI2
