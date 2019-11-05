import requests

# 得到一个 Responsed对象
r = requests.get('https://www.baidu.com')
#显示对象类型
print(type(r))
#显示状态码
print(r.status_code)
#显示响应体i类型
print(type(r.text));
#显示内容
print(r.text)
#显示Cookies
print(r.cookies)

