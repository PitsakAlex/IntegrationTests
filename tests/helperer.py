import random
import string

url = 'http://api.staging.registrarengine.com/'


def sld():
    letters = string.ascii_lowercase + string.digits
    return 'pitsak-' + ''.join(random.choice(letters) for i in range(1))
