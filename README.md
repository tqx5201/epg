# 老张的EPG  
* 基于`python3`及`django4`的节目表数据抓取及发布系统
* 本人并非专业，很多内容只是为实现功能，可能会有很多BUG，见谅。
* 不保证后续会更新。
* DEMO地址：[老张的EPG](http://epg.51zmt.top:8000/)  

## 主要功能  
- 从网上抓取各来源的节目表信息并生成[xmltv](http://wiki.xmltv.org/) 格式文件，用于[perfect player](http://niklabs.com/) 等APP直接载入的节目表信息。
- 后台配置频道获取列表及抓取日志。
- 抓取失败时自动更换来源。
- 各数来源提供节目表的频道获取
- 提供向外发布的接口
- 使用nginx+uwsgi+MYSQL、普通办公电脑经长期测试，一天DIYP接口访问量可千万以上。  

## 节目表来源  
- 电视猫
- 搜视
- 央视
- 中数
- 台湾宽频
- 中华电信
- 香港有线宽频caletv
- 台湾四季电视
- 香港有线宽频i-cable
- 香港NOWTV
- 香港无线电视
- 北京卫视
- 广东卫视
- 香港卫视
- viutv
- 川流TV
- myTVSUPER  
## 需求  
- requests
- django
- BeautifulSoup  
## 使用方法
默认使用[sqlite3](https://www.sqlite.org/) 数据库  
### 下载源码  
```git clone http://github.com/supzhang/```  
### 抓取数据  
```python
python main.py  #抓取数据并存入数据库，可设置为定时任务
python main.py -channel #抓取所有来源的频道
python main.py -n CCTV1 #单独测试某一频道  
```
另：抓取的频道会加入Channel_list表，需要自己手动整理进Channel表中才可以抓取
![抓取](./img/crawl.png)  
### 启动后台及接口
#### 启动后台
```python
python manage.py runserver 0.0.0.0:80
```
#### 访问  
浏览器访问[http://127.0.0.1](http://127.0.0.1)查看已有数据抓取情况。  
![主页](./img/main_page.png)  
浏览器访问[http://127.0.0.1/admin](http://127.0.0.1/admin) 打开后台（用户名密码：`admin/admin`)  
- 后台首页  
![后台](./img/back.png)  
- 频道列表    
![频道列表](./img/channel1.png)  
- 修改频道   
![频道修改](./img/channel2.png)
- DIYP接口`http://127.0.0.1/api/diyp/` 需要提供参数`?ch=CCTV1&date=20230309` 
### 程序配置  
`util/general` 中有大部分配置  
`crawl_info`:需要采集的节目天数、生成xml的天数、是否需要换源等  
`dirs`:生成测试文件目录
`chuanliu_Authorization`:如果使用川流TV来源，需要提供此信息
### 其他配置  
#### 更改数据库    
`epg/settings`在此文件中修改配置如下：
```python
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '数据库名称',
            'USER': '数据库密码',
            'PASSWORD': '数据库密码',
            'HOST': '127.0.0.1',
            'PORT': '3306',
    },
}
```
#### 增加抓取来源  
`crawl/spider`在此文件夹中复制当前存在的采集程序，对其进行修改，主要设置两个方法get_epgs_xxx，get_channels_xxx
`crawl/spider/__init__.py` 中导入上面设置的方法，并参照其他来源加入：epg_funcs,epg_source,func_args,__all__  
#### 增加其他频道  
在后台“频道列表”中增加，“频道来源网站ID:”字段使用`<来源名:id>`格式设置。
****
## 捐赠
如果您觉得本项目对您有所帮助，请您多多支持，您的支持是我最大的动力，多谢。  
- 支付宝  
![支付宝](./img/alipay.jpg)  
- 微信  
![微信](./img/wechat.png)

## 其他
[列表在线转换](https://guihet.com/tvlistconvert.html)
<ul>
<li><a href="https://pan.baidu.com/s/1mhQyxhm" rel="nofollow">ip端口扫描终极版</a> (初步筛选可用ip及端口)</li>
<li><a href="http://tools.jb51.net/aideddesign/ljscq" rel="nofollow">在线正则生成批量链接</a> (不会正则，可以用在线的)</li>
<li><a href="http://wenbenbijiao.renrensousuo.com/" rel="nofollow">在线文本比较</a> (通过比较来确定同一套源的频道增减)</li>
<li><a href="http://www.downmsn.com/rjxz/23256.html" rel="nofollow">IPTV Checker</a> (初步检测http源，无条数限制)</li>
<li><a href="http://www.internetdownloadmanager.com/" rel="nofollow">IDM</a> (可检测http源，单次限制1000条，也适用于部分CDN版无法直接打开的源，成功获取ip后保存)</li>
<li><a href="https://guihet.com/blackbird-player.html" rel="nofollow">黑鸟播放器</a> (多种协议直播源检测，无条数限制，但反应稍慢，正常的源也可能出现超时情况)</li>
<li><a href="https://vlc.media/" rel="nofollow">VLC播放器</a> (用来扫rtsp双id的源不错) (另外rtsp源已知id多线程扫ip易断网，单ip多线程扫id在有些地区也易断网)</li>
<li><a href="https://guihet.com/tvlive-telelist.html" rel="nofollow">直播源列表转换</a> (转换格式供多种播放器使用)</li>
</ul>
<h3><a id="user-content-关于pltv回看" class="anchor" aria-hidden="true" href="#关于pltv回看"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>关于PLTV回看</h3>
<p>部分带PLTV的链接支持7天回看，支持回看的播放器可以直接调用，不支持的也可以通过自定义来实现回看，不过要自己查一下节目单。在地址最后加上?playseek=开始时间-结束时间 (如?playseek=20200722222222-20200722223222代表2020年7月22日22时22分22秒之后的10分钟片段)，再将地址里的PLTV改成TVOD即可播放 例:<a href="http://183.207.248.108/ott.js.chinamobile.com/PLTV/3/224/3221227581/index.m3u8" rel="nofollow">直播格式</a> <a href="http://183.207.248.108/ott.js.chinamobile.com/TVOD/3/224/3221227581/index.m3u8?playseek=20200722222222-20200722223222" rel="nofollow">回看格式</a></p>


