# autores.py
autores = []

while True:
    print("\n=== AUTORES ===")
    print("1. Add | 2. Ver | 3. Detalhes | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        autor = {
            'id': int(input("ID: ")),
            'nome': input("Nome completo: "),
            'nacionalidade': input("Nacionalidade: "),
            'data_nascimento': input("Data Nascimento (DD/MM/AAAA): "),
            'data_falecimento': input("Data Falecimento (DD/MM/AAAA - Enter se vivo): "),
            'biografia': input("Biografia (máx 500 chars): ")[:500]
        }
        autores.append(autor)
        print("✅ Autor cadastrado!")
    
    elif op == "2":
        print("\n--- Lista de Autores ---")
        for a in autores:
            print(f"ID: {a['id']} | Nome: {a['nome']} | Nacionalidade: {a['nacionalidade']}")
    
    elif op == "3":
        autor_id = int(input("ID do Autor: "))
        for a in autores:
            if a['id'] == autor_id:
                print(f"\n--- Detalhes do Autor {autor_id} ---")
                print(f"Nome: {a['nome']}")
                print(f"Nacionalidade: {a['nacionalidade']}")
                print(f"Data Nascimento: {a['data_nascimento']}")
                print(f"Data Falecimento: {a['data_falecimento'] or 'Ainda vivo'}")
                print(f"Biografia: {a['biografia'][:100]}..." if len(a['biografia']) > 100 else f"Biografia: {a['biografia']}")
                break
        else:
            print("❌ Autor não encontrado!")
    
    elif op == "0":
        break
