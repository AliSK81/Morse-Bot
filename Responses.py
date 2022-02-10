import re
from Morsor import *


def morsor(input_text):
    txt = remove_exra_spaces(input_text)
    txt = remove_emojis(txt)
    txt = txt.strip()

    if is_morsor(txt):
        return decrypt(txt).lower()
    else:
        return encrypt(txt.upper())


def remove_exra_spaces(text):
    return re.sub(' +', ' ', text)


def remove_emojis(text):
    emoj = re.compile("["
                      u"\U0001F600-\U0001F64F"  # emoticons
                      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                      u"\U0001F680-\U0001F6FF"  # transport & map symbols
                      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                      u"\U00002500-\U00002BEF"  # chinese char
                      u"\U00002702-\U000027B0"
                      u"\U00002702-\U000027B0"
                      u"\U000024C2-\U0001F251"
                      u"\U0001f926-\U0001f937"
                      u"\U00010000-\U0010ffff"
                      u"\u2640-\u2642"
                      u"\u2600-\u2B55"
                      u"\u200d"
                      u"\u23cf"
                      u"\u23e9"
                      u"\u231a"
                      u"\ufe0f"  # dingbats
                      u"\u3030"
                      "]+", re.UNICODE)

    return re.sub(emoj, '', text)
