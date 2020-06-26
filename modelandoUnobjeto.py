

class Cafetera:
    
    _CAFETERA = ['''
************************
                _
              _(_)_   _ _
            ( ____ ) /_ _|
         ---|======|//   
        |||/           _ _ _
         ---||||---|
       _ _ _||||---|
      (    ( _ _ _ _)       _ _(_ _ _)_ _
=|_ _ )                    |_ _ _ _ _ _ _|
      
************************

''','''
************************

     /\  (¯¯(-)_
    /  \/¯¯--__)
    \  /      /===       
     \/      /=== ▓         
     /      /      ▓
   (_      /        ▓
     ¯¯--__)         ▓
                    _ ▓_ _
                   ||---|
                   ||---|
                _ _(_ _ _)_ _
               |_ _ _ _ _ _ _|
               
************************

''','''
************************ 
                _
              _(_)_   _ _
            ( ____ ) /_ _|
         ---||//            \ | /
        ||======|/             _\|/_
         ---|||=====|---|
       _ _ _||||---|
      (    ( _ _ _ _)         _ _(_ _ _)_ _
=|_ _ )                      |_ _ _ _ _ _ _|
      
************************
''' ]
    
    def __init__(self, inicio): #constructor de clase
        self._inicio = 0
        
    def quiere_café(self): #metodo publico
        self._inicio = 0 #variable para la primera posicion de la lista
        self._mostrar_imagen() #Muestra en pantalla posicion 0 de la lista
        
    def aqui_tienes(self): # metodo publico
        self._inicio = 1
        self._mostrar_imagen()
        
    def disfrutalo(self): #metodo publico
        self._inicio = 2
        self._mostrar_imagen()
        
    def _mostrar_imagen(self): #metodo privado
        if self._inicio == 0: #Si
            print(self._CAFETERA[0]) #Muestra primera posicion de la lista
        elif self._inicio == 1:
            print(self._CAFETERA[1]) #Muestra la segunda posicion de la lista
        elif self._inicio == 2:
            print(self._CAFETERA[2]) #Muestra la tercera posicio de la lista
        else:
            return
            
def run():
    cafetera=Cafetera(inicio = 0)
    
    while True: #Menu de opciones
        command=str(input('''
           ¿Que desea hacer?
                 
           [u]n café?
           [s]irvelo pues!!
           [d]isfrutelo
           [x]alir
                          
           '''))
        if command == 'u':
            cafetera.quiere_café()
        elif command == 's':
            cafetera.aqui_tienes()
        elif command == 'd':
            cafetera.disfrutalo()
        elif command == 'x':
            break
        else:
            print("Este comando no existe!!")
        
if __name__ == '__main__':
    print("************ R E T O  3 *************")
    run()