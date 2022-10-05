from FileService import *
from Person import *
from Service import *
import random as rnd
from printer import *

def getJsonObject(instance):
  fileName = 'info.json'
  jsonObject = instance.readFile(fileName)

  return jsonObject

def setAvailability(person, dataframe, day, hour):
  printer('*'*60)
  printer(f'{person.name}')
  printer(f'dia da semana: {day}')
  printer(f'horario para o dia - {day}: {hour}')
  printer('*'*60)
  printer('[0] Não / [1] Sim')

  awnser = int(input())
  while (awnser != 0 or awnser != 1):
    if (awnser == 0):
      print(f'não disponivel para esse dia - {day} :: {hour}')
      return False
    elif (awnser == 1):
      printer(f'horario para o dia - {day}: {hour}')
      person.setAvailability(day, hour)

      return True
    else:
      printer(f'Opção inválida!')

def initPerson(dataframe):
  persons = []
  isAvailabil = bool
  for person in dataframe['persons']:
    personObject = Person(person, 0)

    for day in dataframe['week']:
      for hour in dataframe['hours']:
        ignoreHour = ignoreInconsistentHour(dataframe, day, hour)
        if (ignoreHour):
          continue
        isAvailabil = setAvailability(personObject, dataframe, day, hour)
    persons.append(personObject)

  return persons

def ignoreInconsistentHour(dataframe, day, hour):
  weekendDay, notHourWeekDay = validateInfo(dataframe, day, hour)
  if (weekendDay):
    return True
  else:
    if(notHourWeekDay):
      return True
    return False

def validateInfo(dataframe, day, hour):
  # if weekend true then notHourWeekDay ignore

  weekendDay = (day == dataframe['week'][5] or day == dataframe['week'][6]) # week = false
  notHourWeekDay = (hour == dataframe['hours'][1] or hour == dataframe['hours'][2]) # if week = false

  return weekendDay, notHourWeekDay

def getAllAvailabilityForDay(persons, day, hour):
  availabilityForDay = []
  for person in persons:
    for availabil in person.availability:
      if (availabil['day'] == day and availabil['hour'] == hour):
        availabilityForDay.append(person)
        break

  return availabilityForDay

def gonnaBeScaled(person):
  return person.serviceAmount <= 2

def incrementServicePerson(person):
  person.setServiceAmount()

def formatPersonData(instance, service):
  person = {
    'name': instance.name,
    'day': service.day,
    'hour': service.hour,
    'amount': instance.serviceAmount
  }
  return person

def subscribePerson(scale, person, service):
  incrementServicePerson(person)
  service.incrementServiceAmount()
  formatedPerson = formatPersonData(person, service)
  scale.append(formatedPerson)

def getServiceForDay(availabilityForDay, weekendDay, notHourWeekDay, service, scale):
  for person in availabilityForDay:
    gonnaBe = gonnaBeScaled(person)
    whoWill = rnd.randint(0, len(availabilityForDay) - 1)
    instance = availabilityForDay[whoWill]
    if (not weekendDay and not notHourWeekDay and service.amount < 1):
      if (gonnaBe):
        subscribePerson(scale, instance, service)

    elif (weekendDay and service.amount < 2):
      if (gonnaBe):
        subscribePerson(scale, person, service)

def validateServiceByData(day, hour):
  weekDay = (day != 'Sábado' or day != 'Domingo')
  invalidHourToWeek = (hour == '10:00' or hour == '17:00')

  return weekDay, invalidHourToWeek

def createService(dataframe):
  services = []
  for day in dataframe['week']:
    for hour in dataframe['hours']:
      weekDay, invalidHourToWeek = validateServiceByData(day, hour)
      if (weekDay and invalidHourToWeek):
        continue
      elif (not weekDay and not invalidHourToWeek):
        serviceInstance = Service(day, hour)
        services.append(serviceInstance)
      else:
        serviceInstance = Service(day, hour)
        services.append(serviceInstance)

  return services


def mountScale(persons, dataframe):
  scale = []

  services = createService(dataframe)
  for service in services:
    weekendDay, notHourWeekDay = validateInfo(dataframe, service.day, service.hour)
    availabilityForDay = getAllAvailabilityForDay(persons, service.day, service.hour)
    getServiceForDay(availabilityForDay, weekendDay, notHourWeekDay, service, scale)
  return scale

def main():
  fileService = FileService()
  dataframe = getJsonObject(fileService)
  persons = initPerson(dataframe)
  scale = mountScale(persons, dataframe)
  fileService.writeCsv('escala_semana', scale)


if __name__ == '__main__':
  main()