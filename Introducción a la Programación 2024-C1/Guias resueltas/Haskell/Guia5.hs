module Guia5 where
import Guia4

-- Ejercicio 1 
-- 1.
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- 2.
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

-- 3.
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

-- 4.
reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = reverso xs ++ [x]

-- Ejercicio 2.
-- 1.
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs
-- 2.
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x:xs) | x == head xs = todosIguales xs
                    | otherwise = False
-- 3.
todosDistintos :: (Eq t) => [t] ->Bool
todosDistintos [x] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs
-- 4.
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [x] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs
-- 5.
quitar :: (Eq t) => t -> [t] -> [t]                  
quitar x [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = x : quitar e xs
-- 6.
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e [] = []
quitarTodos e s | pertenece e s = quitarTodos e (quitar e s)
                | otherwise = s
-- 7.
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | pertenece x xs = x : eliminarRepetidos (quitarTodos x xs)
                         | otherwise = x : eliminarRepetidos xs
-- 8.
mismosElementos :: (Eq t) => [t] -> [t] -> Bool                         
mismosElementos s r = esPermutacion (eliminarRepetidos s) (eliminarRepetidos r)

esPermutacion :: (Eq t) => [t] -> [t] -> Bool
esPermutacion [] [] = True
esPermutacion _ [] = False
esPermutacion [] _ = False
esPermutacion (x:xs) r | pertenece x r = esPermutacion xs (quitar x r)
                       | otherwise = False
-- 9.
capicua :: (Eq t) => [t] -> Bool 
capicua [] = True
capicua [x] = True 
capicua (x:xs) | x == ultimo xs = capicua (principio xs)
               | otherwise = False

-- Ejercicio 3. 
-- 1.
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- 2.
productoria :: [Integer] -> Integer
productoria [] = 0
productoria (x:xs) = x * productoria xs

--3.
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x1:x2:xs) | x1 >= x2 = maximo (x1:xs)
                  | otherwise = maximo (x2:xs)
-- 4.
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [x] = [x + n]
sumarN n (x:xs) = (x + n) : sumarN n xs

-- 5.
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (n:ns) = n : sumarN n ns

-- 6.
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo s = (sumarN (ultimo s) (principio s)) ++ [ultimo s]

-- 7.
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs
-- 8.
multiplosDeN :: Integer -> [Integer] -> [Integer] 
multiplosDeN _ [] = []
multiplosDe n (x:xs) | mod x n == 0 = x : multiplosDeN n xs
                     | otherwise = multiplosDeN n xs
-- 9.
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar s =  ordenar (quitar (maximo s) s) ++ [maximo s]

--Ejercicio 5.
--1.
sumaAcumulada :: [Integer] ->[Integer]
sumaAcumulada [x] = [x]
sumaAcumulada s = sumaAcumulada (principio s) ++ [sumatoria s] 

-- 2.
descomponerEnPrimos :: [Integer] -> [[Integer]] 
descomponerEnPrimos [] = []
descomponerEnPrimos (n:ns) = factorizarEnPrimosDesde n 2 : descomponerEnPrimos ns

factorizarEnPrimosDesde :: Integer -> Integer -> [Integer]
factorizarEnPrimosDesde n k | esPrimo n = [n]
                            | not (esPrimo k) = factorizarEnPrimosDesde n (k + 1)
                            | esPrimo k && mod n k /= 0 = factorizarEnPrimosDesde n (k + 1)
                            | esPrimo k && mod n k == 0 = k : factorizarEnPrimosDesde (div n k) k
