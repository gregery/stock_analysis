from pyspark import SparkConf, SparkContext
import json
import extract
import csv

def addToDict(a,b):
  a[b[0]] = b[1]
  return a

conf = SparkConf().setMaster("local[*]").setAppName("historical diff")
sc = SparkContext(conf = conf)

partitions = 24

with open('tickers.json') as data_file:
  tickers = json.loads(data_file.read().replace('\n',''))

resultsMap = sc.parallelize(tickers, partitions).flatMap(extract.processTicker).combineByKey( lambda a:{a[0]:a[1]}, addToDict, lambda a,b: dict(a,**b) ).collectAsMap()

with open('summary.csv', 'w') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=["TRADE_DATE"] + tickers)
  writer.writeheader()
  for key in sorted(resultsMap.keys()):
    row = {}
    row["TRADE_DATE"] = key
    row.update(resultsMap[key])
    writer.writerow(row)
  csvfile.close()


