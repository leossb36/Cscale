import random as rnd
import csv
import pprint as pp
import itertools as it
from datetime import datetime

semana = ("[0] - Segunda", "[1] - Terça", "[2] - Quarta", "[3] - Quinta", "[4] - Sexta", "[5] - Sábado", "[6] - Domingo")
horarios = ("[0] - 7:00", "[1] - 10:00", "[2] - 17:00", "[3] - 19:30")
pessoas = ["Leonardo Barreiros", "Erick Santos", "Eric Gomes", "Vinicius Lopes", "Luis Henrique", "Pedro Victor", "João Paulo", "Gabriel Guilherme", "Gabriel de sousa"]


def create_tuples(semana, horarios):
  permutacao = list(it.product(semana, horarios))
  return permutacao

semana_dia = create_tuples(semana, horarios)

def seleciona_dia():
  quantidade_dias = int(input('Quantidade de [momentos] disponiveis: '))

  print("Selecione os dias da semana disponível")
  pp.pprint(semana)
  dias_selecionados = list()

  index = 0
  while index < quantidade_dias:
    dia = int(input())
    dias_selecionados.append(semana[dia])
    index += 1

  return dias_selecionados

def seleciona_horario(dias_selecionados):
  horario_disponivel = dict()
  lista_de_disponibilidade = list()

  print("Selecione os horarios disponíveis para cada dia: ")
  pp.pprint(horarios)

  index = 0
  while index < len(dias_selecionados):
    pp.pprint(f'Horário para: {dias_selecionados[index]}')
    horario = int(input())
    horario_disponivel = {
        "dia": dias_selecionados[index],
        "horario": horarios[horario]
    }
    lista_de_disponibilidade.append(horario_disponivel)
    index += 1

  return lista_de_disponibilidade

def monta_disponibilidade():
  lista_membros = list()

  for membro in range(0, len(pessoas)):
    print(f'Nome: {pessoas[membro]}')
    dias_selecionados = seleciona_dia()
    horarios_selecionados = seleciona_horario(dias_selecionados)

    membro_obj = {
        "nome": pessoas[membro],
        "possibilidades": horarios_selecionados
    }

    lista_membros.append(membro_obj)
    pp.pprint(membro_obj)

  return lista_membros
  # pp.pprint(lista_membros)

def vai_servir(nome, dia, horario):
  possibilidade = rnd.randint(0,1)

  obj_possibilidade = {
    "nome": nome,
    "dia": dia,
    "horario": horario,
    "vai_servir": possibilidade
  }

  return obj_possibilidade

def verifica_disponibilidade(lista_membros, dia_semana, horario_missa, escala):
  for membro in lista_membros:
    for possibilidade in membro["possibilidades"]:
      if possibilidade["dia"] == dia_semana and possibilidade["horario"] == horario_missa:
        disponibilidade = vai_servir(membro["nome"], dia_semana, horario_missa)
        escala.append(disponibilidade)

  return escala

def monta_escala(lista_membros):
  escala = list()
  for dia, horario in semana_dia:
    verifica_disponibilidade(lista_membros, dia, horario, escala)

  return escala

def monta_csv(lista_membros):
  with open(f'escala_da_semana-{datetime.timestamp(datetime.now())}.csv', 'w') as arquivo_escala:
    writer = csv.DictWriter(arquivo_escala, lista_membros[0].keys())
    writer.writeheader()
    for membro in lista_membros:
      writer.writerow(membro)


def main():
  lista_membros = monta_disponibilidade()
  escala_final = monta_escala(lista_membros)
  monta_csv(escala_final)

if __name__ == '__main__':
  main()

