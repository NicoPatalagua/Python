import sys
for linea in sys.stdin:
    palabras=linea.split()
    for palabra in palabras:
        print(palabra+'\t'+'1')

