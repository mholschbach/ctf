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
