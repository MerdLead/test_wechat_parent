##项目安装说明 (Liunx/Mac) windows 环境略有不同

###一、Python相关模块安装

####通过requirement文件进行文件安装

```
pip install -r requirement/base.txt

```
####建立virtualenv 虚拟环境

新建并引用虚拟目录

```
virtualenv --no-site-packages appium_env
source appium_env/bin/activate

windows 直接进入Scripts文件夹 运行activate.bat 即可

pip install -r requirement/dev.txt
```

退出虚拟目录

```
deactivate
```
