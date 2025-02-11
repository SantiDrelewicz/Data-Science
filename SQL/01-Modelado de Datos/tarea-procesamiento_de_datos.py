# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : 01 - Modelado de Datos - Tarea - Procesamiento de Dados.
Autor  : Santiago Drelewicz
Fecha  : 2024-02-10
"""

Edad = int
CantHijos = int
DNI = int
Salario = float

#%%=================================================================================================
# Actividad n°1
#===================================================================================================

empleado_01: list[tuple[DNI, Edad, CantHijos, Salario]] = [(20_222_333, 45, 2, 20_000),
                                                           (33_456_234, 40, 0, 25_000),
                                                           (45_432_345, 41, 1, 10_000)]

def supera_salario_actividad_01(empleados: list[tuple[DNI, Edad, CantHijos, Salario]],
                                umbral: Salario) -> list[tuple[DNI, Edad, CantHijos, Salario]]:
  """
    Toma como entrada la matriz de empleados y un valor entero denominado umbral, y devuelve una
    matriz (con las 4 columnas) conteniendo aquellos empleados que ganan un salario > umbral.
    - DNI = int
    - Edad = int
    - CantHijos = int
    - Salario = int
  """
  res = []
  for e in empleados:
    if e[3] > umbral:
      res.append(e)
  return res

assert supera_salario_actividad_01(empleado_01, 15_000) == [(20_222_333, 45, 2, 20_000),
                                                            (33_456_234, 40, 0, 25_000)]

#%%=================================================================================================
# Actividad n°2
#===================================================================================================

empleado_02: list[tuple[DNI, Edad, CantHijos, Salario]] = [(20_222_333, 45, 2, 20_000),
                                                           (33_456_234, 40, 0, 25_000),
                                                           (45_432_345, 41, 1, 10_000),
                                                           (43_967_304, 37, 0, 12_000),
                                                           (42_236_276, 36, 0, 18_000)]

assert supera_salario_actividad_01(empleado_02, 15000) == [(20_222_333, 45, 2, 20_000),
                                                           (33_456_234, 40, 0, 25_000),
                                                           (42_236_276, 36, 0, 18_000)]

#%%=================================================================================================
# Actividad n°3
#===================================================================================================

empleado_03: list[tuple[DNI, Salario, Edad, CantHijos]] = [(20_222_333, 20_000, 45, 2),
                                                           (33_456_234, 25_000, 40, 0),
                                                           (45_432_345, 10_000, 41, 1),
                                                           (43_967_304, 12_000, 37, 0),
                                                           (42_236_276, 18_000, 36, 0)]

# assert supera_salario_actividad_01(empleado_03, 15000) == [(20_222_333, 45, 2, 20_000),
#                                                            (33_456_234, 40, 0, 25_000),
#                                                            (42_236_276, 36, 0, 18_000)]

def supera_salario_actividad_03(empleados_03: list[tuple[DNI, Salario, Edad, CantHijos]],
                                umbral: Salario) -> list[tuple[DNI, Edad, CantHijos, Salario]]:
  empleados = []
  for empl_03 in empleados_03:
      empl = (empl_03[0], empl_03[2], empl_03[3], empl_03[1])
      empleados.append(empl)
  return supera_salario_actividad_01(empleados, umbral)

assert supera_salario_actividad_03(empleado_03, 15000) == [(20_222_333, 45, 2, 20_000),
                                                           (33_456_234, 40, 0, 25_000),
                                                           (42_236_276, 36, 0, 18_000)]

#%%=================================================================================================
# Actividad n°4
#===================================================================================================

empleado_04: tuple[list[DNI], list[Edad], list[CantHijos], list[Salario]] = (
    [20222333, 33456234, 45432345, 43967304, 42236276],
    [      45,       40,       41,       37,       36],
    [       2,        0,        1,        0,        0],
    [   20000,    25000,    10000,    12000,    18000]
)

# assert supera_salario_actividad_01(empleado_03, 15000) == [(20_222_333, 45, 2, 20_000),
#                                                            (33_456_234, 40, 0, 25_000),
#                                                            (42_236_276, 36, 0, 18_000)]

def supera_salario_actividad_04(
    empleados_04: tuple[list[DNI], list[Edad], list[CantHijos], list[Salario]],
    umbral: Salario
  ) -> list[tuple[DNI, Edad, CantHijos, Salario]]:

  num_empleados = len(empleados_04[0])
  empleados = []
  for col in range(num_empleados):
      empleado = tuple(empleados_04[fila][col] for fila in range(4))
      empleados.append(empleado)

  return supera_salario_actividad_01(empleados, umbral)

assert supera_salario_actividad_04(empleado_04, 15000) == [(20_222_333, 45, 2, 20_000),
                                                           (33_456_234, 40, 0, 25_000),
                                                           (42_236_276, 36, 0, 18_000)]
