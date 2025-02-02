class Producto: 
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

   
    def __str__(self):
        return f'Id Producto {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'
    
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    


if __name__ == '__main__':
    producto1 = Producto('camisa', 100.00)
    print(producto1)

    producto2 = Producto('Pantalon', 150.00)
    print(producto2)
