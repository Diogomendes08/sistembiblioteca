emprestimos = []

while True:
    print("\n=== EMPRÉSTIMOS ===")
    print("1. Add | 2. Ver | 3. Detalhes | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        emp = {
            'id': int(input("ID: ")),
            'exemplar_id': int(input("ID Exemplar: ")),
            'usuario_id': int(input("ID Usuário: ")),
            'data_emprestimo': input("Data Empréstimo (DD/MM/AAAA): "),
            'data_devolucao_prevista': input("Data Devolução Prevista (DD/MM/AAAA): "),
            'data_devolucao_efetiva': input("Data Devolução Efetiva (DD/MM/AAAA - Enter se não devolvido): "),
            'status': int(input("Status (1-Ativo / 2-Devolvido / 3-Atrasado): ")),
            'multa': float(input("Multa (R$): ") or "0")
        }
        emprestimos.append(emp)
        print("✅ Empréstimo registrado!")
    
    elif op == "2":
        print("\n--- Lista de Empréstimos ---")
        for e in emprestimos:
            status_text = {1: "Ativo", 2: "Devolvido", 3: "Atrasado"}.get(e['status'], "Desconhecido")
            print(f"ID: {e['id']} | Exemplar: {e['exemplar_id']} | Usuário: {e['usuario_id']} | Status: {status_text}")
    
    elif op == "3":
        emp_id = int(input("ID do Empréstimo: "))
        for e in emprestimos:
            if e['id'] == emp_id:
                print(f"\n--- Detalhes do Empréstimo {emp_id} ---")
                print(f"Exemplar ID: {e['exemplar_id']}")
                print(f"Usuário ID: {e['usuario_id']}")
                print(f"Data Empréstimo: {e['data_emprestimo']}")
                print(f"Data Devolução Prevista: {e['data_devolucao_prevista']}")
                print(f"Data Devolução Efetiva: {e['data_devolucao_efetiva']}")
                print(f"Status: {e['status']}")
                print(f"Multa: R$ {e['multa']:.2f}")
                break
        else:
            print("❌ Empréstimo não encontrado!")
    
    elif op == "0":
        break
