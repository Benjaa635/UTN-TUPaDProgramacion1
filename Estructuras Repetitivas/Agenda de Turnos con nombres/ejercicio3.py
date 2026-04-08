import time

sesion_iniciada = False
lunes1 = 'libre'
lunes2 = 'libre'
lunes3 = 'libre'
lunes4 = 'libre'
martes1 = "libre"
martes2 = "libre"
martes3 = "libre"
cantidad_turnos_lunes = 0
cantidad_turnos_martes = 0

nombre = input('Ingrese su nombre: ')

while sesion_iniciada == False:
    if nombre.isalpha():
        user = nombre
        sesion_iniciada = True
    else:
        print('Ingrese un nombre que solo contenga letras.')
        nombre = input('Ingrese su nombre: ')

if sesion_iniciada:
    while True:
        time.sleep(2)
        print('================================')
        print(f'Bienvenido {user}')
        print('1. Reservar turno')
        print('2. Cancelar turno (por nombre)')
        print('3. Ver agenda del día')
        print('4. Ver resumen general')
        print('5. Cerrar sistema')
        print('================================')
        
        while True:
            respuesta = input('Que desea hacer: ')
            
            if respuesta.isdigit():
                opcion = int(respuesta)
            
                if opcion in (1, 2, 3, 4, 5):
                
                    if opcion == 1:
                        print('================================')
                        print('1. Lunes')
                        print('2. Martes')
                        print('================================')
                        respuesta1 = input('Seleccione el dia (1/2): ')
                        opcion1 = int(respuesta1)
                        if opcion1 == 1:
                            print('Agendar un turno')
                            nombre_paciente = input('Ingrese el nombre del paciente: ')
                            if nombre_paciente.isalpha():
                                if nombre_paciente in (lunes1, lunes2, lunes3, lunes4):
                                    print('Esta persona ya cuenta con un turno para ese dia.')
                                elif nombre_paciente not in lunes1 and lunes1 == 'libre':
                                    lunes1 = nombre_paciente
                                    print(f'Se le ha agendado un turno a {nombre_paciente} para el dia Lunes')
                                elif nombre_paciente not in lunes2 and lunes2 == 'libre':
                                    lunes2 = nombre_paciente
                                    print(f'Se le ha agendado un turno a {nombre_paciente} para el dia Lunes')
                                elif nombre_paciente not in lunes3 and lunes3 == 'libre':
                                    lunes3 = nombre_paciente
                                    print(f'Se le ha agendado un turno a {nombre_paciente} para el dia Lunes')
                                elif nombre_paciente not in lunes4 and lunes4 == 'libre':
                                    lunes4 = nombre_paciente
                                    print(f'Se le ha agendado un turno a {nombre_paciente} para el dia Lunes')
                                else:
                                    print('ERROR. Intentelo nuevamente.')
                            else:
                                print('Asegurese que el nombre sean solo letras.')
                                nombre_paciente = input('Ingrese el nombre del paciente: ')
                        elif opcion1 == 2:
                            print('Agendar un turno')
                            nombre_paciente = input('Ingrese el nombre del paciente: ')
                            if nombre_paciente.isalpha():
                                if nombre_paciente in (martes1, martes2, martes3):
                                    print('Esta persona ya cuenta con un turno para ese dia.')
                                elif nombre_paciente not in martes1 and martes1 == 'libre':
                                    martes1 = nombre_paciente
                                    print(f'Se le ha agendado un turno a {nombre_paciente} para el dia Martes')
                                elif nombre_paciente not in martes2 and martes2 == 'libre':
                                    martes2 = nombre_paciente
                                    print(f'Se le ha agendado un turno a {nombre_paciente} para el dia Martes')
                                elif nombre_paciente not in martes3 and martes3 == 'libre':
                                    martes3 = nombre_paciente
                                    print(f'Se le ha agendado un turno a {nombre_paciente} para el dia Martes')
                                else:
                                    print('ERROR. Intentelo nuevamente.')
                            else:
                                print('Asegurese que el nombre sean solo letras.')
                                nombre_paciente = input('Ingrese el nombre del paciente: ')
                        else:
                            print('Ingrese un numero valido')
                        break

                    elif opcion == 2:
                        print('================================')
                        print('Seleccione el dia en el que desea cancelar su turno')
                        print('1. Lunes')
                        print('2. Martes')
                        print('================================')
                        respuesta1 = input('Seleccione el dia (1/2): ')
                        opcion2 = int(respuesta1)
                        if opcion2 == 1:
                            print('Cancelar un turno')
                            nombre_paciente = input('Ingrese el nombre del paciente: ')
                            if nombre_paciente.isalpha():
                                if nombre_paciente not in (lunes1, lunes2, lunes3, lunes4):
                                    print('Esta persona no cuenta con un turno para ese dia.')
                                elif nombre_paciente in lunes1:
                                    lunes1 = 'libre'
                                    print(f'Se ha a cancelado un turno a {nombre_paciente} para el dia Lunes')
                                elif nombre_paciente in lunes2:
                                    lunes2 = 'libre'
                                    print(f'Se ha a cancelado un turno a {nombre_paciente} para el dia Lunes')
                                elif nombre_paciente in lunes3:
                                    lunes3 = 'libre'
                                    print(f'Se ha a cancelado un turno a {nombre_paciente} para el dia Lunes')
                                elif nombre_paciente in lunes4:
                                    lunes4 = 'libre'
                                    print(f'Se ha a cancelado un turno a {nombre_paciente} para el dia Lunes')
                                else:
                                    print('ERROR. Intentelo nuevamente.')
                            else:
                                print('Asegurese que el nombre sean solo letras.')
                                nombre_paciente = input('Ingrese el nombre del paciente: ')
                        elif opcion2 == 2:
                            print('Cancelar un turno')
                            nombre_paciente = input('Ingrese el nombre del paciente: ')
                            if nombre_paciente.isalpha():
                                if nombre_paciente not in (martes1, martes2, martes3):
                                    print('Esta persona no cuenta con un turno para ese dia.')
                                elif nombre_paciente in martes1:
                                    martes1 = 'libre'
                                    print(f'Se ha a cancelado un turno a {nombre_paciente} para el dia Martes')
                                elif nombre_paciente in martes2:
                                    martes2 = 'libre'
                                    print(f'Se ha a cancelado un turno a {nombre_paciente} para el dia Martes')
                                elif nombre_paciente in martes3:
                                    martes3 = 'libre'
                                    print(f'Se ha a cancelado un turno a {nombre_paciente} para el dia Martes')
                                else:
                                    print('ERROR. Intentelo nuevamente.')
                            else:
                                print('Asegurese que el nombre sean solo letras.')
                                nombre_paciente = input('Ingrese el nombre del paciente: ')
                        else:
                            print('Ingrese un numero valido')
                        break
                        

                    elif opcion == 3:
                        print('================================')
                        print('Agenda del dia')
                        print('1. Lunes')
                        print('2. Martes')
                        print('================================')
                        respuesta1 = input('Seleccione el dia (1/2): ')
                        opcion1 = int(respuesta1)
                        if opcion1 == 1:
                                print(f'Turnos del dia: 1. {lunes1}, 2. {lunes2}, 3. {lunes3}, 4. {lunes4}')
                        elif opcion1 == 2:
                                print(f'Turnos del dia: 1. {martes1}, 2. {martes2}, 3. {martes3}')
                        break

                    elif opcion == 4:
                        if lunes1 != 'libre':
                            cantidad_turnos_lunes = cantidad_turnos_lunes + 1
                        if lunes2 != 'libre':
                            cantidad_turnos_lunes = cantidad_turnos_lunes + 1
                        if lunes3 != 'libre':
                            cantidad_turnos_lunes = cantidad_turnos_lunes + 1
                        if lunes4 != 'libre':
                            cantidad_turnos_lunes = cantidad_turnos_lunes + 1
                        
                        if martes1 != 'libre':
                            cantidad_turnos_martes = cantidad_turnos_martes + 1
                        if martes2 != 'libre':
                            cantidad_turnos_martes = cantidad_turnos_martes + 1
                        if martes3 != 'libre':
                            cantidad_turnos_martes = cantidad_turnos_martes + 1
                        print('=====================================')
                        print('Resumen general')
                        print(f'Turnos del dia Lunes: 1. {lunes1}, 2. {lunes2}, 3. {lunes3}, 4. {lunes4}')
                        print(f'Turnos del dia Martes: 1. {martes1}, 2. {martes2}, 3. {martes3}')
                        if cantidad_turnos_lunes > cantidad_turnos_martes:
                            print('El lunes hay mas turnos')
                        elif cantidad_turnos_martes > cantidad_turnos_lunes:
                            print('El Martes hay mas turnos')
                        elif cantidad_turnos_lunes == cantidad_turnos_martes:
                            print('La cantidad de turnos entre el Lunes y el Martes son iguales')
                            print('Empate')
                        else:
                            print('ERROR')
                        print('=====================================')
                        
                        break

                    elif opcion == 5:
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