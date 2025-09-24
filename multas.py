multas = []

while True:
    print("\n=== MULTAS ===")
    print("1. Add | 2. Ver | 3. Detalhes | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        multa = {
            'id': int(input("ID: ")),
            'usuario_id': int(input("ID Usuário: ")),
            'emprestimo_id': int(input("ID Empréstimo: ")),
            'valor': float(input("Valor (R$): ")),
            'data_multa': input("Data Multa (DD/MM/AAAA): "),
            'data_pagamento': input("Data Pagamento (DD/MM/AAAA - Enter se não pago): "),
            'status': input("Status (1-Pendente / 2-Pago / 3-Cancelado): "),
            'motivo': input("Motivo da multa: ")[:200]
        }
        multas.append(multa)
        print("✅ Multa registrada!")
    
    elif op == "2":
        print("\n--- Lista de Multas ---")
        for m in multas:
            status_text = {1: "Pendente", 2: "Pago", 3: "Cancelado"}.get(int(m['status']), "Desconhecido")
            print(f"ID: {m['id']} | Usuário: {m['usuario_id']} | Valor: R$ {m['valor']:.2f} | Status: {status_text}")
    
    elif op == "3":
        multa_id = int(input("ID da Multa: "))
        for m in multas:
            if m['id'] == multa_id:
                print(f"\n--- Detalhes da Multa {multa_id} ---")
                print(f"Usuário ID: {m['usuario_id']}")
                print(f"Empréstimo ID: {m['emprestimo_id']}")
                print(f"Valor: R$ {m['valor']:.2f}")
                print(f"Data Multa: {m['data_multa']}")
                print(f"Data Pagamento: {m['data_pagamento'] or 'Não pago'}")
                print(f"Status: {m['status']}")
                print(f"Motivo: {m['motivo']}")
                break
        else:
            print("❌ Multa não encontrada!")
    
    elif op == "0":
        break
