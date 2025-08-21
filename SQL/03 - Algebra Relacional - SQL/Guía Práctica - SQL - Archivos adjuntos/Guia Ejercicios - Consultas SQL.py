# -*- coding: utf-8 -*-
"""
Materia            : Laboratorio de datos - FCEyN - UBA
Guía de ejercicios : Consultas SQL
Autor              : Santiago Drelewicz
Fecha              : 2025-02-16
"""
# %%
import pandas as pd
from pandasql import sqldf
import duckdb

# %%
pd.options.display.max_columns = 8

casos = pd.read_csv("casos.csv")
tipoevento = pd.read_csv("tipoevento.csv")
grupoetario = pd.read_csv("grupoetario.csv") 
provincia = pd.read_csv("provincia.csv")
departamento = pd.read_csv("departamento.csv")

# %%
def capitalizar_columnas(self: pd.DataFrame):
    """
    Reemplaza la primer letra de todas las columnas del dataFrame
    por su mayúscula correspondiente.
    """
    self.columns = self.columns.str.capitalize()

pd.DataFrame.capitalizar_columnas = capitalizar_columnas

casos.capitalizar_columnas()
grupoetario.capitalizar_columnas()
provincia.capitalizar_columnas()
tipoevento.capitalizar_columnas()
departamento.capitalizar_columnas()

#%% Para que no se muestra la columna de indices de los dataframes resultado.
def custom_str(self):
    return self.to_string(index=False, max_rows=24)

pd.DataFrame.__str__ = custom_str
pd.DataFrame.__repr__ = custom_str
#%%===========================================================================
# A. Consultas sobre una tabla
#=============================================================================
# a. Listar sólo los nombres de todos los departamentos que hay en la tabla
#    departamento (dejando los registros repetidos).

consultaSQL = """
              SELECT Descripcion
              FROM departamento;
              """

dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# b. Listar sólo los nombres de todos los departamentos que hay en la tabla
#    departamento (eliminando los registros repetidos).

consultaSQL = """
              SELECT DISTINCT Descripcion
              FROM departamento;
              """

dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# c. Listar sólo los códigos de departamento y sus nombres, de todos los
#    departamentos que hay en la tabla departamento.

consultaSQL = """
                SELECT Id, Descripcion
                FROM departamento;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# d. Listar todas las columnas de la tabla departamento

consultaSQL = """
                SELECT *
                FROM departamento;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# e. Listar los códigos de departamento y nombres de todos los departamentos
#    que hay en la tabla departamento. Utilizar los siguientes alias para las
#    columnas: codigo_depto y nombre_depto, respectivamente.

consultaSQL = """
                SELECT Id AS codigo_depto, Descripcion AS nombre_depto
                FROM departamento
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# f. Listar los registros de la tabla departamento cuyo código de provincia es
#    igual a 54

consultaSQL = """
                SELECT *
                FROM departamento
                WHERE Id_provincia = 54
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# g. Listar los registros de la tabla departamento cuyo código de provincia es
#    igual a 22, 78 u 86

consultaSQL = """
                SELECT *
                FROM departamento
                WHERE Id_provincia = 22 OR
                      Id_provincia = 78 OR
                      Id_provincia = 86
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# h. Listar los registros de la tabla departamento cuyo código de provincia se
#    encuentren entre el 50 y el 59 (ambos valores inclusive).

consultaSQL = """
                SELECT *
                FROM departamento
                WHERE 50 <= Id_provincia AND Id_provincia <= 59
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%===========================================================================
# B. Consultas multitabla (INNER JOIN)
#=============================================================================
# a. Devolver una lista con los código y nombres de departamentos, asociados al
#    nombre de la provincia al que pertenecen.

consultaSQL = """
                 SELECT d.Id AS codigo_depto,
                        d.Descripcion AS nombre_depto,
                        p.Descripcion
                 FROM departamento as d
                 INNER JOIN provincia as p
                 ON d.Id_provincia=p.Id
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# b. Devolver los casos registrados en la provincia de “Chaco”.

consultaSQL = """
                SELECT c.Id
                FROM
                  casos as c
                  INNER JOIN departamento AS d
                    ON c.Id_depto = d.Id
                  INNER JOIN provincia as p
                    ON d.Id_provincia = p.Id
                WHERE p.Descripcion = "Chaco";

              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# c. Devolver los casos registrados en la provincia de “Buenos Aires” cuyo campo
