import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-9]', x)
# y = re.findall('[AEIOU]+', x)
# print(y)
#----------------
# import re
# x = 'From: Using the: character'
# y = re.findall('^F.+?:', x)
# print(y)
#----------------
# x = 'From nima.eivazzadeh@gmail.com Sat Jan'
# x = 'From: alice-b@gmail.com at 12:46:21 02.08.2015'
# x = 'From: nima.eivazzadeh@gmail.com Sat Jan Server_name:local@domain.com'
# x = 'we just received $10.00 for cookies'
x = 'Sport shoe $998.99 hat_1980 $100.99 Skins_A200 $1099 Skins $566.90'
# y = re.findall('\S+@\S+', x)
# y = re.findall('^From\s(\S+@\S+).*Server_name:(\S+@\S+)', x)
# y = re.findall('^From:.*? (\S+@\S+)', x)
# y = re.findall('@([^ ]*)', x)
# y = re.findall('^From:\s.*@([^ ]*)', x)
# y = re.findall('^From: .*@([^ ]*)', x)
# y = re.findall('\$[0-9.]+', x)
# y = re.findall('^From:\s*(\S+@\S+)', x)
# y = re.findall('\$[0-9.]+', x)
# y = re.findall('\$[0-9.]+', x)
# print(y)
#----------------------
# import re
# x = ""
# y = re.findall("", x)
# print(y)

# def find_all_example():
#     pattern = r"\d{5}"
#     text= "NY Postal Codes are 10001, 10002, 10003, 10004"
#
#     print ('pattern {0}'.format(pattern))
#     match = re.findall(pattern, text)
#     print (match)
#
# find_all_example()

# -------------------------


# def group_by_name():
#
#     pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})(?P<hour>\d{2})?"
#     text = "Timestamp=20160502"
#     print('pattern {0}'.format(pattern))
#     print('Text {0}'.format(text))
#     match_iter = re.finditer(pattern, text)
#
#     for match in match_iter:
#         print('Match. Text: {0} Index: {1} Lenght: {2}'.format(match.group(0), match.start(), len(match.group(0))))
#         print('Access group by name')
#         print('Year: {0}'.format(match.group('year')))
#         print('Month: {0}'.format((match.group('month'))))
#         print('Day: {0}'.format((match.group('day'))))
#         print('Hour: {0}'.format(match.group('hour')))
#         print('Access all named groups as a dictionary')
#         print('    {0}'.format(match.groupdict()))
#
# group_by_name()

#-------------------------> group(0) refers to entire match

# def group_by_number():
#
#     pattern = r"(\d{4})(\d{2})(\d{2})(\d{2})?"
#     text = "Timestamp=20160502"
#
#     print('pattern {0}'.format(pattern))
#     print('Text {0}'.format(text))
#     match_iter = re.finditer(pattern, text)
#
#     for match in match_iter:
#         print('Match. Text: {0} Index: {1} Length: {2}'.format(match.group(0), match.start(), len(match.group(0))))
#
#         for i, value in enumerate(match.groups()):
#             print(' Group: {0}, value: {1}'.format(i+1, value))
#
#
# group_by_number()

# -------------------------

# re.sub # ------> replace a text that matches find pattern.

# def find_replace():
#
#     pattern = r"(?P<value>\d+(,\d{3})*(\.\d{2})?)\s+dollar(s)?"
#
#     replacement_pattern = r'**USD \g<value>**'
#
#     text = \
#     '''Widget Unit cost: 12,000.56 dollars
#     Taxes: 234.00 dollars
#     Total: 12,234.56 dollars'''
#
#     print('Pattern: {0}'.format(pattern))
#     print('----Text:\n{0}'.format(text))
#
#     new_text = re.sub(pattern, replacement_pattern, text)
#     print('---New Text:\n{0}'.format(new_text))
#
# find_replace()
# -------------------------

# re.split # ------> split text based on pattern.

# def split():
#     pattern = r"\d+\.\s*"
#     text = 'Here is the list...1.soccer 2.tennis 3.basketball 4.\t\football'
#
#     print('Pattern: {0}'.format(pattern))
#     print('Text Before: {0}'.format(text))
#
#     split_text = re.split(pattern, text)
#     print('text after:')
#     for s in split_text:
#         print('  {0}'.format(s))
#
#
# split()

# -------------------------

