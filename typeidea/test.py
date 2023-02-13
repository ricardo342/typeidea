# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test
@time:2023/2/11
@Author:majiaqin 170479
@Desc:用于测试程序代码
'''
import requests
import json
import pprint
import datetime
import random
import os, re
import time
from hyper.contrib import HTTP20Adapter
def startCaptcha():
    url = "https://test-nft-tool-gateway-api.tuoluo.net/generator-server/api/notify/v1/startCaptcha"
    header = {'Content-Type': 'application/json'}
    form = {}
    r = requests.post(url, headers=header, data=json.dumps(form))
    return r.json()

def ajax_php(i, j):
    url = 'https://api.geevisit.com/ajax.php?gt={0}&challenge={1}&lang=zh-cn&pt=0&client_type=web&w=76Xr2L3bHWIYkGRzZzUpGukmao3O2n5Kijmog0Hgi4E4vaDqkT5oy6Fdw(UP9iYrbdhAX0R0bEKDyhOl6Zm)aLbSADtvdTM2f1goiIDcvvB228uXk4sfmzXfEr7uzMsveKEFMAgKmb(DD6TSKHNb7ILfFhIXetvVINOAZ033dNyARIcmgihrCZM4ZHNFTDeTCj6UJHD4iTSDiaxEP6CU28luQBe1Pzga4p2xztiHUhW3R2ska4)etpwC85H6rF5)RX7E80CplPku5(S1IsA0Ep6)E0knkDjPPQ2)GKz4m7Cs56uKMbBsSlXoNHLmK9cQ5Nq)5acNITXeJ8abpNMOi4OidVDv(sSgJLJXmPQZ(MaSajtfNnD25SxJrmGeKm9pFkX7lcPHRvOihigiRMH7hAkzVhoWl451c(l4JVp4yrq7qVD17otAePfB6xKQ4Cj0Paj5IB9Z4qRgLf2v(DX3PwrJB5ijMptAGhvOafPD1bNzHDjvO(5VOxd2lOx3WtrL)PXSYaHdqMsLCYO(Vp3o9bUYCC1JRVXj4qdv)eAARRRfy6N8wWlNUGV2i7T(ea0jBQJLIgrtjbF0wcXNzjTlMbsyDYJbafP93)EcmJJ2T8UjSYW1wE(rLliqHmL(nRhK68TJkmP954EUZcYcSiWXNPm(eMk4nWB9IapLY6xuSWdunRFhq2RVKn1LRuzDPjXyhTEowwHe)htB0sT0wpaCNO3H6kIwsT4uglPVaPexQbJbknchvGHfMBdICbNmp8CHY9njK7ALMSZXinUkt3sigqNYED7j)CgcL1zhIZ(5El8RV0XhNtAVlMrWUSorCvs2FvE6ucref(iJeNoN9UZtAMmhsCfpDHH(f6MGKSrTcGUQ2uNvMfalsKXrGRXrEgoAUTCQQIEb)GvTVpuLbIadlxsJzne)gpuIsw5nPBTootdZGfCTUz2cdLK6v)OHKL8uH5tOwGDO(zVfB0U63lv3YsTaRzLdSzPWZvo((9G0wEitxg9yIJZr)7YwJpNSu)xx4wf28gkdAytw5cHdOEbQa3vx1DSsBZI0JaNqvJdL1p(td2UoQKvEFxY2LoofGa77TPdpuzqIT(bHX)bJgbXTnlt0dCVIyq5oPy7iRm4f((5LmozLsSKfUWNpbznIlwgRekg3DzWkUS5(GWj8hxXAsDCvRyEwiK95m7bLUGnDWPuzTN93Bey2HQjc8Yz5jPHuak)oICQMZVZPYVMPOZxXOWFIi3m)F4mbbbPcPdiAs6M3TWj)DTwxQjoNbS6ZMA5O&callback=geetest_1676081401743'.format(i, j)
    header = {'Accept': '*/*',
              'Accept-Encoding': 'gzip, deflate, br',
              'Content-Type': 'application/json',
              'Host': 'api.geevisit.com',
              'Referer': 'https://test-nft-tool-web-api.tuoluo.net/'}
    r = requests.get(url, headers=header)
    return r.text

def send_code(i):
    url = "https://test-nft-tool-gateway-api.tuoluo.net/generator-server/api/notify/v1/send_code"
    header = {'Content-Type': 'application/json'}
    form = {"to":"mjq13751753979@sina.com","geetestChallenge": i,"geetestSeccode":"85f1380d296d86bb692485c62ca4522a|jordan","geetestValidate":"85f1380d296d86bb692485c62ca4522a","scene":"USER_REGISTER"}
    pprint.pprint(form)
    r = requests.post(url, headers=header, data=json.dumps(form))
    return r.text

def test_test():
    i = startCaptcha()
    params = ajax_php(i['data']['gt'], i['data']['challenge'])
    # params = send_code(i['data']['challenge'])
    return params

if __name__ == '__main__':
    pprint.pprint(test_test())
    pass