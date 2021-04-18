import random

def Criar_Arq():
    
    a = eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open(nome, 'w')
    
    arquivo.write("Sua lista de elementos foi: \n"  + str(a) )
    arquivo.close()
#---------------------------------------------------------------------------------------------------
def Imprimir():

    arquivo = open(nome, 'r')

    print(arquivo.readline())
    arquivo.close
#---------------------------------------------------------------------------------------------------

def Ord_Bol():
    def ordenacao_bolha(e):
        n = len(e)

        for i in range(n):
            for f in range(0, n-1):
                if(e[f]>e[f+1]):
                    temp = e[f]
                    e[f] = e[f+1]
                    e[f+1] = temp

    e = eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open(nome, 'w')
    arquivo.write("Ordenação em bolha" + '/n')
    arquivo.write("=== Ordenação por Bolha === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(e) +"\n"+ " Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    ordenacao_bolha(e)

    with open(nome, 'a') as arquivo3:
        
        for valor3 in e:
            arquivo3.write( str(valor3) + ',')

#---------------------------------------------------------------------------------------------------
def Ord_In():
    def ordenacao_incercao(c):
        n = len(c)

        for d in range(1,n):
            chave = c[d]
            i = d-1

            while i >= 0 and c[i]> chave:
                c[i + 1] = c[i]
                i = i - 1
            c[i+1] = chave

    c = eval('[' + input("Digite sua lista: ") + ']')
    arquivo = open(nome, 'w')
    arquivo.write("=== Ordenação por Ircerção === \n\n\n"+"Arranjo original (não ordenado): \n" + str(c) +"\n" + " Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    ordenacao_incercao(c)

    with open(nome, 'a') as arquivo2:
        
        for valor2 in c:
            arquivo2.write( str(valor2) + ',')

#---------------------------------------------------------------------------------------------------
def Ord_Sel():
    def ordenacao_selecao(a):
        n = len(a)
        for i in range(n):
            minimo = i
            for b in range(i + 1, n):
                if a[minimo] > a[b]:
                    minimo = b
            a[i], a[minimo] = a[minimo], a[i]
    
    arquivo = open(nome, 'w')
    
    arquivo.write("===Ordenação por Seleção === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(a) + "\n"+" Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    ordenacao_selecao(a)

    with open(nome, 'a') as arquivo1:
        
        for valor1 in a:
            arquivo1.write( str(valor1) + ',')

#---------------------------------------------------------------------------------------------------
def Merge_Sort():
    
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
    arquivo = open(nome, 'w')
    
    arquivo.write("===Merge Sort === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(A) + "\n"+" Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    aux = [0] * len(A)
    mergesort(A, aux, 0, len(A) - 1)
    with open(nome, 'a') as arquivo1:
        
        for valor1 in A:
            arquivo1.write( str(valor1) + ',')


    
#---------------------------------------------------------------------------------------------------
def Quick_Sort():
    def quickSort(A):
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
    arquivo = open(nome, 'w')
    
    arquivo.write("===Quick Sort === \n\n\n"+"Arranjo original (não ordenado): \n"  + str(A) + "\n"+" Novo Arranjo (Ordenado): \n" )
    arquivo.close()

    quickSort(A)    
    with open(nome, 'a') as arquivo1:
        
        for valor1 in A:
            arquivo1.write( str(valor1) + ',')

#---------------------------------------------------------------------------------------------------

menu=True
while menu:
    opcao=int(input('''
        
        ============[ Menu Inicial ]============
        
            1) Criar arquivo de dados
            2) Alterar arquivo de dados
            3) Imprimir arquivo de dados
            4) Bubble Sort
            5) Insertion Sort
            6) Selection Sort
            7) Quick Sort
            8) Merge Sort
            9) Finalizar o programa
            
            Escolha a opção desejada: '''))
    
    nome=input("Digite o nome do arquivo: ")

    if opcao == 1:
        Criar_Arq()
    elif opcao == 2:
        Ord_In()
    elif opcao == 3:
        Imprimir()
    elif opcao == 4:
        Ord_Bol()
    elif opcao == 5:
        Ord_In()
    elif opcao == 6:
        Ord_Sel()
    elif opcao == 7:
        Quick_Sort()
    elif opcao == 8:
        Merge_Sort()
    elif opcao == 9:
        print("Programa Finalizado.\n")
        break
    else:
        print("Este número não está nas alternativas, tente novamente :D.\n")
        