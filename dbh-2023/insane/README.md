# insane
> Die Definition von Wahnsinn ist, immer wieder das Gleiche zu tun und andere Ergebnisse zu erwarten.

## Challenge
Given are a flask application [app.py](app.py) and the corrensponding [Dockerfile](Dockerfile) to build and run the application. I modified the Dockerfile to start flask in debug mode and add the [requirements.txt](requirements.txt) and a template [flag.txt](flag.txt) file for convenience.

```console
sudo docker build -t insane .
sudo docker run insane
sudo docker ps
sudo docker exec -it <containerid> /bin/sh
```

## Solution
The app lets you upload a file and the file is always saved as **prog_rzqnilawqb.c** and this becomes important later. Only then the content validation of the file starts: It must not contain "#" or "#include" - which can be easily replaced by "%:include" if you knew about Digraphs and Trigraphs [^1], but I had to learn.

If the compilation is successful, the binary is copied into a different folder and *sudo -u nobody* is used to execute the binary. Then there is an additional check if the output of the binary exactly matches to the source code. That was when I learned that there is a name for it: quine [^2].

Anyway, if that step was also successful, then a loop starts: take the output from the execution, write it to **prog_rsqnilawqb.c**, wait one second, compile it (without the content validation) and execute it again (without the copy and *sudo -u nobody* part). I tried to mess around with the [quine.c](quine.c), but didn't get far.

Before I went insane, the thought came to me what would happen if I just upload a different file from another browser tab. I don't need to pass the content validation, but maybe the already running process loop from the first browser window will try compile it. I just need to upload within one of these one second pauses between write and read.

All it took was [getflag.c](getflag.c) to raise the FailureException in the function compile(fn) which conveniently prints the stderr output from the compile command to the first browser tab.

[^1]: https://en.wikipedia.org/wiki/Digraphs_and_trigraphs
[^2]: http://www.nyx.net/~gthompso/quine.htm
