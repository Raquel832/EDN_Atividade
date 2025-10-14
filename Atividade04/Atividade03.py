# Verificador de senha
# Critérios: pelo menos 8 caracteres e pelo menos 1 número

senha = input("Digite sua senha: ")

# Verifica o tamanho
tamanho_ok = len(senha) >= 8

# Verifica se contém pelo menos um número
tem_numero = any(char.isdigit() for char in senha)

# Resultado da validação
if tamanho_ok and tem_numero:
    print("Senha válida ✅")
else:
    print("Senha inválida ❌")
    if not tamanho_ok:
        print("- A senha deve ter pelo menos 8 caracteres")
    if not tem_numero:
        print("- A senha deve conter pelo menos um número")
