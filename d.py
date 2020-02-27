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
with open("Historia1.txt","r") as f:
    text=f.read()
    for tx in text.split("\n"):
        vocales.append(Vowels(tx))
print(vocales)
a=float(sum(vocales))
b=len(vocales)
print(float(a/b))




