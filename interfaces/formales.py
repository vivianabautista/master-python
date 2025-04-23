"""
Interfaces Formales
- Fuerza a implementar los métodos de la interfaz
- Se define una clase abstracta que hereda de ABC y 
    se utiliza el decorador @abstractmethod para definir los métodos abstractos
"""


from abc import abstractmethod
from abc import ABCMeta

class Mando(metaclass=ABCMeta):

    def holi(self):
        print("Holi") 

    @abstractmethod
    def siguiente_canal(self):
        """
        métodos abstractos son aquellos que son declarados pero no tienen una implementación.
        """
        pass

    @abstractmethod
    def canal_anterior(self):
        pass

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass

class MandoSamsung(Mando):
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")

class MandoLG(Mando):
    """probar a quitar los métodos abstractos"""
    def siguiente_canal(self):
        print("LG->Siguiente")
    def canal_anterior(self):
        print("LG->Anterior")
    def subir_volumen(self):
        print("LG->Subir")
    def bajar_volumen(self):
        print("LG->Bajar")


mando_samsung = MandoSamsung()
mando_samsung.siguiente_canal()
mando_samsung.holi()


mando_lg = MandoLG()
mando_lg.siguiente_canal()
mando_lg.holi()