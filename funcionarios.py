# funcionarios.py
funcionarios = []

while True:
    print("\n=== FUNCIONÁRIOS ===")
    print("1. Add | 2. Ver | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        func = {
            'id': int(input("ID: ")),
            'nome': input("Nome: "),
            'email': input("Email: "),
            'telefone': input("Telefone: "),
            'cargo': input("Cargo: ")
        }
        funcionarios.append(func)
        print("✅ Added")
    
    elif op == "2":
        for f in funcionarios:
            print(f"ID: {f['id']} | Nome: {f['nome']} | Cargo: {f['cargo']}")
    
    elif op == "0":
        break
