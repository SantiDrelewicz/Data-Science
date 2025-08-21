module Guia3 where 
-- 1. Definicion de funciones basicas
-- Ejercicio 1.
-- a)
f :: Integer ->Integer
f 1 = 8
f 4 = 131
f 16 = 16

-- b)
g :: Integer ->Integer
g 8 = 16
g 16 = 4
g 131 = 1

-- c) 
-- h = f o g
h :: Integer ->Integer
h n = f (g n)
-- k = g o f
k :: Integer ->Integer
k n = g (f n)

-- Ejercicio 2.
-- a)
absoluto :: Integer ->Integer
absoluto n | n < 0 = - n
           | otherwise = n
-- b)
maximoabsoluto :: Integer ->Integer ->Integer
maximoabsoluto n m | absoluto n == absoluto m = absoluto n
                   | absoluto n > absoluto m = absoluto n
                   | otherwise = absoluto m
-- c)
maximo3 :: Integer ->Integer ->Integer ->Integer
maximo3 n m l | n <= m && m <= l = l
              | n <= l && l <= m = m
              | m <= n && n <= l = l
              | m <= l && l <= n = n
              | l <= n && n <= m = m
              | l <= m && m <= n = n
-- d)
-- Con pattern matching
algunoEs0 :: Float -> Float ->Bool
algunoEs0 _ 0 = True
algunoEs0 0 _ = True
algunoEs0 n m = False
-- Sin pattern matching
algunoEs0' :: Float -> Float ->Bool
algunoEs0' n m | n == 0 || m == 0 = True
               | otherwise = False
-- e)
-- Con pattern matching
ambosSon0 :: Float ->Float ->Bool
ambosSon0 0 0 = True
ambosSon0 n m = False
-- Sin pattern matching
ambosSon0' :: Float ->Float ->Bool
ambosSon0' n m | n == 0 && m == 0 = True
               | otherwise = False
-- f)
mismoIntervalo :: Float ->Float ->Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | (3 < x && x <= 7) && (3 < y && y <= 7) = True
                   | x > 7 && y > 7 = True
                   | otherwise = False
-- g) 
sumaDistintos :: Integer ->Integer ->Integer ->Integer
sumaDistintos x y z | x == y && y == z = z
                    | x == y && y /= z = y + z
                    | x /= y && y == z = x + z
                    | x /= y && z == x = x + y
                    | otherwise = x + y + z
-- h)
esMultiploDe :: Integer ->Integer ->Bool
esMultiploDe n m = mod n m == 0 

-- i)
digitoUnidades :: Integer ->Integer
digitoUnidades n = mod (absoluto n) 10

-- j)
digitoDecenas :: Integer ->Integer
digitoDecenas n = mod (div (absoluto n - digitoUnidades n) 10) 10

-- Ejercicio 3.
             
-- Ejercicio 4.
-- a)
prodInt :: (Float,Float) ->(Float,Float) ->Float
prodInt (x1,y1) (x2,y2) = x1*y1 + y1*y2

-- b)
todoMenor :: (Float,Float) ->(Float,Float) ->Bool
todoMenor (x1,y1) (x2,y2) | x1 < x2 && y1 < y2 = True
                          | otherwise = False
-- c)
distanciaPuntos :: (Float,Float) ->(Float,Float) ->Float
distanciaPuntos (x1,y1) (x2,y2) = sqrt((x1-x2)**2+(y1-y2)**2) 

-- d)
sumaTerna :: (Float,Float,Float) ->Float
sumaTerna (x,y,z) = x + y + z

-- e)
sumarSoloMultiplos :: (Integer,Integer,Integer) ->Integer ->Integer
sumarSoloMultiplos (n,m,l) k | mod n k == 0 && mod m k == 0 && mod l k == 0 = n + m + l
                             | mod n k == 0 && mod m k == 0 && mod l k /= 0 = n + m
                             | mod n k == 0 && mod m k /= 0 && mod l k == 0 = n + l
                             | mod n k /= 0 && mod m k == 0 && mod l k == 0 = m + l
                             | mod n k == 0 && mod m k /= 0 && mod l k /= 0 = n
                             | mod n k /= 0 && mod m k == 0 && mod l k /= 0 = m
                             | mod n k /= 0 && mod m k /= 0 && mod l k == 0 = l
                             | otherwise = 0
-- f)
posPrimerPar :: (Integer,Integer,Integer) ->Integer
posPrimerPar (n,m,l) | mod n 2 == 0 = 1
                     | mod m 2 == 0 = 2
                     | mod l 2 == 0 = 3
                     | otherwise = 4
-- g)
crearPar :: ta ->tb ->(ta,tb)
crearPar a b = (a,b)

-- h)
invertir :: (ta,tb) ->(tb,ta)
invertir (a,b) = (b,a)

-- Ejercicio 5.
todosMenores :: (Integer, Integer, Integer) ->Bool
todosMenores (t0,t1,t2) = (fE5 t0 > gE5 t0) && (fE5 t1 > gE5 t1) && (fE5 t2 > gE5 t2)

fE5 :: Integer ->Integer
fE5 n | n <= 7 = n*n
      | otherwise = 2*n - 1

gE5 :: Integer ->Integer
gE5 n | mod n 2 == 0 = div n 2
      | otherwise = 3*n + 1 

-- Ejercicio 6.
bisiesto :: Integer ->Bool
bisiesto año = not (not(mod año 4 == 0) || ((mod año 100 == 0) && not(mod año 400 == 0)))

-- Ejercicio 7.
distanciaManhattan :: (Float, Float, Float) ->(Float, Float, Float) ->Float
distanciaManhattan (x1,y1,z1) (x2,y2,z2) = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

-- Ejercicio 8.
comparar :: Integer ->Integer ->Integer
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | otherwise = 0
             where sumaUltimosDosDigitos n = digitoUnidades n + digitoDecenas n
