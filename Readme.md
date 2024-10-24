# 文件自动上传1.0----上传单个文件

mark一下成就感+1

## 环境配置

```
pip install selenium,toml,pyautogui,pyperclip
```

根据自己的chrome版本，设置-关于chrome-版本，根据自用系统下载对应的chromedriver

python版本不要太低就行

## 配置信息

config.toml

本文件为用户配置文件
在credentials，填入用户名、密码
在settings，knowledge_warehouse中填入你想选择的知识库,

import_way中选择你想导入的板块，由数字代号

file_path中复制你本地的文件地址


## 运行入口

```
python main.py
```

## Next

有需求做2.0，没需求就吃灰

记录下我对客户端和服务器端的初步理解
