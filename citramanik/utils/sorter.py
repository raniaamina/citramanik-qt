import re

def natural_sort(array: list):
    convert_this = lambda text: int(text) if text.isdigit() else text
    alphanum = lambda inputtext: [ convert_this(item) for item in re.split('([0-9]+)', inputtext) ]
    array.sort(key=alphanum)
    return array
