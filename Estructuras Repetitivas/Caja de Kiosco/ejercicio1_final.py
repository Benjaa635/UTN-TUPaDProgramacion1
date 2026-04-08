

print('Hey! Bienvenido, como le puedo ayudar? Antes, me indica su nombre?')
nombre_cliente = input("Mi nombre es:")
while not nombre_cliente.isalpha():
    print('Intente un nombre que solo contenga letras.')
    nombre_cliente = input("Mi nombre es:")


print(f'Buenos dias {nombre_cliente}!')
producto = input('Cuantos productos le interesaria comprar?')

while not producto.isdigit() or int(producto) < 1:
    print('Necesito que me indique cuantos productos quiere comprar')
    producto = input('Cuantos productos le interesaria comprar?')

producto = int(producto)

total = 0
total_con_descuento = 0
precios = []
descuentos = []


for i in range(producto):
    print(f'Producto {i + 1}')
    precio = input('Precio:')
    while not precio.isdigit():
        precio = input('Precio:')
    precio = int(precio)
    descuento = input('Tiene descuento? S o N: ').lower()
    while descuento not in ['s', 'n']:
        print('Ingrese "S" o "N"... Indicando Si o No.')
        descuento = input('Tiene descuento? S o N: ').lower()

    if descuento == 's':
        precio_final = precio * 0.9
    else:
        precio_final = precio
    
    total = precio + total
    total_con_descuento = precio_final + total_con_descuento
    
    precios.append(precio_final)
    descuentos.append(descuento)

ahorro = total - total_con_descuento
precio_promedio = total_con_descuento / producto

print(f'Cliente: {nombre_cliente}')
print(f'Cantidad de productos: {producto}')
for i in range(producto):
    print(f'Producto {i + 1} - Precio: {precios[i]:.0f} - Descuento (S/N): {descuentos[i]}')
print(f'Total sin descuentos: {total}')
print(f'Total con descuentos: {total_con_descuento:.0f}')
print(f'Ahorro: {ahorro:.0f}')
print(f'Promedio por producto: {precio_promedio:.2f}')



