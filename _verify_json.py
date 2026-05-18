import json

with open(r'F:\Data\Energy prices\wem_balancing_market.json', 'r') as f:
    d = json.load(f)

meta = d['metadata']
data = d['data']
print('Coverage:', meta['coverage']['start'], '->', meta['coverage']['end'])
print('Total intervals:', meta['coverage']['total_intervals'])

print('\nFirst record:')
print(json.dumps(data[0], indent=2))

print('\nLast record:')
print(json.dumps(data[-1], indent=2))

# Check the 2022->2023 boundary (date format change between files)
idx = next(i for i, r in enumerate(data) if r['trading_date'] >= '2023-01-01')
print('\nLast 2022 record (interval', data[idx-1]['interval'], '):')
print(json.dumps(data[idx-1], indent=2))
print('\nFirst 2023 record (interval', data[idx]['interval'], '):')
print(json.dumps(data[idx], indent=2))
