import json
import argparse
import get_historical

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--resume", help="ticker of stock to resume pulling at")
  args = parser.parse_args()

  with open('tickers.json') as data_file:
    tickers = json.loads(data_file.read().replace('\n',''))

  get_historical.initDataDir()

  found = False
  if args.resume == None:
    found = True

  for ticker in tickers:
    if found == True:
      get_historical.pull(ticker)
      continue

    if args.resume == ticker:
      found = True


