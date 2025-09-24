editoras = []

while True:
    print("\n=== EDITORAS ===")
    print("1. Add | 2. Ver | 3. Detalhes | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        editora = {
            'id': int(input("ID: ")),
            'nome': input("Nome: "),
            'endereco': input("Endereço completo: "),
            'telefone': input("Telefone: "),
            'email': input("Email: "),
            'contato': input("Nome do contato: "),
            'observacoes': input("Observações: ")[:300]
        }
        editoras.append(editora)
        print("✅ Editora cadastrada!")
    
    elif op == "2":
        print("\n--- Lista de Editoras ---")
        for e in editoras:
            print(f"ID: {e['id']} | Nome: {e['nome']} | Telefone: {e['telefone']}")
    
    elif op == "3":
        ed_id = int(input("ID da Editora: "))
        for e in editoras:
            if e['id'] == ed_id:
                print(f"\n--- Detalhes da Editora {ed_id} ---")
                print(f"Nome: {e['nome']}")
                print(f"Endereço: {e['endereco']}")
                print(f"Telefone: {e['telefone']}")
                print(f"Email: {e['email']}")
                print(f"Contato: {e['contato']}")
                print(f"Observações: {e['observacoes']}")
                break
        else:
            print("❌ Editora não encontrada!")
    
    elif op == "0":
        break
