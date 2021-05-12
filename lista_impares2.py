def encontra_impares2(lista):
	if len(lista) == 0:
		return []
	e = lista.pop(0)
	if e % 2 != 0:
		return [e] + encontra_impares2(lista)
	return encontra_impares2(lista)


print(encontra_impares2([1,7,10,12,16,21,3,9,11]))
