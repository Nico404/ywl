import re
import string

def body(text):
    """
    Extracts the body of a text without the header and the footer by gutenberg project
    """
    result = re.findall(r'\*\*\* START OF .+ \*\*\*(.*?)\*\*\* END OF .+ \*\*\*', text, flags=re.DOTALL)
    if result:
        body_ = result[0].strip()
    else:
        body_ = text
    return body_

def body_cleaning(body, to_strip=True, to_lower=True, del_numbers=True, del_punctuation=True):
    """
    Cleans the body of a text by removing whitespaces, lowercasing, removing numbers and punctuation
    """
    # Removing whitespaces
    if to_strip == True: body = body.strip()

    # Lowercasing
    if to_lower == True: body = body.lower()

    # Removing numbers
    if del_numbers == True: body = ''.join(char for char in body if not char.isdigit())

    # Removing punctuation
    if del_punctuation == True:
        for punctuation in string.punctuation:
            body = body.replace(punctuation, '')

    return body


def strip_html(text):
    """
    Removes html tags from a string
    """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
