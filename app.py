import random

def criarArquivo():
    valores = eval(input("Digite sua lista em sequência, por exemplo -> 1, 4, 6: "))
    arquivo = open(nome_arquivo + '.txt', 'w')
    
    arquivo.write(str(valores) )
    arquivo.close()

def imprimirArquivo(nome):
    nome_arquivo = nome

    arquivo = open(nome_arquivo + '.txt', 'r')
    a = arquivo.readlines()
    valores = []

    for i in range(len(a)):
        valores.append(a[i])

    print(valores)

def bubbleSort():
    def ordenacao_bolha(e):
        n = len(e)

        for i in range(n):
            for f in range(0, n-1):
                if(e[f]>e[f+1]):
                    temp = e[f]
                    e[f] = e[f+1]
                    e[f+1] = temp

    e = eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open(nome_arquivo, 'w')
    arquivo.write("Ordenação em bolha" + '/n')
    arquivo.write("=== Ordenação por Bolha === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(e) +"\n"+ " Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    ordenacao_bolha(e)

    with open(nome_arquivo, 'a') as arquivo3:
        
        for valor3 in e:
            arquivo3.write( str(valor3) + ',')

def insertionSort():
    def ordenacao_insercao(c):
        n = len(c)

        for d in range(1,n):
            chave = c[d]
            i = d-1

            while i >= 0 and c[i]> chave:
                c[i + 1] = c[i]
                i = i - 1

            c[i+1] = chave

    c = eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open(nome_arquivo, 'w')
    arquivo.write("=== Ordenação por Ircerção === \n\n\n"+"Arranjo original (não ordenado): \n" + str(c) +"\n" + " Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    ordenacao_insercao(c)

    with open(nome_arquivo, 'a') as arquivo2:
        
        for valor2 in c:
            arquivo2.write( str(valor2) + ',')

def selectionSort():
    def ordenacao_selecao(a):
        n = len(a)
        for i in range(n):
            minimo = i
            for b in range(i + 1, n):
                if a[minimo] > a[b]:
                    minimo = b

            a[i], a[minimo] = a[minimo], a[i]
    
    
    a = eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open(nome_arquivo, 'w')
    
    arquivo.write("===Ordenação por Seleção === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(a) + "\n"+" Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    ordenacao_selecao(a)

    with open(nome_arquivo, 'a') as arquivo1:
        
        for valor1 in a:
            arquivo1.write( str(valor1) + ',')

def mergeSort():
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

    A  =  eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open(nome_arquivo, 'w')
    
    arquivo.write("===Merge Sort === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(A) + "\n"+" Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    aux = [0] * len(A)
    mergesort(A, aux, 0, len(A) - 1)
    with open(nome_arquivo, 'a') as arquivo1:
        
        for valor1 in A:
            arquivo1.write( str(valor1) + ',')


def quickSort():
    def quick_sort(A):
        quickSortHelper(A,0,len(A)-1)

    def quickSortHelper(A,primeiro,ultimo):
        if primeiro<ultimo:
            splitpoint = partition(A,primeiro,ultimo)

            quickSortHelper(A,primeiro,splitpoint-1)
            quickSortHelper(A,splitpoint+1,ultimo)

    def partition(A,primeiro,ultimo):
        pivot = A[primeiro]
        leftmark = primeiro+1
        rightmark = ultimo

        done = False
        while not done:

            while leftmark <= rightmark and A[leftmark] <= pivot:
                leftmark = leftmark + 1

            while A[rightmark] >= pivot and rightmark >= leftmark:
                rightmark = rightmark -1

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

    A  =  eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open(nome_arquivo, 'w')
    
    arquivo.write("===Quick Sort === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(A) + "\n"+" Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    quick_sort(A)    
    with open(nome_arquivo, 'a') as arquivo1:
        
        for valor1 in A:
            arquivo1.write( str(valor1) + ',')

#Programa Principal
opcao = 0
while True:
    print(" ============[ Menu Principal ]============")
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
        nome_arquivo = input("Digite um nome para o arquivo que deseja criar: ")
        criarArquivo()
    #elif opcao == 2:
       
    elif opcao == 3:
        arquivo = input("Digite o nome do arquivo que você deseja visualizar: ")
        imprimirArquivo(arquivo)
    elif opcao == 4:
        bubbleSort()
    elif opcao == 5:
        insertionSort()
    elif opcao == 6:
        selectionSort()
    elif opcao == 7:
        quickSort()
    elif opcao == 8:
        mergeSort()
    elif opcao == 9:
        print("Programa Finalizado.\n")
        break
    else:
        print("Este número não está entre as alternativas! Por favor, tente novamente :D.\n")
        