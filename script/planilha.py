import random as rnd
import csv
import itertools as it
from datetime import datetime
import json as js
import pandas as pd
import pprint as pp

fileName = "info.json"

def read_file():
  with open(fileName, "r") as jsonFile:
    jsonObject = js.load(jsonFile)

    semana = jsonObject["semana"]
    horarios = jsonObject["horarios"]
    pessoas = jsonObject["pessoas"]

    return semana, horarios, pessoas

semana, horarios, pessoas = read_file()

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
    "servir": possibilidade
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



def write_row(buffer, writer):
  for row in buffer:
    writer.writerow(row)

def diaDaSemana(dia):
  if (dia != semana[5] or dia != semana[6]):
    return 1
  return 0

def ignoraHorario(eDiaDeSemana, horaCorreta):
  horaDia = horaCorreta == horarios[0]
  horaNoite = horaCorreta == horarios[3]
  if (eDiaDeSemana == 1 and horaDia or horaNoite):
    return 1
  return 0

def validations_scale(dia, horario, frame):

  condicaoDia = frame['dia'] == dia
  eDiaDeSemana = diaDaSemana(frame['dia'])
  condicaoHorario = frame['horario'] == horario
  condicaoServir = frame['servir'] == 1

  horarioDaCertoDaSemana = ignoraHorario(eDiaDeSemana, horario)

  if (condicaoDia and condicaoHorario and condicaoServir):
    return 1, eDiaDeSemana, horarioDaCertoDaSemana
  return 0, eDiaDeSemana, horarioDaCertoDaSemana

def selecionar_pessoa(dataFrame, escala, dia, horario):
  count = 0
  for index, row in dataFrame.iterrows():
    condicoes, eDiaDeSemana, horarioDaCertoDaSemana = validations_scale(dia, horario, row)
    if (horarioDaCertoDaSemana == 0 and eDiaDeSemana == 1):
      break

    if (condicoes == 1 and count < 1 and eDiaDeSemana == 1):
      escala.append(row)
      count += 1
      if (count == 1):
        break

    elif(condicoes == 1 and count < 2 and eDiaDeSemana == 0):
      escala.append(row)
      count += 1
      if (count == 2):
        break
    else:
      if (count < 1 and eDiaDeSemana == 1):
        continue
      elif (count < 2 and eDiaDeSemana == 0):
        continue
      else:
        break

def monta_escala_final(arquivo_escala, semana_dia):
  data = pd.read_csv(arquivo_escala.name)
  escala = []

  with open(f'escala_final-{datetime.timestamp(datetime.now())}.csv', 'w') as arquivo_escala:
    writer = csv.writer(arquivo_escala, delimiter=',')
    for dia, horario in semana_dia:
      selecionar_pessoa(data, escala, dia, horario)
    write_row(escala, writer)



def main():
  lista_membros = monta_disponibilidade()
  escala = monta_escala(lista_membros)
  arquivo_escala = monta_csv(escala)
  monta_escala_final(arquivo_escala, semana_dia)

if __name__ == '__main__':
  main()

