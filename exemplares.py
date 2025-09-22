# exemplares.py
exemplares = []

while True:
    print("\n=== EXEMPLARES ===")
    print("1. Add | 2. Ver | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        exemplar = {
            'id': int(input("ID: ")),
            'obra_id': int(input("ID Obra: ")),
            'codigo_barras': input("Código de Barras: "),
            'data_aquisicao': input("Data Aquisição: "),
            'localizacao': input("Localização: "),
            'estado_conservacao': input("Estado Conservação: "),
            'disponivel': input("Disponível (S/N): ")
        }
        exemplares.append(exemplar)
        print("✅ Added")
    
    elif op == "2":
        for e in exemplares:
            print(f"ID: {e['id']} | Obra: {e['obra_id']} | Código: {e['codigo_barras']}")
    
    elif op == "0":
        break
