import numpy as np
#perceptron base

entrada = 0
opc = 0
limiar = 0
#definição do pesos
#um peso para cada entrada
w = [0.2,-0.9,0.1]
#definição das primeira e segunda classe
#duas possiveis saidas
target = [-1,1]
#definindo valor do bias
b = 0.6
#definindo a taxa de aprendizagem
alfa = 0.1
yliq = 0
contCiclo = 0
y = 0
yTeste = 0
lin = 0
col = 0
condErro = 1
teste = 0

entrada=np.array([[0,0,1],
         [1,1,0]])

while(opc!=3):
    print("\n\n ************ Programa Perceptron ************")
    print("\n\n Digite 1 para treinar a rede")
    print("\n Digite 2 para operar")
    print("\n Digite 3 para Sair\n ->")
    opc = int(input())
    if(opc == 1):
        while(condErro == 1):
            condErro = 0
            lin = 0
            while(lin<2):
                yliq = 0
                col = 0
                while(col<3):
                    yliq = yliq + (entrada[(lin,col)]*w[col])
                    col+=1
                yliq = yliq + b
                if(yliq >= limiar):
                    y = 1
                else:
                    y = -1
                print(f"\n yLiq: {yliq} - y: {y} - Target: {target[lin]}")
                if(y!=target[lin]):
                    condErro = 1
                    col = 0
                    while(col<3):
                        w[col] = w[col] + (alfa*target[lin]*entrada[(lin,col)])
                        col+=1
                    b = b +(alfa*target[lin])
                lin+=1
            print(f"\nCiclo: {contCiclo} \n")
            contCiclo+=1
        print("\n Rede treinada!")
        col = 0
        while(col<3):
            print(f"\n Peso[{col}]: {w[col]}")
            col+=1
        print(f"\n Bias: {b}")
    if(opc == 2):
        lin = 0
        while(lin<2):
            col=0
            while(col<3):
                print(f"\n Entrada[{lin}][{col}]:{entrada[(lin,col)]}")
                col+=1
            lin+=1
        for lin in range(2):
            teste = 0
            for col in range(3):
                teste = teste + (entrada[(lin,col)]*w[col])
            teste = teste + b
            if(teste >= limiar):
                yTeste = 1
            else:
                yTeste = -1
            print(f"\n Saida da rede[{lin}]: {yTeste}")
    


        




