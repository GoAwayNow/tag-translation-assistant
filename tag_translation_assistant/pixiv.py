import requests
import urllib

# This endpoint only returns translations if you're logged in with an english account.
#def getTranslation(tag):
#    try:
#        r = requests.get('https://www.pixiv.net/ajax/tag/info?tag='+urllib.parse.quote(tag)+'&pixp_lang=en&lang=en')
#    except requests.exceptions as e:
#        return str(e)
#    else:
#        return str(r.text)

def getTranslation(tag):
    try:
        h = {'Accept-Language': 'en-US,en;q=0.5'}
        r = requests.get('https://www.pixiv.net/ajax/search/tags/'+urllib.parse.quote(tag), headers=h)
    except requests.exceptions as e:
        return str(e)
    else:
        if r.status_code == requests.codes.ok:
            try:
                json = r.json()
            except requests.exceptions as e:
                return str(e)
            else:
                return processResponse(json, tag)
        else:
            return str(r.raise_for_status())
    
def processResponse(json, tag):
    try:
        t = json['body']['tagTranslation'][tag]['en']
    except:
        return 'Not found'
    else:
        if not t == '':
            return t
        else:
            return 'Not found'