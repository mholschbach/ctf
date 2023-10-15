# BeepBoop Blog
> A few robots got together and started a blog! It's full of posts that make absolutely no sense, but a little birdie told me that one of them left a secret in their drafts. Can you find it?

## Challenge
You are given the URL to the blog https://beepboop.web.2023.sunshinectf.games

## Solution
The web site shows a list of blog posts and you can guess the URL of a single post from the source code. Then download all posts and look for the posts, where the key hidden is true.

```shell
#!/bin/sh

for ((i=1; i<=1024;i=i+1))
do
	curl -k https://beepboop.web.2023.sunshinectf.games/post/$i > $i.json
done
```

```shell
grep \"hidden\":true *.json
608.json:{"hidden":true,"post":"sun{wh00ps_4ll_IDOR}","user":"Robot #000"}
```
