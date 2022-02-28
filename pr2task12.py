import re
str = '#%%\nfrom itertools import groupby\ndef rle_encode(data):\n\treturn [(k, len(list(g))) for k, g in groupby(data)]\n#%% md\n**Заача 12**'
str = str.replace(r'"([^"]*)"/g', '{$1}')
print