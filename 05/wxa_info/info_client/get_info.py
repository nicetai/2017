#!/usr/bin/env python
# -*- coding: utf-8 -*-
#获取性能数据后写入到本地文件中


try:
    import sys
    import time
    from pyadb import ADB

except ImportError,e:
    # should never be reached
    print "[f] Required module missing. %s" % e.args[0]
    sys.exit(-1)

def get_MemoryInfo():

    #currenttime_string, filename = setTime_devices()
    f = open('./data/memory/' + filename + '.txt', 'w')
    while (True):
    #for i in range(10):
        try:
            memoryInfo = adb.shell_command("ps | grep appbrand2")
            VMSIZE = memoryInfo.split()[3]
            RSS = memoryInfo.split()[4]
            VMSIZE_mb = str(int(VMSIZE)/1024)
            RSS_mb = str(int(RSS)/1024)
            memory_string = currenttime_string+"---VMSIZE:"+VMSIZE_mb+"MB---RSS:"+RSS_mb+"MB\n"
            f.write(memory_string)
            f.flush()
        except:
            print "小程序进程不存在"
            f.close()
    f.close()



def get_CpuInfo():

    #currenttime_string, filename = setTime_devices()
    f = open('./data/cpu/' + filename + '.txt', 'w')
    while(True):
    #for i in range(10):
        try:
            CpuInfo = adb.shell_command("top -n 1 | grep com.tencent.mm.appbrand")
            CpupercentageInfo = CpuInfo.split()[2]
            cpu_string = currenttime_string+"---"+"CpupercentageInfo:"+CpupercentageInfo+"---"+"\n"
            f.write(cpu_string)
            f.flush()
        except:
            print "小程序进程不存在"
            f.close()
    f.close()

def get_Info():

    #currenttime_string, filename = setTime_devices()
    f = open('./data/' + filename + '.txt', 'w')
    while (True):
        for i in range(10):
            try:
                memoryInfo = adb.shell_command("ps | grep appbrand")
                VMSIZE = memoryInfo.split()[3]
                RSS = memoryInfo.split()[4]
                VMSIZE_mb = str(int(VMSIZE)/1024)
                RSS_mb = str(int(RSS)/1024)
                memory_string = currenttime_string+"---VMSIZE:"+VMSIZE_mb+"MB---RSS:"+RSS_mb+"MB\n"
                CpuInfo = adb.shell_command("top -n 1 | grep com.tencent.mm.appbrand2")
                CpupercentageInfo = CpuInfo.split()[2]
                cpu_string = currenttime_string + "---" + "CpupercentageInfo:" + CpupercentageInfo + "---" + "\n"
                f.write(cpu_string)
                f.write(memory_string)
            except:
                print "小程序进程不存在"
                f.close()
        f.flush()
    f.close()

# 获取当前时间，和设备name
def setTime_devices():
    global currenttime_string
    currenttime_string   = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    device_name = adb.get_devices()
    devices_name_string = " ".join(list(device_name)[1])
    global filename
    filename  = currenttime_string + "_" + devices_name_string

# 初始化函数
def set_init(adb_path):

    adb = ADB()
    if adb.set_adb_path(adb_path) is True:
        print "Version: %s" % adb.get_version()
    else:
        print "Check ADB binary path"
    return adb

if __name__ == "__main__":
    adb_path = "D:\\androidtest\\sdk\\sdk\\platform-tools\\adb.exe"
    adb = set_init(adb_path)
    setTime_devices()
    get_Info()