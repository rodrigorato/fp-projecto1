# Rodrigo Rato - 81500
#
# Escrito e testado para Python versao:
# 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43)


# COBRIR TODOS OS CASOS DE INPUT INVALIDO??
# VALE A PENA USAR ELIFS? OU SO IFS E NO FIM RETURN?
#     ___
#    /   \
#     | |
#     | | Questoes aqui em cima!
#     | |

import random

# Usam se tuplos para guardar a informacao da Tabela 1 do 
# enunciado com a seguinte estrutura. ABREV e' substituido pela abreviatura da rede:
# ABREV[0] = Tuplo com os prefixos possiveis em tipo string
# ABREV[1] = Tuplo com os numeros de digitos possiveis em inteiro
# ABREV[2] = Nome da rede emissora em string
AE = (("34", "37"), (15,), "American Express")
DCI = (("309", "36", "38", "39"), (14,), "Diners Club International")
DC = (("65",), (16,), "Discover Card")
M = (("5018", "5020", "5038"), (13, 19), "Maestro")
MC = (("50", "51", "52", "53", "54", "19"), (16,), "Master Card")
VE = (("4026", "426", "4405", "4508"), (16,), "Visa Electron")
V = (("4024", "4532", "4556"), (13, 16), "Visa")

def calc_soma(cadeia):
    '''
    Recebe uma string e devolve o inteiro correspondente 'a 
    soma ponderada dos digitos, calculada com o algoritmo de Luhn.
    '''
    cadeia = inverte_string(cadeia)
    cadeia = duplicaImparesESubtraiNove(cadeia)
    soma = 0
    for i in cadeia:
        soma = soma + eval(i)
    return soma

def inverte_string(cadeia):
    '''
    Recebe uma string e devolve a string correspondente 'a 
    primeira invertida, necessario para o algoritmo de Luhn.
    '''
    cadeia_invertida = ""
    n = len(cadeia) - 1
    while n >= 0:
        cadeia_invertida = cadeia_invertida + cadeia[n]
        n = n - 1
    return cadeia_invertida

def duplicaImparesESubtraiNove(cadeia):
    '''
    Recebe uma string e devolve a string com os numeros em 
    indices impares multiplicados por dois e caso esses numeros
    sejam superiores a 9 e' lhes subtraido o valor 9. 
    Esta string tera' de ser uma em que para qualquer que seja 
    o numero inteiro n, eval(cadeia[n]) existe e e' um numero inteiro.
    '''
    duplicados = ""
    n = 0
    for n in range(len(cadeia)):
            if ((n+1) % 2) != 0:
                if (eval(cadeia[n]) * 2) > 9:
                    duplicados = duplicados + str((eval(cadeia[n]) * 2) - 9)
                else:
                    duplicados = duplicados + str(eval(cadeia[n]) * 2)
            else:
                duplicados = duplicados + cadeia[n]
    return duplicados

