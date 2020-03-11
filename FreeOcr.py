import base64
import json
import requests
import re

def BaiduFreeOcr(img_path):
    with open(file=img_path, mode='rb') as file:
        base64_data = base64.b64encode(file.read())
        base64_data_ex = str(base64_data).split('\'', -1)
        sss = "data:image/jpeg;base64," + base64_data_ex[1]
        # print(sss)

    form_date = {
        "image" : sss,
        "image_url" : "",
        "type" : "commontext",
        "detect_direction" :"false"
    }

    r = requests.post('https://ai.baidu.com/aidemo', data=form_date)
    rs = json.loads(r.text)
    # print(rs)
    code = rs['data']['words_result'][0]['words']
    # print(code)
    return code

# 优图 image_url
def UtOcrA(image_url):
    date = {
        "image_url":image_url,
    }
    r = requests.post('https://ai.qq.com/cgi-bin/appdemo_generalocr?g_tk=5381', data=date)
    rs = json.loads(r.text)
    # print(rs)
    if rs['ret'] == 0:
        if rs['data']['item_list'] == []:
            return "OCR未识别到值"
        else:
            # print(rs)
            code_0 = rs['data']['item_list'][0]['itemstring']
            # print("code 0--" + code_0)
            code_1 = re.compile(r'[\u4e00-\u9fa5]?')
            code_2 = code_1.findall(code_0)
            # print("code 2--" + str(code_2))
            if code_2 != []:
                code = code_2[0]
                if code != '':
                    # print("code ---" + code)
                    return code
                else:
                    return "OCR未识别到值"
            else:
                 # print("OCR未识别到值")
                 return "OCR未识别到值"
    else:
        # print("OCR未识别到值")
        return "OCR未识别到值"

# 优图 本地图片
def UtOcrB(imgpath):
    files = {
        'image_file': ('file', open(imgpath, 'rb'), 'image/jpeg')
    }
    r = requests.post('https://ai.qq.com/cgi-bin/appdemo_generalocr?g_tk=5381', files=files)
    rs = json.loads(r.text)
    # print(rs)
    if rs['ret'] == 0:
        if rs['data']['item_list'] == []:
            return "OCR未识别到值"
        else:
            # print(rs)
            code_0 = rs['data']['item_list'][0]['itemstring']
            # print("code 0--" + code_0)
            code_1 = re.compile(r'[\u4e00-\u9fa5]?')
            code_2 = code_1.findall(code_0)
            # print("code 2--" + str(code_2))
            if code_2 != []:
                code = code_2[0]
                if code != '':
                    # print("code ---" + code)
                    return code
                else:
                    return "OCR未识别到值"
            else:
                 # print("OCR未识别到值")
                 return "OCR未识别到值"
    else:
        # print("OCR未识别到值")
        return "OCR未识别到值"


# UtOcr("https://www.keaidian.com/uploads/allimg/190423/23233733_1.jpeg")
# TencentFreeOcr(r'tpyzm_trans.jpg')
# UtOcrB(r'123.png')



