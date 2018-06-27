# coding=utf-8

import os
from fabric.api import run, local, env, cd, lcd, put, hosts, roles, execute

"""
curr_dir 当前文件所在目录
base_dir 当前项目的父目录
project  当前项目文件名

upload_file 上传的压缩文件
excludes  排除的文件和文件夹

project_path 项目路径
virtualenv_path    虚拟环境路径
nginx_path nginx路径
supervisor_path supervisor路径
"""
curr_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(curr_dir)
PROJECT = curr_dir.split('/')[-1]

upload_file = '{}.tar.gz'.format(PROJECT)
excludes = []

project_path = ''
virtualenv_path = ''
nginx_path = ''
supervisor_path = ''


env.roledefs = {
    'dev': [''],
    'prod': [''],
}
env.password = ''


class Deploy(object):

    pass


class Sync(object):

    def init_app(self):
        with cd('~/{}'.format(PROJECT)):
            run('../v3/bin/python manage.py init')

    def drop_app(self):
        with cd('~/{}'.format(PROJECT)):
            run('../v3/bin/python manage.py drop_db')

    def local_setting(self):
        """
        本地目录配置
        """
        with lcd(base_dir):
            local('tar zcvf {0} {1}'.format(upload_file, PROJECT))
            put(upload_file, '~/{}'.format(upload_file))
            local('rm {0}'.format(upload_file))

    def server_setting(self):
        """
        服务器目录配置
        """
        with cd('~/'):
            run('tar zxvf {}'.format(upload_file))
            run('rm {}'.format(upload_file))

    def etc_setting(self):
        """
        配置系统文件: nginx supervisor
        """
        self.nginx_setting()
        self.supervisor_setting()

    def nginx_setting(self):
        with cd('~/{}/etc'.format(PROJECT)):
            run('cp nginx.conf /etc/nginx/conf.d/{}.conf'.format(PROJECT))
        run('nginx -s reload')

    def supervisor_setting(self):
        with cd('~/{}/etc'.format(PROJECT)):
            run('cp supervisor.conf /etc/supervisor/{}.conf'.format(PROJECT))

        run('supervisorctl reread')
        run('supervisorctl update')
        run('supervisorctl restart {}'.format(PROJECT))

    def reload_server(self):
        run('supervisorctl restart {}'.format(PROJECT))


@roles('dev')
def test():
    sync = Sync()
    sync.local_setting()
    sync.server_setting()


@roles('prod')
def go():
    sync = Sync()
    sync.local_setting()
    sync.server_setting()



@roles('prod')
def drop_db():
    sync = Sync()
    sync.drop_app()
