# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:52:12 2024

@author: santiago
"""

from p7 import *

# 1. Archivos

# Ejercicio 1.
# 1.
def contar_lineas(nombre_archivo: str) -> int:
    archivo: str = open(nombre_archivo,"r")
    cant_lineas: int = 0
    for linea in archivo.readlines():
        cant_lineas += 1
    archivo.close()
    return cant_lineas
# 2.       
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
   res: bool =False
   archivo = open(nombre_archivo,"r")
   for linea in archivo.readlines():
       if palabra in linea:
           res = True
   archivo.close()
   return res
# 3.
def sacar_signos_de_puntuacion(palabras: list[str]) -> list[str]:
    res: list[int] = []
    for palabra in palabras:
        if (palabra[-1] < 'A') or ('Z' < palabra[-1] < 'a') or ('z' < palabra[-1]):
            res.append(palabra[:-1])
        else:
            res.append(palabra)
    return res
        
    
def cantidad_apariciones(nombre_archivo: str, palabra: str) -> int:
    res: int = 0
    archivo = open(nombre_archivo,'r')
    contenido_del_archivo: str = archivo.read()
    palabras_del_archivo: list[str] = sacar_signos_de_puntuacion(contenido_del_archivo.split())
    for palabra_del_archivo in palabras_del_archivo:
        if palabra == palabra_del_archivo:
            res += 1
    archivo.close()
    return res

# Ejercicio 2. 
def clonar_sin_comentarios(nombre_archivo: str):
    archivo = open(nombre_archivo,'r')
    archivo_sin_comentarios = open("clon.py","w")
    lineas: list[str] = archivo.readlines()
    for linea in lineas:
        if not linea.strip()[0] == "#":
            archivo_sin_comentarios.write(linea)
    archivo.close()
    archivo_sin_comentarios.close()

# Ejercicio 3.
def invertir_lista(lista: list) -> list:
    i: int = 0
    lista_invertida: list = []
    while i < len(lista):
        lista_invertida.append(lista[-i-1])
        i += 1
    return lista_invertida
        
def invertir_texto(nombre_archivo: str):
    archivo = open(nombre_archivo,'r')
    lineas: list[str] = archivo.readlines()
    lineas_al_reves: list[str] = invertir_lista(lineas)
    reverso = open('reverso.txt','w')
    for linea in lineas_al_reves:
        reverso.write(linea)
    archivo.close()
    reverso.close()

# Ejercicio 4.
def agregar_frase_al_final(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo,'a')
    archivo.write(frase)
    archivo.close()

# Ejercicio 5.
def agregar_frase_al_principio(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo,'r+')
    lineas: list[str] = archivo.readlines()
    archivo.writelines([frase + '\n'] + lineas)
    archivo.close()

# Ejercicio 7.
def promedio_estudiante(nombre_archivo: str, lu: str) -> float:
    archivo = open('notas.csv','r')
    lineas: list[str] = archivo.readlines()
    cant_notas: int = 0
    nota_acumulada: float = 0
    for linea in lineas:
        datos: list[str] = linea.split(",")
        if datos[0] == lu:
            cant_notas += 1
            nota_acumulada += datos[3]
    archivo.close()
    promedio: float = nota_acumulada / cant_notas
    return promedio

# def calcular_promedio_por_estudiante(nombre_archivo_notas : str, nombre_archivo_promedios : str) -> str:
    
    

# 2. Pilas.
from queue import LifoQueue as Pila
import random

# Ejercicio 8.
def generar_nros_al_azar_pila(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p: Pila[int] = Pila ()
    n: int = 0
    while n < cantidad:
        p.put(random.randint(desde,hasta))
        n += 1
    return p

# Ejercicio 9.
def cantidad_elementos_pila(p: Pila) -> int:
    res: int = 0
    elementos_de_p_desapilados: list = []
    while not p.empty():
        elementos_de_p_desapilados.append(p.get())
    elementos_de_p_apilados: list = invertir_lista(elementos_de_p_desapilados)
    for elementos_de_p in elementos_de_p_apilados:
        p.put(elementos_de_p)
    res = len(elementos_de_p_apilados)
    return res

# Ejercicio 10.
def buscar_el_maximo_pila(p: Pila[int]) -> int:
    maximo: int = p.get()
    elementos_de_p_desapilados: list[int] = []
    elementos_de_p_desapilados.append(maximo)
    while not p.empty():
        numero: int = p.get()
        elementos_de_p_desapilados.append(numero)
        if numero > maximo:
            maximo = numero
    elementos_de_p_apilados: list[int] = invertir_lista(elementos_de_p_desapilados)
    for elementos_de_p in elementos_de_p_apilados:
        p.put(elementos_de_p)
    return maximo


# 2. Colas.
from queue import Queue as Cola

# Ejercicio 13.
def generar_nros_al_azar_cola(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    res: Cola[int] = Cola ()
    for _ in range(cantidad):
        n: int = random.randint(desde,hasta) 
        res.put(n)
    return res

# Ejercicio 14.
def cantidad_elementos_cola(c : Cola) -> int:
    res : int = 0
    elementos_de_c : list = []
    while not c.empty():
        elementos_de_c.append(c.get())
    res = len(elementos_de_c)
    for elemento in elementos_de_c:
        c.put(elemento)
    return res

# Ejercicio 15.
def buscar_el_maximo_cola(c : Pila[int]) -> int:
    maximo : int = c.get()
    elementos_de_c : list[int] = []
    while not c.empty():
        numero : int = c.get()
        elementos_de_c.append(numero)
        if numero > maximo:
            maximo = numero
    for elemento in elementos_de_c:
        c.put(elemento)
    return maximo
              
# Ejericio 16.
# 1.
def armar_secuencia_de_bingo() -> Cola[int] :
    secuencia: Cola[int] = Cola ()
    nums_0_a_99 = list(range(0, 99))
    random.shuffle(nums_0_a_99)
    bolillero = nums_0_a_99
    for bola in bolillero:
        secuencia.put(bola)
    return secuencia
# 2
def armar_carton() -> list[int]:
    carton : list[int] = []
    nums_0_99 = list(range(0,99))
    random.shuffle(nums_0_99)
    i : int = 0
    while i < 12:
        carton.append(nums_0_99[i])
        i += 1
    return carton

def jugar_carton_de_bingo(carton : list[int], bolillero : Cola[int]) -> int:
    cant_jugadas : int = 0
    cruces : int = 0
    while cruces < 12:
        bola = bolillero.get()
        if pertenece(carton,bola):
            cruces += 1
        cant_jugadas += 1
    return cant_jugadas

# Ejericio 17.
def n_pacientes_urgentes(pedidos_de_atencion : Cola[tuple[int, str, str]]) -> int: 
    rango : list[int] = [1,2,3]
    pacientes_urgs : int = 0
    todos_los_pacientes : list[(int,str,str)] = []
    while not pedidos_de_atencion.empty():
        paciente : (int,str,str) = pedidos_de_atencion.get()
        todos_los_pacientes.append(paciente)
        if pertenece(rango,paciente[0]):
            pacientes_urgs += 1 
    for paciente in todos_los_pacientes:
        pedidos_de_atencion.put(paciente)
    return pacientes_urgs

# Ejercicio 18.
def atencion_a_clientes(cola : Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    cola_prioridades : Cola[tuple[str, int, bool, bool]] = Cola()
    cola_preferenciales : Cola[tuple[str, int, bool, bool]] = Cola()
    cola_resto : Cola[tuple[str, int, bool, bool]] = Cola()
    cola_ordenada : Cola[tuple[str, int, bool, bool]] = Cola()
    cola_aux : Cola[tuple[str, int, bool, bool]] = Cola()
    while not cola.empty():
        cliente:(str,int,bool,bool)=cola.get()
        cola_aux.put(cliente)
        if cliente[3]:
            cola_prioridades.put(cliente)
        elif cliente[2]:
            cola_preferenciales.put(cliente)
        else:
            cola_resto.put(cliente)
    while not cola_aux.empty():
        cliente : (str,int,bool,bool) = cola_aux.get()
        cola.put(cliente) 
    while not cola_prioridades.empty():
        cola_ordenada.put(cola_prioridades.get())
    while not cola_preferenciales.empty():
        cola_ordenada.put(cola_preferenciales.get())
    while not cola_resto.empty():
        cola_ordenada.put(cola_resto.get())
    
    return cola_ordenada


# 4. Diccionarios.

# Ejercicio 19.
def agrupar_por_longitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo,'r')
    palabras = sacar_signos_de_puntuacion((archivo.read()).split())
    res: dict = {} 
    for palabra in palabras:
        longitud: int = len(palabra)
        claves: list[int] = list(res.keys())
        if pertenece(claves,longitud):
            res[longitud] += 1
        else:
            res[longitud] = 1
    archivo.close()
    return res

# Ejercicio 20.
def libretas_universitarias(nombre_archivo_notas: str) -> list[str]:
    res: list[str] = []
    archivo = open(nombre_archivo_notas,'r')
    lineas = archivo.readlines()
    i: int = 0
    while i < len(lineas):
        linea = lineas[i]
        lu: str = linea[0]
        if pertenece(res, lu):
            i += 1
        else:
            res.append(lu)
    archivo.close()
    return res
            
def calcular_promedio_por_estudiante(nombre_archivo_notas: str) -> dict[str, float]:
    lus = libretas_universitarias(nombre_archivo_notas)
    res: dict = {}
    for lu in lus:
        res[lu] = promedio_estudiante(nombre_archivo_notas, lu)
    return res

# Ejercicio 21.
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo,'r')
    palabras = sacar_signos_de_puntuacion((archivo.read()).split())
    diccionario: dict[str,int] = {}
    for palabra in palabras:
        if pertenece(list(diccionario.keys()),palabra):
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    claves = list(diccionario.keys())
    res: str = claves[0]
    for clave in claves:
        apariciones = diccionario[clave]
        if apariciones > diccionario[res]:
            res = clave
    archivo.close()
    return res

# Ejercicio 22.

def visitar_sitio(historiales: dict, usuario: str, sitio: str):
    historiales[usuario].put(sitio)

def navegar_atras(historiales: dict ,usuario: str):
    historiales[usuario].get()

# Ejercicio 23.
# 1.
def agregar_producto(inventario: dict[str, dict[str,int]], nombre: str, precio: int, cantidad: int) -> dict[str, dict[str, int]]:
  inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
# 2.
def actualizar_stock(inventario: dict[str, dict[str, int]], nombre: str, cantidad: int):
  inventario[nombre]['cantidad'] = cantidad
# 3.
def actualizar_precios(inventario: dict[str, dict[str, int]], nombre: str, precio: int):
  inventario[nombre]['precio'] = precio
# 4.
def calcular_valor_inventario(inventario : dict[str, dict[str, int]]) -> float:
  valor_inventario : int = 0
  for clave in inventario.keys():
    valor_inventario += inventario[clave]['precio'] * inventario[clave]['cantidad']
  return valor_inventario     
    
    
    
    
