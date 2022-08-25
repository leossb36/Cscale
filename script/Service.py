class Service:
  def __init__(self, day, hour):
    self.day = day
    self.hour = hour
    self.amount = 0

  def incrementServiceAmount(self):
    self.amount = self.amount + 1

