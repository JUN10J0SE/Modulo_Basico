#modulo sao novos arquivos que vc cria a  parte  e pode chama-los no arquivo principal com o import

#biblioteca criada para chamar suas funcoes
#import cinematica as cn /# pode dar um 'apelido' aqui no caso demos o nome 'cn' a biblioteca utilizando o 'as' seguido do nome que se quer. porem chama todo arquivo
                         #para chamar usa o apelido + . seguido do nome da funcao Ex cn.mostrar_menu ou cn.clacular_ep

# import cinematica import mostrar_menu, calcular_ep / pode escolher a funcao que se quer separando por virgula

#desta forma chama tudo da biblioteca
from cinematica import * #/ tras todas as funcoes

#chamar o menu do arquivo 'cinematica' usa-se o nome ou apelido da biblioteca com . + nome da funcao
while True:
    mostrar_menu()

    opcao = input('Opcao do Usuario: ')

    match opcao:
        case '1':
            m = float(input('Informe a massa em kg: ').replace(',','.'))
            h = float(input('Informe a altura em metros: ').replace(',','.'))
            print(f'Energia potencial: {calcular_ep(m,h):,.2f} j.')
            continue
        case '2':
            m = float(input('Informar a massa em Kg: ').replace(',','.'))
            v = float(input('Informe a velocidade em m/s: ').replace(',','.'))
            print(f'Energia cinematica: {calcular_ec(m,v):,.2f} j.')
            continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opcao Ivalida')
            continue