#    cantidad supere los 10 casos

consultaSQL = """
                SELECT c.Id
                FROM
                  casos as c
                  INNER JOIN departamento AS d
                    ON c.Id_depto = d.Id
                  INNER JOIN provincia as p
                    ON d.Id_provincia = p.Id
                WHERE p.Descripcion = "Buenos Aires" AND c.Cantidad > 10;

              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%===========================================================================
# C. Consultas multitabla (OUTER JOIN)
#=============================================================================
# a. Devolver un listado con los nombres de los departamentos que no tienen
#    ningún caso asociado.

consultaSQL = """
                SELECT d.Descripcion
                FROM
                  departamento as d
                  LEFT OUTER JOIN casos as c
                    ON d.Id = c.Id_depto
                WHERE c.Id IS NULL;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# b. Devolver un listado con los tipos de evento que no tienen ningún caso
#    asociado.


consultaSQL = """
                SELECT t.Descripcion
                FROM
                  tipoevento as t
                  LEFT OUTER JOIN casos as c
                    ON t.Id = c.Id_tipoevento
                WHERE c.Id IS NULL;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%===========================================================================
# D. Consultas resumen
#=============================================================================
# a. Calcular la contidad total de casos que hay en la tabla casos

consultaSQL = """
                SELECT SUM(Cantidad) AS Cant_tot_casos
                FROM casos;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# b. Calcular la cantidad total de casos que hay en la tabla casos para cada año
#    y cada tipo de caso. Presentar la información de la siguiente manera:
#    descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso
#    (ascendente) y año (ascendente)

consultaSQL = """
                SELECT te.Descripcion as Tipo_evento,
                       c.Anio,
                       SUM(c.Cantidad) AS Cantidad
                FROM
                  casos AS c
                  INNER JOIN tipoevento as te
                  ON c.Id_tipoevento = te.Id
                  GROUP BY te.Descripcion, c.Anio
                  ORDER BY te.Descripcion ASC, c.Anio DESC;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# c. Misma consulta que el item anterior pero sólo para el año 2019

consultaSQL = """
                SELECT te.Descripcion AS Tipo_evento,
                       c.Anio,
                       SUM(c.Cantidad) AS Cantidad
                FROM
                    casos AS c
                    INNER JOIN tipoevento as te
                    ON c.Id_tipoevento = te.Id
                    GROUP BY te.Descripcion, c.Anio
                    HAVING c.Anio = 2019
                    ORDER BY te.Descripcion ASC, c.Anio DESC;
              """

dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# d. Calcular la cantidad total de departamentos que hay por provincia.
#    Presentar la información ordenada por código de provincia

consultaSQL = """
                SELECT Id_provincia, COUNT(*) AS Cant_deptos
                FROM departamento
                GROUP BY Id_provincia
                ORDER BY Id_provincia ASC;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# e. Listar todos los departamentos con menos cantidad de casos en el
#    año 2019

consultaSQL1 = """
                SELECT Id_depto, SUM(Cantidad) AS Cant_casos
                FROM casos
                GROUP BY Id_depto
                HAVING Anio = 2019
              """
casosPorDepartamento2019 = sqldf(consultaSQL1)

consultaSQL2 = """
                SELECT d.Descripcion AS Departamentos_con_menos_casos, c.Cant_casos
                FROM departamento as d
                INNER JOIN casosPorDepartamento2019 as c
                ON d.Id = c.Id_depto
                WHERE c.Cant_casos = (SELECT MIN(Cant_casos)
                                      FROM casosPorDepartamento2019)
              """
dataFrameResultado = sqldf(consultaSQL2)

dataFrameResultado

#%%-----------
# f. Listar los departamentos con más cantidad de casos en el año 2020.

consultaSQL1 = """
                SELECT Id_depto, SUM(Cantidad) AS Cant_casos
                FROM casos
                GROUP BY Id_depto
                HAVING Anio = 2020
              """
casosPorDepartamento2019 = sqldf(consultaSQL1)

