import mysql.connector
from getpass import getpass

conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=getpass("Senha do Mysql: "),
    database="kizuna_sports"
)

cursor = conexao.cursor(dictionary=True)
cursor.execute("SELECT * FROM quadras ORDER BY nome")
quadras = cursor.fetchall()

cursor.close
conexao.close

 # Funções
def mostrar_quadra(dados_quadra):

    print(f"Quadra: {dados_quadra["nome"]}")
    print(f"Modalidade: {dados_quadra["modalidade"]}")
    print(f"Preço por hora: {dados_quadra["preco_por_hora"]}")
    if dados_quadra["coberta"]:
        print("Coberta: Sim")
    else:
        print("Coberta: Não")


def calcular_valor(preco_por_hora, quantidade_horas):
    valor_total = preco_por_hora * quantidade_horas
    return valor_total

def ler_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida, informe um número inteiro")


print("KIZUNA SPORTS")
while True:
    print("QUADRAS DISPONÍVEIS PARA CONSULTA")
    numero = 1

    for quadra in quadras:
        print()
        print(f"OPÇÃO {numero}")
        mostrar_quadra(quadra)
        numero +=1
    print("Digite 0 para sair")
    escolha = ler_inteiro("Digite o número da quadra: ")


    if escolha == 0:
        print("Programa encerrado.")
        break
    
    if escolha >=1 and escolha <=len(quadras):
        indice = escolha - 1
        quadra_escolhida= quadras[indice]

        print(F"Você escolheu: {quadra_escolhida['nome']}")

        horas = ler_inteiro("Por quantas horas você deseja jogar? ")
        if horas >0:
            preco = quadra_escolhida['preco_por_hora']
            total = calcular_valor(preco,horas)

            print(f"Orçamento")
            print(f"Quadra: {quadra_escolhida['nome']}")
            print(F"Preço por hora: R$ {preco:.2f}")
            print(f"Duração: {horas} hora(s)")
            print(f"Valor total: R$ {total:.2f}")
            print("Esta consulta ainda não cria uma reserva.")

        else:
            print("A duração precisa ser maior que zero")

    else:
        print("Opção invalída. Essa quadra não existe")





