# Rodrigo Rato - 81500
#
# Escrito e testado para Python versao:
# 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)]

# questoes:
# luhn_verifica com eval strs
# comeca_por_um qual das maneiras

import random

# Tabela 1 do enunciado, onde tuplo e' substituido pela abreviatura da rede:
# tuplo[0] = Tuplo com os prefixos possiveis em tipo string
# tuplo[1] = Tuplo com os numeros de digitos possiveis em inteiro
# tuplo[2] = Nome da rede emissora em string
AE = (("34", "37"), (15,), "American Express")
DCI = (("309", "36", "38", "39"), (14,), "Diners Club International")
DC = (("65",), (16,), "Discover Card")
M = (("5018", "5020", "5038"), (13, 19), "Maestro")
MC = (("50", "51", "52", "53", "54", "19"), (16,), "Master Card")
VE = (("4026", "426", "4405", "4508"), (16,), "Visa Electron")
V = (("4024", "4532", "4556"), (13, 16), "Visa")

def calc_soma(cadeia):
    # Recebe uma string e devolve inteiro
    cadeia = inverte_string(cadeia)
    cadeia = duplicaImparesESubtraiNove(cadeia)
    soma = 0
    for i in cadeia:
        soma = soma + eval(i)
    return soma

def inverte_string(cadeia):
    # Recebe e devolve uma string
    cadeia_invertida = ""
    n = len(cadeia) - 1
    while n >= 0:
        cadeia_invertida = cadeia_invertida + cadeia[n]
        n = n - 1
    return cadeia_invertida

def duplicaImparesESubtraiNove(cadeia):
    # Recebe e devolve uma string
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
    digito_verificacao = eval(str_nr_cartao) % 10
    str_nr_sem_verificacao = str(eval(str_nr_cartao) // 10)
    cartao_somado = calc_soma(str_nr_sem_verificacao) + digito_verificacao
    if cartao_somado % 10 == 0:
        return True
    else:
        return False

def comeca_por(cad1, cad2):
    if len(cad2) > len(cad1) or cad2 == "":
        return False
    comeca = True
    for n in range(len(cad2)):
        if cad1[n] != cad2[n]:
            comeca = False
    return comeca

def comeca_por_um(cad, t_cads):
    # falta confirmar
    for elemento in t_cads:
        if comeca_por(cad, elemento):
            return True
    return False
    #for i in range(len(t_cads)):
        #if comeca_por(cad, t_cads[i]):
            #return True
    #return False

def valida_iin(cadeia):
    # DEFINICOES DOS TUPLOS ESTAO NO CABECALHO DO PROGRAMA!!    
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
    for i in range(len(tup1)):
        if len(cad1) == tup1[i]:
            return True
    return False

def categoria(cadeia):
    # para uma categoria invalida (n0 = 0) devolve "" (cc vazia)
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
    if cadeia[0] == "0":
        return ""

def verifica_cc(numero_cartao):
    cc_cartao = str(numero_cartao)
    # posso tar a falhar/esquecer algum caso neste if, testar l8r
    # se der erro remover ultima condicao e depois penultima (testar entretanto)
    if luhn_verifica(cc_cartao) and categoria(cc_cartao) != "" and valida_iin(cc_cartao) != "":
        return (categoria(cc_cartao), valida_iin(cc_cartao))
    else:
        return "cartao invalido"
    
#1a parte em cima  /\
#                  ||
#2a parte em baixo \/

def randomCartaoSemVerificacao(abrev):
    num = 0
    if abrev == "AE":
        num = encheRandomAte(escolheElementoTuplo(AE[0]), AE[1][0] - 1)
    if abrev == "DCI":
        num = encheRandomAte(escolheElementoTuplo(DCI[0]), DCI[1][0] - 1)
    if abrev == "DC":
        num = encheRandomAte(escolheElementoTuplo(DC[0]), DC[1][0] - 1)
    if abrev == "M":
        num = encheRandomAte(escolheElementoTuplo(M[0]), escolheElementoTuplo(tuploInteirosTuploCadeias(M[1])) - 1)
    if abrev == "MC":
        num = encheRandomAte(escolheElementoTuplo(MC[0]), MC[1][0] - 1)
    if abrev == "VE":
        num = encheRandomAte(escolheElementoTuplo(VE[0]), VE[1][0] - 1)
    if abrev == "V":
        num = encheRandomAte(escolheElementoTuplo(V[0]), escolheElementoTuplo(tuploInteirosTuploCadeias(V[1])) - 1)    
    return num

def tuploInteirosTuploCadeias(tuplo_ints):
    tuplo_cadeias = ()
    for i in tuplo_ints:
        tuplo_cadeias = tuplo_cadeias + (str(i),)
    return tuplo_cadeias

def gera_num_cc(abrev):
    num = 0
    num = randomCartaoSemVerificacao(abrev)
    num = (num * 10) + eval(digito_verificacao(str(num)))
    return num        
        
def encheRandomAte(numero, comprimento):
    while len(str(numero)) < comprimento:
        numero = (numero * 10) + randomZeroANum(9)
    return numero

def randomZeroANum(num):
    return int(random.random() * (num + 1))

def escolheElementoTuplo(tuplo_de_cadeias):
    tuplo_de_inteiros = ()
    for i in tuplo_de_cadeias:
        tuplo_de_inteiros = tuplo_de_inteiros + (eval(i),)
    return tuplo_de_inteiros[randomZeroANum(len(tuplo_de_inteiros) - 1)]
    
def digito_verificacao(cc_cartao_sem_ultimo):
    soma_sem_ultimo = calc_soma(cc_cartao_sem_ultimo)
    if soma_sem_ultimo % 10 == 0:
        return "0"
    else:
        return str(10 - (soma_sem_ultimo % 10))