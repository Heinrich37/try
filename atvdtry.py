






clientes    = []
passagens   = []
avioes      = []
tripulacoes = []

while True:
    print("\n=== SISTEMA DE VENDA DE PASSAGEM AÉREA ===")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Passagem")
    print("3 - Cadastrar Avião")
    print("4 - Cadastrar Tripulação")
    print("5 - Listar Todos os Cadastros")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":

        while True:
            nome       = input("Nome: ")
            sobrenome  = input("Sobrenome: ")
            rg         = input("RG: ")
            cpf        = input("CPF: ")
            endereco   = input("Endereço: ")
            fone       = input("Telefone: ")
            idade_str  = input("Idade: ")
            try:
                idade = int(idade_str)
                break
            except ValueError:
                print("Idade inválida! Digite um número inteiro para Idade.")

        cliente = {
            "nome": nome,
            "sobrenome": sobrenome,
            "rg": rg,
            "cpf": cpf,
            "endereco": endereco,
            "fone": fone,
            "idade": idade
        }
        clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    elif escolha == "2":

        destino = input("Destino: ")
        origem  = input("Origem: ")

        while True:
            duracao_str = input("Duração (em horas): ")
            try:
                duracao = float(duracao_str)
                break
            except ValueError:
                print("Duração inválida! Digite um número (ex: 2.5) para horas.")

        while True:
            valor_str = input("Valor da Passagem (R$): ")
            try:
                valor = float(valor_str)
                break
            except ValueError:
                print("Valor inválido! Digite um número (ex: 150.75) para valor.")

        desconto = 5.0

        passagem = {
            "destino": destino,
            "origem": origem,
            "duracao": duracao,
            "valor": valor,
            "desconto": desconto
        }
        passagens.append(passagem)
        print("Passagem cadastrada com sucesso!")

    elif escolha == "3":

        modelo = input("Modelo: ")

        while True:
            ano_str = input("Ano (ex: 2020): ")
            try:
                ano = int(ano_str)
                break
            except ValueError:
                print("Ano inválido! Digite um número inteiro para o ano.")

        while True:
            horas_str = input("Horas de Voo: ")
            try:
                horas_voo = float(horas_str)
                break
            except ValueError:
                print("Horas de voo inválido! Digite um número (ex: 1500.5).")

        cor = input("Cor: ")

        while True:
            qtd_str = input("Quantidade de Passageiros: ")
            try:
                qtd_passageiros = int(qtd_str)
                break
            except ValueError:
                print("Quantidade inválida! Digite um número inteiro.")

        aviao = {
            "modelo": modelo,
            "ano": ano,
            "horas_voo": horas_voo,
            "cor": cor,
            "qtd_passageiros": qtd_passageiros
        }
        avioes.append(aviao)
        print("Avião cadastrado com sucesso!")

    elif escolha == "4":

        nome_trip       = input("Nome: ")
        descricao_cargo = input("Descrição do Cargo: ")

        while True:
            idade_str = input("Idade: ")
            try:
                idade_trip = int(idade_str)
                break
            except ValueError:
                print("Idade inválida! Digite um número inteiro para idade.")

        data_admissao = input("Data de Admissão (dd/mm/aaaa): ")
        fone_trip     = input("Telefone: ")

        tripulacao = {
            "nome": nome_trip,
            "descricao_cargo": descricao_cargo,
            "idade": idade_trip,
            "data_admissao": data_admissao,
            "fone": fone_trip
        }
        tripulacoes.append(tripulacao)  
        print("Tripulação cadastrada com sucesso!")

    elif escolha == "5":
       

        print("\n--- Clientes ---")
        for c in clientes:
            print(f"Nome: {c['nome']} {c['sobrenome']}, RG: {c['rg']}, CPF: {c['cpf']}, "
                  f"Endereço: {c['endereco']}, Telefone: {c['fone']}, Idade: {c['idade']}")  

        print("\n--- Passagens ---")
        for p in passagens:
            valor_final = p['valor'] * (1 - p['desconto']/100) 
            print(f"Destino: {p['destino']}, Origem: {p['origem']}, "
                  f"Duração: {p['duracao']}h, Valor: R${p['valor']:.2f}, "
                  f"Desconto: {p['desconto']}%, Valor c/ desconto: R${valor_final:.2f}")

        print("\n--- Aviões ---")
        for a in avioes:
            print(f"Modelo: {a['modelo']}, Ano: {a['ano']}, Horas de Voo: {a['horas_voo']:.1f}, "
                  f"Cor: {a['cor']}, Capacidade: {a['qtd_passageiros']} passageiros") 

        print("\n--- Tripulação ---")
        for t in tripulacoes:
            print(f"Nome: {t['nome']}, Cargo: {t['descricao_cargo']}, Idade: {t['idade']}, "
                  f"Data Admissão: {t['data_admissao']}, Telefone: {t['fone']}")  

    elif escolha == "0":
        print("Saindo do sistema. Até logo!") 
        break

    else:
        print("Opção inválida! Tente novamente.") 
