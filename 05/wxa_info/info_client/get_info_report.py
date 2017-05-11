#!/usr/bin/env python
# -*- coding: utf-8 -*-
#获取性能数据后上报到php后台


try:
    import sys
    import time
    import requests
    import json
    from pyadb import ADB

except ImportError,e:
    # should never be reached
    print "[f] Required module missing. %s" % e.args[0]
    sys.exit(-1)


def get_Info():

    while (True):
        report_data_list = []
        for i in range(1):
            try:
                # 字典是可变对象，初始化一定不能放在for循环前面
                report_data_info = {'currenttime': '', 'CPU': '', 'VMSIZE': '', 'RSS': ''}
                memoryInfo = adb.shell_command("ps | grep appbrand")
                VMSIZE = memoryInfo.split()[3]
                RSS = memoryInfo.split()[4]
                CpuInfo = adb.shell_command("top -n 1 | grep com.tencent.mm.appbrand")
                CpupercentageInfo = CpuInfo.split()[2]
                report_data_info['currenttime'] = time.time()
                report_data_info['CPU'] = CpupercentageInfo
                report_data_info['VMSIZE'] = VMSIZE
                report_data_info['RSS'] = RSS
                report_data_list.append(report_data_info)
            except:
                print "小程序进程不存在"

        report_data['info'] = report_data_list
        encode_json = json.dumps(report_data)
        requests.post(url, data=encode_json);
        print report_data_list
        report_data_list = []
        print report_data_list

# 获取当前时间，和设备name
def setTime_devices():

    currenttime_string  = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    device_name = adb.get_devices()
    devices_name_string = " ".join(list(device_name)[1])

    report_data['sessiontime'] = currenttime_string
    report_data['dev_name'] = devices_name_string


# 初始化函数
def set_init(adb_path):

    adb = ADB()
    if adb.set_adb_path(adb_path) is True:
        print "Version: %s" % adb.get_version()
    else:
        print "Check ADB binary path"
    return adb

if __name__ == "__main__":
    report_data = {'sessiontime': '', 'dev_name': '', 'info': ''}

    adb_path = "D:\\androidtest\\sdk\\sdk\\platform-tools\\adb.exe"
    url = "http://wxa.jd.com/wxatest/php/report_memory_cpuInfo.php"

    adb = set_init(adb_path)
    setTime_devices()
    get_Info()




