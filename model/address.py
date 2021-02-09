import re
from functools import reduce

# https://biz.kkc.co.jp/software/geo/addressmatch/function/
# https://yamagata.int21h.jp/tool/testdata/

class Address:
    full = ""
    pref = ""
    city = ""
    town = ""
    extra1 = ""
    extra2 = ""
    zip7 = None

    def __init__(self, va):
        self.normalize(va)
        self.parse()

    def normalize(self, va):
        self.full = va.translate(str.maketrans({chr(0xFF01 + i) : chr(0x21 + i) for i in range(94)}))

    def parse(self):
        _pat = '(...??[都道府県])*((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下>松|岩国|田川|大村|宮古|富良野|別府|佐伯|黒部|小諸|塩尻|玉野|周南)市|(?:余市|高市|[^市]{2,3}?)郡(?:玉村|大町|.{1,5}?)[町村]|(?:.{1,4}市)?[^町]{1,4}?区|.{1,7}?[市町村])(.+)'
        _address = re.split(_pat, self.full)
        
        if(len(_address) > 3):
            self.pref = _address[1]
            self.city = _address[2]
            self.town = _address[3]

            self.normalizeJou()
            self.parseFloor()
    
    def normalizeJou(self):
        if (self.town == ""):
            return

        _pat = '([東西南北])([0-9]+)(条)'
        _result1 = re.search(_pat, self.town)
        if (_result1 != None):        
            # convert number to kanji
            d = {'10':'十','20':'二十','30':'三十','1':'一','2':'二','3':'三','4':'四',' 5':'五','6':'六','7':'七','8':'八','9':'九'}
            _f = reduce(lambda x, y: x.replace(y, d[y]), d, _result1.group(2))
            if (len(_f) == 2 and not re.match('.十', _f)):
                _f = f'{_f[0]}十{_f[1]}'
            # replace
            self.town = re.sub(_pat, r'\1' + _f + r'\3', self.town)

    def parseFloor(self):
        if (self.town == ""):
            return

        _pat = '(.*)([0-9〇一-十]+(棟|号棟|F|階|号室))(.*)'
        _result1 = re.match(_pat, self.town)
        if (_result1 != None):
            self.town = _result1.group(1)
            self.extra1 = _result1.group(2)
            self.extra2 = _result1.group(4)
        #     self.pref = _result1.group(0)
        #     self.city = va.replace(self.pref, "")
        # else:
        #     self.city = self.full

        # _result2 = re.match(r'^(.{1,3}郡.{1,4}(町|村)|市.市|.{1,3}市.{1,4}区|.{1,4}?市|.{1,3}区)(.*)', self.city)
        # # _result2 = re.match(r'^(.{1,3}市)(.*)', self.city)
        # if _result2:
        #     self.city = _result2.group(1)
        #     self.town = _result2.group(2)
        # else:
        #     self.city = ""

            # print(_result.group())

