# hashpump
> Kannst du die Verschluesselung knacken und wirst du VIP?

## Challenge
Given is the file [challenge.py](challenge.py) and the name of the challenge.

## Solution
You can start the server side locally and take a look at what the server is sending from a second shell:

```console
python3 challenge.py
telnet localhost 10000
```

If you send the example hex string back to the server, the response will include the name of the user which started the server.

After a look in the source code you can see that the second part of the hex string is the sha512 hash value of a string starting with a secret key and ending with the command. This use of SHA512( SECRET || MESSAGE) is vulnerable to a length extension attack [^1] which allows to compute SHA512( SECRET || MESSAGE || EXTENSION ) without knowing the SECRET.

It took me more time than necessary to recognize that the existing exploit code was called hashpipe of all things. The decision to download the source code of hashpump and compile the binary was also not a good one, because I never solved all encoding issues.

It was much easier to install an additional python environment using pyenv [^3] (installation and selecting the environment is documented there) and install hashpumpy into this environment:

```console
curl https://pyenv.run | zsh
...
pyenv install 3.9
...
pip install hashpumpy
```

You will have to update the receive variable in [solve.py](solve.py) and you can set the additional commands in the data_to_add variable. All the heavy lifting is done by the call to hashpumpy:

```
newdigest, newcommand = hashpumpy.hashpump(hexdigest.decode(), command, data_to_add, keylen)
```

Take a look at HMAC [^2] now and never fail the temptation to invent your own crypto.

[^1]: https://en.wikipedia.org/wiki/Length_extension_attack
[^2]: https://en.wikipedia.org/wiki/HMAC
[^3]: https://github.com/pyenv/pyenv
