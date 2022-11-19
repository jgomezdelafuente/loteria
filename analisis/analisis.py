class analisis():
    """Clase dedicada a realizar un estudio sobre las combinaciones"""
    
    def __init__(self,nElementos):
        """ Se inicializara todos los valores necesarios"""
        self._nElementos=nElementos
        self._ficheroCombinaciones = 'combinaciones.lst'    
    
    def calcularRangoElementos(self):
        df = pd.read_csv(self._ficheroCombinaciones,  sep=';',  comment='#', header=0)
                      
        with open(self._ficheroCombinaciones,'r') as f:
            for combinacion in f:
                #Se quita los salto de linea
                combinacion = combinacion.strip()
                #Se realiza un split por el separados;
                combinacionArray=combinacion.split(';')
                
                
                