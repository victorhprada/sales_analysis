from random import randint


estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
print(estudantes)

def gera_codigo():
    return str(randint(0, 999))

codigo_estudantes = []

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))

print(codigo_estudantes)

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list=[0]) -> float:
    
    calculo = sum(lista) / len(lista)

    return calculo

medias = [round(media(nota), 1) for nota in notas]
print(medias)

nomes = [nome[0] for nome in codigo_estudantes]
print(nomes)

estudante_media = list(zip(nomes, medias))
print(estudante_media)

candidatos = [estudante_media[0] for estudante_media in estudante_media if estudante_media[1] >= 8.0 ]
print(candidatos)

situacao = ["Aprovado(a)" if media >= 6 else "Reprovado(a)" for media in medias]
print(situacao)

cadastro = [x for x in [nomes, notas, medias, situacao]]
print(cadastro)

lista_completa = [nomes, notas, medias, situacao]
print(lista_completa)