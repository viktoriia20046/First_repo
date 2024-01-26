import re
 
s = 'Hello! How are you? Im fine'
result = re.findall(r'[abcdhlinABCBHLIN]\w+', s)