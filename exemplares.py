exemplares = []

while True:
    print("\n=== EXEMPLARES ===")
    print("1. Add | 2. Ver | 3. Detalhes | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        exemplar = {
            'id': int(input("ID: ")),
            'obra_id': int(input("ID Obra: ")),
            'codigo_barras': input("Código de Barras: "),
            'data_aquisicao': input("Data Aquisição (DD/MM/AAAA): "),
            'localizacao': input("Localização (ex: Prateleira A-12): "),
            'estado_conservacao': input("Estado Conservação (1-Ótimo / 2-Bom / 3-Regular / 4-Ruim): "),
            'disponivel': input("Disponível (S/N): ").upper() == 'S',
            'observacoes': input("Observações: ")[:300]
        }
        exemplares.append(exemplar)
        print("✅ Exemplar cadastrado!")
    
    elif op == "2":
        print("\n--- Lista de Exemplares ---")
        for e in exemplares:
            disp = "Sim" if e['disponivel'] else "Não"
            print(f"ID: {e['id']} | Obra: {e['obra_id']} | Código: {e['codigo_barras']} | Disp: {disp}")
    
    elif op == "3":
        ex_id = int(input("ID do Exemplar: "))
        for e in exemplares:
            if e['id'] == ex_id:
                print(f"\n--- Detalhes do Exemplar {ex_id} ---")
                print(f"Obra ID: {e['obra_id']}")
                print(f"Código Barras: {e['codigo_barras']}")
                print(f"Data Aquisição: {e['data_aquisicao']}")
                print(f"Localização: {e['localizacao']}")
                print(f"Estado Conservação: {e['estado_conservacao']}")
                print(f"Disponível: {'Sim' if e['disponivel'] else 'Não'}")
                print(f"Observações: {e['observacoes']}")
                break
        else:
            print("❌ Exemplar não encontrado!")
    
    elif op == "0":
        break
