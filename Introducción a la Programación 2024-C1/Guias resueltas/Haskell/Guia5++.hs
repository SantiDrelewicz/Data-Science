import Guia5
-- Renombre de Tipos
-- 2. Renombre de secuencias
-- Ejercicio 4.
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

elNombre :: Contacto ->Nombre
elNombre contacto = fst contacto

elTelefono :: Contacto ->Telefono
elTelefono contacto = snd contacto

-- a)
enLosContactos :: Nombre ->ContactosTel ->Bool
enLosContactos nombre [] = False
enLosContactos nombre (contacto:contactos) | nombre == elNombre contacto = True
                                           | otherwise = enLosContactos nombre contactos
-- b)
agregarContacto :: Contacto ->ContactosTel ->ContactosTel
agregarContacto contactoNuevo [] = [contactoNuevo]
agregarContacto contactoNuevo (contacto:contactos) | elNombre contactoNuevo == elNombre contacto = contactoNuevo:contactos
                                                   | otherwise = contacto:(agregarContacto contactoNuevo contactos)
-- c)
eliminarContacto :: Nombre ->ContactosTel ->ContactosTel
eliminarContacto nombre [] = []
eliminarContacto nombre (contacto:contactos) | nombre == elNombre contacto = contactos
                                             | otherwise = contacto:(eliminarContacto nombre contactos)

-- Ejercicio 5. 
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
data Disponibilidad = Libre | Ocupado deriving (Eq, Show)

-- 1.
existeElLocker :: Identificacion ->MapaDeLockers ->Bool
existeElLocker numero [] = False
existeElLocker numero ((identificacion,estado):lockers) | numero == identificacion = True
                                                        | otherwise = existeElLocker numero lockers
-- 2.



