import re, string
from collections import Counter 

def procesar(cadena):
    print("In: "+str(cadena))
    cadena=" ".join(cadena)
    print("Join: "+str(cadena))
    cadena=cadena.lower()
    cadena=re.sub('[%s]' % re.escape(string.punctuation), ' ', cadena)
    cadena=cadena.split()
    print("Out: "+str(cadena))

def reducir(cadena):
    print("In: "+str(cadena))
    cadena=Counter(cadena)
    print("Out: "+ str(cadena)[8:-1])

def contador_vocales(x):
    voc=0
    for i in len(cad):
        if cad[i]=='a' or cad[i]=='e'or cad[i]=='i' or cad[i]=='o' or cad[i]=='u' or cad[i]=='A'or cad[i]=='E' or cad[i]=='I' or cad[i]=='O'or cad[i]=='U':
            voc=voc+1
        return voc


b=["Erase una vez una casa grande! y BLANCA, con muchas ventanas..."]
contador_vocales(b)
