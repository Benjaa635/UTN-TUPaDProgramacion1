vida_gladiador = 100
vida_enemigo = 100
c_pociones = 3
dano_base_gladiador = 15
dano_base_enemigo = 12
mi_turno = True
juego_activo = False
dano_final = 0

player = input('Inserte su nombre: ')
while not player.isalpha():
    print('Error: Solo se permiten letras.')
    player = input('Inserte su nombre: ')

while vida_gladiador > 0 and vida_enemigo > 0:
    
    if mi_turno:
        print('============================================================')
        print(f'Enemigo - {vida_enemigo}hp')
        print(f'{player} - {vida_gladiador}hp')
        print('Pociones:', c_pociones)
        print('============================================================')
        print('Es tu turno')
        print('============================================================')
        print('1. Ataque Pesado')
        print('2. Rafaga Veloz')
        print('3. Curar')
        while True:
            opcion = input('Elige un movimiento. 1/2/3: ')
            if not opcion.isdigit():
                print('Error: Solo se permiten numeros')
                continue
            
            opcion = int(opcion)
            
            if opcion in (1,2,3):
                break
            else:
                print('Error: Numero no valido')
        
        if opcion == 1:
            print('============================================================')
            print('Elegiste, Ataque pesado')
            if vida_enemigo < 20:
                dano_final = round(dano_base_gladiador * 1.5) # Redondeo dano critico (float)
            else:
                dano_final = dano_base_gladiador
            
            vida_enemigo = vida_enemigo - dano_final
            print('============================================================')
            print(F'¡Atacaste al enemigo por {dano_final} puntos de daño!')
            mi_turno = False
            
        elif opcion == 2:
            print('============================================================')
            print('Usando Ráfaga Veloz')
            print('============================================================')
            for i in range(3):
                dano_final = 5
                vida_enemigo = vida_enemigo - dano_final
                print('> Golpe conectado por 5 de daño')
            
            mi_turno = False
        elif opcion == 3:
            print('============================================================')
            print('Utilizando Pocion')
            if c_pociones > 0:
                vida_gladiador = vida_gladiador + 30
                c_pociones = c_pociones - 1
                print('Has recuperado 30 puntos de salud')
            else:
                print('============================================================')
                print('¡No quedan pociones!')
            
            mi_turno = False
    
    else:
        print('============================================================')
        print('Turno del Enemigo')
        vida_gladiador = vida_gladiador - dano_base_enemigo
        print('============================================================')
        print('¡El enemigo te atacó por 12 puntos de daño!')
        mi_turno = True
else:
    print('============================================================')
    print('La partida a finalizado...')
    if vida_enemigo <= 0:
        print('============================================================')
        print(f'¡VICTORIA! {player} ha ganado la batalla.')
        print('============================================================')
    elif vida_gladiador <= 0:
        print('============================================================')
        print('DERROTA. Has caído en combate.')
        print('============================================================')