# author:  ZhaoKun
# contact: 1161678627@qq.com
# datetime:2019-11-01 10:29
# software: PyCharm

import re

#此处放入自己复制的请求头信息，直接从浏览器中复制即可。
headers= """
#从此处开始替换
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
#此处为替换结尾
"""
header = ''
for i in headers:
    if i == '\n':
        i = "',\n'"
    header += i
header=re.sub(': ',"': '",header)

ret=header[2:].replace(' ', '')+'\''
#结果将会输出在控制台中，直接复制用即可。
print(ret[:-4])
