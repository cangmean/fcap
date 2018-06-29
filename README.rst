fcap
=========
fcap是模仿了Django-admin的脚手架, 用于快速搭建和配置项目.

下载
------
通过复制下载后, 进入目录里执行以下命令安装

.. code-block:: python

    python setup.py install

简单例子
---------
执行fcap命令创建项目

.. code-block:: text

    $ fcap --project <project_name>
    或者 
    $ fcap -P <project_name> -A <app_name>

模板化
-------
每个人的项目结构可能不一样， 这个时候就需要自定义templates

.. code-block:: text
    $ fcap -T <template_path>

这个命令会把所有的.py文件改成.py-tpl, 只要把templates替换掉就可以使用自定义的模板了.