def finding_dup_numb(numb):
    numb.sort()
    for i in range (1, len(numb)):
        if numb[i] == numb[i-1]:
            print(numb[i])
            
finding_dup_numb([34, 645, 6, 4, 2, 4, 6])

def numb_func(num):
    dic = {}
    for numb in num:
        dic[numb] = dic.get(numb, 0) + 1
    for man,die in dic.items():
        if die > 1:
            print(man,'was repeated', die,'times!')

numb_func([23, 2, 4, 6, 1, 3, 4])