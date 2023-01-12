def string_to_number(s):
    try:
        converted = int(s)
    except:
        print('bad input')
    pass
    return converted

# sample tests


string_to_number("1234")
string_to_number("605")
string_to_number("1405")
string_to_number("-7")
string_to_number("32574325")