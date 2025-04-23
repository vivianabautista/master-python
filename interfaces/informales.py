"""
Interfaces informales
- No fuerza a implementar los métodos de la interfaz
"""


class Mando:
    def siguiente_canal(self):
        raise NotImplementedError
    def canal_anterior(self):
        print("no se implementa je")
    def subir_volumen(self):
        pass
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
    

    def subir_volumen(self):
        print("LG->Subir")
    def bajar_volumen(self):
        print("LG->Bajar")


mando = MandoSamsung()
mando.siguiente_canal()
mando.canal_anterior()
mando = MandoLG()
mando.subir_volumen()
mando.canal_anterior() 
mando.siguiente_canal()