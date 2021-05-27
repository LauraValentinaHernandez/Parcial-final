list_elementos=['piedra','papel','tijeras','lagarto','holk']
while(True):
  juegos= int(input("Ingrese la cantidad de veces a jugar:"))
  for i in list(range(0, juegos)):
    print("\n","Caso #",i+1,":")
    Caso= str(input("Ingrese respuestas de los jugadores:")).lower().replace("roca","piedra") 
    if len(Caso.split(" "))!=2:
      print("Respuesta no valida")
    elif  Caso.split(" ")[0] in list_elementos and Caso.split(" ")[1] in list_elementos:
      Brayan= Caso.split(" ")[0]
      Brigitte= Caso.split(" ")[1]
      if (Brayan == 'tijeras' and Brigitte =='papel') or (Brayan == 'papel' and Brigitte =='piedra') or (Brayan == 'piedra' and Brigitte == 'lagarto') or (Brayan == 'lagarto' and Brigitte =='holk'):
        
