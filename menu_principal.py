# menu_principal.py
while True:
    print("\n=== SISTEMA BIBLIOTECA ===")
    print("1. Usuários")
    print("2. Obras") 
    print("3. Empréstimos")
    print("4. Autores")
    print("0. Sair")
    
    op = input("Opção: ")
    
    if op == "1":
        import usuarios
    elif op == "2":
        import obras
    elif op == "3":
        import emprestimos
    elif op == "4":
        import autores
    elif op == "0":
        break
