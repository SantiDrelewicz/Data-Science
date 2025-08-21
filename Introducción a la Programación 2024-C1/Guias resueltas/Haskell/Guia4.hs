module Guia4 where
-- Recursión sobre n°s Z

digitoUnidades :: Integer ->Integer
digitoUnidades n = mod (abs (n)) 10

digitoDecenas :: Integer ->Integer
digitoDecenas n = mod (div (abs (n) - digitoUnidades n) 10) 10

-- Ejercicio 1.
fibonacci :: Integer ->Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

-- Ejercicio 2.
parteEntera :: Float ->Integer
parteEntera x | 0 <= abs(x) && abs(x) < 1 = 0
              | otherwise = 1 + parteEntera (x-1)

-- Ejercicio 3.
esDivisible :: Integer ->Integer ->Bool
esDivisible _ 1 = True
esDivisible 0 _ = True
esDivisible a b | a < b = False
                | a == b = True
                | otherwise = esDivisible (a-b) b

-- Ejercicio 4.
sumaImpares :: Integer ->Integer
sumaImpares 1 = 1
sumaImpares n = 2 * n - 1 + sumaImpares (n-1)

-- Ejercicio 5.
medioFact :: Integer ->Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n * medioFact (n-2)

-- Ejercicio 6.
sumaDigitos :: Integer ->Integer
sumaDigitos n | n < 10 = n
              | otherwise = (mod n 10) + sumaDigitos (div (n - digitoUnidades n) 10)
              
-- Ejercicio 7.
todosDigitosIguales :: Integer ->Bool
todosDigitosIguales n | n < 10 = True
                      | digitoUnidades n /= digitoDecenas n = False
                      | otherwise = todosDigitosIguales (div (n - digitoUnidades n) 10)

-- Ejercicio 8.
iesimoDigito :: Integer ->Integer ->Integer
iesimoDigito n i = mod (div n (10^(cantDigitos n - i))) 10

cantDigitos :: Integer ->Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (div (n - digitoUnidades n) 10)

-- Ejercicio 9.
esCapicua :: Integer ->Bool
esCapicua n | n < 10 = True
            | n < 100 = digitoUnidades n == digitoDecenas n
            | iesimoDigito n 1 == iesimoDigito n (cantDigitos n) = esCapicua (quitarPrimerYultimoDigito n)
            | otherwise = False
            where quitarPrimerYultimoDigito m = div ((mod m 10^(cantDigitos m - 1)) - digitoUnidades m) 10

-- Ejercicio 10
-- a)
f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2 ^ n + f1 (n - 1)

-- b)
f2 :: (Integer, Float) -> Float
f2 (1, q) = q
f2 (n, q) = q ^ n + f2 (n - 1, q)

-- c)
f3 :: (Integer, Float) -> Float
f3 (n, q) = f2 (2 * n, q)

-- d)
f4 :: (Integer, Float) -> Float
f4 (n, q) = f3 (n, q) - f2 (n - 1, q)

-- Ejercicio 13
f :: (Integer, Integer) -> Integer
f (1, m) = m
f (n, m) = g (n, m) + f (n - 1, m)

g :: (Integer, Integer) -> Integer
g (i, 1) = 1
g (i, m) = i ^ m + g (i, m - 1)

-- Ejercicio 14
--sumaPotencias :: Integer ->Integer ->Integer ->Integer
--sumaPotencias q n m = f2 (n, q) * f2 (m, q)

-- Ejercicio 16.
-- a)
menorDivisor :: Integer ->Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer ->Integer ->Integer
menorDivisorDesde n k | k >= n = n
                      | mod n k == 0 = k
                      | otherwise = menorDivisorDesde n (k + 1)
-- b)
esPrimo :: Integer ->Bool
esPrimo n = menorDivisor n == n

-- c)
sonCoprimos :: Integer ->Integer ->Bool
sonCoprimos a b = mcd (a, b) == 1

