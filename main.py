import os
import urllib.parse
import urllib.request
import subprocess

def sc_send(text, desp='', key=os.getenv('SCKEY')):
    postdata = urllib.parse.urlencode({'text': text, 'desp': desp}).encode('utf-8')
    url = f'https://sctapi.ftqq.com/{key}.send'
    req = urllib.request.Request(url, data=postdata, method='POST')
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
    return result

process_1 = subprocess.Popen(['python', 'APPLYDAILY.py'], stdout=subprocess.PIPE)
output_1, _ = process_1.communicate()

process_2 = subprocess.Popen(['python', 'COLLECTDAILY.py'], stdout=subprocess.PIPE)
output_2, _ = process_2.communicate()

process_3 = subprocess.Popen(['python', 'APPLYWEEKLY.py'], stdout=subprocess.PIPE)
output_3, _ = process_3.communicate()

process_4 = subprocess.Popen(['python', 'COLLECTWEEKLY.py'], stdout=subprocess.PIPE)
output_4, _ = process_4.communicate()

# 合并输出为一个变量
merged_output = output_1.decode() + output_2.decode() + output_3.decode() + output_4.decode()

# 打印合并后的输出
print(merged_output)

ret = sc_send('SouthPlus签到提示', merged_output)
print(ret)