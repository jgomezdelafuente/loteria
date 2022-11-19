import random
import numpy as np

import pickle


class combinaciones():
    """Clase dedicada para validar los datos almacendos y generar estadísticas"""
    def __init__(self,vMin,vMax,nElementos):
        """ Se inicializara todos los valores necesarios"""
        self._vMin = vMin
        self._vMax = vMax
        self._nElementos = nElementos
        self._ficheroCombinaciones = 'combinaciones.lst'

      
    
    def ordenarCombinacion(self,vMin,vMax,nElementos):
        pass
    
    
    def generarNumeros(self):
        """El método genera una combinación que estarán entre un valor vMin y vMax"""
        combinacionAleatoria = []
        i=0
        while i < self._nElementos:
            elemento=random.randint(self._vMin,self._vMax)
            combinacionAleatoria.insert(i,elemento)
            i+=1
        combinacionAleatoria.sort()
        #print(combinacionAleatoria)
        return combinacionAleatoria
    
    
    def validarNumerosJugada(self,combinacion):
        """ valida si la combinación no tiene numeros repetidos"""
        if len(combinacion) == len(set(combinacion)):
            print("combinacion valida")
            return True
        else:
            print("combinacion NO valida")
            return False
        
        
    def escribirCombinacionEnFichero(self,combinacion):
        f=open(self._ficheroCombinaciones,'a+')              
        cont=1
        for i in combinacion:
            if cont <self._nElementos:
                f.write(str(i)+";")    
            else:
                f.write(str(i)) 
            cont=cont+1             
        f.write("\n")
        f.close()
            
            
        
        
        
    
    def validarTodosParesImpares(self,combinacion):
        pass
    
    
    
    def mostrarCombinacion(self,combinacion):
        print("valor de la combinacion:", combinacion)
                   
    
        
    
    def tieneRepetidos(self, combinacion):
        """valida que la combinación generada no tenga repetidos"""
        pass
    
    

    
    
        

