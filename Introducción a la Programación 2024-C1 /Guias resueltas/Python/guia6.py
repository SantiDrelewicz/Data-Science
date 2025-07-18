# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:03:36 2024

@author: santiago
"""
import math

# Ejercicio 1
# 1.
def imprimir_hola_mundo() -> str:
    print("¡Hola Mundo!")

# 3.
def raizDe2() -> float:
    return (round(2**(1/2), 4))
    
# 3.
def factorial_de_dos() -> int:
    return 2*1

# 4
def perimetro() -> float:
    return 2*math.pi


# Ejercicio 2
# 1.
def imprimir_saludo(nombre: str):
    print("Hola " + nombre)

# 2.
def raiz_cuadrada_de(numero: float) -> float:
    return math.sqrt(numero)

# 3.
def fahrenheit_a_celsius(t: float) -> float:
    return ((t - 32) * 5) / 9

# 4.
def imprimir_dos_veces(estribillo: str) -> str:
    print((estribillo+"\n\n")*2)

# 5.
def es_multiplo_de(n: int, m: int) -> bool:
    return n % m == 0

# 6.
def es_par(numero: float) -> bool:
    return es_multiplo_de(numero, 2)

# 7.
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int)->int:
    cant_total_de_porciones = comensales * min_cant_de_porciones
    res:int = (cant_total_de_porciones + cant_total_de_porciones%8) // 8
    return res


# Ejercicio 3
# 1.
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0

# 2.
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0

# 3.
def es_nombre_largo(nombre:str)->bool:
    return 3 <= len(nombre) <=8

# 4.
def es_bisiesto(año: int)-> bool:
    return es_multiplo_de(año, 400) or (es_multiplo_de(año, 4) and (not es_multiplo_de(año, 100)))


# Ejercicio 4
def peso_pino(altura_m: float)->float:
    altura_cm = altura_m * 100
    peso_hasta_3m:float = min(altura_cm, 300) * 3
    peso_sobre_3m:float = max(altura_cm - 300, 0) * 2
    return peso_hasta_3m + peso_sobre_3m

def es_peso_util(peso_kg: float) -> bool:
    return 400 <= peso_kg <= 1000

def sirve_pino_1(altura_m: float) -> bool:
    return 400 <= peso_pino(altura_m) <=1000

def sirve_pino_2(altura_m: float) -> bool:
    return es_peso_util(peso_pino(altura_m))


# Ejercicio 5
# 1.
def devolver_el_doble_si_es_par(numero: int) -> int:
    return numero * (2**((numero + 1) % 2))

# 2.
def devolver_valor_si_es_par_sino_el_que_sigue1(numero: int) -> int:
    return numero + numero % 2

def devolver_valor_si_es_par_sino_el_que_sigue2(numero: int) -> int:
    if es_par(numero):
        return numero
    else:
        return numero+1

def devolver_valor_si_es_par_sino_el_que_sigue3(numero: int) -> int:
    if numero % 2 == 0:
        return numero
    if numero % 2 == 1:
        return numero+1

# 3.
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if numero % 3 == 0 :
        res = 2*numero
    if numero % 9 == 0 :
        res = 3*numero
    else:
        res = numero
    return res

# 4.
def lindo_nombre(nombre: str)-> str:
    if len(nombre) >= 5 :
        print("Tu nombre tiene muchas letras")
    else:
        print("Tu nombre tiene menos de 5 caracteres")

# 5.
def elRango(numero: int) -> str:
    if numero < 5:
        print("Menor a 5")
    if 10 <= numero <= 20:
        print("Entre 10 y 20")
    else:
        print("Mayor a 20")

# 6.
def vacaciones_trabajo(edad: int, sexo:str)->str:
    if sexo == 'M' and (edad < 18 or edad >= 65):
        print("Andá de vacaciones")
    if sexo == 'M' and (18 <= edad < 65):
        print("Te toca trabajar")
    if sexo == 'F' and (edad < 18 or edad >= 60):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")
        
        
# Ejercicio 6
# 1.
def imprimir_numeros_del_1_al_20():
    n = 1
    while n < 21:
        print(n)
        n += 1
        
# 2.
def imprimir_numeros_pares_del_10_al_40():
    n = 10
    while n < 41:
        if n % 2 == 0:
            print(n)
        n += 1

# 3.
def eco():
    n = 1
    while n < 11:
        print("eco")
        n += 1

# 4.
def cuenta_regresiva(N: int):
    n = N
    while n > 0:
        print(n)
        n -= 1
    print("Despegue")
        
# 5.
def monitoreo_de_viaje_en_el_tiempo(año_partida: int, año_llegada: int):
    año_actual = año_partida
    while año_actual > año_llegada:
        print("Viajó un año al pasado, estamos en el año: "+ str(año_actual-1))
        año_actual -= 1
        
# 6.
def monitoreo_de_viaje_en_el_tiempo_aristoteles(año_partida: int, año_llegada: int):
    año_actual = año_partida
    while año_actual > año_llegada:
        if año_actual >= 0:
            print("Viajó un año al pasado, estamos en el año: "+ str(año_actual-20) + " d.C")
            año_actual -= 20
        else
            print("Viajó un año al pasado, estamos en el año: "+ str(abs(año_actual)+20) + " a.C")
            año_actual -= 20
                
 
Ejercicio 7
def monitoreo_de_viaje_en_el_tiempo_aristoteles2(año_partida: int, año_llegada: int):
    for año_actual in range(año_partida,año_llegada,20):
        print(año_actual)
        if año_actual >= 0:
            print("Viajó un año al pasado, estamos en el año: "+ str(año_actual - 20) + " d.C")
        else:
            print("Viajó un año al pasado, estamos en el año: "+ str(abs(año_actual) + 20) + " a.C")
