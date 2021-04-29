import uteis
import time
while True:
    l = '=' * 40
    print(l)
    print(f'             MENU PRINCIPAL')
    print(l)
    print('\033[1;33m 1 \033[m- \033[1;34m VER PESSOAS CADASTRADAS \033[m')
    print('\033[1;33m 2 \033[m- \033[1;34m CADASTRAR NOVA PESSOA \033[m')
    print('\033[1;33m 3 \033[m- \033[1;34m SAIR DO SISTEMA \033[m')
    print(l)
    opc = uteis.leiaopc()
    if opc == 1:
        print('NOME DOS CADASTRADOS',end='')
        print(' '*14,'IDADE')
        arquivo = open('Casdatro.txt', 'r')
        for c in arquivo:
            time.sleep(0.7)
            print(c,end='')
    if opc == 2:
        uteis.cadastrar()
    if opc == 3:
        print('\033[1;33mFINALIZANDO...\033[m')
        break

