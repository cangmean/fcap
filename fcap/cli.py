import os
import sys
import click
import shutil
from jinja2 import Environment, select_autoescape, FileSystemLoader

# pylint: disable=all

base_path = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(base_path, 'templates')

env = Environment(
    loader=FileSystemLoader(templates_path),
    autoescape=select_autoescape(
        default_for_string=True,
        default=True,
    )
)


class ProjectMaker(object):
    """ 项目脚手架
    """

    rewrite_template_suffixes = (
        ('.py-tpl', '.py'),
    )
    
    def __init__(self, project_name, app_name, base_name='project_name'):
        """
        :param project_name: 新建的项目名称
        :param app_name: 新建项目中app的名称
        :param base_name: 覆盖的变量 {{ project_name }}
        :param prefix_length: 路径前缀
        """
        self.base_name = base_name
        self.project_name = project_name
        self.app_name = app_name
        self.prefix_length = len(templates_path) + 1
    
    @property
    def top_dir(self):
        """ 项目的顶级目录
        """
        return os.path.join(
            os.getcwd(), self.project_name,
        )
    
    def render_templates(self, path):
        """ 渲染函数
        :param path: 模板目录
        """
        # 参考了 https://github.com/django/django/blob/master/django/core/management/templates.py#L120
        prefix_length = len(templates_path) + 1
        for root, dirs, files in os.walk(path):
            # 获取相对文件路径
            path_rest = root[prefix_length:]
            # 修改子目录名称为app_name
            relative_dir = path_rest.replace(
                self.base_name,
                self.app_name
            )
            # 如果相对目录不存在则创建
            if relative_dir:
                target_dir = os.path.join(self.top_dir, relative_dir)
                if not os.path.exists(target_dir):
                    os.mkdir(target_dir)

            # 清除隐藏文件和缓存文件
            for dirname in dirs[:]:
                if dirname.startswith('.') or dirname == '__pycache__':
                    dirs.remove(dirname)
            
            for filename in files:
                if filename.endswith(('.pyo', '.pyc', '.py.class')):
                    # Ignore some files as they cause various breakages.
                    continue
                # 模板文件路径, 和需要生成文件路径
                old_path = os.path.join(root, filename)
                new_path = os.path.join(
                    self.top_dir,
                    relative_dir,
                    filename.replace(
                        self.base_name,
                        self.app_name,
                    )
                )
                # 将.py-tpl文件重命名成.py文件
                for old_suffix, new_suffix in self.rewrite_template_suffixes:
                    if new_path.endswith(old_suffix):
                        new_path = new_path[:-len(old_suffix)] + new_suffix
                        break  # Only rewrite once

                _template = env.get_template(
                    os.path.join(path_rest, filename)
                )
                kw = {
                    self.base_name: self.app_name
                }
                content = _template.render(**kw)
                with open(new_path, 'w', encoding='utf-8') as fd:
                    fd.write(content)

    def make(self):
        if os.path.exists(self.top_dir):
            raise FileExistsError(
                '{} already exists.'.format(self.project_name)
            )
        else:
            os.mkdir(self.top_dir)
        self.render_templates(templates_path)
    
    @classmethod
    def _make_templates(cls, path):
        """ 将目录加载成templates格式的文件"""
        for root, dirs, files in os.walk(path):
            for filename in files:
                if not filename.endswith('.py'):
                    continue
                file_path = os.path.join(root, filename)
                new_file_path = file_path[:-3] + '.py-tpl'
                os.rename(file_path, new_file_path)


@click.command()
@click.option('-P', '--project', help='make a project.')
@click.option('-A', '--app', help='set a app name.')
@click.option('-T', '--templates', help="load template path")
def make_app(project, app, templates):
    if templates:
        ProjectMaker._make_templates(templates)
        return
    if not project:
        click.echo('Project name is not defined.')
        return
    if not app:
        app = project
    pm = ProjectMaker(project, app)
    pm.make()


def main():
    make_app()

if __name__ == '__main__':
    main()
