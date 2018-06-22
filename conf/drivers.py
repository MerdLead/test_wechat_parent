import time
from multiprocessing import Pool
from macaca import WebDriver

from conf.ports import Ports
from conf.devices import Devices
from conf.macaca_server import MacacaServer
from conf.run_cases import RunCases
from conf.report_path import ReportPath
from conf.base_page import BasePage
from conf.log import Log
from conf.login_status import LoginStatus


class Drivers:
    @staticmethod
    def _run_cases(server_url, run, cases):
        log = Log()
        log.set_logger(run.get_device()['deviceName'], run.get_path() + '\\' + 'client.log')
        log.i('platformName: %s', run.get_device()['platformName'])
        log.i('platformVersion: %s', run.get_device()['platformVersion'])
        log.i('deviceName: %s', run.get_device()['deviceName'])
        log.i('app: %s', run.get_device()['app'])
        log.i('package: %s', run.get_device()['package'])
        log.i('activity: %s', run.get_device()['activity'])
        log.i('chromeOptions: %s', run.get_device()['chromeOptions'])
        log.i('unicodeKeyboard: %s', run.get_device()['unicodeKeyboard'])
        log.i('resetKeyboard: %s', run.get_device()['resetKeyboard'])
        log.i('reuse: %s', run.get_device()['reuse'])

        log.i('macaca server port: %d\n', run.get_port())

        # init driver
        driver = WebDriver(run.get_device(), server_url)
        driver.init()

        # set cls.path, it must be call before operate on any page
        path = ReportPath()
        path.set_path(run.get_path())

        login_status = LoginStatus()
        login_status.set_status(False)

        # set cls.driver, it must be call before operate on any page
        base_page = BasePage()
        base_page.set_driver(driver)

        try:
            # run cases
            run.run(cases)
        except AssertionError as e:
            log.e('AssertionError, %s', e)

        # quit driver
        driver.quit()

    def run(self, cases):
        # read all devices on this PC
        devices = Devices().get_devices()

        # read free ports on this PC
        ports = Ports().get_ports(len(devices))

        if not len(devices):
            print('there is no device connected this PC')
            return

        runs = []
        for i in range(len(devices)):
            runs.append(RunCases(devices[i], ports[i]))

        # start macaca server
        macaca_server = MacacaServer(runs)
        macaca_server.start_server()

        # run on every device
        pool = Pool(processes=len(runs))
        for run in runs:
            pool.apply_async(self._run_cases,
                             args=(macaca_server.server_url(run.get_port()), run, cases,))

            # fix bug of macaca, android driver can not init in the same time
            time.sleep(2)

        pool.close()
        pool.join()

        macaca_server.kill_macaca_server()
