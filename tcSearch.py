import requests
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
def search(number):
    number=str(number)
    response = requests.get('https://search5-noneu.truecaller.com/v2/search?q='+number+'&type=2&adId=5649d5bf-31c0-4e7d-a5be-1653b3babee1&encoding=json', auth=BearerAuth('a1i0m--Wx2_Q0VfF2YzoRYBUQKCX6LImG3Whp14R_-Lp3bz0RZiwMqnu46CxkmOJ'))
    info = response.json()
    return info
