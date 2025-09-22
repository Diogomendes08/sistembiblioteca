# emprestimos.py
emprestimos = []

while True:
    print("\n=== EMPRÉSTIMOS ===")
    print("1. Add | 2. Ver | 0. Voltar")
    op = input("Opção: ")
    
    if op == "1":
        emp = {
            'id': int(input("ID: ")),
            'user_id': int(input("ID User: ")),
            'obra_id': int(input("ID Obra: ")),
            'data': input("Data: ")
        }
        emprestimos.append(emp)
        print("✅ Added")
    
    elif op == "2":
        for e in emprestimos:
            print(f"ID: {e['id']} | User: {e['user_id']} | Obra: {e['obra_id']}")
    
    elif op == "0":
        break
