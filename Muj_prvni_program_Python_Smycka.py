# muj_seznam=[1,2,3,4,5]
# chci  vypsat každou položku  seznamu
# print(muj_seznam[0])
# print(muj_seznam[1])
# print(muj_seznam[2])
# print(muj_seznam[3])
# print(muj_seznam[4])

muj_iterator= iter([1,2,3,4,5])
print(muj_iterator)
seznam=list()
for muj_iterator in [1,2,3,4,5]:
	if muj_iterator ==3 :
		seznam.append(muj_iterator)
		# print(seznam)
	elif muj_iterator == 5 :
		seznam.append(muj_iterator)
		print(seznam)
else:
	print ("program ukončen !!!") 
		

# chci  vypsat každou položku  seznamu
# print(muj_seznam[0])
# print(muj_seznam[1])
# print(muj_seznam[2])
# print(muj_seznam[3])
# print(muj_seznam[4])





