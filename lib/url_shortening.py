import string

ALLOWED_CHARS = string.ascii_lowercase + string.ascii_uppercase +  string.digits

def shorten_url(last_shortened_url):
    num_chars = len(ALLOWED_CHARS)
    sequence_num = 0
    for char in last_shortened_url:
        sequence_num = sequence_num * num_chars + ALLOWED_CHARS.index(char)
    
    sequence_num += 1
    new_shortened_url = ""
    while sequence_num > 0:
        sequence_num, index = divmod(sequence_num, num_chars)
        new_shortened_url = ALLOWED_CHARS[index] + new_shortened_url
    return new_shortened_url