consultaSQL2 = """
                SELECT d.Descripcion AS Departamentos_con_menos_casos,
                       c.Cant_casos
                FROM departamento as d
                INNER JOIN casosPorDepartamento2019 as c
                ON d.Id = c.Id_depto
                WHERE c.Cant_casos = (SELECT MAX(Cant_casos)
                                      FROM casosPorDepartamento2019)
              """

dataFrameResultado = sqldf(consultaSQL2)

dataFrameResultado

#%%-----------
# g. Listar el promedio de la cantidad de casos por provincia y año

consultaSQL = """
                SELECT p.Descripcion AS Provincia,
                        c.Anio AS Año,
                        AVG(c.Cantidad) AS Promedio_casos
                FROM
                  casos AS c
                  INNER JOIN departamento AS d
                    ON c.Id_depto = d.Id
                  INNER JOIN provincia AS p
                    ON d.Id_provincia = p.Id
                GROUP BY p.Descripcion, c.Anio
                ORDER BY p.Id ASC, c.Anio DESC;
              """

dataFrameResultado = sqldf(consultaSQL)
dataFrameResultado

#%%-----------
# h. Listar, para cada provincia y año, cuáles fueron los departamentos que más
#    cantidad de casos tuvieron.

consultaSQL1 = """
                 SELECT p.Descripcion AS Provincia,
                        c.Anio AS Año,
                        d.Descripcion AS Departamento,
                        SUM(c.Cantidad) AS Cantidad
                 FROM
                   casos AS c
                   INNER JOIN departamento AS d
                     ON c.Id_depto = d.Id
                   INNER JOIN provincia AS p
                     ON d.Id_provincia = p.Id
                 GROUP BY p.Descripcion, c.Anio, d.Descripcion
                 ORDER BY p.Id ASC, c.Anio DESC, d.Id ASC;
              """
casosPorDeptoPorProvYAnio = sqldf(consultaSQL1)

consultaSQL2 = """
                SELECT Provincia, Año,
                       Departamento AS Departamento_con_mas_casos,
                       MAX(Cantidad) AS Cantidad
                FROM casosPorDeptoPorProvYAnio
                GROUP BY Provincia, Año
                ORDER BY Año DESC;
              """
dataFrameResultado = sqldf(consultaSQL2)
dataFrameResultado

#%%-----------
# i. Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo la
#    provincia de Buenos Aires en el año 2019.

consultaSQL = """
                SELECT p.Descripcion AS Provincia,
                       c.Anio AS Año,
                       SUM(c.Cantidad) AS Cantidad_total,
                       MAX(c.Cantidad) AS Cantidad_max,
                       MIN(c.Cantidad) AS Cantidad_min,
                       AVG(c.Cantidad) AS Cantidad_promedio
                FROM
                  casos AS c
                  INNER JOIN departamento AS d
                    ON c.Id_depto = d.Id
                  INNER JOIN provincia AS p
                    ON d.Id_provincia = p.Id
                GROUP BY p.Descripcion, c.Anio
                HAVING p.Descripcion = "Buenos Aires" AND c.Anio = 2019
              """
dataFrameResultado = sqldf(consultaSQL)
dataFrameResultado

#%%-----------
# j. Misma consulta que el ítem anterior, pero sólo para aquellos casos en que la
#    cantidad total es mayor a 1000 casos.

consultaSQL = """
                SELECT p.Descripcion AS Provincia,
                       c.Anio AS Año,
                       SUM(c.Cantidad) AS Cantidad_total,
                       MAX(c.Cantidad) AS Cantidad_max,
                       MIN(c.Cantidad) AS Cantidad_min,
                       AVG(c.Cantidad) AS Cantidad_promedio
                FROM
                  casos AS c
                  INNER JOIN departamento AS d
                    ON c.Id_depto = d.Id
                  INNER JOIN provincia AS p
                    ON d.Id_provincia = p.Id
                GROUP BY p.Descripcion, c.Anio
                HAVING SUM(c.Cantidad) > 1000 AND c.Anio = 2019;
              """
dataFrameResultado = sqldf(consultaSQL)
dataFrameResultado

#%%-----------
# k. Listar los nombres de departamento (y nombre de provincia) que tienen
#    mediciones tanto para el año 2019 como para el año 2020. Para cada uno de
#    ellos devolver la cantidad de casos promedio. Ordenar por nombre de
#    provincia (ascendente) y luego por nombre de departamento (ascendente)

