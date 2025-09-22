# editoras.py
editoras = []

while True:
    print("\n=== EDITORAS ===")
    print("1. Add | 2. Ver | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        editora = {
            'id': int(input("ID: ")),
            'nome': input("Nome: "),
            'endereco': input("Endereço: "),
            'telefone': input("Telefone: "),
            'email': input("Email: ")
        }
        editoras.append(editora)
        print("✅ Added")
    
    elif op == "2":
        for e in editoras:
            print(f"ID: {e['id']} | Nome: {e['nome']}")
    
    elif op == "0":
        break
