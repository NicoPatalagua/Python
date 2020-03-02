#-*- coding: utf-8 -*-
import re, string
from collections import Counter 

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
        ("“"," "),
        ("”"," "),
        (","," "),
        ("."," ")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
def Vowels(cad):
    return sum(c in {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"} for c in cad)

def VowelsU(cad):
    a=sum(c in{"a"} for c in cad)
    print("Promedio a "+str(a/9))
    e=sum(c in{"e"} for c in cad)
    print("Promedio e "+str(e/9))
    i=sum(c in{"i"} for c in cad)
    print("Promedio i "+str(i/9))
    o=sum(c in{"o"} for c in cad)
    print("Promedio o "+str(o/9))
    u=sum(c in{"u"} for c in cad)
    print("Promedio u "+str(u/9))


ff = open ('Historia1.txt','w')
with open("historia.txt", "r") as f:
    text = f.read()
    text2 = text.lower()
    text2= normalize(text2)
    #matchObjs = re.findall(r'[\w]+', text2)
    print(text2)
    ff.write(text2)
    print("___________________")
ff.close()
vocales=[]
v=[]
a1=[]
with open("Historia1.txt","r") as f:
    text=f.read()
    for tx in text.split("\n"):
        vocales.append(Vowels(tx))
    v.append(VowelsU(text))
    
print(vocales)
a=vocales
a=float(sum(vocales))
print(a)
b=len(vocales)
print(float(a/b))




