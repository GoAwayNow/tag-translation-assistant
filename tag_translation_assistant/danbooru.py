import pybooru
import requests
import urllib

dbClient = pybooru.Danbooru('danbooru')

def getTranslation(tag):
    try:
        r = dbClient.wiki_list(other_names_match=tag)
    except:
        return 'Error'
    else:
        if r:
            if len(r) > 1:
                finalres = ''
                for i in range(len(r)):
                    finalres += getCategory(r[i]['title'])
                    if not i == len(r)-1:
                        finalres += ', '
                return finalres
            return getCategory(r[0]['title'])
        else:
            return 'Not found'

def getCategory(tag):
    try:
        r = dbClient.tag_list(name=tag)
    except:
        return 'Error'
    else:
        if r:
            if r[0]['category'] == 1:
                tagCat = "creator:"
            elif r[0]['category'] == 3:
                tagCat = "series:"
            elif r[0]['category'] == 4:
                tagCat = "character:"
            else:
                tagCat = ""
            
            return str(tagCat+tag).replace('_', ' ')
        else:
            return tag
        
# Pybooru's artist_list function doesn't actually work for searches other than name.
def getArtist(tag):
    tag = tag.removeprefix('creator:')

    try:
        r = requests.get('https://danbooru.donmai.us/artists.json?search[order]=post_count&search[any_other_name_like]='+urllib.parse.quote(tag))
    except requests.exceptions as e:
        return str(e)
    else:
        if r.status_code == requests.codes.ok:
            if not r.text == '[]':
                if len(r.json()) > 1:
                    finalres = ''
                    for i in range(len(r.json())):
                        finalres += str('creator:'+r.json()[i]['name']).replace('_', ' ')
                        if not i == len(r.json())-1:
                            finalres += ', '
                    return finalres
                return str('creator:'+r.json()[0]['name']).replace('_', ' ')
            else:
                return 'Not found'
        else:
            return str(r.raise_for_status())