consultaSQL = """
                SELECT d.Descripcion AS Departamento,
                       p.Descripcion AS Provincia,
                       AVG(c.Cantidad) AS Cantidad_promedio
                FROM
                  casos AS c
                  INNER JOIN departamento AS d
                    ON c.Id_depto = d.Id
                  INNER JOIN provincia AS p
                    ON d.Id_provincia = p.Id
                GROUP BY d.Descripcion, p.Descripcion
                HAVING c.Anio = 2019 OR c.Anio = 2020
                ORDER BY p.Descripcion ASC, d.Descripcion ASC;
              """
dataFrameResultado = sqldf(consultaSQL)
dataFrameResultado

#%%-----------
# l. Devolver una tabla que tenga los siguientes campos: descripción de tipo de
#    evento, id_depto, nombre de departamento, id_provincia, nombre de
#    provincia, total de casos 2019, total de casos 2020.

consultaSQL2019 = """
                    SELECT te.Descripcion AS Tipo_evento,
                           Id_depto,
                           d.Descripcion AS Departamento,
                           Id_provincia,
                           p.Descripcion AS Provincia,
                           SUM(c.Cantidad) AS Cantidad_2019
                    FROM
                    casos AS c
                    INNER JOIN tipoevento AS te
                    ON c.Id_tipoevento = te.Id
                    INNER JOIN departamento AS d
                    ON c.Id_depto = d.Id
                    INNER JOIN provincia AS p
                    ON d.Id_provincia = p.Id
                    GROUP BY te.Descripcion, Id_depto, d.Descripcion, Id_provincia, p.Descripcion
                    HAVING c.Anio = 2019
                  """
dataFrameResultado = sqldf(consultaSQL2019)
print("CORREGIR")
dataFrameResultado

#%%===========================================================================
# E. Subconsultas (ALL, ANY)
#=============================================================================
# a. Devolver el departamento que tuvo la mayor cantidad de casos sin hacer uso
#    de MAX, ORDER BY ni LIMIT.

consultaSQL = """
                SELECT d.Descripcion AS Depto_con_mayor_cant_casos,
                       SUM(c.Cantidad) AS Cantidad_total
                FROM casos AS c
                INNER JOIN departamento AS d
                ON c.Id_depto = d.Id
                GROUP BY d.Descripcion
                HAVING SUM(c.Cantidad) >= ALL (
                  SELECT SUM(Cantidad)
                  FROM casos
                  GROUP BY Id_depto
                );
              """
dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado

#%%-----------
# b. Devolver los tipo de evento que tienen casos asociados. (Utilizando ALL o
#    ANY).

consultaSQL = """
                SELECT Descripcion AS Tipo_evento_sin_casos,
                FROM tipoevento
                WHERE Id = ANY (
                  SELECT DISTINCT Id_tipoevento
                  FROM casos
                );
              """
dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado

#%%===========================================================================
# F. Subconsultas (IN, NOT IN)
#=============================================================================
# a. Devolver los tipo de evento que tienen casos asociados (Utilizando IN, NOT
#    IN).

consultaSQL = """
                SELECT Descripcion AS Tipo_evento_con_casos
                FROM tipoevento
                WHERE Id IN (
                  SELECT DISTINCT Id_tipoevento
                  FROM casos
                );
              """
dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado

#%%-----------
# b. Devolver los tipo de evento que NO tienen casos asociados. (Utilizando ALL
#    o ANY).

consultaSQL = """
                SELECT Descripcion AS Tipo_evento_con_casos
                FROM tipoevento
                WHERE Id NOT IN (
                  SELECT DISTINCT Id_tipoevento
                  FROM casos
                );
              """

dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado

#%%===========================================================================
# G. Subconsultas (EXISTS, NOT EXISTS)
#=============================================================================
# a. Devolver los tipo de evento que tienen casos asociados (Utilizando EXISTS,
#    NOT EXISTS).

consultaSQL = """
                SELECT Descripcion AS Tipo_evento_con_casos
                FROM tipoevento AS te
                WHERE EXISTS (
                  SELECT *
                  FROM casos AS c
                  WHERE c.Id_tipoevento = te.Id
                );
              """
dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado

