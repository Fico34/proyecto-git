#1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo.
"""class rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area_rectangulo(self):
        return self.base * self.altura
Rectangulo=rectangulo(100,200)
print(f"el area del rectangulo es:{Rectangulo.area_rectangulo()}")"""


"""2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""
"""class mate():
    def __init__(self,num_cebadas,estado):
        self.num_cebadas=num_cebadas
        self.estado=estado
        self.max_cebadas=False
    def cebar(self):
        if self.esta_lleno:
            raise Exception("cuidado, te quemaste")
        self.esta_lleno=True
    def beber(self):
        if not self.esta_lleno:
            raise Exception("el mate esta vacio")
        self.esta_lleno=False
        if self.cebadas_rastantes>0:
            self.cebadas_restantes-=1
        else:
            print("el mate esta lavado")
    def __str__(self):
        Estado="lleno"if self.esta_lleno  else"vacio"
        return f"mate{Estado}cebadas restantes:{self.cebadas_restantes}."""""


"""3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho."""
"""class Corcho:
    def __init__(self,bodega):
        self.bodega=bodega
class Botella:
    def __init__(self,corcho=None):
        self.corcho=corcho
class Sacacorchos:
    def destapar(self):
        self.corcho=None
    def destapar(self,botella):
        if self.corcho is not None:
            return("el sacacorchos ya contiene un corcho.")
        self.corcho=botella.destapar()
    def limpiar(self):
        if self.corcho is None:
            return("no hay corcho en el sacacorcho para liompiar.")
        self.corcho=None
corcho=Corcho("bodega cafayate")
botella=Botella(corcho)"""
 


"""4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método. """
class Restaurante:
    def __init__(self,restaurante_nombre,tipo_comida):
        self.restaurante_nombre=restaurante_nombre
        self.tipo_comida=tipo_comida
    def describir_restaurante(self):
        print(f"Nombre del restaurante:{self.restaurante_nombre}")
        print(f"Tipo de comida:{self.tipo_comida}")
    def abrir_restaurante(self):
        print(f"El restaurante{self.restaurante_nombre},esta abierto.")
class heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores=[]
    def mostrar_sabores(self):
        if self.sabores:
                print(f"sabores disponibles en {self.restaurante_nombre}:")
                for sabor in self.sabores:
                    print(f"- {sabor}")
        else:
                print(f"no hay sabores disponibles actualmente en {restaurante_nombre}.")
Heladeria=heladeria("Grido", "Helados")
Heladeria.describir_restaurante()
Heladeria.abrir_restaurante()
Heladeria.sabores=["vainilla","dulce de leche","frutilla","banana"]
Heladeria.mostrar_sabores()
