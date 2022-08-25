import json as js
import csv
from datetime import datetime

class FileService:

  def readFile(self, filename):
    with open(filename, "r") as jsonFile:
      jsonObject = js.load(jsonFile)
      return jsonObject

  def writeCsv(self, filename, dataframe):
    with open(f'{filename}-{datetime.timestamp(datetime.now())}.csv', 'w') as csvFile:
      writer = csv.DictWriter(csvFile, dataframe[0].keys())
      writer.writeheader()
      for member in dataframe:
        writer.writerow(member)

    return csvFile