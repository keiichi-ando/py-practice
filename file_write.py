import locale
import os
import re

from model.person import Person

print (locale.getpreferredencoding())

def createFolderIfNotExists(filename = ''):
    _path = os.path.dirname(filename)
    if (not os.path.exists(_path)):
        os.makedirs(_path)
        print('create path ' + _path)


path = 'data/personal.txt'
createFolderIfNotExists(path)

with open(path) as f:
    l = [Person(s.strip().split('\t')) for s in f.readlines()] # strip \n


    # f.close()
# print (l)

for p in l:
    print (p.id, p.addr.pref, p.addr.city, "\t", p.addr.town, "\t", p.addr.full)

# town = "西五反田七ノ二二ノ一七 ABCビル5階"
# _pat = '(.*)([0-9〇一-十]+(棟|号棟|F|階|号室))(.*)'
# # _pat = r'([0-9〇一-十]+号)'
# _result1 = re.match(_pat, town)
# print(_result1.group(4))

