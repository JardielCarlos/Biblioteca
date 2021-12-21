from random import randint
print('-=' * 20)
print(f'{"Biblioteca":^38}')
print('-=' * 20)
indisponivel = []
ind2 = []
disponivel = []
disponivel2 = []
suspenso = []
ativo = []
cargo = []
pessoaativa = []
datageral = []
emprestado = []
quant = []
codigoitem = []
codigoindisponivel = []
while True:
    print('O que você deseja?')
    print('[ 1 ]Cadastrar leitores\n[ 2 ]Cadastrar itens\n[ 3 ]Buscar item\n[ 4 ]Realizar empréstimo de item\n[ 5 ]Devolver item\n[ 6 ]Listar itens disponíveis\n[ 7 ]Sair da biblioteca')
    escolha = input('\nQual a sua opção: ')
    if escolha == '1':
        print('-=' * 15)
        print(f'{"Cadastro de leitor":^28}')
        print('-=' * 15)
        matricula = input('Digite sua matrícula: ').strip()
        ativo.append(matricula)
        nome = input('Digite seu nome: ').strip().capitalize()
        pessoaativa.append(nome)
        tipo = input('Professor, aluno ou funcionario: ').strip().lower()
        if tipo == 'aluno':
            cargo.append(tipo)
            print('Cadasto concluido com sucesso!')
        elif tipo == 'professor':
            cargo.append(tipo)
            print('Cadasto concluido com sucesso!')
        elif tipo == 'funcionario':
            cargo.append(tipo)
            print('Cadasto concluido com sucesso!')
        else:
            print('Tipo não identificado, cadastre-se novamente!')
            ativo.remove(matricula)
            pessoaativa.remove(nome)
        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
        if escolha == 'n':
            print('-=' * 20)
            print(f'{"Volte sempre!":^38}')
            print('-=' * 20)
            break
        if escolha != 's':
            print('valor digitado incorreto!')
            print('-=' * 20)
            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
            print('-=' * 20)
    elif escolha == '2':
        print('-=' * 15)
        print(f'{"Cadastro de itens":^28}')
        print('-=' * 15)
        titulo = input('Digite o Título: ').strip().lower()
        disponivel.append(titulo)
        quantidade = int(input('Digite a quantidade:'))
        if quantidade == 0:
            indisponivel.append(titulo)
        if quantidade > 0:
            disponivel2.append(titulo)
        quant.append(quantidade)
        print('Cadasto concluido com sucesso!')
        aleatorio = randint(0, 100000)
        aleatorio2 = str(aleatorio)
        codigoitem.append(aleatorio2)
        print(f'Esse é o codigo de registro {aleatorio}')
        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
        if escolha == 'n':
            print('-=' * 20)
            print(f'{"Volte sempre!":^38}')
            print('-=' * 20)
            break
        if escolha != 's':
            print('valor digitado incorreto!')
            print('-=' * 20)
            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
            print('-=' * 20)
    elif escolha == '3':
        print('-=' * 15)
        print(f'{"Buscar itens":^28}')
        print('-=' * 15)
        codigo_titulo = input('Digite o código/titulo do item a ser buscado:').strip().lower()
        if codigo_titulo in codigoitem:
            posicaobusca = codigoitem.index(codigo_titulo)
            print('O titulo é {}'.format(disponivel[posicaobusca]))
            print('O codigo é {}'.format(codigoitem[posicaobusca]))
            print('Quantidade: {}'.format(quant[posicaobusca]))
            if disponivel[posicaobusca] in disponivel2:
                print('Status:Disponível')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
            elif disponivel[posicaobusca] in indisponivel:
                print('Status:Indisponível')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
        elif codigo_titulo in disponivel:
            posicaobusca = disponivel.index(codigo_titulo)
            print('O titulo é {}'.format(disponivel[posicaobusca]))
            print('O codigo é {}'.format(codigoitem[posicaobusca]))
            print('Quantidade: {}'.format(quant[posicaobusca]))
            if disponivel[posicaobusca] in disponivel2:
                print('Status:Disponível')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
            elif disponivel[posicaobusca] in indisponivel:
                print('Status:Indisponível')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
        else:
            print('Este codigo/titulo não foi encontrado.')
            escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
            if escolha == 'n':
                print('-=' * 20)
                print(f'{"Volte sempre!":^38}')
                print('-=' * 20)
                break
            if escolha != 's':
                print('valor digitado incorreto!')
                print('-=' * 20)
                print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                print('-=' * 20)
    elif escolha == '4':
        print('Preparando emprestimo de itens...')
        itemx = input('Digite o código/título desejado:').strip().lower()
        if itemx in indisponivel:
            print('-' * 20)
            print('Este item não está disponível no momento!')
            print('-' * 20)
            escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
            if escolha == 'n':
                print('-=' * 20)
                print(f'{"Volte sempre!":^38}')
                print('-=' * 20)
                break
            if escolha != 's':
                print('valor digitado incorreto!')
                print('-=' * 20)
                print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                print('-=' * 20)
        elif itemx in disponivel2:
            print('Este item esta disponivél, podemos proseguir.')
            matriculax = str(input('Digite sua matrícula:')).strip()
            if matriculax in suspenso:
                print('Sua matrícula esta suspensa!')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
            elif matriculax in ativo:
                data1 = int(input('Digite o dia que deseja pegar o item:'))
                data2 = data1 + 7
                posicao2 = disponivel.index(itemx)
                if data2 < 30:
                    print('A data de devolução sera {} desse mesmo mês.'.format(data2))
                    datageral.append(data2)
                    valor = quant[posicao2] - 1
                    quant.remove(valor + 1)
                    quant.insert(posicao2, valor)
                    emprestado.append(matriculax)
                    codigoindisponivel.append(codigoitem[posicao2])
                    if quant[posicao2] == 0:
                        indisponivel.append(disponivel[posicao2])
                        disponivel2.remove(disponivel[posicao2])
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
                    else:
                        ind2.append(disponivel[posicao2])
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
                elif data2 > 30:
                    nova_data = data2 - 30
                    nova_data1 = 0
                    data_devolucao = nova_data1 + nova_data
                    datageral.append(data_devolucao)
                    emprestado.append(matriculax)
                    print('A data de devolução sera {} do próximo mês.'.format(data_devolucao))
                    if quant[posicao2] == 0:
                        indisponivel.append(disponivel[posicao2])
                        disponivel2.remove(disponivel[posicao2])
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
                    elif quant[posicao2] != 0:
                        ind2.append(disponivel[posicao2])
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
            else:
                print('Matricula não encontrada')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
        elif itemx in codigoitem:
            print('Este item esta disponivél, podemos proseguir.')
            matriculax = str(input('Digite sua matrícula:')).strip()
            if matriculax in suspenso:
                print('Sua matrícula esta suspensa!')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
            elif matriculax in ativo:
                data1 = int(input('Digite o dia que deseja pegar o item:'))
                data2 = data1 + 7
                posicao2 = codigoitem.index(itemx)
                ind2.append(disponivel[posicao2])
                if data2 < 30:
                    print('A data de devolução sera {} desse mesmo mês.'.format(data2))
                    codigoindisponivel.append(itemx)
                    datageral.append(data2)
                    emprestado.append(matriculax)
                    valor = quant[posicao2] - 1
                    quant.remove(valor + 1)
                    quant.insert(posicao2, valor)
                    if quant[posicao2] == 0:
                        titulo2 = disponivel[posicao2]
                        indisponivel.append(titulo2)
                        disponivel2.remove(disponivel[posicao2])
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
                    else:
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
                elif data2 > 30:
                    nova_data = data2 - 30
                    nova_data1 = 0
                    data_devolucao = nova_data1 + nova_data
                    print('A data de devolução sera {} do próximo mês.'.format(data_devolucao))
                    datageral.append(nova_data)
                    codigoindisponivel.append(itemx)
                    emprestado.append(matriculax)
                    valor = quant[posicao2] - 1
                    quant.remove(valor + 1)
                    quant.insert(posicao2, valor)
                    if quant[posicao2] == 0:
                        titulo2 = disponivel[posicao2]
                        indisponivel.append(titulo2)
                        disponivel2.remove(disponivel[posicao2])
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
                    else:
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
            else:
                print('Sua matricula não foi encontrada.')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
        else:
            print('Item não encontrado.')
            escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
            if escolha == 'n':
                print('-=' * 20)
                print(f'{"Volte sempre!":^38}')
                print('-=' * 20)
                break
            if escolha != 's':
                print('valor digitado incorreto!')
                print('-=' * 20)
                print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                print('-=' * 20)
    elif escolha == '5':
        codigo_item = input('Digite o codigo/titulo do item que deseja devolver:').strip().lower()
        matriculay = input('Digite sua matricula:').strip()
        if codigo_item in codigoindisponivel:
            positem = codigoindisponivel.index(codigo_item)
            if matriculay in emprestado:
                posmatricula = emprestado.index(matriculay)
                if posmatricula == positem:
                    if matriculay in ativo:
                        if codigo_item in indisponivel:
                            posicao = indisponivel.index(codigo_item)
                            datadev = int(input('Digite a data que está devolvendo o item:'))
                            if datadev > datageral[posicao]:
                                valor = quant[posicao] + 1
                                quant.remove(valor - 1)
                                quant.insert(posicao, valor)
                                datanova = datageral[posicao]
                                atraso = datadev - datanova
                                datasuspensao = atraso * 3
                                print('Sua matricula está supensa por {} dias.'.format(datasuspensao))
                                suspenso.append(matriculay)
                                disponivel2.append(indisponivel[posicao])
                                indisponivel.remove(indisponivel[posicao])
                                renovar = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar == 's':
                                    if emprestado[posicao] in suspenso:
                                        print('Você esta suspenso')
                                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                        if escolha == 'n':
                                            print('-=' * 20)
                                            print(f'{"Volte sempre!":^38}')
                                            print('-=' * 20)
                                            break
                                        if escolha != 's':
                                            print('valor digitado incorreto!')
                                            print('-=' * 20)
                                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                            print('-=' * 20)
                                elif renovar == 'n':
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                            elif datadev <= datageral[posicao]:
                                renovar2 = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar2 == 's':
                                    datageral.pop(posicao)
                                    datageral.insert(posicao, datadev + 7)
                                    print('Você tem mais 7 dias para devolver o item.')
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                                elif renovar2 == 'n':
                                    valor = quant[posicao] + 1
                                    quant.remove(valor - 1)
                                    quant.insert(posicao, valor)
                                    disponivel2.append(indisponivel[posicao])
                                    indisponivel.remove(indisponivel[posicao])
                                    datanova = datageral[posicao]
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)

                        elif codigo_item in ind2:
                            posicao = ind2.index(codigo_item)
                            datadev = int(input('Digite a data que está devolvendo o item:'))
                            if datadev > datageral[posicao]:
                                valor = quant[posicao] + 1
                                quant.remove(valor - 1)
                                quant.insert(posicao, valor)
                                datanova = datageral[posicao]
                                atraso = datadev - datanova
                                datasuspensao = atraso * 3
                                print('Sua matricula está supensa por {} dias.'.format(datasuspensao))
                                suspenso.append(matriculay)
                                disponivel2.append(ind2[posicao])
                                renovar = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar == 's':
                                    if emprestado[posicao] in suspenso:
                                        ind2.remove(ind2[posicao])
                                        print('Você esta suspenso')
                                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                        if escolha == 'n':
                                            print('-=' * 20)
                                            print(f'{"Volte sempre!":^38}')
                                            print('-=' * 20)
                                            break
                                        if escolha != 's':
                                            print('valor digitado incorreto!')
                                            print('-=' * 20)
                                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                            print('-=' * 20)
                                elif renovar == 'n':
                                    ind2.remove(ind2[posicao])
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                            elif datadev <= datageral[posicao]:
                                renovar2 = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar2 == 's':
                                    datageral.pop(posicao)
                                    datageral.insert(posicao, datadev + 7)
                                    print('Você tem mais 7 dias para devolver o item.')
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                                elif renovar2 == 'n':
                                    ind2.remove(ind2[posicao])
                                    valor = quant[posicao] + 1
                                    quant.remove(valor - 1)
                                    quant.insert(posicao, valor)
                                    disponivel2.append(indisponivel[posicao])
                                    indisponivel.remove(indisponivel[posicao])
                                    datanova = datageral[posicao]
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                        elif codigo_item in codigoitem:
                            posicao = codigoindisponivel.index(codigo_item)
                            datadev = int(input('Digite a data que está devolvendo o item:'))
                            if datadev > datageral[posicao]:
                                valor = quant[posicao] + 1
                                quant.remove(valor - 1)
                                quant.insert(posicao, valor)
                                datanova = datageral[posicao]
                                atraso = datadev - datanova
                                datasuspensao = atraso * 3
                                print('Sua matricula está supensa por {} dias.'.format(datasuspensao))
                                suspenso.append(matriculay)
                                disponivel2.append(indisponivel[posicao])
                                indisponivel.remove(indisponivel[posicao])
                                renovar = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar == 's':
                                    if emprestado[posicao] in suspenso:
                                        print('Você esta suspenso')
                                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                        if escolha == 'n':
                                            print('-=' * 20)
                                            print(f'{"Volte sempre!":^38}')
                                            print('-=' * 20)
                                            break
                                        if escolha != 's':
                                            print('valor digitado incorreto!')
                                            print('-=' * 20)
                                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                            print('-=' * 20)
                            elif datadev <= datageral[posicao]:
                                renovar2 = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar2 == 's':
                                    datageral.pop(posicao)
                                    datageral.insert(posicao, datadev + 7)
                                    print('Você tem mais 7 dias para devolver o item.')
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                                else:
                                    disponivel2.append(indisponivel[posicao])
                                    indisponivel.remove(indisponivel[posicao])
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                        else:
                            print('Este item não foi encontrado.')
                            escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                            if escolha == 'n':
                                print('-=' * 20)
                                print(f'{"Volte sempre!":^38}')
                                print('-=' * 20)
                                break
                            if escolha != 's':
                                print('valor digitado incorreto!')
                                print('-=' * 20)
                                print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                print('-=' * 20)
                    else:
                        print('Matricula invalida.')
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
            else:
                print('Essa matricula não corresponde ao item.')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
        elif codigo_item in ind2:
            positem = ind2.index(codigo_item)
            if matriculay in emprestado:
                posmatricula = emprestado.index(matriculay)
                if posmatricula == positem:
                    if matriculay in ativo:
                        if codigo_item in indisponivel:
                            posicao = indisponivel.index(codigo_item)
                            datadev = int(input('Digite a data que está devolvendo o item:'))
                            if datadev > datageral[posicao]:
                                valor = quant[posicao] + 1
                                quant.remove(valor - 1)
                                quant.insert(posicao, valor)
                                datanova = datageral[posicao]
                                atraso = datadev - datanova
                                datasuspensao = atraso * 3
                                print('Sua matricula está supensa por {} dias.'.format(datasuspensao))
                                suspenso.append(matriculay)
                                disponivel2.append(indisponivel[posicao])
                                indisponivel.remove(indisponivel[posicao])
                                renovar = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar == 's':
                                    if emprestado[posicao] in suspenso:
                                        print('Você esta suspenso')
                                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                        if escolha == 'n':
                                            print('-=' * 20)
                                            print(f'{"Volte sempre!":^38}')
                                            print('-=' * 20)
                                            break
                                        if escolha != 's':
                                            print('valor digitado incorreto!')
                                            print('-=' * 20)
                                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                            print('-=' * 20)
                                elif renovar == 'n':
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                            elif datadev <= datageral[posicao]:
                                renovar2 = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar2 == 's':
                                    datageral.pop(posicao)
                                    datageral.insert(posicao, datadev + 7)
                                    print('Você tem mais 7 dias para devolver o item.')
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                                elif renovar2 == 'n':
                                    valor = quant[posicao] + 1
                                    quant.remove(valor - 1)
                                    quant.insert(posicao, valor)
                                    disponivel2.append(indisponivel[posicao])
                                    indisponivel.remove(indisponivel[posicao])
                                    datanova = datageral[posicao]
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                        elif codigo_item in ind2:
                            posicao = ind2.index(codigo_item)
                            datadev = int(input('Digite a data que está devolvendo o item:'))
                            if datadev > datageral[posicao]:
                                valor = quant[posicao] + 1
                                quant.remove(valor - 1)
                                quant.insert(posicao, valor)
                                datanova = datageral[posicao]
                                atraso = datadev - datanova
                                datasuspensao = atraso * 3
                                print('Sua matricula está supensa por {} dias.'.format(datasuspensao))
                                suspenso.append(matriculay)
                                disponivel2.append(ind2[posicao])
                                renovar = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar == 's':
                                    if emprestado[posicao] in suspenso:
                                        ind2.remove(ind2[posicao])
                                        print('Você esta suspenso')
                                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                        if escolha == 'n':
                                            print('-=' * 20)
                                            print(f'{"Volte sempre!":^38}')
                                            print('-=' * 20)
                                            break
                                        if escolha != 's':
                                            print('valor digitado incorreto!')
                                            print('-=' * 20)
                                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                            print('-=' * 20)
                                elif renovar == 'n':
                                    ind2.remove(ind2[posicao])
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                            elif datadev <= datageral[posicao]:
                                renovar2 = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar2 == 's':
                                    datageral.pop(posicao)
                                    datageral.insert(posicao, datadev + 7)
                                    print('Você tem mais 7 dias para devolver o item.')
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                                elif renovar2 == 'n':
                                    ind2.remove(ind2[posicao])
                                    valor = quant[posicao] + 1
                                    quant.remove(valor - 1)
                                    quant.insert(posicao, valor)
                                    datanova = datageral[posicao]
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                        elif codigo_item in codigoitem:
                            posicao = codigoitem.index(codigo_item)
                            datadev = int(input('Digite a data que está devolvendo o item:'))
                            if datadev > datageral[posicao]:
                                valor = quant[posicao] + 1
                                quant.remove(valor - 1)
                                quant.insert(posicao, valor)
                                datanova = datageral[posicao]
                                atraso = datadev - datanova
                                datasuspensao = atraso * 3
                                print('Sua matricula está supensa por {} dias.'.format(datasuspensao))
                                suspenso.append(matriculay)
                                disponivel2.append(indisponivel[posicao])
                                indisponivel.remove(indisponivel[posicao])
                                renovar = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar == 's':
                                    if emprestado[posicao] in suspenso:
                                        print('Você esta suspenso')
                                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                        if escolha == 'n':
                                            print('-=' * 20)
                                            print(f'{"Volte sempre!":^38}')
                                            print('-=' * 20)
                                            break
                                        if escolha != 's':
                                            print('valor digitado incorreto!')
                                            print('-=' * 20)
                                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                            print('-=' * 20)
                            else:
                                renovar2 = input('Você deseja renovar [S/N]:')[0].strip().lower()
                                if renovar2 == 's':
                                    datageral.pop(posicao)
                                    datageral.insert(posicao, datadev + 7)
                                    print('Você tem mais 7 dias para devolver o item.')
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                                else:
                                    disponivel2.append(indisponivel[posicao])
                                    indisponivel.remove(indisponivel[posicao])
                                    escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                                    if escolha == 'n':
                                        print('-=' * 20)
                                        print(f'{"Volte sempre!":^38}')
                                        print('-=' * 20)
                                        break
                                    if escolha != 's':
                                        print('valor digitado incorreto!')
                                        print('-=' * 20)
                                        print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                        print('-=' * 20)
                        else:
                            print('Este item não foi encontrado.')
                            escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                            if escolha == 'n':
                                print('-=' * 20)
                                print(f'{"Volte sempre!":^38}')
                                print('-=' * 20)
                                break
                            if escolha != 's':
                                print('valor digitado incorreto!')
                                print('-=' * 20)
                                print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                                print('-=' * 20)
                    else:
                        print('Matricula invalida.')
                        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                        if escolha == 'n':
                            print('-=' * 20)
                            print(f'{"Volte sempre!":^38}')
                            print('-=' * 20)
                            break
                        if escolha != 's':
                            print('valor digitado incorreto!')
                            print('-=' * 20)
                            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                            print('-=' * 20)
            else:
                print('Essa matricula não corresponde ao item.')
                escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
                if escolha == 'n':
                    print('-=' * 20)
                    print(f'{"Volte sempre!":^38}')
                    print('-=' * 20)
                    break
                if escolha != 's':
                    print('valor digitado incorreto!')
                    print('-=' * 20)
                    print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                    print('-=' * 20)
        else:
            print('Código inválido.')
            escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
            if escolha == 'n':
                print('-=' * 20)
                print(f'{"Volte sempre!":^38}')
                print('-=' * 20)
                break
            if escolha != 's':
                print('valor digitado incorreto!')
                print('-=' * 20)
                print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
                print('-=' * 20)
    elif escolha == '6':
        for dis in disponivel2:
            print(f'Esta disponível {dis}')
        escolha = input('Deseja continuar na biblioteca?[S/N]:')[0].strip().lower()
        if escolha == 'n':
            print('-=' * 20)
            print(f'{"Volte sempre!":^38}')
            print('-=' * 20)
            break
        if escolha != 's':
            print('valor digitado incorreto!')
            print('-=' * 20)
            print('POR FAVOR ESCOLHA UMA OPÇÃO ABAIXO')
            print('-=' * 20)
    elif escolha == '7':
        print('-=' * 20)
        print(f'{"Volte sempre!":^38}')
        print('-=' * 20)
        break
    else:
        print('-=' * 20)
        print('Por favor digite uma opção valida!')
        print('-=' * 20)
