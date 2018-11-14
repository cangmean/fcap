fcap
=========
fcap是模仿了Django-admin的脚手架, 用于快速搭建和配置项目.

下载
------
通过复制下载后, 进入目录里执行以下命令安装

```
python setup.py install
```

简单例子
---------
执行fcap命令创建项目

```
$ fcap --project <project_name>
或者 
$ fcap -P <project_name> -A <app_name>
```

模板化
-------
每个人的项目结构可能不一样， 这个时候就需要自定义templates

```
$ fcap -T <template_path>
```

这个命令会把所有的.py文件改成.py-tpl, 只要把templates替换掉就可以使用自定义的模板了.


执行部署
--------
部署代码需要在服务器上进行配置, 首先需要将`config`中创建`production.py`文件来区分本地和线上环境隔离.
并在`producation.py`中写入线上的重要配置信息

```
cp default.py production.py
```
还需要将`manage.py`复制一份并改成`manage.py.old`

```
# manage.py.old

# 在配置文件中将使用线上的配置, 以上操作都是在线上环境修改
app = create_app('production')

```
修改玩之后可以使用`pm2`启动程序

```
pm2 start xxx/deploy/server.sh
```
这里`server.sh`中的项目路径需要修改成自己的, 这样项目就可以启动起来了.

每次代码更新后的自动提交需要执行`deploy.sh`脚本, 并配置脚本中的`host`和`branch`信息, 修改`deploy/remote.sh`中的`项目路径`和`pm2中的项目名称`.
以上操作只需在本地修改，如果代码存放在私有项目库无需修改, 如果代码是放在公有项目库，需要将以上所有脚本放入`.gitignore`避免上传上去.