import xlrd
import subprocess
import time
import os
import multiprocessing


def read_IP():
    IPList = xlrd.open_workbook('计算机和打印机IP地址统计表20210414.xls')

    sheet1 = IPList.sheets()[0]

    nrows = sheet1.nrows

    print('表格总行数', nrows)

    ncols = sheet1.ncols

    print('表格总列数', ncols)

    row3_values = sheet1.row_values(2)

    print('第3行值', row3_values)

    col3_values = sheet1.col_values(2)

    print('第3列值', col3_values)

    cell_5_5 = sheet1.cell(4, 4).value

    print('第5行第5列的单元格的值：', cell_5_5)
    IPList = []  # 存储各行IP信息

    line = 0

    while line < sheet1.nrows:
        IPList.append(sheet1.cell(line, 3).value)
        line = line + 1

    print(IPList)

    print(len(IPList))

    print(sheet1.nrows)

    print(line)
    OFIPList = []
    for ip in IPList:
        if "10.204" in ip:
            print(ip)
            OFIPList.append(ip)
            # ks = int(time.time())  # 记录开始时间
    return OFIPList


def check_alive(ip):
    result = subprocess.call('ping -w 1000 -n 1 %s' % ip, stdout=subprocess.PIPE, shell=True)
    if result == 0:
        h = subprocess.getoutput('ping ' + ip)
        returnnum = h.split('平均 = ')[1]
        info = ('\033[32m%s\033[0m 能ping通，延迟平均值为：%s' % (ip, returnnum))
        print('\033[32m%s\033[0m 能ping通，延迟平均值为：%s' % (ip, returnnum))
        return info
    else:
        # with open('notong.txt', 'a') as f:
        #     f.write(ip)
        info = ('\033[31m%s\033[0m ping 不通！' % ip)
        print('\033[31m%s\033[0m ping 不通！' % ip)
        return info


def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec



if __name__ == '__main__':
    # 这是隔5秒执行一次
    second = sleeptime(0, 0, 300)
    while 1 == 1:
        time.sleep(second)
        print('do action')
        print("开始批量ping所有IP！")
        OFIPList = read_IP()
        for ip in OFIPList:
            p = multiprocessing.Process(target=check_alive, args=(ip,))
            p.start()


    # with open('ip.txt', 'r') as f:  # ip.txt为本地文件记录所有需要检测连通性的ip
    #     for i in f:
    #         p = multiprocessing.Process(target=check_alive, args=(i,))
    #         p.start()
