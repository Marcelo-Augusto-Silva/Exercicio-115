def armazenar(n,i):
    arquivo = open('Casdatro.txt','a')
    arquivo.write(n)
    arquivo.write(espaco(n,i))
    arquivo.write(i)
    arquivo.write(' anos')
    arquivo.write('\n')


def espaco(n,m):
    s = len(n) + len(m)
    es = 35 - s
    e = ' ' * es
    return e

def leiaopc():
    n = 0
    try:
        n = int(input('\033[1;35m Numero: \033[m'))
        if 0 < n < 4:
            return n
    except:
        print('\033[1;31m Valor invalido \033[m')
        while True:
            try:
                n = int(input('\033[1;35m Numero:\033[m'))
                if 0 < n < 4:
                    return n
            except:
                print('\033[1;31m Valor invalido \033[m')



def cadastrar():
    while True:
        try:
            nome = str(input('\033[1;35m Nome: \033[m'))
            idade = int(input('\033[1;35m Idade: \033[m'))
            print('\033[1;35m CADASTRADO...\033[m')
            break
        except:
            print('\033[1;31m Invalido \033[m')
    idade = str(idade)
    armazenar(nome,idade)
