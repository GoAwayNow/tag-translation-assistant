import pykakasi

def getRomaji(strIn):
    kks = pykakasi.kakasi()
    try:
        r = kks.convert(strIn)
    except:
        return "Error"
    else:
        return concatHepburn(r)
    
def concatHepburn(dictIn):
    s = ''
    for i in dictIn:
        s += i['hepburn']+' '
    return s.strip()