import numpy as np
#perceptron base

entrada = 0
opc = 0
limiar = 0
#definição do pesos
#um peso para cada entrada
w = [0.2,-0.9,0.1]
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

# entradaTeste=np.array([[0,0],
#                   [0,1],
#                   [1,0],
#                   [1,1]])

entrada=np.array([[0,0],
                  [0,1],
                  [1,0],
                  [1,1]])

while(opc!=7):
    print("\n\n ************ Programa Perceptron ************")
    print("\n\n Digite 1 para treinar AND")
    print("\n Digite 2 para treinar OR")
    print("\n Digite 3 para treinar NAND")
    print("\n Digite 4 para treinar NOR")
    print("\n Digite 5 para treinar XOR")
    print("\n Digite 6 para operar")
    print("\n Digite 7 para Sair\n ->")
    opc = int(input())
    if(opc == 1):
        target = [-1,-1,-1,1]
        yliq = 0
        contCiclo = 0
        y = 0
    if(opc == 2):
        target = [-1,1,1,1]
        yliq = 0
        contCiclo = 0
        y = 0
    if(opc == 3):
        target = [1,1,1,-1]
        yliq = 0
        contCiclo = 0
        y = 0
    if(opc == 4):
        target = [1,-1,-1,-1]
        yliq = 0
        contCiclo = 0
        y = 0
    if(opc == 5):
        target = [-1,1,1,-1]
        yliq = 0
        contCiclo = 0
        y = 0
    if(1 <= opc < 6):
        while(condErro == 1):
            condErro = 0
            lin = 0
            while(lin<4):
                yliq = 0
                col = 0
                while(col<2):
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
                    while(col<2):
                        w[col] = w[col] + (alfa*target[lin]*entrada[(lin,col)])
                        col+=1
                    b = b +(alfa*target[lin])
                lin+=1
            print(f"\nCiclo: {contCiclo} \n")
            contCiclo+=1
        print("\n Rede treinada!")
        col = 0
        while(col<2):
            print(f"\n Peso[{col}]: {w[col]}")
            col+=1
        print(f"\n Bias: {b}")
    if(opc == 6):
        yTeste = 0
        teste = 0
        entradaTeste = np.array([[0,0]])
        entradaTeste[0][0] = int(input())
        entradaTeste[0][1] = int(input())
        lin = 0
        while(lin<1):
            col=0
            while(col<2):
                print(f"\n Entrada[{lin}][{col}]:{entrada[(lin,col)]}")
                col+=1
            lin+=1
        for lin in range(1):
            teste = 0
            for col in range(2):
                teste = teste + (entradaTeste[(lin,col)]*w[col])
            teste = teste + b
            if(teste >= limiar):
                yTeste = 1
            else:
                yTeste = -1
            print(f"\n Saida da rede[{lin}]: {yTeste}")
    


        




