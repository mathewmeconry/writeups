# HackVent 2016

Another edition of Hacking-Lab's annual advent calender CTF. Every day between December 1 and Christmas, a new challenge is released. Solve it on the day of release for maximum points, solve it later (but before the new year) for one point less.

## Overview
```
Title                                     Flag
----------------------------------------  -----------------------------
Hidden: We are people, not machines       HV17-bz7q-zrfD-XnGz-fQos-wr2A
Day 01: 5th anniversary                   HV17-5YRS-4evr-IJHy-oXP1-c6Lw
Day 02: Wishlist                          HV17-Th3F-1fth-Pow3-r0f2-is32
```

## Hidden: We are people, not machines
Go to [https://hackvent.hacking-lab.com/robots.txt](https://hackvent.hacking-lab.com/robots.txt) and you'll see ```We are people, not machines```.
Follow this hint and go to [https://hackvent.hacking-lab.com/humans.txt](https://hackvent.hacking-lab.com/humans.txt).
```
All credits go to the following incredibly awesome HUMANS (in alphabetic order):
avarx
DanMcFly
HaRdLoCk
inik
Lukasz
M.
Morpheuz
MuffinX
PS
pyth0n33

HV17-bz7q-zrfD-XnGz-fQos-wr2A
```

## Day 01
### Description
Day 01: 5th anniversary
time to have a look back

![](Desciptions/HV17-hv16-hv15-hv14.svg)

### Solution
Thanks to shiltemann for the writeups of the years 2014,2015 and 2016 to get the flags.
[https://github.com/shiltemann/CTF-writeups-public](https://github.com/shiltemann/CTF-writeups-public)

```
Flag 2014: HV24-BAAJ-6ZtK-IJHy-bABB-YoMw
Flag 2015: HV15-Tz9K-4JIJ-EowK-oXP1-NUYL
Flag 2016: HV16-t8Kd-38aY-QxL5-bn4K-c6Lw
```
```
Solution: HV17-5YRS-4evr-IJHy-oXP1-c6Lw
```

## Day 02
### Description
Day 02: Wishlist  
The fifth power of two

[Wishlist.txt](./Ressources/Wishlist.txt)

### Solution
```2^5 = 32```

So we can assume that it is base32 encoded. But after the first run, we just got another base32 encoded string.

Let's solve this with python:
```python
import base64

f = open('./Wishlist.txt', 'r')
data = f.read()
while True:
    data = base64.b64decode(data)
    if "HV17" in data:
        print data
        break
```
```
Solution: HV17-Th3F-1fth-Pow3-r0f2-is32
```
