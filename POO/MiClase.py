class MiClase:
    variable_clase = 'valor variable calse'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    ###Este metodo no tiene una relacion directa con nuestra clase    
    @staticmethod
    def metodo_statico():
        print (MiClase.variable_clase)

    ##Este metodo de clase Si tiene una relacion con la clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_statico()
        print(self.variable_clase)
        print(self.variable_instancia)
        




####Metodo estatico, a esta clase no podemos acceder desde un objeto
MiClase.metodo_statico()      

###Metodo de clase, con este metodo si se puede acceder desde un objeto al metodo de clase
## Al generar un objeto(contexto dinamico) ya se guarda en memoria la clase( a esto incluye el contexto dinamico), es por esto que un objeto si puede acceder al contexto estatico y dinamico
MiClase.metodo_clase()
miObjeto1 = MiClase('variable_instancia')
miObjeto1.metodo_clase()

##metodo de instancia si puede acceder al metodo estatico y de clase porque al crear un objeto ya se guarda en la memoria la clase
miObjeto1.metodo_instancia()






print(MiClase.variable_clase)
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

MiClase.varaible_clase2 = 'Valor variable clase 2'

miClase = MiClase('Otro valor de variable instancia')

miClase2 = MiClase('Otro valor de variable instancia')
print(miClase2.variable_instancia)