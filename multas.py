# multas.py
multas = []

while True:
    print("\n=== MULTAS ===")
    print("1. Add | 2. Ver | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        multa = {
            'id': int(input("ID: ")),
            'usuario_id': int(input("ID Usuário: ")),
            'emprestimo_id': int(input("ID Empréstimo: ")),
            'valor': input("Valor: "),
            'data_multa': input("Data Multa: "),
            'data_pagamento': input("Data Pagamento: "),
            'status': input("Status: ")
        }
        multas.append(multa)
        print("✅ Added")
    
    elif op == "2":
        for m in multas:
            print(f"ID: {m['id']} | Usuário: {m['usuario_id']} | Valor: {m['valor']}")
    
    elif op == "0":
        break
