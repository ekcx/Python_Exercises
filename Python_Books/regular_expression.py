import re

phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d-\d\d\d-\d\d\d\d\d\d\d\d\d\d\d')
mo = phoneNumRegex.search('My number is 4152423-550-4242673543643564.')
print('Phone number found: ' + mo.group())

