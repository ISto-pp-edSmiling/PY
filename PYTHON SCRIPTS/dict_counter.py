slither  = dict()
snake = ('help', 'gun', 'focus', 'gun')

#for venom in snake:
    #if venom not in slither:
        #slither[venom] = 1
    #else:
        #slither[venom] += 1
        #print(slither[venom])
#print(slither)

for snap in snake:
    slither[snap] = slither.get(snap, 0) + 1
print(slither)