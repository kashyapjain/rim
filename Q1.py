import re

phone_regex = '^\+?\d{0,3}((\d{0,3}?-)|\s)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}?$'

phone_numbers = ['2124567890',
                 '212-456-7890',
                 '212.456.7890',
                 '212 456 7890',
                 '1-212-456-7890',
                 '(212)456-7890',
                 '(212)-456-7890',
                 '+12124567890',
                 '+12124567890',
                 '+1 212.456.7890',
                 '+212-456-7890',
                 '+212-456-7890 +212-456-7890',
                 '+212-456-789',
                 '+212 456-7890']

for phone_number in phone_numbers:
    re_obj = re.match(phone_regex, phone_number)

    if(re_obj == None):
        print(phone_number + "\tis not valid")
        continue

    match = re_obj.group(0)

    if(match == phone_number):
        print(phone_number + "\tis valid")
