import random
import string

url = SwaggerShort


def sld():
    letters = string.ascii_lowercase + string.digits
    return 'pitsak-' + ''.join(random.choice(letters) for i in range(1))
