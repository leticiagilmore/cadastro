cardapio = ["cachorro quente", 8.00, "hamburguer", 12.00, "nachos",
            10.00, "refrigerante 350 ml", 4.00, "cerveja longneck", 7.00]
pedido = list()


def exibir_menu(list):
    ''' 
    retorna a lista do cardápio organizada para visualização.
    '''
    for i, items in enumerate(list):
        if i % 2 == 0:
            print(f"{items:.<40}", end="")
        else:
            print(f"R$ {items:.2f}".replace(".", ","))


def escolha(lista, pedido=[]):
    '''
    organiza e monta o pedido em uma lista vazia, ou acrescenta mais itens no caso da lista ser diferente de None.
    '''
    while True:
        while True:
            escolha = input("faça seu pedido: ")
            if escolha not in lista:
                print("produto inexistente")
            else:
                break
        qtde = int(input(f"Quantidade de {escolha}: "))
        for items in lista:
            if escolha == items:
                for c in range(0, qtde):
                    pedido.append(escolha)
                    pedido.append(lista[lista.index(escolha) + 1])
                resumo(pedido)
                ask = input(
                    "deseja mais alguma coisa? [S/N] ").upper().strip()[0]
                if ask == "N":
                    return pedido


def resumo(lista):
    '''
    exibi um resumo do pedido até o momento.
    '''
    print(f'''
{"="*50}
{"RESUMO".center(50)}
{"="*50}''')
    for i, items in enumerate(lista):
        if i % 2 == 0:
            print(f"{items:.<40}", end="")
        else:
            print(f"R$ {items:.2f}".replace(".", ","))
    print(f"{'total':.<40}R$ ", end='')
    print(f"{total(lista):.2f}".replace(".", ","))


def total(lista):
    '''
    return => valor total a ser pago do pedido
    '''
    valor_total = 0
    for i, itens in enumerate(lista):
        if i % 2 == 1:
            valor_total += itens
    return valor_total


def excluir_pedido(lista):
    resumo(lista)
    product_del = input("digite o nome do Produto que deseja exluir: ")
    for i, itens in enumerate(lista):
        if product_del == itens:
            del(lista[i+1])
            del(lista[i])
    resumo(lista)
    return lista


def finalizar_pedido(lista):
    print(f'''
{"="*50}
{"PEDIDO FINALIZADO".center(50)}
{"="*50}''')
    for i, items in enumerate(lista):
        if i % 2 == 0:
            print(f"{items:.<40}", end="")
        else:
            print(f"R$ {items:.2f}".replace(".", ","))
    print("="*50)
    print(f"{'total':.<40}R$ ", end='')
    print(f"{total(lista):.2f}".replace(".", ","))
    print("OBRIGADO E VOLTE SEMPRE!!".center(50))


# programing main
exibir_menu(cardapio)
e = escolha(cardapio)
while True:
    choise = int(input("Digite <1> para confirmar o pedido\n"
                       "Digite <2> para excluir um produto\n"
                       "Digite <3> para adicionar mais algum produto\n"
                       "Digite <4> para cancelar o pedido\n"))
    if choise == 1:
        finalizar_pedido(e)
        break
    elif choise == 2:
        excluir_pedido(e)
    elif choise == 3:
        escolha(cardapio, e)
    elif choise == 4:
        print("Pedido cancelado com sucesso!")
        break
    else:
        print("erro, opção inválida.")