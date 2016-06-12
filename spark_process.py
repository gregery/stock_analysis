from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("historical diff")
sc = SparkContext(conf = conf)

with open('tickers.json') as data_file:
  tickers = json.loads(data_file.read().replace('\n',''))
print tickers

