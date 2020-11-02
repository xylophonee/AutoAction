#coding=UTF-8
import requests
import time
from lxml import etree
import json
from hashlib import md5

url = 'https://ksky.zzvzz.top/login/?next=/'
server = 'SCU43267Tdfa013d220d7955c54df031021df05b05c4af8f4d81c5'
def get(xh,mm,lc):
    r = requests.session()
    res = r.get('https://ksky.zzvzz.top/login/?next=/')
    t = time.time()
    t = str(t)
    t = t[0:9]
    ress = r.get('https://ksky.zzvzz.top/getcheckimg/?timestamp='+t)
    cap = run(ress.content)
    selector = etree.HTML(res.content)
    
    post_value = selector.xpath('//*[@id="login-form"]/input[1]')[0].attrib['value']
    headers = {
            'Connection': 'keep - alive',
            'Host': 'ksky.zzvzz.top',
            'Referer': 'https://ksky.zzvzz.top/login/?next=/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36',
    }    
    data = {
        'csrfmiddlewaretoken':post_value,
        'username':xh,
        'password':mm,
        'next':'/',
        'check_code':cap
    }
    r.headers = headers
    response = r.post(url,data=data)
    final_response = r.get('https://ksky.zzvzz.top/NCIR/user_data/add/')
    #print(final_response.text)
    try:
        selector_ = etree.HTML(final_response.content)
        post_value_ = selector_.xpath('//*[@id="user_data_form"]/input')[0].attrib['value']
    except:
        print(final_response.text)
        send("error"+xh)
        return
    final_data = {
        'csrfmiddlewaretoken':post_value_,
        'tw':'36.4',
        'fl':'False',
        'gk':'False',
        'hx':'False',
        'qt':'False',
        'jc':'False',
        'fx':'False',
        'jqjc':'',
        'lc':lc,
        'actionName':'actionValue'
    }
    fin_res = r.post('https://ksky.zzvzz.top/NCIR/user_data/add/',data=final_data)
    print(fin_res.text)
    if '成功' in fin_res.text:
        send(xh)
    else:
        send(fin_res.text)
    
    
def send(text_):
    data = {
        'text':'体温',
        'desp':text_
    }
    requests.post('https://sc.ftqq.com/'+server+'.send',data=data)



def run(im):
    #可去http://www.chaojiying.com/注册账号
    chaojiying = Chaojiying_Client('12781220600', 'smartisanT4mol', '903406') #第一个填账号 第二个填密码 第三个填  用户中心>>软件ID 生成一个替换
    #im = open('/Users/xylophone/Pictures/a.jpg', 'rb').read() 
    data = chaojiying.PostPic(im, 1902)
    print ("验证码为"+data['pic_str'])     
    return data['pic_str']  

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

def auto():
    all_info = [
        ['0162170128','ting123456','河北省 秦皇岛市 昌黎县'],

    ]
    for i in all_info:
        get(i[0],i[1],i[2])  

if __name__ == "__main__":
    auto()
