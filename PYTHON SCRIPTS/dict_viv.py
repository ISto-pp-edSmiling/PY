viv = dict()                  #not a list but the dict is the most powerful data type... (also the brackets are for show, to make a dict use variable_name = {'input' = x})

viv['money'] = 6
viv['cash'] = 'mulla'
viv['cheddar3'] = 56

print(viv)
viv['money'] = viv['money'] + 5
print(viv['money'])

gg = {'house' : 'dog', 'ralph' : 6}
print(gg['house'])

if 'house' in gg:
    x = gg['house']
else:
    x = 0

print(x)

x = gg.get('hse', 0)

print(x)