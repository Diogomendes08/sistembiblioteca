reservas = []

while True:
    print("\n=== RESERVAS ===")
    print("1. Add | 2. Ver | 3. Detalhes | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        reserva = {
            'id': int(input("ID: ")),
            'obra_id': int(input("ID Obra: ")),
            'usuario_id': int(input("ID Usuário: ")),
            'data_reserva': input("Data Reserva (DD/MM/AAAA): "),
            'data_expiracao': input("Data Expiração (DD/MM/AAAA): "),
            'status': input("Status (1-Ativa / 2-Cancelada / 3-Concluída): "),
            'observacoes': input("Observações: ")[:200]
        }
        reservas.append(reserva)
        print("✅ Reserva cadastrada!")
    
    elif op == "2":
        print("\n--- Lista de Reservas ---")
        for r in reservas:
            status_text = {1: "Ativa", 2: "Cancelada", 3: "Concluída"}.get(int(r['status']), "Desconhecido")
            print(f"ID: {r['id']} | Obra: {r['obra_id']} | Usuário: {r['usuario_id']} | Status: {status_text}")
    
    elif op == "3":
        res_id = int(input("ID da Reserva: "))
        for r in reservas:
            if r['id'] == res_id:
                print(f"\n--- Detalhes da Reserva {res_id} ---")
                print(f"Obra ID: {r['obra_id']}")
                print(f"Usuário ID: {r['usuario_id']}")
                print(f"Data Reserva: {r['data_reserva']}")
                print(f"Data Expiração: {r['data_expiracao']}")
                print(f"Status: {r['status']}")
                print(f"Observações: {r['observacoes']}")
                break
        else:
            print("❌ Reserva não encontrada!")
    
    elif op == "0":
        break
