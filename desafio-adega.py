# Luigi Paschoalino

class Vinho:
    def __init__(self, nome, tipo, qtd):
        self.nome = nome
        self.tipo = tipo
        self.qtd = qtd
    
    def setQtd(self, qtd):
        self.qtd = qtd

def contaVinhos(adega, slotAdega):
    cont = 0
    for i in range(0, len(adega[slotAdega])):
        cont += adega[slotAdega][i].qtd
    return cont

adega = [[], [], [], []] # adega[0] = vinhos tintos, adega[1] = vinhos brancos, adega[2] = vinhos rosados, adega[3] = outros tipos de vinhos

# cria quantidades declaradas de cada tipo de vinho
qtd = 0
nome = ''

while nome != 'Sair':
    flag = 0 # flag para verificar se o vinho já existe na adega
    nome = str.capitalize(input('Digite o nome do vinho ou digite "Sair" para parar de cadastrar vinhos: '))
    if nome == 'Sair':
        continue
    tipo = str.upper(input('Digite o tipo de vinho: Tinto (T), Branco (B), Rosé (R) ou outro (O): '))
    if tipo != 'T' and tipo != 'B' and tipo != 'R' and tipo != 'O':
        print('Tipo de vinho inválido!\n')
        continue
    qtd = int(input('Digite a quantidade em estoque desse vinho: '))
    if qtd <= 0:
        print('Quantidade inválida!\n')
        continue
    if tipo == 'T':
        for i in range(0, len(adega[0])):
            if adega[0][i].nome == nome:
                flag = 1
                opcao = int(input('Vinho já cadastrado! Deseja alterar a quantidade atual ({}) para o valor informado?\n1 - Sim\n2 - Não\nOutro valor - Cadastrar de qualquer forma\n'.format(adega[0][i].qtd)))
                if opcao == 1:
                    adega[0][i].setQtd(qtd)
                    print('Quantidade alterada com sucesso!\n')
                    break
                elif opcao == 2:
                    print('Quantidade não alterada!\n')
                    break
                else:
                    adega[0].append(Vinho(str(nome + ' (recadastrado)'), 'Tinto', qtd))
                    print('Vinho recadastrado com sucesso!')
                    break
        if flag == 0:
            adega[0].append(Vinho(nome, 'Tinto', qtd))
            print('Vinho cadastrado com sucesso!')
    elif tipo == 'B':
        for i in range(0, len(adega[1])):
            if adega[1][i].nome == nome:
                flag = 1
                opcao = int(input('Vinho já cadastrado! Deseja alterar a quantidade atual ({}) para o valor informado?\n1 - Sim\n2 - Não\nOutro valor - Cadastrar de qualquer forma\n'.format(adega[1][i].qtd)))
                if opcao == 1:
                    adega[1][i].setQtd(qtd)
                    print('Quantidade alterada com sucesso!')
                    break
                elif opcao == 2:
                    print('Quantidade não alterada!')
                    break
                else:
                    adega[1].append(Vinho(str(nome + ' (recadastrado)'), 'Branco', qtd))
                    print('Vinho recadastrado com sucesso!')
                    break
        if flag == 0:
            adega[1].append(Vinho(nome, 'Branco', qtd))
            print('Vinho cadastrado com sucesso!')
    elif tipo == 'R':
        for i in range(0, len(adega[2])):
            if adega[2][i].nome == nome:
                flag = 1
                opcao = int(input('Vinho já cadastrado! Deseja alterar a quantidade atual ({}) para o valor informado?\n1 - Sim\n2 - Não\nOutro valor - Cadastrar de qualquer forma\n'.format(adega[2][i].qtd)))
                if opcao == 1:
                    adega[2][i].setQtd(qtd)
                    print('Quantidade alterada com sucesso!')
                    break
                elif opcao == 2:
                    print('Quantidade não alterada!')
                    break
                else:
                    adega[2].append(Vinho(str(nome + ' (recadastrado)'), 'Rosé', qtd))
                    print('Vinho recadastrado com sucesso!')
                    break
        if flag == 0:
            adega[2].append(Vinho(nome, 'Rosé', qtd))
            print('Vinho cadastrado com sucesso!')
    elif tipo == 'O':
        for i in range(0, len(adega[3])):
            if adega[3][i].nome == nome:
                flag = 1
                opcao = int(input('Vinho já cadastrado! Deseja alterar a quantidade atual ({}) para o valor informado?\n1 - Sim\n2 - Não\nOutro valor - Cadastrar de qualquer forma\n'.format(adega[3][i].qtd)))
                if opcao == 1:
                    adega[3][i].setQtd(qtd)
                    print('Quantidade alterada com sucesso!')
                    break
                elif opcao == 2:
                    print('Quantidade não alterada!')
                    break
                else:
                    adega[3].append(Vinho(str(nome + ' (recadastrado)'), 'Outro', qtd))
                    print('Vinho recadastrado com sucesso!')
                    break
        if flag == 0:
            adega[3].append(Vinho(nome, 'Outro', qtd))
            print('Vinho cadastrado com sucesso!')
    else:
        print('Erro no cadastro, tente novamente')
    print()

