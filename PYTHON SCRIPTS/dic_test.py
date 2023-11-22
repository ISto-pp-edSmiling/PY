dic = dict()
list = ['jake', 'unstable', 'kill','fuck', 'jake']

for word in list:
    dic[word] = dic.get(word, 0) + 1
print(dic)

big_count = None
small_count = None
for aaa,bbb in dic.items():
    if bbb > big_count or big_count is None:
        big_count = bbb
    if small_count > bbb or small_count is None:
        small_count = bbb
    
print(small_count, big_count)