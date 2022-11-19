from Juegos.combinaciones import *

#Se pueble un total de $numeroJugadas en un fichero de combinaciones
numeroJugadas=10
i=0
while i <= numeroJugadas-1:
    
    jugada = combinaciones(1,49,6)
    combinacion = jugada.generarNumeros()
    jugada.mostrarCombinacion(combinacion)
    jugada.validarNumerosJugada(combinacion)
    jugada.escribirCombinacionEnFichero(combinacion)
    i=i+1

