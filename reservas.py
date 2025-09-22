# reservas.py
reservas = []

while True:
    print("\n=== RESERVAS ===")
    print("1. Add | 2. Ver | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        reserva = {
            'id': int(input("ID: ")),
            'obra_id': int(input("ID Obra: ")),
            'usuario_id': int(input("ID Usuário: ")),
            'data_reserva': input("Data Reserva: "),
            'data_expiracao': input("Data Expiração: "),
            'status': input("Status: ")
        }
        reservas.append(reserva)
        print("✅ Added")
    
    elif op == "2":
        for r in reservas:
            print(f"ID: {r['id']} | Obra: {r['obra_id']} | Usuário: {r['usuario_id']}")
    
    elif op == "0":
        break
