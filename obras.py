# obras.py
obras = []

while True:
    print("\n=== OBRAS ===")
    print("1. Add | 2. Ver | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        obra = {
            'id': int(input("ID: ")),
            'titulo': input("Título: "),
            'autor': input("Autor: "),
            'ano': int(input("Ano: "))
        }
        obras.append(obra)
        print("✅ Added")
    
    elif op == "2":
        for o in obras:
            print(f"ID: {o['id']} | Título: {o['titulo']}")
    
    elif op == "0":
        break
