#hello = 'be;normal;please'

#bye = hello.split(';')                  #(you can specify a delimiter)

hand = open('bee.txt')

for bee in hand:
    bee = bee.rstrip()
    fuck = bee.split()
    if fuck[0] == 'Its':
        print(fuck)
        break

count = 0
for ass in fuck:
    count += 1
    if ass == 'small':
        print(ass, count)
        break
