#!/usr/bin/python
# -*- coding: utf-8 -*-

def imprimir_txt(direcciones,elementos,beneficio):#Funcion que imprime el beneficio y los elementos, en un archivo de texto
    archivo = open("resultado.txt", "w")
    archivo.write(str(beneficio))
    archivo.write("\n")
    for i in range(1,elementos+1):
        if i in direcciones:
            archivo.write('1')
        else:
            archivo.write('0')
    print("Los resultados se guardaron en el archivo con nombre resultados.txt")
    archivo.close()     
    
def mochila(n,c,elementos): #función mochila realiza el algoritmo de programación dinámica
    v=matrix_zeros(c,elementos)
    for i in range(1,elementos+1):
        for w in range(1,c+1):
            w_i=n[i-1][0]
            b_i=n[i-1][1]
            if w_i<=w:
                if (b_i+v[i-1][w-w_i])>v[i-1][w]:
                    v[i][w]=b_i+v[i-1][w-w_i]
                else:
                    v[i][w]=v[i-1][w]
            else:
                v[i][w]=v[i-1][w]
    inside(v,elementos,c,v[c-1][c])
    #print ("El mayor beneficio es %i"%(v[c-1][c]))
    


def inside(v,elementos,c,beneficio):#función que registra los elementos que van dentro de la mochila
    presente=[]
    direcciones=[]
    i=elementos
    k=c
    #print(v)
    while i>0 and k>0:
        if (v[i][k])!=(v[i-1][k]):

            #Presente en la mochila
            presente.append(n[i-1])
            direcciones.append(i)
            w_i=n[i-1][0]
            i=i-1
            k=k-w_i
        else:
            #el elemento no esté en la mochila
            i=i-1
    #print presente
    imprimir_txt(direcciones,elementos,beneficio)
 
   
def matrix_zeros(c,elementos):#Función crea una matris de ceros
    v=list()
    for i in range(elementos+1):
        lista_aux=[]
        for j in range(c+1):
            lista_aux.append(0)
        v.append(lista_aux)
    return v 
            


def leer(direccion):#Lee el archivo de texto y lo envía a una lista 
    numeros=[]
    archivo=open(str(direccion),"r")
    #print(archivo.read())
    #print (direccion)
    datos=archivo.read()
    anterior=10
    numero=''
    for i in datos:
        if ord(i)==10 or ord(i)==32:
            if numero!='':
                numeros.append(numero)
                numero=''
        else:
            numero=numero+i
    c,n,elementos=con_tuplas(numeros)
    return c,n,elementos

def con_tuplas(numeros): #convierte los elementos que estaán en una lista en tuplas de la forma (peso,beneficio)
    n=[]
    for i in range(len(numeros)):
        if i%2==0 and i<len(numeros)-1:
            n.append((int(numeros[i]),int(numeros[i+1])))
    c=n[0][1]
    elementos=n[0][0]
    n.pop(0)
    return c,n,elementos



if __name__ == '__main__':
    import sys
    if len(sys.argv)>2:
        file_location =sys.argv[1].strip()
        algorith =sys.argv[2].strip()
        print("Ejecutando el algoritmo %s en %s"%(algorith,file_location))
        c,n,elementos=leer(file_location)
        mochila(n,c,elementos)
        
        
        




    
  