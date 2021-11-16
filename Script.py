print('Para adicionar à fila preferencial digite: P')
print('Para atender alguém da fila preferencial digite: L')
print('Para adicionar à fila normal digite: F')
print('Para atender alguém da fila normal digite: A')
print('para sair digite: S')
print('Para rever os comandos digite C')
fila_p=list()
fila_n=list()
últimoP=0
últimoN=0
s=False
while True:
    x=0
    print('Total fila P: ',len(fila_p))
    print('Total fila N: ',len(fila_n))
    comando=input('Insira um comando: ')
    while x<len(comando):
        if comando[x] == 'P':
            últimoP+=1
            fila_p.append(últimoP)
        elif comando[x] == 'L':
            atendido=fila_p.pop(0)
            print('Cliente P %d atendido' %atendido)
        elif comando[x] == 'F':
            últimoN+=1
            fila_n.append(últimoN)
        elif comando[x] == 'A':
            atendido=fila_n.pop(0)
            print('Cliente N %d atendido' %atendido)
        elif comando[x] == 'C':
            print('Para adicionar à fila preferencial digite: P')
            print('Para atender alguém da fila preferencial digite: L')
            print('Para adicionar à fila normal digite: F')
            print('Para atender alguém da fila normal digite: A')
            print('para sair digite: S')
            print('Para rever os comandos digite C')
        elif comando[x] == 'S':
            s=True
        x=x+1
    if s == True:
        print('Programa encerrado!')
        break
