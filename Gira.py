from Pila import *

def Resolv(A, X, Clock):
	B = [0] * len(X) # creo es la forma mas adecuada
	for i in range(len(X)):
		B[i] = X[i]
	#sentido manecillas de reloj
	if Clock == 'R':
		if B[0]=='B':
			#Cambio Derecha de 0
			B[0],B[1]= B[1],B[0];
			#si coincide con
			#la matriz buscada
			if B == A:
				#C.apilar(B);
				print 'coincidio!'
				return B, True
			else:
				return B, False
		elif B[1]=='B':
			#Cambio Abajo de 1
			B[1],B[3]= B[3],B[1];
			#si coincide con
			#la matriz buscada
			if B == A:
				print 'coincidio!'
				return B, True
			else:
				return B, False
		elif B[3]=='B':
			#Cambio Izquerda de 3
			B[3],B[2]= B[2],B[3];
			#si coincide con
			#la matriz buscada
			if B == A:
				print 'coincidio!'
				return B, True
			else:
				return B, False
		elif B[2]=='B':
			#Cambio Arriba de 2
			B[2],B[0]= B[0],B[2];
			#si coincide con
			#la matriz buscada
			if B == A:
				print 'coincidio!'
				return B, True
			else:
				return B, False
#seccion para cambio en sentido en manecillas				
	elif Clock == 'I':
		if B[0]=='B':
			#Cambio Abajo de 0
			B[0],B[2]= B[2],B[0];
			#si coincide con
			#la matriz buscada
			if B == A:
				print 'coincidio!'
				return B, True
			else:
				return B, False
		elif B[1]=='B':
			#Cambio Izquieda de 1
			B[1],B[0]= B[0],B[1];
			#si coincide con
			#la matriz buscada
			if B == A:
				print 'coincidio!'
				return B, True
			else:
				return B, False
		elif B[2]=='B':
			#Cambio Derecha de 2
			B[2],B[3]= B[3],B[2];
			#si coincide con
			#la matriz buscada
			if B == A:
				print 'coincidio!'
				return B, True
			else:
				return B, False
		elif B[3]=='B':
			#Cambio Arriba de 3
			B[3],B[1]= B[1],B[3];
			#si coincide con
			#la matriz buscada
			if B == A:
				print 'coincidio!'
				return B, True
			else:
				return B, False
	else:
		print "error, ingresa parametros de forma Resolv".rstrip('\n')
		print "(Matriz A, Matriz B, Direccion)"
		print "Donde Matriz A es la Matriz Generada"
		print "Donde Matriz B es Matriz Buscada,".rstrip('\n')
		print "Direccion R o I dependiendo sentido de Reloj o Inverso"
		print "esta funcion regresa nueva matriz rotada".rstrip('\n')
		print "y booleano si coincide o no con la buscada (B==A)"
		return False 
