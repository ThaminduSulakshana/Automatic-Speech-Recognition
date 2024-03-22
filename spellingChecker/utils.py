import re

def filter_punctuation(input_str, remove_duplicate_space=True):
    """
    Remove punctuations and extra spaces from input string.
    """
    regex = re.compile(u'[^\u4E00-\u9FA5\s]')  # Matches non-Chinese characters and non-space characters
    if remove_duplicate_space:
        result = re.sub(' +', ' ', regex.sub(' ', input_str))
    else:
        result = regex.sub(' ', input_str)
    result = re.sub("\d+", " ", result)  # Replace digits with spaces
    result = strQ2B(result)  # Convert full-width characters to half-width characters
    return result.strip()  # Strip leading and trailing spaces

def strQ2B(ustring):
    """
    Convert full-width characters to half-width characters.
    """
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring

def digits2Chinese(string, mode='int'):
    """
    Convert digits in the string to Chinese characters.
    """
    # Implementation needed
    pass

def reviseString(string):
    """
    Revise the input string according to some rules.
    """
    re_int = re.compile('\d+')
    re_float = re.compile('\d+\.\d+')
    # Implementation needed
    pass

if __name__ == '__main__':
    a = 'abcd我是，,,,...上升！!!!~[][][]·「·」「{}345'
    print(filter_punctuation(a))
