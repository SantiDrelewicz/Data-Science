# -*- coding: utf-8 -*-
"""
Created on Thu May 23 02:58:34 2024

@author: santiago
"""

# 1. Primera Parte

# Ejercicio 1
# 1.
def pertenece(s:[int], e:int)->bool:
    i=0
    while i < len(s):
        if s[i] == e :
            return True
        else:
            i = i + 1
    return False

# 2.
def divide_a_todos(s:[int], e:int)->bool:
    i:int = 0
    if len(s) == 0:
        return False
    while i < len(s):
        if s[i] % e == 0:
            i += 1
        else:
            return False
    return True

# 3.
def suma_total(s:[int])->int:
    i:int = 0
    s_t:int = 0
    while i < len(s):
        s_t += s[i]
        i += 1
    return s_t

# 4.
def ordenados(s:[int])->bool:
    i:int = 0
    while i < len(s) - 1:
        if s[i] > s[i+1]:
            return False
        i += 1
    return True

# 5.
def alguna_palabra_con_long_mayor_7(s:[str])->bool:
    i = 0
    while i < len(s):
        if len(s[i]) > 7:
            return True
        i += 1
    return False

# 6.
def es_palindromo(s:str)->bool:
    i = 0
    while i < len(s)/2:
        if s[i] != s[-i-1]:
            return False
        i += 1
    return True

# 7.
def cant_mins_mays_digs(s:str)->int:
    c_m = 0
    c_M = 0
    c_d = 0
    i = 0
    while i < len(s):
        if ('a' <= s[i] <= 'z') or (s[i] == 'ñ') :
            c_m += 1
        if ('A' <= s[i] <= 'Z') or (s[i] == 'Ñ') :
            c_M +=1
        if ('0' <= s[i] <= 'Z') or (s[i] == '9') :
            c_d += 1
        i += 1
    return [c_m,c_M,c_d]
        
def fortaleza_de_contraseña(s:str):
    if (len(s) > 8) and (cant_mins_mays_digs(s)[0] > 0) and (cant_mins_mays_digs(s)[1] > 0) and (cant_mins_mays_digs(s)[2] > 0):
        return "VERDE"
    if len(s) < 5:
        return "ROJA"
    else: 
        return "AMARILLA"

# 8.
def saldo_actual(movs:(str,int))->int:
    saldo_inicial:int = 0
    i = 0
    while i < len(movs) :
        if movs[i][0] == "I" :
            saldo_inicial += movs[i][1]
        else:
            saldo_inicial -= movs[i][1]
        i += 1
    return saldo_inicial
            

# 2. Segunda Parte

# Ejercicio 2. 
# 1.    
def poner_0_en_posiciones_pares1(lista:[int])->[int]:
    for i in range(0,len(lista)):
        if i % 2 == 0:
            lista[i] = 0
    return lista
# 2.
def poner_0_en_posiciones_pares2(lista:[int])->[int]:
    res:[int] = []
    for i in range(0,len(lista)):
        if i % 2 == 0:
            res.append(0)
        else:
            res.append(lista[i])
    return res
# 3.
def es_vocal(caracter:chr)->bool:
    return pertenece(['a','e','i','o','u'],caracter)

def borrar_vocales(lista:[chr])->[chr]:
    lista_nueva:[chr] = []
    for i in range(0,len(lista)):
        if not(es_vocal(lista[i])):
            lista_nueva.append(lista[i])
    return lista_nueva
# 4.
def reemplazar_vocales(lista:[chr])->[chr]:
    lista_nueva:[chr] = []
    for i in range(0,len(lista)):
        if es_vocal(lista[i]):
            lista_nueva.append('_')
        else:
            lista_nueva.append(lista[i])
    return lista_nueva
# 5.
def da_vuelta_str(palabra:str)->str:
    palabra_al_reves:str = ""
    for i in range(0,len(palabra)):
        palabra_al_reves += palabra[-i-1]
    return palabra_al_reves
# 6.
def eliminar_repetidos(lista:[chr])->[chr]:
    lista_nueva:[chr] = []
    for i in range(0,len(lista)):
        if not pertenece(lista_nueva,lista[i]):
            lista_nueva.append(lista[i])
    return lista_nueva

# Ejercicio 3.
def todos_mayores_o_iguales_a_4(lista:[int])->bool:
    res:bool = True
    for i in range(0,len(lista)):
        if lista[i] < 4:
            return False
    return res

def promedio(lista:[int])->float:
    return suma_total(lista)/len(lista)

def aprobado(notas:[int])->int:
    if (todos_mayores_o_iguales_a_4(notas)) and (promedio(notas) >= 7):
        return 1
    elif (todos_mayores_o_iguales_a_4(notas)) and (4 <= promedio(notas) < 7):
        return 2
    else: 
        return 3

# Ejercicio 4.
# 1.
def lista_de_estudiantes()->[str]:
    res:[str]=[]
    nombre=""
    while(nombre != "listo"):
        print("Ingrese un nombre: ")
        nombre=str(input('> '))
        if(nombre != 'listo'):
            res.append(nombre)
    return res
# 2.
def historial_SUBE() -> [(str,int)]:
    res:[(str,int)]=[]
    plata_actual:int = 0
    opcion:str = ""
    while opcion != "X":
        print("Ingrese una opción: C = Cargar, D = Descontar, X = Cerrar")
        opcion=input('> ')
        if(opcion == "C"):
            print("Ingrese un monto:")
            monto = int(input('> '))
            plata_actual += monto
            res.append((opcion,monto))
        elif(opcion == "D"):
            print("Ingrese un monto:")
            monto=int(input('> '))
            plata_actual -= monto
            res.append((opcion,monto))
    print("Terminó con: $" + str(plata_actual))        
    return res

# Ejercicio 5.
# 1.
def problema_pertenece_a_cada_uno(s: list[list[int]], e: int) -> list[bool]:
    res: list[bool] = []
    for i in range(0,len(s)):
        res.append(pertenece(s[i], e))
    return res
# 3.
def es_matriz(s: list[list[int]]) -> bool:
    res: bool = True
    if len(s) == 0 or len(s[0]) == 0:
        res = False
    else:
        for i in range(0,len(s)):
            if len(s[i]) != len(s[i+1]):
                res = False
    return res
# 4.
def filas_ordenadas(m: list[list[int]]) -> bool:
    res: bool = True
    for i in range(0,len(m)):
        if not ordenados(m[i]):
            res = False
    return res
# 5.
import numpy as np

def multiplicar_matrices(M1: list[list[int]], M2: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range(0,len(M1)):
        fila: list[int] = []
        for j in range(0,len(M1[0])):
            elemento_i_j: int = 0
            for k in range(0,len(M1[0])):
                elemento_i_j += M1[i][k] * M2[k][j]
            fila.append(elemento_i_j)
        res.append(fila)
    return res

def matriz_identidad(d: int) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range(d):
        fila: list[int] = []
        for j in range(d):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        res.append(fila)
    return res

def elevar_matriz_random1(d,p,i,f):
    M: list[list[int]] = np.random.randint(i,f,(d,d))
    res: list[list[int]] = matriz_identidad(d) 
    for _ in range(0,p):
        res = multiplicar_matrices(res,M)
    return res
        
def elevar_matriz_random2(d,p):
    M: list[list[int]] = np.random.random((d,d))
    res: list[list[int]] = matriz_identidad(d) 
    for _ in range(0,p):
        res = multiplicar_matrices(res,M)
    return res    

        
    
        
    
            

