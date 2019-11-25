import re
# def find_all_example():
#     pattern = r"\d{5}"
#     text= "NY Postal Codes are 10001, 10002, 10003, 10004"
#
#     print ('pattern {0}'.format(pattern))
#     match = re.findall(pattern, text)
#     print (match)
#
# find_all_example()
#-------------------------
def group_by_name():

    pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})(?P<hour>\d{2})?"
    text = "Tomastamp=20160502"
    print('pattern {0}'.format(pattern))
    print('Text {0}'.format(text))
    match_iter = re.finditer(pattern, text)

    for match in match_iter:
        print('Match. Text: {0} Index: {1} Lenght: {2}'.format(match.group(0), match.start(), len(match.group(0))))
        print('Access group by name')
        print('Year: {0}'.format(match.group('year')))
        print('Month: {0}'.format((match.group('month'))))
        print('Day: {0}'.format((match.group('day'))))
        print('Hour: {0}'.format(match.group('hour')))
        print('Access all named groups as a dictionary')
        print('    {0}'.format(match.groupdict()))

group_by_name()


