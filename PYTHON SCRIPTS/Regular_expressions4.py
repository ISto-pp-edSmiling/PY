import re

string = 'baby just keep loving me like you doooo..'
str = re.findall('^baby.+ lo([^e]+)', string)

print(str)