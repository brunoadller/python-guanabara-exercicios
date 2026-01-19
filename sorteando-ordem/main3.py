import pandas as pd
import random

planilha_alunos = pd.read_csv('sorteando-ordem/listaalunos.csv', sep=';')
lista_nova = planilha_alunos['NOME']
print(f'O aluno sorteado foi: {random.choice(lista_nova)}')