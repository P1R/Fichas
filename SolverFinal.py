from Pila import *
from Gira import Resolv


def main():
	Fin=[1,2,3,'B'];
	#X=Pila();
	C=Pila();
	X=['B',3,1,2];
	C.apilar(X);
	An, Con = Resolv(Fin, X, 'R')
	C.apilar(An);
	#print Con
	#Bn, Con = Resolv(Fin, B, 'I')
	#C.apilar(Bn);
	#print Con
	#Cn, Con = Resolv(Fin, An, 'R')
	#C.apilar(Cn);
	#print Con
	#Dn, Con = Resolv(Fin, An, 'I')
	#C.apilar(Dn);
	#print Con
	#En, Con = Resolv(Fin, Bn, 'R')
	#C.apilar(En);
	#print Con
	#Fn, Con = Resolv(Fin, Bn, 'I')
	#C.apilar(Fn);
	#print Con
	
	print C.items
	
         
if __name__ == '__main__':
    main()
