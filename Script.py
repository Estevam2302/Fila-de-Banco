print('Adicionar à fila preferencial: P')
print('Atender alguém da fila preferencial: L')
print('Adicionar à fila normal: F')
print('Atender alguém da fila normal: A')
print('Para sair: S')
print('Para rever os comandos: comandos')
últimoP=0
últimoN=0
fila_preferencial=list()
fila_normal=list()
while True:
    if len(fila_preferencial + fila_normal) == 0:
        print('Filas vazias, ninguem para atender!')
    elif len(fila_preferencial + fila_normal) > 0:
        print('Fila prefrencial: ', len(fila_preferencial))
        print('Fila normal: ', len(fila_normal))
    comando = input('Insira um comando: ')
    if comando == 'P':
        últimoP+=1
        fila_preferencial.append(últimoP)
    elif comando == 'L':
        atendido = fila_preferencial.pop(0)
        print('Cliente P %d atendido' %atendido)
    elif comando == 'F':
        últimoN+=1
        fila_normal.append(últimoN)
    elif comando == 'A':
        atendido = fila_normal.pop(0)
        print('Cliente N %d atendido' %atendido)  
    elif comando == 'comandos':
        print('Adicionar à fila preferencial: P')
        print('Atender alguém da fila preferencial: L')
        print('Adicionar à fila normal: F')
        print('Atender alguém da fila normal: A')
        print('Para sair: S')
        print('Para rever os comandos: comandos')
    if comando == 'S':
        print('Programa encerrado!')
        break
    else:
        print('Comando inválido!')
