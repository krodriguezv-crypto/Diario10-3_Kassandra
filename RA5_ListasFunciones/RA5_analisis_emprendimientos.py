"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(ventas):
    """Recibe una lista y retorna el total de ventas"""
    return sum(ventas)

def calcular_porcentaje_logro(total,meta):
    """Calcula el porcentaje de cumplimiento de la venta"""
    porcentaje = meta/meta * 100
    return porcentaje

def calcular_clasificacion(porcentaje):
    if porcentaje >= 100:
        mensaje = "Meta alcanzada"
    elif porcentaje >= 90:
        mensaje = "Advertencia, meta no lograda"
    else: 
        mensaje = "Totalmete insuficiente, revisar perdidas"
    return mensaje

def imprimir_reporte(datos_reporte):
    """Imprime el reporte final de ventas por emprendimiento"""
    
    
    #Encabezado
    print("\nReporte final")
    print("-"* 60)
    
    for fila in datos_reporte:
        print(f"Sede: {fila["nombre"]}")
        print(f"Provincia: {fila["provincia"]}")
        print(f"Tipo: {fila["tipo"]}")
        
        print(f"Total de ventas semanal: ₡{fila["total"]:,.2f}")
        print(f"Porcentaje meta: {fila["porcentaje"]:.2f}%")
        print(f"Promedio diario: {fila["total"]/5:,.2f}")
        print(fila["clasificacion"])
        #cOMPLETAR LO QUE FALTA 
        print("-"*60) 
        

reporte = []
#print("La variable sedes es tipo" , type(sedes).__name__)
for emprendimiento in sedes:
#primer_emprendimiento = sedes[0]
#print("Primer emprendimiento: " , primer_emprendimiento)
#print("El primer emprendimiento es tipo: " , type  (primer_emprendimiento).__name__)
#print("Nombre: " , primer_emprendimiento ["nombre"])
#print("Provincia: " , primer_emprendimiento ["provincia"])
#print("Vemtas: " , primer_emprendimiento ["ventas"])
    ventas = emprendimiento ["ventas"]
    meta = emprendimiento ["meta"]
    nombre = emprendimiento["nombre"]

    total_ventas = calcular_total(ventas)
    porcentaje_emprendimiento = calcular_porcentaje_logro(total_ventas, meta)
    clasificacion = calcular_clasificacion(porcentaje_emprendimiento)
    
    reporte.append(
        {
        "nombre" : emprendimiento["nombre"],
        "provincia" : emprendimiento["provincia"],
        "tipo" : emprendimiento["tipo"],
        "total" : total_ventas,
        "porcentaje" : porcentaje_emprendimiento,
        "clasificacion" :clasificacion
        }
    )
imprimir_reporte(reporte)
    #print(f"/n------ Emprendimiento {nombre} ------")
    #print("Total ventas: " , total_ventas)
    #print("Porcentaje de logros: ", porcentaje_emprendimiento)
    #print (calcular_clasificacion(porcentaje_emprendimiento))