#%%-----------
# b. Devolver los tipo de evento que NO tienen casos asociados. (Utilizando
#    EXISTS, NOT EXISTS).

consultaSQL = """
                SELECT Descripcion AS Tipo_evento_con_casos
                FROM tipoevento AS te
                WHERE NOT EXISTS (
                  SELECT DISTINCT Id_tipoevento
                  FROM casos AS c
                  WHERE c.Id_tipoevento = te.Id
                );
              """

dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado

#%%===========================================================================
# H. Subconsultas correlacionadas
#=============================================================================
# a. Listar las provincias que tienen una cantidad total de casos mayor al
#    promedio de casos del país. Hacer el listado agrupado por año.


consultaSQL = """
                SELECT c.Anio,
                       p.Descripcion AS Provincia,
                FROM 
                  departamento AS d
                  INNER JOIN provincia AS p
                    ON p.Id = d.Id_provincia
                  INNER JOIN casos AS c
                    ON d.Id = c.Id_depto
                GROUP BY c.Anio, p.Descripcion
                HAVING SUM(c.Cantidad) > ALL (
                  SELECT AVG(Cantidad)
                  FROM casos
                  WHERE c.Anio = Anio
                )
                ORDER BY c.Anio DESC;
              """
dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado

#%%-----------
# b. Por cada año, listar las provincias que tuvieron una cantidad total de casos
#    mayor a la cantidad total de casos que la provincia de Corrientes.

consultaSQL = """
                SELECT c1.Anio, p1.Descripcion AS Provincia
                FROM
                  departamento AS d1
                  INNER JOIN provincia AS p1
                    ON p1.Id = d1.Id_provincia
                  INNER JOIN casos AS c1
                    ON d1.Id = c1.Id_depto
                GROUP BY c1.Anio, p1.Descripcion
                HAVING SUM(c1.Cantidad) > (
                  SELECT SUM(c2.Cantidad)
                  FROM casos AS c2
                  INNER JOIN departamento AS d2
                  ON d2.Id = c2.Id_depto
                  INNER JOIN provincia AS p2
                  ON d2.Id_provincia = p2.Id
                  WHERE p2.Descripcion = 'Corrientes' AND 
                        c2.Anio = c1.Anio
                )
                ORDER BY c1.Anio DESC;
              """

dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado

#%%===========================================================================
# I. Más consultas sobre una tabla 
#=============================================================================
# a. Listar los códigos de departamento y sus nombres, ordenados por estos
#    últimos (sus nombres) de manera descendentes (de la Z a la A). En caso de
#    empate, desempatar por código de departamento de manera ascendente.

consultaSQL = """
                SELECT Id, Descripcion
                FROM departamento
                ORDER BY Descripcion DESC, Id ASC;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# b. Listar los registros de la tabla provincia cuyos nombres comiencen con la
#    letra M.

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE Descripcion LIKE 'M%';
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# c. Listar los registros de la tabla provincia cuyos nombres comiencen con la
#    letra S y su quinta letra sea una letra A.

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE Descripcion LIKE 'S%' AND Descripcion LIKE '____a%';
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# d. Listar los registros de la tabla provincia cuyos nombres terminan con la
#    letra A.

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE Descripcion LIKE '%a';
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# e. Listar los registros de la tabla provincia cuyos nombres tengan
#    exactamente 5 letras.

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE Descripcion LIKE '_____';
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# f. Listar los registros de la tabla provincia cuyos nombres tengan ”do” en
#    alguna parte de su nombre.

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE Descripcion LIKE '%do%';
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# g. Listar los registros de la tabla provincia cuyos nombres tengan ”do” en
#    alguna parte de su nombre y su código sea menor a 30.

consultaSQL = """
                SELECT *
                FROM provincia
                WHERE Descripcion LIKE '%do%' AND Id < 30;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# h. Listar los registros de la tabla departamento cuyos nombres tengan ”san”
#    en alguna parte de su nombre. Listar sólo id y descripcion. Utilizar los
#    siguientes alias para las columnas: codigo_depto y nombre_depto,
#    respectivamente. El resultado debe estar ordenado por sus nombres de
#    manera descendentes (de la Z a la A).

