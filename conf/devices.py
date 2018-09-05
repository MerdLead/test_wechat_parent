
# coding=utf-8
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
        for v in value.readlines():   # TODO 暂时修改为只获取一个模拟器设备
            android = {}
            s_value = str(v).replace("\n", "").replace("\t", "")
            if s_value.rfind('device') != -1 and (not s_value.startswith("List")) and s_value != "":
                android['platformName'] = 'Android'
                android['deviceName'] = s_value[:s_value.find('device')].strip()
                android['package'] = 'com.vanthink.student.debug'
                android['platformVersion'] = gv.PLATFORM_VER
                android['app'] = PATH(gv.APP)
                android["recreateChromeDriverSessions"] = True
                # android['package'] = 'com.vanthink.student.debug'
                # android['appActivity'] = "com.vanthink.vanthinkstudent.v2.ui.splash.SplashActivity"
                android["automationName"] = "uiautomator2"
                android["unicodeKeyboard"] = True
                android["resetKeyboard"] = True
                android["noReset"] = True

                devices.append(android)
        return devices

    def start_android_devices(self):
        """启动安卓模拟器"""
        command = r'start D:\Program" "Files" "\Nox\bin\Nox.exe'
        os.system(command)
        # time.sleep(10)
        print('模拟器启动成功')
        adb = 'adb devices'
        os.system(adb)
        print('\n')

    def stop_android_devices(self):
        """结束安卓模拟器进程"""
        command = r'taskkill -f -im Nox.exe'
        os.system(command)
        print('所有任务执行完毕，关闭模拟器')
        print('\n')
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

