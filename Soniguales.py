def sonListasIguales(lista_a, lista_b):
	con = 0 
	if len(lista_a) != len(lista_b):
		return False
	else:
		for i in range(0, len(lista_a)):
			if(lista_a[i] == lista_b[i]):
				con = con + 1
	if con == len(lista_a):
		return True
	else:
		return False
