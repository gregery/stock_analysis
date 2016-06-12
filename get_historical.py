import os
import csv
import StringIO
import requests
import json
import datetime
import argparse
import gzip


def initDataDir():
  if os.path.exists('./data') == False:
    print 'creating data dir'
    os.mkdir('data')
  else:
    print 'using existing data dir'

def openFile(filename_):
  return gzip.open(os.path.join('./data', filename_ + '.txt.gz'), 'wb')

def pull(ticker_):
  r = requests.get('http://ichart.yahoo.com/table.csv', params = {'s' : ticker_ } )
  if 'Yahoo! - 404 Not Found' in r.content:
    print 'Error while pulling ticker: ' + ticker_
    return

  new = 0 
  existing = 0

  reader = csv.DictReader(StringIO.StringIO(r.content))
  datafile = openFile(ticker_)
  for row in reader:
    datafile.write(json.dumps(row) + '\n')

  datafile.close()

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("ticker", help="ticker of stock data to pull")
  args = parser.parse_args()

  initDataDir()
  pull(args.ticker)


