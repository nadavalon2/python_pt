import json, requests

def main():

    url = 'http://www.matthewproctor.com/Content/postcodes/australian_postcodes.json'

    r = requests.get(url)

    postcodes = json.loads(r.text)

    with open('postcodes.tsv', 'w+') as outfile:
        print('postcode', 'locality', 'state', sep='\t', file=outfile)

        for p in postcodes:
            print(p['postcode'], p['locality'], p['state'], sep='\t', file=outfile)

if __name__ == "__main__":
    main()