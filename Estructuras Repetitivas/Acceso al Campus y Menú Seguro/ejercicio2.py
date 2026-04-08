import time

user = 'alumno'
clave = 'python123'
maximos_intentos = 3
intentos = 0
sesion_iniciada = False

login_user = input('Ingrese su Usuario: ')
clave_user = input('Ingrese su Contraseña: ')
if login_user == user and clave_user == clave:
    sesion_iniciada = True

while not sesion_iniciada and intentos != 2:
    print(f'Usuario: {login_user}' )
    print(f'Clave ******')
    print(f'Credenciales invalidas, tiene {maximos_intentos - intentos - 1} intentos restantes')
    login_user = input('Ingrese su Usuario: ')
    clave_user = input('Ingrese su Contraseña: ')
    intentos = intentos + 1
    
    if login_user == user and clave_user == clave:
        sesion_iniciada = True
        print(f'Usuario: {user}' )
        print(f'Clave {clave}')
        print(f'Acceso Concedido')

    if intentos == 2:
        print('================')
        print('Cuenta bloqueada')
        print('Cuenta bloqueada')
        print('Cuenta bloqueada')
        print('================')
        break
        
if sesion_iniciada:
    while True:
        time.sleep(1)
        print('================================')
        print(f'Bienvenido {user}')
        print('1. Ver estado de inscripcion')
        print('2. Cambiar Clave')
        print('3. Mostrar mensaje motivacional')
        print('4. Salir')
        print('================================')
        
        while True:
            respuesta = input('Que quiere hacer: ')
            
            if respuesta.isdigit():
                opcion = int(respuesta)
            
                if opcion in (1, 2, 3, 4):
                
                    if opcion == 1:
                        print('================================')
                        print('Inscripto')
                        break

                    elif opcion == 2:
                        print('================================')
                        print('Para cambiar la clave necesita ingresar una nueva clave')
                        print('Recuerda que esta requiere un minimo de 6 caracteres')
                        nueva_clave = input('Nueva clave: ')
                        

                        while len(nueva_clave) < 6:
                            print('Se requiere un minimo de 6 caracteres')
                            nueva_clave = input('Nueva clave: ')

                        confirmacion_clave = input('Repita la contraseña: ')

                        if nueva_clave == confirmacion_clave:
                            print('Has actualizado tu contraseña correctamente')
                        else:
                            print('Las contraseñas no coinciden.')
                        
                        break
                        

                    elif opcion == 3:
                        print('================================')
                        print('La vida te sonríe cuando decides mirarla con optimismo')
                        break

                    elif opcion == 4:
                        print('================================')
                        print('Cerrando sesion...')
                        print('================================')
                        sesion_iniciada = False
                        break
                else:
                    print('ERROR: opcion fuera de rango')
            else:
                print('Ingrese un numero valido')
        if sesion_iniciada == False:
            break