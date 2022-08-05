import collections

# default_dic = collections.defaultdict(list)
default_dic = collections.defaultdict(lambda: 'Not found')
default_dic['1'] = 'Apple'
default_dic['2'] = 'Microsoft'
default_dic['3'] = 'Huawei'

print(default_dic['4'])  # prints Not found

# Under the hood

# missing method takes default_factory as an argument
# in our case anonymous function returning 'Not found'

# If we provide None as default_factory then missing
# will return keyerror
# default_dic = collections.defaultdict(None)
# it is then same as using normal dictionary class

#  __getitem__ calls __missing__ when key is not found
# __missing__ holds the default value for key
# which can be anything provided as argument to
# defaultdict

# 'Not found' is default value for every key
print(default_dic.__missing__('1'))  # Not found
print(default_dic.__missing__('2'))  # Not found
print(default_dic.__missing__('4'))  # Not found

# in case of normal dict class __getitem__
# will return item or raise keyerror
# but in case of defaultdic it'll always return
# value returned by __missing__ method

# we can say __getitem__ is only invoked when
# key is not found
print(default_dic.__getitem__('1'))  # Not found
print(default_dic.__getitem__('2'))  # Not found
print(default_dic.__getitem__('4'))  # Not found