def luhn_verifica(str_nr_cartao):
    '''
    Recebe uma string (numero do cartao) e devolve o valor 
    logico True se o numero do cartao passar o algoritmo de Luhn
    e False em caso contrario.
    '''
    digito_verificacao = eval(str_nr_cartao) % 10
    str_nr_sem_verificacao = str(eval(str_nr_cartao) // 10)
    cartao_somado = calc_soma(str_nr_sem_verificacao) + digito_verificacao
    return cartao_somado % 10 == 0

def comeca_por(cad1, cad2):
    '''
    Recebe duas cadeias e verifica se a segunda esta'
    contida no inicio da primeira. Devolve True/False.
    '''
    if len(cad2) > len(cad1) or cad2 == "":
        return False
    for n in range(len(cad2)):
        if cad1[n] != cad2[n]:
            return False
    return True

def comeca_por_um(cad, t_cads):
    '''
    Recebe uma cadeia e um tuplo de cadeias e 
    verifica se alguma das cadeias no tuplo esta' 
    contida no inicio da primeira cadeia. Devolve True/False
    '''
    for elemento in t_cads:
        if comeca_por(cad, elemento):
            return True
    return False

def valida_iin(cadeia):
    '''
    Usa os tuplos definidos no inicio do ficheiro para 
    validar o iin da cadeia que a funcao recebe.Recebe o 
    numero de um cartao e devolve o nome da rede emissora em string.
    '''    
    if comeca_por_um(cadeia, AE[0]) and numero_digitos(cadeia, AE[1]): 
        return AE[2]
    if comeca_por_um(cadeia, DCI[0]) and numero_digitos(cadeia, DCI[1]):
        return DCI[2]
    if comeca_por_um(cadeia, DC[0]) and numero_digitos(cadeia, DC[1]):
        return DC[2]
    if comeca_por_um(cadeia, M[0]) and numero_digitos(cadeia, M[1]):
        return M[2]
    if comeca_por_um(cadeia, MC[0]) and numero_digitos(cadeia, MC[1]):
        return MC[2]
    if comeca_por_um(cadeia, VE[0]) and numero_digitos(cadeia, VE[1]):
        return VE[2]        
    if comeca_por_um(cadeia, V[0]) and numero_digitos(cadeia, V[1]):
        return V[2]      
    return ""    

def numero_digitos(cad1, tup1):
    '''
    Recebe uma cadeia e um tuplo de inteiros e verifica 
    se o comprimento da cadeia e' igual a algum dos inteiros no tuplo.
    '''
    for i in range(len(tup1)):
        if len(cad1) == tup1[i]:
            return True
    return False

def categoria(cadeia):
    '''
    Recebe uma cadeia e verifica o se o que esta' no indice 0 
    dessa cadeia e' alguma categoria conhecida e devolve a cadeia 
    correspondente 'a categoria. Em caso contrario devolve a cadeia 
    de caracteres vazia.
    '''
    if cadeia[0] == "1":
        return "Companhias aereas"
    if cadeia[0] == "2":
        return "Companhias aereas e outras tarefas futuras da industria"
    if cadeia[0] == "3":
        return "Viagens e entretenimento e bancario / financeiro"
    if cadeia[0] == "4":
        return "Servicos bancarios e financeiros"
    if cadeia[0] == "5":
        return "Servicos bancarios e financeiros"
    if cadeia[0] == "6":
        return "Merchandising e bancario / financeiro"
    if cadeia[0] == "7":
        return "Petroleo e outras atribuicoes futuras da industria"
    if cadeia[0] == "8":
        return "Saude, telecomunicacoes e outras atribuicoes futuras da industria"
    if cadeia[0] == "9":
        return "Atribuicao nacional"
    return ""

def verifica_cc(numero_cartao):
    '''
    Recebe um numero de um cartao e verifica se e' valido, 
    ou seja: e' verificado pelo algoritmo de Luhn, tem uma
    categoria valida associada ao mesmo e o seu iin pode ser validado.
    Devolve o tuplo correspondente as strings da categoria e do
    nome da rede emissora. Em caso de um cartao inva'lido devolve 
    a cadeia de caracteres "cartao invalido".
    '''
    cc_cartao = str(numero_cartao)
    if luhn_verifica(cc_cartao) and categoria(cc_cartao) != "" and valida_iin(cc_cartao) != "":
        return (categoria(cc_cartao), valida_iin(cc_cartao))
    else:
        return "cartao invalido"

# Comeca aqui a segunda parte do projeto, tudo relacionado com gerar numeros esta' daqui para baixo.

def randomCartaoSemVerificacao(abrev):
    '''
    Recebe abreviatura da rede emissora, se for 
    valida gera o numero aleatoriamente pela funcao
    encheRandomAte para a qual passa como argumentos 
    o digito inicial (ou digitos iniciais, se for o caso
    usa escolheElementoTuplo para escolher um prefixo
    aleatoriamente) e o numero de digitos possiveis menos
    um, o digito de verificacao. Em caso de diferentes 
    "comprimentos" possiveis escolhe do tuplo dos comprimentos
    um aleatoriamente, como para os prefixos. Devolve o
    inteiro do numero do cartao sem dig. de verificacao.
    '''
    num = 0
    if abrev == "AE":
        num = encheRandomAte(escolheElementoTuplo(AE[0]), AE[1][0] - 1)
    if abrev == "DCI":
        num = encheRandomAte(escolheElementoTuplo(DCI[0]), DCI[1][0] - 1)
    if abrev == "DC":
        num = encheRandomAte(eval(DC[0][0]), DC[1][0] - 1) # Nao e' necessario escolher o prefixo, so' 1 e' possivel.
    if abrev == "M":
        num = encheRandomAte(escolheElementoTuplo(M[0]), escolheElementoTuplo(tuploInteirosTuploCadeias(M[1])) - 1) # Neste caso tem de se escolher um comprimento aleatoriamente.
    if abrev == "MC":
        num = encheRandomAte(escolheElementoTuplo(MC[0]), MC[1][0] - 1)
    if abrev == "VE":
        num = encheRandomAte(escolheElementoTuplo(VE[0]), VE[1][0] - 1)
    if abrev == "V":
        num = encheRandomAte(escolheElementoTuplo(V[0]), escolheElementoTuplo(tuploInteirosTuploCadeias(V[1])) - 1) # Neste caso tem de se escolher um comprimento aleatoriamente.
    return num

def tuploInteirosTuploCadeias(tuplo_ints):
    '''
    Recebe um tuplo com membros do tipo 
    inteiro e devolve um tuplo com as cadeias 
    de caracteres correspondentes a esses inteiros.
    '''
    tuplo_cadeias = ()
    for i in tuplo_ints: # Nao se usa range() para evitar problemas, e' mais facil de obter a string correspondente ao inteiro deste modo.
        tuplo_cadeias = tuplo_cadeias + (str(i),)
    return tuplo_cadeias

def gera_num_cc(abrev):
    '''
    Gera um numero de cartao aleatorio dada a 
    abreviatura da rede emissora como parametro, 
    devolve um numero de um cartao valido (inteiro) 
    que pertence 'a rede desejada.
    '''
    num = 0
    num = randomCartaoSemVerificacao(abrev)
    num = (num * 10) + eval(digito_verificacao(str(num)))
    return num        
        
def encheRandomAte(numero, comprimento):
    '''
    Devolve um inteiro "completado", aleatoriamente, com 
    prefixo de valor igual 'a variavel numero, ate' o seu 
    comprimento ser igual ao valor do inteiro comprimento.
    '''
    while len(str(numero)) < comprimento: # len(str(numero)) da' o "comprimento" do numero a "preencher".
        numero = (numero * 10) + randomZeroANum(9)
    return numero

def randomZeroANum(num):
    '''
    Escolhe um inteiro aleatoriamente desde 0,
    ate' o valor da variavel/parametro num. E'
    possivel obter tanto o numero 0 como o valor de num.
    '''
    return int(random.random() * (num + 1)) # int() faz com que so seja devolvida a parte inteira do numero gerado

def escolheElementoTuplo(tuplo_de_cadeias):
    '''
    Escolhe aleatoriamente um elemento de um tuplo cujos
    elementos sao strings e devolve o inteiro correspondente 
    a esse elemento.
    '''
    tuplo_de_inteiros = ()
    for i in tuplo_de_cadeias: # aqui define-se todos os elementos de um tuplo_de_inteiros, que sao os inteiros correspondentes 'as strings do primeiro tuplo.
        tuplo_de_inteiros = tuplo_de_inteiros + (eval(i),)
    return tuplo_de_inteiros[randomZeroANum(len(tuplo_de_inteiros) - 1)]
    
def digito_verificacao(cc_cartao_sem_ultimo):
    '''
    Calcula o digito de verificacao de uma cadeia de 
    caracteres correspondente a um numero de um cartao
    sem este ultimo digito. Devolve apenas o ultimo digito.
    '''
    soma_sem_ultimo = calc_soma(cc_cartao_sem_ultimo)
    if soma_sem_ultimo % 10 == 0:
        return "0"
    else:
        return str(10 - (soma_sem_ultimo % 10))