consultaSQL = """
                SELECT Id AS Codigo_depto, Descripcion AS Nombre_depto
                FROM departamento
                WHERE Descripcion LIKE '%san%'
                ORDER BY Descripcion DESC;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# i. Devolver aquellos casos de las provincias cuyo nombre terminen con la letra
#    a y el campo cantidad supere 10. Mostrar: nombre de provincia, nombre de
#    departamento, año, semana epidemiológica, descripción de grupo etario y
#    cantidad. Ordenar el resultado por la cantidad (descendente), luego por el
#    nombre de la provincia (ascendente), nombre del departamento
#    (ascendente), año (ascendente) y la descripción del grupo etario
#    (ascendente).

consultaSQL = """
                SELECT p.Descripcion AS Provincia,
                       d.Descripcion AS Departamento,
                       c.Anio,
                       c.Semana_epidemiologica,
                       ge.Descripcion AS Grupo_etario,
                       c.Cantidad
                FROM
                  casos AS c
                  INNER JOIN departamento AS d
                  ON c.Id_depto = d.Id
                  INNER JOIN provincia AS p
                  ON d.Id_provincia = p.Id
                  INNER JOIN grupoetario AS ge 
                  ON c.Id_grupoetario = ge.Id
                WHERE p.Descripcion LIKE '%a' AND c.Cantidad > 10
                ORDER BY c.Cantidad DESC, 
                         p.Descripcion ASC, 
                         d.Descripcion ASC, 
                         c.Anio ASC, 
                         ge.Descripcion ASC;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# j. Ídem anterior, pero devolver sólo aquellas tuplas que tienen el máximo en 
#    el campo cantidad.

consultaSQL = """
                SELECT p.Descripcion AS Provincia,
                       d.Descripcion AS Departamento,
                       c.Anio,
                       c.Semana_epidemiologica,
                       ge.Descripcion AS Grupo_etario,
                       c.Cantidad
                FROM
                  casos AS c
                  INNER JOIN departamento AS d
                  ON c.Id_depto = d.Id
                  INNER JOIN provincia AS p
                  ON d.Id_provincia = p.Id
                  INNER JOIN grupoetario AS ge 
                  ON c.Id_grupoetario = ge.Id
                WHERE c.Cantidad >= ALL (
                  SELECT c2.Cantidad
                  FROM casos AS c2
                )
                ORDER BY c.Cantidad DESC, 
                         p.Descripcion ASC, 
                         d.Descripcion ASC, 
                         c.Anio ASC, 
                         ge.Descripcion ASC;
              """
dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado

#%%===========================================================================
# J. Reemplazos
#=============================================================================
# a. Listar los id y descripción de los departamentos. Estos últimos sin tildes 
#    y en orden alfabético.

consultaSQL = """
                SELECT Id, REPLACE(Descripcion, 'á', 'a') AS Descripcion
                FROM (
                  SELECT Id, REPLACE(Descripcion, 'é', 'e') AS Descripcion
                  FROM (
                    SELECT Id, REPLACE(Descripcion, 'í', 'i') AS Descripcion
                    FROM (
                      SELECT Id, REPLACE(Descripcion, 'ó', 'o') AS Descripcion
                      FROM (
                        SELECT Id, REPLACE(Descripcion, 'ú', 'u') AS Descripcion
                        FROM departamento
                      )
                    )
                  )
                )  
                ORDER BY Descripcion ASC;
              """
dataFrameResultado = sqldf(consultaSQL)

dataFrameResultado

#%%-----------
# b. Listar los nombres de provincia en mayúscula, sin tildes y en orden
#    alfabético.

consultaSQL = """
                SELECT UPPER(
                  REPLACE(Descripcion, 'á', 'a')
                ) AS Descripcion
                FROM (
                  SELECT REPLACE(Descripcion, 'é', 'e') AS Descripcion
                  FROM (
                    SELECT REPLACE(Descripcion, 'í', 'i') AS Descripcion
                    FROM (
                      SELECT REPLACE(Descripcion, 'ó', 'o') AS Descripcion
                      FROM (
                        SELECT REPLACE(Descripcion, 'ú', 'u') AS Descripcion
                        FROM provincia
                      )
                    )
                  )
                )
                ORDER BY Descripcion ASC;
              """
dataFrameResultado = duckdb.query(consultaSQL).to_df()

dataFrameResultado