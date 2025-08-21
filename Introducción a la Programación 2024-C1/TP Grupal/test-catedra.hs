import Test.HUnit
import Solucion
import Data.List
-- No está permitido agregar nuevos imports.

runCatedraTests = runTestTT allTests

allTests = test [
    "esMinuscula" ~: testsEjesMinuscula,
    "letraANatural" ~: testsEjletraANatural,
    "desplazar" ~: testsEjdesplazar,
    "cifrar" ~: testsEjcifrar,
    "descifrar" ~: testsEjdescifrar,
    "cifrarLista" ~: testsEjcifrarLista,
    "frecuencia" ~: testsEjfrecuencia,
    "cifradoMasFrecuente" ~: testsEjcifradoMasFrecuente,
    "esDescifrado" ~: testsEjesDescifrado,
    "todosLosDescifrados" ~: testsEjtodosLosDescifrados,
    "expandirClave" ~: testsEjexpandirClave,
    "cifrarVigenere" ~: testsEjcifrarVigenere,
    "descifrarVigenere" ~: testsEjdescifrarVigenere,
    "peorCifrado" ~: testsEjpeorCifrado,
    "combinacionesVigenere" ~: testsEjcombinacionesVigenere
    ]


testsEjesMinuscula = test [
    "Caracter anterior: eM '`'" ~: (esMinuscula '`') ~?= False,
    "1era minuscula: eM 'a'" ~: (esMinuscula 'a') ~?= True,
    "Minúscula intermedia: eM 'm'" ~: (esMinuscula 'm') ~?= True,
    "Última minúscula" ~: (esMinuscula 'z') ~?= True,
    "Caracter siguiente: eM '{'" ~: (esMinuscula '{') ~?= False
    ]

testsEjletraANatural = test [
    "Caso 0: lAN 'a'" ~: (letraANatural 'a') ~?= 0,
    "Caso Intermedio: lAN 'm'" ~: (letraANatural 'm') ~?= 12,
    "Caso Límite: lAN 'z' " ~: (letraANatural 'z') ~?= 25
    ]

testsEjdesplazar = test [
    "No desplazar: desplazar 'm' 0" ~: (desplazar 'm' 0) ~?= 'm',
    "Caso letra anterior: desplazar 'a' 25" ~: (desplazar 'a' 25) ~?= 'z',
    "Volver a la misma letra: dezplazar 'm' 26" ~: (desplazar 'm' 26) ~?= 'm',
    "Caso n negativo: desplazar 'a' -1" ~: (desplazar 'a' (-1)) ~?= 'z'
    ]

testsEjcifrar = test [
    "Caso string vacio: cifrar '' 3" ~: (cifrar "" 3) ~?= "",
    "Caso 0: cifrar 'computacion' 0" ~: (cifrar "computacion" 0) ~?= "computacion",
    "Caso cifrar sin cifrar: cifrar 'computacion' 26" ~: (cifrar "computacion" 26) ~?= "computacion",
    "Caso sin minúsculas: cifrar 'COMPUTACION' 3" ~: (cifrar "COMPUTACION" 1) ~?= "COMPUTACION",
    "Caso mezclado: cifrar 'TrabajoPractico' 1" ~: (cifrar "TrabajoPractico" 1) ~?= "TsbcbkpPsbdujdp"
    ]

testsEjdescifrar = test [
    "Caso string vacio: descifrar '' 3" ~: (descifrar "" 3) ~?= "",
    "Caso 0: descifrar 'computacion' 0" ~: (descifrar "computacion" 0) ~?= "computacion",
    "Caso descifrar sin descifrar: cifrar 'computacion' 26" ~: (descifrar "computacion" 26) ~?= "computacion",
    "Caso sin minúsculas: cifrar 'COMPUTACION' 3" ~: (descifrar "COMPUTACION" 1) ~?= "COMPUTACION",
    "Caso mezclado: cifrar 'TsbcbkpPsbdujdp' 1" ~: (descifrar "TsbcbkpPsbdujdp" 1) ~?= "TrabajoPractico"
    ]

testsEjcifrarLista = test [
    "Caso lista vacia: cifrarLista []" ~: (cifrarLista []) ~?= [],
    cifrarLista ["compu", "labo", "intro"] ~?= ["compu", "mbcp", "kpvtq"],
    cifrarLista ["compu", "labo", "pastelitos"] ~?= ["compu", "mbcp", "sdvwholwrv"]
    ]

