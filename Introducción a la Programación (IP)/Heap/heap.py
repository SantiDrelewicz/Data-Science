#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:29:43 2024

@author: publico
"""

import numpy as np

class Heap:
    
    def __init__(self):
        self.__elems = np.array([])
    
    def __len__(self) -> int:
        return len(self.__elems)
    
    def vacio(self) -> bool:
        return len(self.__elems) > 0
    
    def obtener(self, indice: int):
        return self.__elems[indice]
    
    def raiz(self):
        return self.__elems[0] 
    
    def __subir_iterativo(self, indice: int): 
        ''' Sube el elemento nº indice del heap hasta la raiz mientras tenga padres de menor valor'''
        elem = self.__elems[indice]
        posicion_actual: int = indice
        posicion_padre: int = (indice - 1) // 2
        while posicion_actual > 0 and elem > self.__elems[posicion_padre]:
            self.__elems[posicion_actual] = self.__elems[posicion_padre]
            self.__elems[posicion_padre] = elem
            posicion_actual = posicion_padre
            posicion_padre = (posicion_actual - 1) // 2
            
    
    def agregar(self, elem: any):
        self.__elems = np.append(self.__elems, elem)
        self.__subir_iterativo(len(self.__elems) - 1)
        
    def show(self):
        print(self.__elems)
                

if __name__ == '__main__':
    print('hola')
    
    
    
    
    



