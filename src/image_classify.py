from aip import AipImageClassify
""" 参考 https://ai.baidu.com/ai-doc/IMAGERECOGNITION/8k3e7f69o 进行操作"""


def get_file_content(file_path):
    """ 读取图片 """
    with open(file_path, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    """ 你的 APPID AK SK """
    APP_ID = '25723147'
    API_KEY = '8g5EB282r9RXZxfMra7ZRi1b'
    SECRET_KEY = 'OcxdsU4GMpytmR1W9oWQvldn15ihbeDG'
    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

    # 读取图片信息测试接口
    test_path = '/Users/mahao/PycharmProjects/pythonTools/pic_data/OIP-C.jpeg'
    image = get_file_content(test_path)

    # 可选参数设置
    options = {"baike_num": 1}

    # 调用通用物体和场景识别
    advanced_general = client.advancedGeneral(image)
