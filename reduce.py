import sys
ObjContadorcito=0
ObjAnteriorcito=None
for linea in sys.stdin:
    key,value=linea.split('\t')
    value=int(value)
    if key==ObjAnteriorcito:
        ObjContadorcito+=1
    elif ObjAnteriorcito is None:
        ObjContadorcito+=1
    else:
        print(ObjAnteriorcito+'\t'+str(ObjContadorcito))
        ObjContadorcito=1
    ObjAnteriorcito=key
    