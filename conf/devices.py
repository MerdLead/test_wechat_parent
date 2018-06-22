import os
from conf.base_config import GetVariable as gv
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class Devices:
    """获取连接的设备的信息"""
    def __init__(self):
        self.GET_ANDROID = "adb devices"
        # self.GET_IOS = "instruments -s devices"

    def get_devices(self):
        value = os.popen(self.GET_ANDROID)

        devices = []
        for v in value.readlines():
            android = {}
            s_value = str(v).replace("\n", "").replace("\t", "")
            if s_value.rfind('device') != -1 and (not s_value.startswith("List")) and s_value != "":
                android['platformName'] = 'Android'
                android['deviceName'] = s_value[:s_value.find('device')].strip()
                android['platformVersion'] = gv.PLATFORM
                android['app'] = PATH(gv.APP)
                android['package'] = gv.PACKAGE
                android['activity'] = gv.ACTIVITY
                android["chromeOptions"] = {"androidProcess": "com.tencent.mm:tools"}
                android["unicodeKeyboard"] = True
                android["resetKeyboard"] = True
                android["reuse"] = '4'

                devices.append(android)

        # value = os.popen(self.GET_IOS)
        #
        # for v in value.readlines():
        #     iOS = {}
        #
        #     s_value = str(v).replace("\n", "").replace("\t", "").replace(" ", "")
        #
        #     if v.rfind('Simulator') != -1:
        #         continue
        #     if v.rfind("(") == -1:
        #         continue
        #
        #     iOS['platformName'] = 'iOS'
        #     iOS['platformVersion'] = re.compile(r'\((.*)\)').findall(s_value)[0]
        #     iOS['deviceName'] = re.compile(r'(.*)\(').findall(s_value)[0]
        #     iOS['udid'] = re.compile(r'\[(.*?)\]').findall(s_value)[0]
        #     iOS['bundleId'] = 'xxxx'
        #
        #     device.append(iOS)

        return devices
