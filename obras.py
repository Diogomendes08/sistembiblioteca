obras = []

while True:
    print("\n=== OBRAS ===")
    print("1. Add | 2. Ver | 3. Detalhes | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        obra = {
            'id': int(input("ID: ")),
            'titulo': input("Título: "),
            'isbn': input("ISBN (13 dígitos): "),
            'ano_publicacao': int(input("Ano Publicação: ")),
            'edicao': input("Edição: "),
            'editora_id': int(input("ID Editora: ")),
            'sinopse': input("Sinopse (máx 1000 chars): ")[:1000]
        }
        obras.append(obra)
        print("✅ Obra cadastrada!")
    
    elif op == "2":
        print("\n--- Lista de Obras ---")
        for o in obras:
            print(f"ID: {o['id']} | Título: {o['titulo'][:30]}... | Ano: {o['ano_publicacao']}")
    
    elif op == "3":
        obra_id = int(input("ID da Obra: "))
        for o in obras:
            if o['id'] == obra_id:
                print(f"\n--- Detalhes da Obra {obra_id} ---")
                print(f"Título: {o['titulo']}")
                print(f"ISBN: {o['isbn']}")
                print(f"Ano Publicação: {o['ano_publicacao']}")
                print(f"Edição: {o['edicao']}")
                print(f"Editora ID: {o['editora_id']}")
                print(f"Sinopse: {o['sinopse'][:150]}..." if len(o['sinopse']) > 150 else f"Sinopse: {o['sinopse']}")
                break
        else:
            print("❌ Obra não encontrada!")
    
    elif op == "0":
        break
