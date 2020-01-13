#  输出多个字符串   遇到逗号输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')


# 输出整数 或者输出 计算结果
print(100)
print(100+100)

# ps: 转义字符 \    \n换行   \t制表符
print('I\'m ok')

print('I\'m learning \nhello python ')

# 如果字符串里面 很多 字符都需要转义 就需要加很多 '/'  python提供了 一种简单的方法 r''  ''里面的内内容默认不转义
print('11\t11')
print(r'11\t11') # 输出显示 11\t11 转义符失效

#如果字符串内容很多不方便阅读      
# ***交互式命令行内

# │>>> print('''line1                                      │
# │... line2                                               │
# │... line3''')                                           │
# │line1                                                   │
# │line2                                                   │
# │line3                                                   │
# │                                                        │
# │>>> _  

# 文件内就是
print('''line1
line2
line3''')