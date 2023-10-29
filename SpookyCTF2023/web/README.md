# Category web

## Aliens Make Me Wanna Curl 254

### Challenge
>We are expecting communications from an artificial intelligence device called MU-TH-UR 6000, referred to as mother by the crew. We disabled the login page and implemented a different method of authentication. The username is mother and the password is ovomorph. To ensure security, only mothers specific browser is allowed.

### Solution
CURL!
```shell
curl -H "User-Agent: MU-TH-UR 6000" -u "mother:ovomorph" -v https://spooky-aliens-make-me-wanna-curl-web.chals.io/flag
NICC{dOnt_d3pEnD_On_h3AdeRs_4_s3eCu1ty}
```

## Ghosts in the Code 403

### Challenge
>Some student here spun up a site where people are submitting their stories about all of the spooky stuff on campus!
>
>This site is clearly haunted... or, at the very least, cursed.
>
>https://niccgetsspooky.xyz
>
>Flag Format: NICC{w0rds_may_c0nta1n_nums_and_chars!?} - but there are no apostrophes, commas, for colons

### Solution
This one was a treasure hunt! There are six parts of the flag and they were hidden here:
```pre
1) https://niccgetsspooky.xyz/js/scary.js
 // You found part one:)
    alert("BOO! ahh! You found part one... -> NICC{gh0sts");

2) https://niccgetsspooky.xyz/css/bootstraps.css
  .flg-txt-pt2{
	  value: '_c@n_b3_tr1';
  }

3) https://niccgetsspooky.xyz/js/scary.js
"They shouted that you found the third!: cky_2_s33_b",

4) https://niccgetsspooky.xyz/
<img class="oh cemescary" src="../../../../4thPartofyourflag/'u7_n0t_1f_y'"

5) Cookie (I found it using curl, continuing from the previos challenge)
curl -v https://niccgetsspooky.xyz/
Set-Cookie: flagpart5=0u_kn0w_wh3; Secure; HttpOnly; SameSite=Strict

6) https://niccgetsspooky.xyz/
 <!--the final piece of your puzzle: r3_2_l00k!} -->

NICC{gh0sts_c@n_b3_tr1cky_2_s33_bu7_n0t_1f_y0u_kn0w_wh3r3_2_l00k!}
```

## Jasons Baking Services 502

### Challenge
>Hey intern! We were able to swipe Jasons application from Github, see if you can find anything useful in the code that will allow you to exploit the real application.
>
>(Be ready to be flash-banged, the web-app is all white!)

### Solution
A nice challenge on JSON Web Signatures. You were able to find the *secret* hash for the HS256 algorithm to sign the JWT and from there create your own token. Very helpful for JWT is https://jwt.io

Register and login to Jasons Baking Service and receive a token with your browser, paste this token (or the following example) to the jwt.io page:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWRtaW4iLCJhdXRob3JpemVkIjp0cnVlLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTY5ODUyMDgzMywiZXhwIjoxNjk4NTIxMTMzfQ.s0RNkXAfw6g4wIsiJHriFYW2Im38PGQKe_l82WY-tVE 

Update the payload to "admin": true, add the found secret y5ABWPpr76vyLjWxZQZvxpFZuprCwAZa6HhWaaDgS7WBEbzWWceuAe45htGLa and get a freshly signed token. Exchange the token in your browser with the new one and open this URL: https://spooky-jason-bakeshop-web.chals.io/flag

```pre
NICC{jWoT_tOkeNs_nEed_saf3_secr3ts}
```

## Dig Up Their Bones 713

### Challenge
>That blog seems suspicious and I bet that there's more to it than meets the eye.
>
>See if you can dig up anything about the owner of the site?
>
>You'll know what you're looking for once you find it.
>
>https://niccgetsspooky.xyz

### Solution
DIG!
```shell
dig -t TXT niccgetsspooky.xyz

NICC{gh0sts_ar3_h4rd_2_f1nd}
```

## Space Intruders 997

### Challenge
> Our space ship was hacked a few days ago. We have made sure to improve our security posture by changing all default credentials. We made sure to stop invalid logins by limiting username input to a length of 3 including an equals, legacy software is a pain but it should be secure now.
