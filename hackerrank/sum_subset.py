
def chupa_negao():
    #v = [-2, -3, 4, -1, -2, 1, 5, -3]
    v = [10, -1, -9, 1, 15]
    tamanho = len(v)
    soma_ant = -1000000
    while(tamanho >= 0):
        for i in range(0, tamanho):
            soma = 0
            pos_inic = i
            pos_final = tamanho
            for j in range(pos_inic, pos_final):
                soma += v[j]
                if(soma > soma_ant):
                    soma_ant = soma
        
        tamanho -= 1
    
    print(soma_ant)
chupa_negao()