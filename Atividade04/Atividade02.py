# Registro de notas de alunos e cálculo da média da turma

notas = []  # lista para armazenar as notas

print("=== Registro de Notas da Turma ===")

while True:
    try:
        nota = float(
            input("Digite a nota do aluno (ou 'sair' para finalizar): "))
        if 0 <= nota <= 10:  # verifica se a nota está no intervalo válido
            notas.append(nota)
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
    except ValueError:
        # quando o usuário digitar "sair", o loop termina
        break

# Verifica se foram inseridas notas
if len(notas) == 0:
    print("Nenhuma nota registrada.")
else:
    media = sum(notas) / len(notas)  # calcula a média
    print(f"\nNotas registradas: {notas}")
    print(f"Média da turma: {media:.2f}")
