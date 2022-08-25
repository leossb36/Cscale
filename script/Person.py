from Service import *

class Person:
  def __init__(self, name: str, serviceAmount: int):
    self.name =  name
    self.serviceAmount = serviceAmount
    self.availability = []
    self.service = []

  def setAvailability(self, day, hour):
    self.availability.append(
      {
        'day': day,
        'hour': hour
      }
    )

  def setServiceAmount(self):
    self.serviceAmount = self.serviceAmount + 1

  def getServiceInfo(self):
    return {
      'amount': self.serviceAmount,
      'services': self.service
    }