testsEjfrecuencia = test [
    "Caso string vacio: frecuencia '' " ~:
    expectlistProximity (frecuencia "") [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    "Caso una letra minuscula: frecuencia 'm'" ~: 
    expectlistProximity (frecuencia "m") [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,100.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    "Caso todas minusculas: frecuencia 'dolor'" ~:
    expectlistProximity (frecuencia "dolor") [0.0,0.0,0.0,20.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,20.0,0.0,0.0,40.0,0.0,0.0,20.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    "Caso sin minusculas: frecuencia 'TALLER'" ~:
    expectlistProximity (frecuencia "TALLER") [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    "Caso mezclado: frecuencia 'TaLlEr'" ~:
    expectlistProximity (frecuencia "TaLlEr") [33.33333,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,33.33333,0.0,0.0,0.0,0.0,0.0,33.33333,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    ]

testsEjcifradoMasFrecuente = test [
    "Caso una sola letra: cMF 'm'" ~: expectAnyTuplaAprox (cifradoMasFrecuente "m" 3) [('p', 100.0)],
    "Caso una letra repetida" ~: expectAnyTuplaAprox (cifradoMasFrecuente "taller" 3) [('o', 33.333336)],
    "Caso todas repetidas: cMF 'mmm'" ~: expectAnyTuplaAprox (cifradoMasFrecuente "mmm" 3) [('p', 100.0)],
    "Caso dos repetidas: cMF 'sees'" ~: expectAnyTuplaAprox (cifradoMasFrecuente "sees" 3) [('h', 50.0),('v',50.0)]
    ]

testsEjesDescifrado = test [
    "Caso una sola letra: eD 'a' 'z'" ~: (esDescifrado "a" "z") ~?= True,
    "Caso mismo string: eD 'compu' 'compu'" ~: (esDescifrado "compu" "compu") ~?= True,
    "Caso 1era letra mal cifrada: eD 'compu' 'dqorw'" ~: (esDescifrado "compu" "dqorw") ~?= False,
    "Caso ultima letra mal cifrada: eD 'compu' 'eqorv'" ~: (esDescifrado "compu" "eqorv") ~?= False,
    "Caso verdadero: eD 'cncnr' 'jujuy' " ~: (esDescifrado "cncnr" "jujuy") ~?= True
    ]

testsEjtodosLosDescifrados = test [
    "Caso 1 string: tLD ['compu']" ~: (todosLosDescifrados ["compu"]) ~?= [],
    "Caso ninguno es cifrado: tLD ['compu', 'jujuy', 'taller']" ~: (todosLosDescifrados ["compu", "jujuy", "taller"]) ~?= [],
    "Caso todos son cifrados: tLD ['compu', 'dpnqv', 'eqorw']" ~: 
    expectPermutacion (todosLosDescifrados ["compu", "dpnqv", "eqorw"]) [("compu","dpnqv"),("compu","eqorw"),("dpnqv","compu"),("dpnqv","eqorw"),("eqorw","compu"),("eqorw","dpnqv")],
    "Caso uno es cifrado y otro no: tLD ['compu', 'frpsx', 'bpnqt']" ~: 
    expectPermutacion (todosLosDescifrados ["compu", "frpsx", "bpnqt"]) [("compu", "frpsx"), ("frpsx", "compu")]
    ]

testsEjexpandirClave = test [
    expandirClave "compu" 8 ~?= "compucom",
    expandirClave "clavicornio" 2 ~?= "cl"
    ]

testsEjcifrarVigenere = test [
    cifrarVigenere "computacion" "ip" ~?= "kdueciirqdv",
    cifrarVigenere "sufrimiento" "dolor" ~?= "viqfzpwpbkr"
    ]

testsEjdescifrarVigenere = test [
    descifrarVigenere "kdueciirqdv" "ip" ~?= "computacion",
    descifrarVigenere "viqfzpwpbkr" "dolor" ~?= "sufrimiento"
    ]

testsEjpeorCifrado = test [
    peorCifrado "computacion" ["ip", "asdef", "ksy"] ~?= "asdef",
    peorCifrado "porque" ["das"] ~?= "das"
    ]

testsEjcombinacionesVigenere = test [
    combinacionesVigenere ["hola", "mundo"] ["a", "b"] "ipmb" ~?= [("hola", "b")]
    ]

-- Funciones útiles

-- margetFloat(): Float
-- asegura: res es igual a 0.00001
margenFloat = 0.00001

-- expectAny (actual: a, expected: [a]): Test
-- asegura: res es un Test Verdadero si y sólo si actual pertenece a la lista expected
expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- expectlistProximity (actual: [Float], expected: [Float]): Test
-- asegura: res es un Test Verdadero si y sólo si:
--                  |actual| = |expected|
--                  para todo i entero tal que 0<=i<|actual|, |actual[i] - expected[i]| < margenFloat()
expectlistProximity:: [Float] -> [Float] -> Test
expectlistProximity actual expected = esParecidoLista actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esParecidoLista :: [Float] -> [Float] -> Bool
esParecidoLista actual expected = (length actual) == (length expected) && (esParecidoUnaAUno actual expected)

esParecidoUnaAUno :: [Float] -> [Float] -> Bool
esParecidoUnaAUno [] [] = True
esParecidoUnaAUno (x:xs) (y:ys) = (aproximado x y) && (esParecidoUnaAUno xs ys)

aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat


-- expectAnyTuplaAprox (actual: CharxFloat, expected: [CharxFloat]): Test
-- asegura: res un Test Verdadero si y sólo si:
--                  para algun i entero tal que 0<=i<|expected|,
--                         (fst expected[i]) == (fst actual) && |(snd expected[i]) - (snd actual)| < margenFloat()

expectAnyTuplaAprox :: (Char, Float) -> [(Char, Float)] -> Test
expectAnyTuplaAprox actual expected = elemAproxTupla actual expected ~? ("expected any of: " ++ show expected ++ "\nbut got: " ++ show actual)

elemAproxTupla :: (Char, Float) -> [(Char, Float)] -> Bool
elemAproxTupla _ [] = False
elemAproxTupla (ac,af) ((bc,bf):bs) = sonAprox || (elemAproxTupla (ac,af) bs)
    where sonAprox = (ac == bc) && (aproximado af bf)



-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)

expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)
