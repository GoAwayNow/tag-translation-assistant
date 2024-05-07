import argparse
import csv
from . import config as tataconfig
from . import danbooru
from . import google as googletl
from . import deepl as deepltl
from . import romanize
from . import pixiv

def main():
    tags = []

    parser = argparse.ArgumentParser(
                    prog='Tag Translation Asssistant',
                    description='Automatically machine-translate multiple tags')
    parser.add_argument('tags', help="A space-delemited list of tags", nargs='*')
    parser.add_argument('-i', '--infile', help="A text file containing tags to be translated")
    parser.add_argument('-o', '--outfile', help="Path to a CSV file where results are saved", required=True)
    parser.add_argument('-a', '--artist', help='Perform an artist alias lookup instead of a normal tag lookup. Only uses Danbooru as a source.', action='store_true')
    args = parser.parse_args()
    
    if args.tags:
        tags.extend(args.tags)
    if args.infile:
        try:
            with open(args.infile, 'r', encoding="utf-8") as tagsIn:
                tags.extend(tagsIn.read().splitlines())
        except FileNotFoundError as e:
            print (e)

    if len(tags) == 0:
        parser.print_help()
        return

    #tempTag = "おっぱい"
    #tempTag = "紅咲桜花"

    #for tag in tags:
        #print(tag)
        #print("Danbooru:"+danbooru.getTranslation(tag))
        #print("Google:"+googletl.translate(tag))
        #print("DeepL:"+deepltl.getTranslation(tag))
        #print("Romanized:"+str(romanize.getRomaji(tag)))
        #print("single tag finished")
    #return

    # Config loading writing test
    #print(tataconfig.config)
    #print(tataconfig.config["danbooru"]["apikey"])

    csvFieldNames = ['Original']

    if args.artist:
        csvFieldNames.append('Danbooru')
    else:
        csvFieldNames.extend(['Pixiv', 'Danbooru', 'Google', 'Rōmaji'])
        if tataconfig.config['deepl']['apikey']:
            csvFieldNames.insert(3, 'DeepL')


    with open(args.outfile, 'w', encoding="utf-8") as csvOut:
        writer = csv.DictWriter(csvOut, fieldnames=csvFieldNames, dialect='unix')
        writer.writeheader()
        for tag in tags:
            csvRow = { 'Original': tag }
            if args.artist:
                csvRow['Danbooru'] = danbooru.getArtist(tag)
            else:
                csvRow['Pixiv'] = pixiv.getTranslation(tag)
                csvRow['Danbooru'] = danbooru.getTranslation(tag)
                csvRow['Google'] = googletl.getTranslation(tag)
                csvRow['Rōmaji'] = romanize.getRomaji(tag)
                if tataconfig.config['deepl']['apikey']:
                    csvRow['DeepL'] = deepltl.getTranslation(tag)

            writer.writerow(csvRow)
            print('Completed tag: '+tag)


if __name__ == '__main__':
    main()