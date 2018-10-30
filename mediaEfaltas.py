nome = input('Digite o nome do aluno: ')
notaProva1 = float(input('Digite a nota da prova 1: '))
notaProva2 = float(input('Digite a nota da prova 2: '))
faltas = int(input('Digite o total de faltas: '))

media = (notaProva1+notaProva2)/2
assid = (20-faltas)/20

if media >= 6 and assid >= 0.7:
    resultado = 'Aprovado'

elif media < 6 and assid < 0.7:
    resultado = 'Reprovado por média e faltas'

elif media < 6:
    resultado = 'Reprovado por média'

elif assid < 0.7:
    resultado = 'Reprovado por faltas'

else:
    print('Erro')

print('Nome:',nome)
print('Media:',media)
print('Assiduidade:',str(assid*100)+'%')
print('Resultado:',resultado)
    
