import os
import subprocess
import re
import asyncio


process_1 = subprocess.Popen(['python', 'APPLYDAILY.py'], stdout=subprocess.PIPE)
output_1, _ = process_1.communicate()

process_2 = subprocess.Popen(['python', 'COLLECTDAILY.py'], stdout=subprocess.PIPE)
output_2, _ = process_2.communicate()

process_3 = subprocess.Popen(['python', 'APPLYWEEKLY.py'], stdout=subprocess.PIPE)
output_3, _ = process_3.communicate()

process_4 = subprocess.Popen(['python', 'COLLECTWEEKLY.py'], stdout=subprocess.PIPE)
output_4, _ = process_4.communicate()

response_text1 = output_2.decode()

if re.search(r"完成", response_text1):
    title1 = "南+ 日常成功，"
else:
    title1 = "南+ 日常失败，"

response_text2 = output_4.decode()

if re.search(r"成功", response_text1):
    title2 = "周常成功，"
else:
    title2 = "周常失败，"


# 合并输出为一个变量
merged_content = output_1.decode() + output_2.decode() + output_3.decode() + output_4.decode()
merged_title = title1 + title2

print(merged_title)
print(merged_content)


from telegram import Bot

bot_token = os.environ.get('BOTTOKEN')
chat_id = os.environ.get('USERID')

# 创建 Bot 实例
bot = Bot(token=bot_token)

# 发送消息
async def send_message():
    await bot.send_message(chat_id=chat_id, text=merged_title + '\n' + merged_content)

# 运行异步函数
asyncio.run(send_message())
