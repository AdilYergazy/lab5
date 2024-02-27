import re


def match_string(txt):
    pattern = r'ab*'
    if re.search(pattern, txt):
        return True
    return False


def match2(txt):
    pattern = r'ab{2,3}'
    if re.search(pattern, txt):
        return True
    return False


def match3(txt):
    pattern = r'[a-z]+_[a-z]'
    if re.search(pattern, txt):
        return True
    return False


def match4(txt):
    pattern = r'[A-Z][a-z]+'
    if re.search(pattern, txt):
        return True
    return False


def match5(txt):
    pattern = r'a+.*b'
    if re.search(pattern, txt):
        return True
    return False


def match6(txt):
    x = re.sub(r"[;,\s]", '', txt)
    return x


def match7(txt):
    x = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), txt)
    return x


def match8(txt):
    x = re.split(r'[A-Z]', txt)
    return x


def match9(txt):
    x = re.sub(r'[A-Z]', lambda m: m.group(0) + " ", txt)
    return x


def match10(txt):
    x = re.sub(r'(?<!^)([A-Z])', r'_\1', txt).lower()
    return x
