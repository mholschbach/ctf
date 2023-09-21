# icar
> iCar ist ein experimentelles Anti-Virus Produkt der Firma DBHLabs. Diese Beta-Version kann Testviren erkennen und versucht, diese zu analysieren. Damit die Beta-Version nicht "die Runde macht", wird geprüft, ob die Beta-Version auf einem Computer der DBHLabs läuft. Die Beta-Version kann von anderen Anti-Virus-Lösungen als Virus eingestuft werden, ist jedoch absolut ungefährlich.

## Challenge
Given is the file [iCar.exe](iCar.exe) and the description text.

## Solution
I started with strings and ghidra to see if there was already something interesting to find and found nothing of use. But iCar sounds to similar to EICAR [^1], so lets start by executing the binary using Wine and Kali Linux.

```console
wine iCar.exe
```
The output contains a long list of environment variables, some marketing and ended with this line:
```
Bitte den Testvirus vor dem Start in das aktuelle Verzeichnis kopieren.
```
After downloading eicar.com into the same folder the end of the output changed to:
```
CHECK: Testvirus gefunden.

Aus Sicherheitsgruenden wird der Testvirus nur auf Computern der Firma DBHLabs analysiert.
Bitte richten Sie Ihren Computer entsprechend ein.
```
I was interested if wine itself would allow to change some of the environment variable but didn't make any progress. A wild and lucky guess was to change the hostname before starting wine:
```console
sudo hostname DBHLabs; wine iCar.exe
```
and the output changed to
```
CHECK: Testvirus gefunden.

CHECK: Plausibilitaetspruefung fuer DBHLabs-Computer erfuellt.

Testvirus wird analysiert...

OK: DBH{e1c4r_t3sTf1l3_i5t_l3g3nDe}
```

[^1]: https://www.eicar.com/download-anti-malware-testfile/
