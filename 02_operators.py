# -*- coding: utf-8 -*-
"""02_Operators.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bjw8uJsyCTCXU90sdbw8jniMqUGdzmy_
"""

### Operadores aritmeticos###
#operaciones con enteros
#print(3+4)
#print(3-4)
#print(3*4)
#print(3/4)
#print(10%3)
#print(10//3)
#print(2**3)
#print(2 ** 3+3-7/1//4)


#operacion con cadenas de texto
#print("Hola"+"Phyton"+"¿Que tal?")
#print("Hola"+str(5))


#Operaciones mixtas
#print("hola " * 5)
#print("hola " * (2 ** 3))
#my_float = 2.5*2
#print("hola " * int(my_float))

###Operadores comparativos###

#print(3>4)
#print(3<4)
#print(3>=4)
#print(4<=4)
#print(3==4)
#print(3!=4)


# Operaciones con cadenas de texto
#print ("Hola">"Phyton")
#rint ("Hola"<"Phyton")
#print ("aaaa">="abaa")#Ordenacion alfebetica ASCII
#print (len("aaaa")>=len("abaa"))#cuenta caracteres
#print ("Hola"<="Phyton")
#print ("Hola"=="Phyton")
#print ("Hola"!="Phyton")


###Operadores logicos###
#Basada el el algebra de boole https://es.wikipedia.org/wiki/%C3%811gebra
print(3>4 and "Hola" > "Python")
print(3>4 or "Hola"  > "Python")
print(3<4 and "Hola"< "Python")
print(3<4 or "Hola"  > "Python")
print(3<4 and ("Hola"> "Python" and 4==4))
print (not(3>4))