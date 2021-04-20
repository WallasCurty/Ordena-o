def criarArquivo():
    lista = []
    opcao = 's'
    while opcao == 's' or opcao == 'S':
        valor = int(input("Adicione um valor a sua lista: "))
        lista.append(valor)
        opcao = input(
            "Deseja continuar adicionando valores para a sua lista? ")

    nome_arquivo = input("Digite um nome para o arquivo que deseja criar: ")
    arquivo = open(nome_arquivo + '.txt', 'w')
    arquivo.write(str(lista))
    arquivo.close()


def alterarArquivo():
    nome_arquivo = input("Digite o nome do arquivo que deseja alterar: ")
    arquivo = open(nome_arquivo + '.txt', 'r')
    leitura_arquivo = arquivo.readlines()
    dados = []

    for i in range(len(leitura_arquivo)):
        dados.append(leitura_arquivo[i])

    arquivo.close()

    opcao = 0
    while opcao != 5:
        print("----------- ALTERAR ARQUIVO ---------")
        print("1) Incluir valores no arquivo")
        print("2) Excluir valor do arquivo")
        print("3) Alterar valor no arquivo")
        print("4) Visualizar arquivo")
        print("5) Voltar ao Menu Principal")
        opcao = int(input("Digite a opção desejada: "))

        arquivo = open(nome_arquivo + '.txt', 'w')

        if opcao == 1:
            valor = int(input("Digite o valor que deseja adicionar: "))
            dados.append(valor)
            arquivo.write(str(dados))
            print("Valor {} adicionado com sucesso!".format(valor))
        elif opcao == 2:
            posicao = int(
                input("Digite a posição do valor que deseja excluir: "))
            del dados[posicao]
            arquivo.write(str(dados))
            print("Valor da posição {} excluido com sucesso!".format(posicao))
        elif opcao == 3:
            posicao = int(input("Digite a posição que deseja alterar: "))
            valor = int(input("Digite o valor que deseja inserir: "))
            dados.insert(posicao, valor)
            del dados[posicao + 1]
            arquivo.write(str(dados))
            print("Valor {} da posição {} alterado com sucesso!".format(valor, posicao))
        elif opcao == 4:
            print("Lista do arquivo atual:")
            print(dados)
        elif opcao == 5:
            break
        else:
            print(
                "Este número não está entre as alternativas! Por favor, tente novamente :D.\n")

        arquivo.write(str(dados))


def imprimirArquivo(nome):
    nome_arquivo = nome

    arquivo = open(nome_arquivo + '.txt', 'r')
    a = arquivo.readlines()
    valores = []

    for x in range(len(a)):
        valores.append(a[x])
    print(valores)


def converterArquivoToList(nome):
    nome_arquivo = nome
    arquivo = open(nome_arquivo + '.txt', 'r')

    lista = arquivo.readlines()
    listaN = []

    for i in range(len(lista)):
        listaN.append(int(lista[i]))

    return listaN


def bubbleSort(arquivo):
    nome_arquivo = arquivo

    def ordenacao_bolha(lista):
        n = len(lista)

        for i in range(n):
            for f in range(0, n-1):
                if(lista[f] > lista[f+1]):
                    temp = lista[f]
                    lista[f] = lista[f+1]
                    lista[f+1] = temp

    lista = converterArquivoToList(nome_arquivo)
    ordenacao_bolha(lista)
    print(lista)


def insertionSort(arquivo):
    nome_arquivo = arquivo

    def ordenacao_insercao(lista):
        n = len(lista)

        for d in range(1, n):
            chave = lista[d]
            i = d-1

            while i >= 0 and lista[i] > chave:
                lista[i + 1] = lista[i]
                i = i - 1

            lista[i+1] = chave

    lista = converterArquivoToList(nome_arquivo)
    ordenacao_insercao(lista)
    print(lista)


