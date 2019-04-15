from tests.helperer import *
from tests.domain_check.helper_check import *
from tests.contracts import *
import requests


def test_domain_check_15():
    domainName = sld() + randomTld(info)
    payload = {"domains": [domainName], "priceFlags": "15"}
    r = requests.post(url=url + path, json=payload)
    result = r.json()
    fst = result[0]
    if fst['availability']['isAvailable'] == True:
        assert r.status_code == 200
        assert fst['domainName'] == domainName
    else:
        print(fst['availability']['reason'])


    #assert fst['availability']['isAvailable'] is True, "Domain is exist"
    # print(fst['domainName'])
    # print(fst['availability']['isAvailable'])
    #print (fst['register'])
    print(r.json())
    # print(r.status_code)


test_domain_check_15()



