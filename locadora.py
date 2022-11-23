print('-'*20)
print('Bem vindo à locadora de carros! ')
print('-'*20)

def alugar(codigo):
    portifolio_devolver[codigo] = [portifolio_alugar[codigo][0], portifolio_alugar[codigo][1]]
    portifolio_alugar.pop(codigo)

def devolver(codigo_devolver):
    portifolio_alugar[codigo_devolver] = [portifolio_devolver[codigo_devolver][0], portifolio_devolver[codigo_devolver][1]]
    portifolio_devolver.pop(codigo_devolver)

portifolio_devolver = {}
portifolio_alugar = {0: ['Chevrolet Traker', 120],
                     1: ['Chevrolet Onix', 90],
                     2: ['Chevrolet Spin', 150]}
continuar = 0
while continuar == 0:
    menu = int(input('O que deseja fazer ? \n'
                     '0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro\n'))
    if menu == 0:
        for i, v in portifolio_alugar.items():
            print(f'[{i}] {v[0]} - R$ {v[1]} /dia')

    if menu == 1:
        for i, v in portifolio_alugar.items():
            print(f'[{i}] {v[0]} - R$ {v[1]} /dia')

        print()
        carro_alugado = int(input('Escolha o código do carro: '))
        if carro_alugado not in portifolio_alugar.keys():
            print('Código não consta na lista.')
            continue
        dias_alugado = int(input('Por quantos dias deseja alugar: '))

        print()
        total_aluguel = (portifolio_alugar[carro_alugado][1])*dias_alugado
        deseja_alugar = int(input(f'Você escolheu o {portifolio_alugar[carro_alugado][0]}'
                                  f' por {dias_alugado} dias\nO aluguel totalizaria R$ {total_aluguel}.'
                                  f' Deseja aluguar ?\n'
                                  f'0 - SIM | 1 - NÃO\n'))
        print()
        if deseja_alugar == 0:
            print(f'Parabéns você alugou o {portifolio_alugar[carro_alugado][0]} por {dias_alugado} dias.')
            alugar(carro_alugado)
        if deseja_alugar == 1:
            continue

    if menu == 2:
        if len(portifolio_devolver) == 0:
            print('Nenhum carro para devolver, escolha outra opção.')
            continue
        print('Segue a lista de carros alugados. Qual você deseja devolver ?')
        for i, v in portifolio_devolver.items():
            print(f'[{i}] {v[0]} - R$ {v[1]} /dia')
        print()
        carro_devolver = int(input('Escolha o código do carro que deseja devolver:\n'))
        if carro_devolver not in portifolio_devolver.keys():
            print('Código não consta na lista.')
            continue
        print(f'Obrigado por devolver o carro {portifolio_devolver[carro_devolver][0]}.')
        devolver(carro_devolver)

    print()
    continuar = int(input('0 - CONTINUAR | 1 - SAIR\n'))
