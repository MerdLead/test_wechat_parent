import urllib3
# from pprint import pprint


def verify_find(phone):
    http = urllib3.PoolManager()
    r = http\
        .request('GET', "http://dev.vanthink-core-api.vanthink.cn/master/tool/testEngineerGetCaptcha?phone=%s" % phone)
    value = r._body.decode('utf-8')
    print(value)
    # pprint(vars(r))
    return value
# http://dev.vanthink-core-api.vanthink.cn/master/tool/testEngineerGetCaptcha?phone=18211111003
