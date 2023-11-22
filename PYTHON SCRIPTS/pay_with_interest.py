gg = input('what is your pay')
ss = input('what are your hours')
hh = float(gg)
dd = float(ss)
if dd > 50:
    reg=hh * dd
    ovt=(dd - 50) * (hh * 0.5)
    print('your pay is equal' , ovt + reg)
else:
    vv=(hh * dd)
    print('kill yourself loser:' , vv)