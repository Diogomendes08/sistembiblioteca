# usuarios.py
usuarios = []

while True:
    print("\n=== USUÁRIOS ===")
    print("1. Add | 2. Ver | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        user = {
            'id': int(input("ID: ")),
            'nome': input("Nome: "),
            'email': input("Email: "),
            'telefone': input("Telefone: ")
        }
        usuarios.append(user)
        print("✅ Added")
    
    elif op == "2":
        for u in usuarios:
            print(f"ID: {u['id']} | Nome: {u['nome']}")
    
    elif op == "0":
        break
