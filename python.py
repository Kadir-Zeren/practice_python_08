sozluk = {'ali':25, 'veli':30, 'ayse':35}
print(type(sozluk))
sozluk = {'ali':25, 'veli':30, 'ayse':35,'ali':49}
print(sozluk)

sozluk = {'ali':'mehmet', 'veli':'ahmet', 'ayse':'fatma'}
sozluk = {5:'mehmet', 7:'ahmet', 9:'fatma'}

sozluk = {(1,2,3):'mehmet', 7:'ahmet', 9:'fatma'}

text = 'abcde'
print(type(text))
print(text[2])

liste = [1,2,3,4]
liste[2]=95

dict(ali =25,mehmet = 30, fatma = 35)

dict(ali = (25,30,35,40), mehmet= 30, fatma = 35)

dict([('ali',25),('mehmet',30),('fatma',35)])

sozluk['mahmut'] = 55
print(sozluk)

sozluk['veli'] = 25

print(sozluk.get('ali','duzgun yaz'))

sozluk['hasan'] = 77

print(dict([('name1','ali'),('name2','ayse'),('name3','fatma')]))

print(sozluk.items())
print(sozluk.keys())

print(sozluk.values())

kelime = 'abcdefg'
listem = list(kelime)
print(listem)

del listem[2]
del sozluk['hasan']

sozluk['mahmut'] = None
sozluk['mahmut'] = [25,76]
sozluk['mahmut'] [1] = 45

sozluk = {'ali':25,'veli':25,'ayse':35,'mahmut':[25],'kemal':21, 'huseyin':27}
sozluk.pop('mahmut')

print(sozluk.popitem())

a = [1,2,3,4,5]
a.remove(3)

a = [1,2,3,4,5]
a[2:3] = []
print(a)

a = [1,2,3,4,5]

print(1 in a)

print(21 in sozluk.values())
print('ali' in sozluk)