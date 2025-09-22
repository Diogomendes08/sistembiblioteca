# autores.py
autores = []

while True:
    print("\n=== AUTORES ===")
    print("1. Add | 2. Ver | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        autor = {
            'id': int(input("ID: ")),
            'nome': input("Nome: "),
            'nacionalidade': input("Nacionalidade: ")
        }
        autores.append(autor)
        print("✅ Added")
    
    elif op == "2":
        for a in autores:
            print(f"ID: {a['id']} | Nome: {a['nome']}")
    
    elif op == "0":
        break
