import gzip
import argparse
import json
import os


def processFile(filename_, ticker_):
  data = {}
  try:
    for line in gzip.open(filename_, 'rb'):
      line = line.rstrip('\n')
      line = json.loads(line)
      data[line['Date']] = line
  except IOError:
    return

  keys = sorted(data.keys())
  for index in range(1,len(keys)):
    try:
      if data[keys[index]]['Open'] == '0.00':
        continue
      else:
        yield (str(data[keys[index]]['Date']), (str(ticker_), "{:.4f}".format(((float(data[keys[index]]['Open']) - float(data[keys[index-1]]['Open'])) / float(data[keys[index]]['Open']) * 100.0))))
    except ZeroDivisionError:
      print data[keys[index]]
      continue

def processTicker(ticker_):
  return [x for x in processFile(os.path.join('./data', ticker_ + '.txt.gz'), ticker_)]

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("ticker", help="ticker of stock data to pull")
  args = parser.parse_args()

  print processTicker(args.ticker)
