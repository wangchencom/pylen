# -*- coding: utf-8 -*-
# coding:utf-8
#python中的字符串
#编码 python 使用的是 Unicode 也就是 兼容大多数编码

# 单个字的编码 
# 获取字符的整数表示
print(ord('a'))
# 把编码转换为对应字符
print(chr(ord('a')))

# str可以转换编码为指定的bytes
print('ABC'.encode('ascii'))
print(type('ABC'.encode('ascii')))

print('中文'.encode('utf-8'))
# 把中文转换为awcii就报错了 因为编码不支持
print('中文'.encode('ascii'))
# Traceback (most recent call last):
#   File "c:\Workspaces\vscode\pylen\Basics\tempCodeRunnerFile.py", line 1, in <module>
#     print('����'.encode('ascii'))
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

# python 里 python str类型 转为 byte类型 
strToByte = b'byte'
print(type(strToByte))
# python 里  byte 转为 str类型 
byteToByte = b'byte'.decode('ascii')
print(byteToByte)
print(type(byteToByte))

CNToStr =  b'\xe4\xb8\xad\xe6\x96\x87\f'.decode('utf-8')
print(CNToStr)
print(type(CNToStr))