mcd :: (Integer, Integer) ->Integer
mcd (0, b) = b
mcd (a, 0) = a
mcd (a, b) | a == 1 || b == 1 = 1
           | otherwise = mcd (b, mod a b)
-- d)
nEsimoPrimo :: Integer ->Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = primerPrimoDesde (1 + nEsimoPrimo (n - 1))

primerPrimoDesde :: Integer ->Integer
primerPrimoDesde k | esPrimo k = k
                   | otherwise = primerPrimoDesde (k + 1)
                   
-- Ejercicio 17.
esFibonacci :: Integer -> Bool
esFibonacci 0 = True
esFibonacci 1 = True
esFibonacci n = esAlgunFibonacci n 2

esAlgunFibonacci :: Integer -> Integer -> Bool 
esAlgunFibonacci n k | fibonacci k > n = False
                     | fibonacci k == n = True
                     | fibonacci k < n = esAlgunFibonacci n (k + 1)

-- Ejercicio 18. 
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | n < 10 && mod n 2 == 0 = n
                 | n < 10 && mod n 2 == 1 = -1
                 | mod n 2 == 1 = mayorDigitoPar (sacarDigitoUnidades n)
                 | mod n 2 == 0 && mod (digitoDecenas n) 2 == 1 = mayorDigitoPar (sacarDigitoDecenas n)
                 | mod n 2 == 0 && mod (digitoDecenas n) 2 == 0 && digitoUnidades n > digitoDecenas n = mayorDigitoPar (sacarDigitoDecenas n)
                 | mod n 2 == 0 && mod (digitoDecenas n) 2 == 0 && digitoUnidades n < digitoDecenas n = mayorDigitoPar (sacarDigitoUnidades n)

sacarDigitoUnidades :: Integer -> Integer
sacarDigitoUnidades n = div (n - digitoUnidades n) 10

sacarDigitoDecenas :: Integer -> Integer
sacarDigitoDecenas n = div (n - mod n 100) 10 + digitoUnidades n

-- Ejericicio 19.
esSumaInicialDePrimos :: Integer ->Bool
esSumaInicialDePrimos n = esSumaInicialDeKPrimosDesde n 1

esSumaInicialDeKPrimosDesde :: Integer ->Integer ->Bool
esSumaInicialDeKPrimosDesde n k | sumaInicialDeKprimos k > n = False
                                | sumaInicialDeKprimos k == n = True
                                | sumaInicialDeKprimos k < n = esSumaInicialDeKPrimosDesde n (k + 1)
                                      
sumaInicialDeKprimos :: Integer ->Integer
sumaInicialDeKprimos 1 = 2
sumaInicialDeKprimos k = nEsimoPrimo k + sumaInicialDeKprimos (k - 1)
                              
-- Ejercicio 20
tomaValorMax :: Int ->Int ->Int
tomaValorMax n1 n2 | n1 == n2 = n2
                   | sumaDivisores n1 > sumaDivisores n2 = tomaValorMax n1 (n2 - 1)
                   | sumaDivisores n1 < sumaDivisores n2 = tomaValorMax (n1 + 1) n2

sumaDivisores :: Int ->Int
sumaDivisores n = sumaDivisoresDesde n 1

sumaDivisoresDesde :: Int ->Int ->Int
sumaDivisoresDesde n k | n == k = n
                       | n > k && mod n k == 0 = k + sumaDivisoresDesde n (k + 1)
                       | otherwise = sumaDivisoresDesde n (k + 1)

-- Ejercicio 21
pitagoras :: Integer ->Integer ->Integer ->Integer
pitagoras 0 m r = pitagorasConPfijo 0 m r
pitagoras n m r = pitagorasConPfijo n m r + pitagoras (n - 1) m r

pitagorasConPfijo :: Integer ->Integer ->Integer ->Integer
pitagorasConPfijo p m r | m == 0 && p > r = 0
                        | m == 0 && p <= r = 1
                        | p^2 + m^2 <= r^2 = 1 + pitagorasConPfijo p (m - 1) r
                        | otherwise = pitagorasConPfijo p (m - 1) r



