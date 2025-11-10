''' Exercício: Gerenciador de alunos
Descrição:
Crie um programa que gerencia uma lista de alunos em uma turma.
O programa deve eprmitir ao usuário inserir nomes,
Organizar e manipular a lista usando os métodos estudados.

Passo a Passo para resolver os exercícios:
1.Peça ao usuário que digite os nomes dos alunos separados por vírgula.
2. Mostre:
    -Quantos alunos foram cadastrados
    - O nome do primeiro e do último aluno da lista
3. Peça ao usuário para adicionar mais um aluno no final da lista.
4. Peça ao usuário para adicionar um aluno no início da lista.
5. Peça ao usuário para remover um aluno pelo nome.
6. Mostre a lista de alunos em ordem alfabética.
7. Inverta a ordem da lista e mostre o resultado.
8. Faça uma cópia da lista original e limpe a original.
9. Mostre ambas as listas para o usuário.

'''


nomes = input("Digite o nome dos alunos(separe por vírgula):  " )
alunos = nomes.split(',')


print("\nA quantidade de alunos cadastrados é",len(alunos))
print(f'O primeiro aluno cadastrado é {alunos[0]} e o último aluno cadastrado é {alunos[-1]}')

add_aluno = input("\nAdicione um aluno ao final da lista:")
alunos.append(add_aluno)
add_aluno2 = input("Adicione um aluno ao início da lista: ")
alunos.insert(0,add_aluno2)
del_aluno = input("Digite um aluno para remover: ")
alunos.remove(del_aluno)
print(f'A lista de alunos em ordem alfabética é {alunos.sort()}')
print(f'A ordem da lista invertida é: {alunos.reverse()}')
copia_alunos = alunos.copy()
alunos.clear()
print(f'Primeira lista:{alunos} e a Segunda lista: {copia_alunos}')