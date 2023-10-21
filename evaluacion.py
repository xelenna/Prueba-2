class Producto:
    productos_dict = {}

    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = self.calcular_precio_de_venta()

    def calcular_precio_de_venta(self):
        return self.costo / (1 - self.margen_de_venta)

    @classmethod
    def registrar_producto(cls, producto):
        cls.productos_dict[producto.id] = producto
        return producto.precio_de_venta

    @classmethod
    def imprimir_productos(cls):
        for id, producto in cls.productos_dict.items():
            print(f"ID: {id}, Nombre: {producto.nombre}, Precio de Venta: {producto.precio_de_venta}")


# Uso de la clase
p1 = Producto(1, "Camiseta", "Camiseta de algodón", 10, 100, 0.2)
precio_de_venta = Producto.registrar_producto(p1)
print(f"Precio de Venta del Producto {p1.nombre}: {precio_de_venta}")

# Agregando más productos para el ejemplo
p2 = Producto(2, "Pantalón", "Pantalón de denim", 20, 50, 0.25)
Producto.registrar_producto(p2)

Producto.imprimir_productos()
