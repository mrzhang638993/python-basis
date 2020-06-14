# 学习正则表达式进行查找操作实现
#  学习正则表达式的时候对应的就是很艰难的
import re

result = re.search(r'FishC', 'I love FishC.com')
# 'I love FishC.com'.find('FishC')
# 匹配换行符号之外的任意的字符信息
result = re.search(r'.', 'I love FishC.com')
# 匹配点号
result = re.search(r'\.', 'I love FishC.com')
#  \d  匹配的是任意的数字字符信息，匹配的是单个的字符
result = re.search(r'\d', 'I love FishC.com')
#  匹配单个的字符信息,匹配集合中的单个的元素信息,可以使用[aeiou]或者是[a-e]
result = re.search(r'[aeiou]', 'I love FishC.com')
# 限定重复匹配的次数信息,使用大括号进行操作匹配
result = re.search(r'ab{3}c', 'abbbc')
# 指定匹配的次数范围
result = re.search(r'ab{3,10}c', 'abbbc')
# 匹配到0-255范围内的数字,下面的这个实例是错误的。正则表达式匹配的是字符串的，数字对应的是0-9的。
result = re.search(r'[0-255]\.[0-255]\.[0-255]\.[0-255]', '192.168.1.101')
# [0-255] 对应的意思是匹配0-2之间的数字然后加上5，即对应的是0125的数字可以匹配到的
# 下面是匹配0-255之间的数字的，对应的匹配的公式的，需要注意的是正则表达式只能够匹配字符串的
# 下面的语句要求的都是三位数的，不一定匹配到的，存在问题的，需要进行修改操作的
# () 对应的是将匹配的内容是整体操作的
result = re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])', '192.168.1.1')
# \1  对应的是匹配前面的元祖信息的。
