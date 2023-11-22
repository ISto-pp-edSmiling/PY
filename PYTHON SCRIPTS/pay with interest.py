gg = input('what is your pay: ')
for line in gg:
    try:
        hh = float(line)
    except:
       print ('numeric value please')
       continue
ss = input('what are your hours: ')
for sam in ss:
    try : dd = float(sam)
    except: 
        print('enter a numeric value!')
        continue    
if dd > 50:
    reg=hh * dd
    ovt=(dd - 50) * (hh * 0.5)
    fuck=ovt + reg
    print('your pay is equal' , round(fuck, ndigits=1))
else:
    vv=(hh * dd)
    print('kill yourself loser:' , round(vv,  ndigits=1))