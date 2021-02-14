def check_email(string):
    return (' ' not in string and '@.' not in string and '.' in string
            and string.rfind(".") > string.find("@") and string.count('@') == 1)
