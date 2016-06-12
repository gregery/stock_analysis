import gzip
import argparse
import json
import os


def processTicker(filename_, ticker_):
  data = {}
  for line in gzip.open(filename_, 'rb'):
    line = line.rstrip('\n')
    line = json.loads(line)
    data[line['Date']] = line

  keys = sorted(data.keys())
  for index in range(1,len(keys)):
    print (data[keys[index]]['Date'], (ticker_, ((float(data[keys[index]]['Open']) - float(data[keys[index-1]]['Open'])) / float(data[keys[index]]['Open']) * 100.0)))

  return data


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("ticker", help="ticker of stock data to pull")
  args = parser.parse_args()

  processTicker(os.path.join('./data', args.ticker + '.txt.gz'), args.ticker)
