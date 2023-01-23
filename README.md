# 班级小管家文件 / 图片上传服务

这是一个来自 [z0z0r4/xinger-api](https://github.com/z0z0r4/xinger-api) 的 Fork。

此 Fork 只保留了班级小管家的上传功能。支持图片上传和文件上传，分别为`imageupload.py` 和 `fileupload.py`。

通过 `pip install -r requirements.txt` 安装前置库。

使用前必须注册班级小管家，并创建教师角色。在相册网盘中查看您 `OSS` 的 Cookie，并写入 `cookie.txt` 中。他应该长得像一个 JSON 文件。

```cookie
{COOKIE_OF_OSS}
```

<https://banjixiaoguanjia.com/public/website/index.html#page1/1>

> **Warning**  
> 已知图片直接返回 OSS 的 RedirectResponse 导致浏览器直接访问 api 时会直接下载。但是不会影响作为图床使用。

请在克隆仓库时务必加上 `--depth=1` 参数，否则会爆炸。

`git clone --depth=1 https://github.com/Nofated095/xinger-api.git`
