import csv
import numpy as np

with open('info_estudiantes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Genero", "TV", "Computador","Dormir","AlturaE","AlturaMama","AlturaPapa","EjercicioE","Promedio"])
    for i in range (180):
      gen=np.random.randint(0,2)
      if gen == 1:
         genero='Male'
      elif gen==0:
        genero='Female'
      tv = np.random.randint(0,12)
      com = np.random.randint(0,18)
      dor = np.random.randint(0,9)
      Alte = np.random.randint(100,192)
      Altm = np.random.randint(100,169)
      Altp = np.random.randint(100,192)
      ejer = np.random.randint(0,9)
      prom = np.random.uniform(3,5)
      writer.writerow([genero,tv,com,dor,Alte,Altm,Altp,ejer,prom])