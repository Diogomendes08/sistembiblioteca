funcionarios = []

while True:
    print("\n=== FUNCIONÁRIOS ===")
    print("1. Add | 2. Ver | 3. Detalhes | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        func = {
            'id': int(input("ID: ")),
            'nome': input("Nome completo: "),
            'email': input("Email: "),
            'telefone': input("Telefone: "),
            'cargo': input("Cargo: "),
            'data_admissao': input("Data Admissão (DD/MM/AAAA): "),
            'salario': float(input("Salário (R$): ")),
            'observacoes': input("Observações: ")[:200]
        }
        funcionarios.append(func)
        print("✅ Funcionário cadastrado!")
    
    elif op == "2":
        print("\n--- Lista de Funcionários ---")
        for f in funcionarios:
            print(f"ID: {f['id']} | Nome: {f['nome']} | Cargo: {f['cargo']} | Salário: R$ {f['salario']:.2f}")
    
    elif op == "3":
        func_id = int(input("ID do Funcionário: "))
        for f in funcionarios:
            if f['id'] == func_id:
                print(f"\n--- Detalhes do Funcionário {func_id} ---")
                print(f"Nome: {f['nome']}")
                print(f"Email: {f['email']}")
                print(f"Telefone: {f['telefone']}")
                print(f"Cargo: {f['cargo']}")
                print(f"Data Admissão: {f['data_admissao']}")
                print(f"Salário: R$ {f['salario']:.2f}")
                print(f"Observações: {f['observacoes']}")
                break
        else:
            print("❌ Funcionário não encontrado!")
    
    elif op == "0":
        break
