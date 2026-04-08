import time

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0
nombre = ''
start = False

nombre = input('Agente, inserte su nombre: ')
while not nombre.isalpha():
        print('AGENTE, asegurese que su nombre este bien escrito. Sin numeros, simbolos o espacios. Solo letras.')
        nombre = input('Agente, inserte su nombre: ')

        print('==========================================')
        print(f'Energia: {energia}')
        print(f'Tiempo: {tiempo}')
        print(f'Cerraduras Abiertas: {cerraduras_abiertas}')    
        print('Alarma: Apagada')
        
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
        if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
            print('==========================================')
            print('Se Activo la Alarma y se bloqueo el sistema.')
            break
        else:
            time.sleep(2)
            print('==========================================================================================')
            print('1. Forzar cerradura (costo: -20 energía, -2 tiempo)')
            print('2. Hackear panel (costo: -10 energía, -3 tiempo)')
            print('3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)')
            print('==========================================================================================')
            opcion = input('Seleccione una opcion 1/2/3: ')
            if opcion.isdigit():
                opcion = int(opcion)
                if opcion in (1,2,3):
                    
                    if opcion != 1:
                        forzar_seguidas = 0
                    
                    if opcion == 1:
                        forzar_seguidas = forzar_seguidas + 1
                        if forzar_seguidas == 3:
                            alarma = True
                            print('==========================================')
                            print('la cerradura se trabó')
                            print('Se activo la alarma')
                            
                        energia = energia - 20
                        tiempo = tiempo - 2
                        if energia < 40:
                            print('riesgo de alarma')
                            riesgo_alarma = input(f'inserte un numero del 1 al 3 para intentar evitarlo: ')
                            if not riesgo_alarma.isdigit() or int(riesgo_alarma) not in (1, 2, 3):
                                print('Ingrese un numero valido')
                            elif int(riesgo_alarma) == 3:
                                alarma = True
                        if not alarma and cerraduras_abiertas < 3:
                            print('==========================================')
                            print('Estas Forzando la cerradura')
                            time.sleep(1)
                            cerraduras_abiertas = cerraduras_abiertas + 1
                            print('==========================================')
                            print(f'Forzaste una cerradura - [{cerraduras_abiertas}/3]')
                        
                        print('==========================================')
                        print(f'Energia: {energia}')
                        print(f'Tiempo: {tiempo}')
                        print(f'Cerraduras Abiertas: {cerraduras_abiertas}')
                        if alarma:
                            print(f'Alarma: Activa ')
                        else:
                            print('Alarma: Apagada')
                    elif opcion == 2:
                        energia = energia - 10
                        tiempo = tiempo - 3
                        for i in range(4):
                            print(f'Intentando Hackear... {i+1}/4')
                            codigo_parcial = codigo_parcial + 'X'
                        
                        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                            cerraduras_abiertas = cerraduras_abiertas + 1
                            print('==========================================')
                            print(f'Hackeaste la cerradura - [{cerraduras_abiertas}/3]')
                        
                        print('==========================================')
                        print(f'Energia: {energia}')
                        print(f'Tiempo: {tiempo}')
                        print(f'Cerraduras Abiertas: {cerraduras_abiertas}')
                        if alarma:
                            print(f'Alarma: Activa ')
                        else:
                            print('Alarma: Apagada')
                    elif opcion == 3:
                        if alarma:
                            tiempo = tiempo - 1
                            energia = energia + 15 #energia normal
                            energia = energia - 10 # menos energia pq esta la alarma. no estoy seguro si llevaba ambas. o unicamente la negativa
                            if energia > 100:
                                energia = 100
                            print('==========================================')
                            print('Intentaste descansar mientras la alarma esta activa...')
                        else:
                            print('==========================================')
                            print('Estas Descansando')
                            energia = energia + 15
                            if energia > 100:
                                energia = 100
                            tiempo = tiempo - 1
                        time.sleep(1)
                        print('==========================================')
                        print(f'Energia: {energia}')
                        print(f'Tiempo: {tiempo}')
                        print(f'Cerraduras Abiertas: {cerraduras_abiertas}')
                        if alarma:
                            print(f'Alarma: Activa ')
                        else:
                            print('Alarma: Apagada')
                else:
                    print('Ingrese un numero valido.')
            else:
                print('ERROR opcion fuera de rango')
            
            
if energia <= 0:
    print('==========================================')
    print(f'Te quedaste sin energia [{energia}].')
elif tiempo <= 0:
    print('==========================================')
    print(f'Te quedaste sin tiempo [{tiempo}].')
elif cerraduras_abiertas == 3:
    print('==============================================')
    print(f'Ganaste? Desbloqueaste la Boveda, felicidades.')
    print('==============================================')

