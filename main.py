from googletrans import Translator
from httpcore import SyncHTTPProxy
import pyperclip


def convert(un_convert_str):
    lines = un_convert_str.splitlines()
    ret_list = []
    for line in lines:
        ret_list.append(line.strip().strip('//'))
    ret = ""
    for p in ret_list:
        ret = ret + " " + p
    return ret


if __name__ == '__main__':
    ip = input('输入代理服务器ip地址:')
    ip = bytes(ip, encoding="utf8")
    port = input('输出代理服务器端口号:')
    port = int(port)
    translator = Translator(service_urls=[
        'translate.google.com',
        'translate.google.cn'
    ], proxies={"https": SyncHTTPProxy((b'http', ip, port, b''))})
    last_clip = ""
    while True:
        data = pyperclip.paste()  # sudo apt-get install xclip
        if data != last_clip:
            last_clip = data
            input_str = convert(last_clip)
            print(input_str)
            t = translator.translate(input_str, dest='zh-cn')
            print(t.text)
            print('------------------------------------------------')
