import json
import task
import time

try:
    with open("lucro.json","r") as lucro:
        lucro = json.load(lucro)
except (FileNotFoundError, json.JSONDecodeError):
    lucro = []
    print("criando lista vazia de lucro")
try:
    with open("gastos.json","r") as gasto:
        gasto = json.load(gasto)
except (FileNotFoundError, json.JSONDecodeError):
    gasto = []
    print("criando lista vazia de gasto")

while True:
    try:
        comando = int(input("(1) adicionar\n(2) ler\n(3) deletar\n(4) total\n(5) lucro-gasto\n(6) Quit\n>>> "))
    except (ValueError , UnboundLocalError):
        print("permitido apenas numeros inteiros")
        continue

    if comando == 1:
        try:
            pergunta = int(input("(1) gasto (2) lucro "))
        except (ValueError ,UnboundLocalError):
            print("comando não conhecido")
            continue
        if pergunta == 1:
            task.adicionando_gasto(gasto)
            with open("gastos.json","w",encoding="utf-8") as arquivo:
                json.dump(gasto,arquivo,indent=4)

        elif pergunta == 2:
            task.adicionando_lucro(lucro)
            with open("lucro.json", "w", encoding="utf-8") as arquivo:
                json.dump(lucro, arquivo, indent=4)
        else:
            print("comando não conhecido")

    elif comando == 2:
        try:
            pergunta = int(input("(1) gasto (2) lucro "))
        except (ValueError ,UnboundLocalError):
            print("comando não conhecido")
        if pergunta == 1:
            task.leitura_gasto(gasto)
        elif pergunta == 2:
            task.leitura_gasto(lucro)
    elif comando == 3:
        try:
            pergunta = int(input("(1) gasto (2) lucro "))
        except (ValueError , UnboundLocalError):
            print("comando não conhecido")
        if pergunta == 1:
            task.deletar_produto(gasto)
        elif pergunta == 2:
            task.deletar_produto(lucro)

    elif comando ==4:
        try:
            pergunta = int(input("(1) gasto (2) lucro "))
        except (ValueError , UnboundLocalError):
            print("comando não conhecido")
        if pergunta == 1:
            task.total(gasto)
        elif pergunta == 2:
            task.total(lucro)
    elif comando == 5:
        task.gasto_lucro(lucro,gasto)
    elif comando == 6:
        print("saindo em ...")
        for tempo in range(10,0,-1):
            print(tempo)
            time.sleep(0.3)
        break
    else:
        print("comando não reconhecido")
        continue