def selectionSort(arquivo):
    nome_arquivo = arquivo

    def ordenacao_selecao(a):
        n = len(a)
        for i in range(n):
            minimo = i
            for b in range(i + 1, n):
                if a[minimo] > a[b]:
                    minimo = b

            a[i], a[minimo] = a[minimo], a[i]

    lista = converterArquivoToList(nome_arquivo)
    ordenacao_selecao(lista)
    print(lista)


def mergeSort(arquivo):
    nome_arquivo = arquivo

    def merge(A, aux, esquerda, meio, direita):

        for k in range(esquerda, direita + 1):
            aux[k] = A[k]
        i = esquerda
        j = meio + 1

        for k in range(esquerda, direita + 1):
            if i > meio:
                A[k] = aux[j]
                j += 1
            elif j > direita:
                A[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                A[k] = aux[j]
                j += 1
            else:
                A[k] = aux[i]
                i += 1

    def mergesort(A, aux, esquerda, direita):
        if direita <= esquerda:
            return
        meio = (esquerda + direita) // 2

        mergesort(A, aux, esquerda, meio)
        mergesort(A, aux, meio + 1, direita)
        merge(A, aux, esquerda, meio, direita)

    lista = converterArquivoToList(nome_arquivo)
    aux = [0] * len(lista)
    mergesort(lista, aux, 0, len(lista) - 1)
    print(lista)


def quickSort(arquivo):
    nome_arquivo = arquivo

    def quick_sort(A):
        quickSortHelper(A, 0, len(A)-1)

    def quickSortHelper(A, primeiro, ultimo):
        if primeiro < ultimo:
            splitpoint = partition(A, primeiro, ultimo)

            quickSortHelper(A, primeiro, splitpoint-1)
            quickSortHelper(A, splitpoint+1, ultimo)

    def partition(A, primeiro, ultimo):
        pivot = A[primeiro]
        leftmark = primeiro+1
        rightmark = ultimo

        done = False
        while not done:

            while leftmark <= rightmark and A[leftmark] <= pivot:
                leftmark = leftmark + 1

            while A[rightmark] >= pivot and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = A[leftmark]
                A[leftmark] = A[rightmark]
                A[rightmark] = temp

        temp = A[primeiro]
        A[primeiro] = A[rightmark]
        A[rightmark] = temp

        return rightmark

    lista = converterArquivoToList(nome_arquivo)
    quick_sort(lista)
    print(lista)


# Programa Principal
opcao = 0
while True:
    print(" ------------ Algoritmos de Ordenação -----")
    print(" ------------ Menu Principal --------------")
    print("1) Criar arquivo de dados")
    print("2) Alterar arquivo de dados")
    print("3) Imprimir arquivo de dados")
    print("4) Bubble Sort")
    print("5) Insertion Sort")
    print("6) Selection Sort")
    print("7) Quick Sort")
    print("8) Merge Sort")
    print("9) Finalizar o programa")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        criarArquivo()
    elif opcao == 2:
        alterarArquivo()
    elif opcao == 3:
        arquivo = input(
            "Digite o nome do arquivo que você deseja visualizar: ")
        imprimirArquivo(arquivo)
    elif opcao == 4:
        nome_arquivo = input(
            "Digite o nome do arquivo que você deseja ordenar: ")
        bubbleSort(nome_arquivo)
    elif opcao == 5:
        nome_arquivo = input(
            "Digite o nome do arquivo que você deseja ordenar: ")
        insertionSort(nome_arquivo)
    elif opcao == 6:
        nome_arquivo = input(
            "Digite o nome do arquivo que você deseja ordenar: ")
        selectionSort(nome_arquivo)
    elif opcao == 7:
        nome_arquivo = input(
            "Digite o nome do arquivo que você deseja ordenar: ")
        quickSort(nome_arquivo)
    elif opcao == 8:
        nome_arquivo = input(
            "Digite o nome do arquivo que você deseja ordenar: ")
        mergeSort(nome_arquivo)
    elif opcao == 9:
        print("\n Programa Finalizado.")
        break
    else:
        print(
            "Este número não está entre as alternativas! Por favor, tente novamente :D.\n")