print('\n----------------------------------------------------')

opcao = ''
while opcao != 'F':
    opcao = str.upper(input('\nQual tipo de vinho deseja consultar: Tinto (T), Branco (B), Rosé (R) ou outros (O)?\nDigite F para finalizar a busca: '))
    if opcao == 'T':
        print('Porcentagem de vinhos tintos: {0:.2f}%'.format((contaVinhos(adega, 0) * 100) / (contaVinhos(adega, 0) + contaVinhos(adega, 1) + contaVinhos(adega, 2) + contaVinhos(adega, 3))))
    elif opcao == 'B':
        print('Porcentagem de vinhos brancos: {0:.2f}%'.format((contaVinhos(adega, 1) * 100) / (contaVinhos(adega, 0) + contaVinhos(adega, 1) + contaVinhos(adega, 2) + contaVinhos(adega, 3))))
    elif opcao == 'R':
        print('Porcentagem de vinhos rosados: {0:.2f}%'.format((contaVinhos(adega, 2) * 100) / (contaVinhos(adega, 0) + contaVinhos(adega, 1) + contaVinhos(adega, 2) + contaVinhos(adega, 3))))
    elif opcao == 'O':
        print('Porcentagem de outros tipos de vinho: {0:.2f}%'.format((contaVinhos(adega, 3) * 100) / (contaVinhos(adega, 0) + contaVinhos(adega, 1) + contaVinhos(adega, 2) + contaVinhos(adega, 3))))
    elif opcao == 'F':
        continue
    else:
        print('Opção inválida!')

print('\n----------------------------------------------------')

opcao = 1
while opcao == 1:
    opcao = int(input('\nDeseja consultar alguma lista específica de vinhos?\n1 - Sim\nOutro valor - Não\nDigite a opção: '))
    if opcao != 1:
        continue
    tipo = str.upper(input('Qual tipo de vinho deseja consultar: Tinto (T), Branco (B), Rosé (R) ou outros (O)? '))
    if tipo == 'T':
        print('\nVinhos tintos:')
        for vinho in adega[0]:
            print(vinho.nome + ' (x' + str(vinho.qtd) + ')')
    elif tipo == 'B':
        print('\nVinhos brancos:')
        for vinho in adega[1]:
            print(vinho.nome + ' (x' + str(vinho.qtd) + ')')
    elif tipo == 'R':
        print('\nVinhos rosados:')
        for vinho in adega[2]:
            print(vinho.nome + ' (x' + str(vinho.qtd) + ')')
    elif tipo == 'O':
        print('\nOutros tipos de vinho:')
        for vinho in adega[3]:
            print(vinho.nome + ' (x' + str(vinho.qtd) + ')')
    else:
        print('\nOpção inválida!')

print('\n----------------------------------------------------')

print('\nVinhos tintos: {}\nVinhos brancos: {}\nVinhos rosés: {}\nOutros vinhos: {}\n\nTotal de vinhos: {}'.format(contaVinhos(adega, 0), contaVinhos(adega, 1), contaVinhos(adega, 2), contaVinhos(adega, 3), (contaVinhos(adega, 0) + contaVinhos(adega, 1) + contaVinhos(adega, 2) + contaVinhos(adega, 3))))