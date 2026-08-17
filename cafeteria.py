produtos = []
pedidos = []

while True:
    print("\n--- ☕ SISTEMA DE CAFETERIA---")
    print("1. Cadastrar Produtos")
    print("2. Registrar Pedidos")
    print("3. Calcular Total de Vendas")
    print("4. Sair")
    
    opcao = input("Escolha uma opção(1-4): ")
    
    if opcao =="1":
        print("\n--- CADASTRO DE PRODUTO ---")
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto (R$): "))
        
        produto = {"id": len(produtos) + 1, "nome": nome, "preco": preco}
        produtos.append(produto)
        print(f"✅ Produto '{nome}' cadastrado com sucesso!")
        
    elif opcao == "2":
        print("\n--- REGISTRAR PEDIDO ---")
        if not produtos:
            print("❌ Nenhum produto cadastrado ainda!")
        else:
            print("Produto disponíveis: ")
            for p in produtos:
                print(f"[{p['id']}] {p['nome']} - R$ {p['preco']:.2f}")
                
            id_prod = int(input("Digite o ID do produto desejado: "))
            
            produto_selecionado = None 
            for p in produtos:
                if p["id"] == id_prod:
                    produto_selecionado = p
                    
            if produto_selecionado:
                qtd = int(input(f"Quantidade de '{produto_selecionado['nome']}':"))
                subtotal = produto_selecionado["preco"] * qtd
                
                pedidos.append({
                    "produto": produto_selecionado["nome"],
                    "quantidade": qtd,
                    "subtotal": subtotal
                })
                print(f"✅ Pedido registrado! Subtotal: R$ {subtotal:.2f}")
            else:
                print("❌ Produto não encontrado!")
                
    elif opcao == "3":
        print("\n--- RELATÓRIO DE VENDAS ---")
        if not pedidos:
            print("Nenhuma venda registrada até o momento.")
        else:
            total_vendas = 0
            print("Pedidos realizados:")
            for item in pedidos:
                print(f"- {item['quantidade']}x {item['produto']} = R$ {item['subtotal']:.2f}")
                total_vendas += item["subtotal"]
            
            print(f"\n💰 VALOR TOTAL DE VENDAS: R$ {total_vendas:.2f}")
   
    elif opcao == "4":
        print("Saindo do sistema... Até Logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
        
        