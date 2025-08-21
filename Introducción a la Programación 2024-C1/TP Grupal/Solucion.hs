module Solucion where
import Data.Char
-- No se permite agrear nuevos imports
-- Sólo está permitido usar estas funciones:
-- https://campus.exactas.uba.ar/pluginfile.php/557895/mod_resource/content/1/validas_tp.pdf


-- Completar!
-- Nombre de grupo: {noSaltesYaCompila}
-- Integrante1: { 41916549,Steg Victoria}
-- Integrante2: { 42727029,Drelewicz Santiago}
-- Integrante3: { 43875342,Perez Ruiz Victoria}
-- Integrante4: { 96193115,Bravo Leonardo}
-- Integrantes que abandonaron la materia: {}


-- EJ 1
esMinuscula :: Char -> Bool
esMinuscula x = 97 <= ord x && ord x <= 122

-- EJ 2
letraANatural :: Char -> Int
letraANatural c = ord c - 97

-- EJ 3
desplazar :: Char -> Int -> Char
desplazar c n | esMinuscula c = chr (nuevaPosicion + 97)  
              | otherwise = c
                -- Hacer que la nueva posicion viva entre el 0 al 25
              where nuevaPosicion = mod (letraANatural c + n) 26

-- EJ 4
cifrar :: String -> Int -> String
cifrar [] _ = []
cifrar [c] n = [desplazar c n]
cifrar (c:cs) n = desplazar c n : cifrar cs n

--EJ 5
descifrar :: String -> Int -> String
descifrar cifrado n = cifrar cifrado (-n)

-- EJ 6
cifrarLista :: [String] -> [String]
cifrarLista ls = cifrarCadaStringConSuPosicion ls (numerosDesdeHasta 0 (length ls - 1))

cifrarCadaStringConSuPosicion :: [String] -> [Int] -> [String]
cifrarCadaStringConSuPosicion [] [] = []
cifrarCadaStringConSuPosicion (x:xs) (n:ns) = cifrar x n : cifrarCadaStringConSuPosicion xs ns

numerosDesdeHasta :: Int -> Int -> [Int]
numerosDesdeHasta n m | n > m = []
                      | n == m = [n]
                      | otherwise = numerosDesdeHasta n (m-1) ++ [m]

-- EJ 7
frecuencia :: String -> [Float]
frecuencia s = frecuenciaDeCadaElementoDeEn (minusculasDesdeHasta 'a' 'z') (minusculasEn s)

frecuenciaDeCadaElementoDeEn :: (Eq t) => [t] -> [t] -> [Float]
frecuenciaDeCadaElementoDeEn [] _ = []
frecuenciaDeCadaElementoDeEn (x:xs) listaOriginal | length listaOriginal == 0 = repetirNVeces 0 (length (x:xs))
                                                  | otherwise = frecuenciaDeX : frecuenciaDeCadaElementoDeEn xs listaOriginal
                                                  where frecuenciaDeX = 100 * fromIntegral(cantidadApariciones x listaOriginal) / fromIntegral (length  listaOriginal)

minusculasDesdeHasta :: Char -> Char -> [Char]
minusculasDesdeHasta c1 c2 | c1 == c2 = [c1]
                           | otherwise = minusculasDesdeHasta c1 (chr(ord c2 - 1)) ++ [c2]

repetirNVeces :: (Eq t) => t -> Int -> [t]
repetirNVeces x n | n <= 0 = []
                  | otherwise = x : repetirNVeces x (n - 1)

cantidadApariciones :: (Eq t) => t -> [t] -> Int
cantidadApariciones y [] = 0
cantidadApariciones y (x:xs) | y == x = 1 + cantidadApariciones y xs
                             | otherwise = cantidadApariciones y xs

minusculasEn :: String -> String
minusculasEn [] = []
minusculasEn (x:xs) | esMinuscula x = x : minusculasEn xs
                    | otherwise = minusculasEn xs

-- Ej 8
cifradoMasFrecuente :: String -> Int -> (Char, Float)
cifradoMasFrecuente s n = masFrecuente (frecuencia (cifrar s n)) (minusculasDesdeHasta 'a' 'z')

