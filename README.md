# SouthPlus签到
## 源代码来自只会用BurpSuite的我和神通广大的ChatGPT
### 感谢[能把Curl转换成各种语言的网站](https://curlconverter.com/),感谢万能的[ChatGPT](https://poe.com/ChatGPT),感谢优秀的渗透工具[BurpSuite](https://portswigger.net/burp)感谢大毛病不多，小毛病不断的浏览器[Chromium](https://www.chromium.org/chromium-projects/)及[Google Chrome](https://www.google.com/chrome/)
## 使用方法
1.支持Server酱推送，将**SCKEY**添加到**Action Secrets**  
2.将**COOKIE**添加到**Action Secrets**  
3.添加了定时任务，会在每天北京时间凌晨一点运行  
4.低调使用，避免迭代  
## 开发过程
1.安装PyCharm，安装BurpSuite  
2.使用BurpSuite抓包，登录到领取任务页面，打开拦截，F12开启录制请求，点击“领取任务”  
3.查看并复制已录制请求，粘贴到翻译网站获得Python代码，查看拦截内容，复制其中“Cookie”字段的值，询问ChatGPT获得将Cookie转化为请求格式的代码  
4.将两段代码融合，并加上从系统变量提取Cookie的代码，即可完成四个执行脚本之一，其余三个脚本以此类推完成  
5.在BurpSuite中丢弃请求，关闭拦截，运行代码，刷新页面检查任务是否成功领取  
6.询问ChatGPT得到处理及融合个脚本输出的代码，与Server酱的官方Python实例融合，得到控制脚本  
7.询问ChatGPT得到GitHubAction配置文件，放置于“.github/workflows”文件夹内  
8，将项目上传GitHub  
## 缺点   
1.url的请求参数里有名为vwerify的验证参数，分析页面内容可获取，暂时不知道有什么用，以及会不会改变  
2.url的请求参数还有个时间戳，问了ChatGPT，暂时整不了  
3.Server酱的推送花钱才能看内容，后期将切换到其他平台，或者采用标题显示成败，内容显示详细的方式  
4.整个项目基本上都是依赖ChatGPT写的，所以**你提issues≠我会维护**，有公式做题就是快
## 以上内容完成于23/12/13，19:32  
