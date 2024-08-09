calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    new_int = len(string)
    up_str = string
    up_str = up_str.upper()
    low_str = string
    low_str = low_str.lower()
    string = (new_int, up_str, low_str)
    count_calls()
    return string


def is_contains(strung, list_to_search):
    new_list = []
    for i in list_to_search:
        new_list.append(i.lower())
    new_str = strung.lower()
    strung = (new_str in new_list)
    count_calls()
    return strung


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