masFrecuente :: (Ord t, Eq u) => [t] -> [u] -> (u, t)
-- Buscar la frecuencia mas grande y su posicion en la lista para devolver elemento
masFrecuente [x] [c] = (c, x)
masFrecuente (x1:x2:xs) (c1:c2:cs) | x1 >= x2 = masFrecuente (x1:xs) (c1:cs)
                                   | otherwise = masFrecuente (x2:xs) (c2:cs)

-- EJ 9
esDescifrado :: String -> String -> Bool
esDescifrado s1 s2 = esDescifradoParaAlgunN s1 s2 (numerosDesdeHasta 0 25)

esDescifradoParaAlgunN :: String -> String -> [Int]-> Bool
esDescifradoParaAlgunN s1 s2 [] = False
esDescifradoParaAlgunN s1 s2 (n:ns) = (s2 == cifrar s1 n) || esDescifradoParaAlgunN s1 s2 ns

-- EJ 10
todosLosDescifrados :: [String] -> [(String, String)]
todosLosDescifrados ls = todosLosDescifradosEn ls ls

todosLosDescifradosEn :: [String] -> [String] -> [(String, String)]
todosLosDescifradosEn [] _ = []
todosLosDescifradosEn (x:xs) listaOriginal = descifradosDe x listaOriginal ++ todosLosDescifradosEn xs listaOriginal

descifradosDe :: String -> [String] -> [(String, String)]
descifradosDe _ [] = []
descifradosDe s (y:ys) | s /= y && esDescifrado s y = (s, y) : descifradosDe s ys
                       | otherwise = descifradosDe s ys

-- EJ 11
expandirClave :: String -> Int -> String
expandirClave clave 1 = [head clave]
expandirClave clave n = expandirClave clave (n-1) ++ [iesimoElemento clave (mod (n-1) (length clave))]

iesimoElemento :: (Eq t) => [t] -> Int -> t
iesimoElemento (c:cs) 0 = c
iesimoElemento (c:cs) i = iesimoElemento cs (i-1)

-- EJ 12
cifrarVigenere :: String -> String -> String
cifrarVigenere s clave = cifrandoVigenere s (expandirClave clave (length s))

cifrandoVigenere :: String -> String -> String
cifrandoVigenere [] (y:ys) = []
cifrandoVigenere [] [] = []
cifrandoVigenere (x:xs) (y:ys) = (desplazar x n) : (cifrandoVigenere xs ys)
                             where n = letraANatural y
                      
-- EJ 13
descifrarVigenere :: String -> String -> String
descifrarVigenere cifrado clave = descifrandoVigenere cifrado (expandirClave clave (length cifrado))

descifrandoVigenere :: String -> String -> String
descifrandoVigenere [] (y:ys) = []
descifrandoVigenere [] [] = []
descifrandoVigenere (x:xs) (y:ys) = desplazar x (-n) : descifrandoVigenere xs ys
                              where n = letraANatural y

-- EJ 14
peorCifrado :: String -> [String] -> String
peorCifrado s [c] = c
peorCifrado s (c1:c2:cs) | distancia1 <= distancia2 = peorCifrado s (c1:cs)
                         | otherwise = peorCifrado s (c2:cs)
                         where distancia1 = distancia s (cifrarVigenere s c1)
                               distancia2 = distancia s (cifrarVigenere s c2)

distancia :: String -> String -> Int
distancia [x] [y] = distanciaEntreLetras x y
distancia (x:xs) (y:ys) = distanciaEntreLetras x y + distancia xs ys
                    
distanciaEntreLetras :: Char -> Char -> Int
distanciaEntreLetras c1 c2 = diferenciaAbsoluta (letraANatural c1) (letraANatural c2)

diferenciaAbsoluta :: Int -> Int -> Int
diferenciaAbsoluta x y | x >= y = x - y
                       | otherwise = y - x

-- EJ 15
combinacionesVigenere :: [String] -> [String] -> String -> [(String,String)]
combinacionesVigenere [] clave cifrado = []
combinacionesVigenere (m:ms) claves cifrado = (obtenerClaves m claves cifrado) ++ (combinacionesVigenere ms claves cifrado)

obtenerClaves :: String -> [String] -> String -> [(String, String)]
obtenerClaves m [] cifrado = []
obtenerClaves m (c:cs) cifrado | cifrarVigenere m c == cifrado = (m,c) : (obtenerClaves m cs cifrado)
                               | otherwise = obtenerClaves m cs cifrado
