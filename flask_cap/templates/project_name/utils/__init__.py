"""
公共函数
"""

import os
import re
import time
import random
import string
import datetime
import xlwt
from {{ project_name }}.config import DOWN_DIR

# pylint: disable=all


def get_current_time(fmt="%F %T"):
    """ 获取当前时间字符串"""
    return datetime.datetime.now().strftime(fmt)


def get_code(length=6, code_type='int'):
    """ 获取短信验证码
    :param length: 返回长度
    :param code_type: 返回类型
    """
    alpha = string.digits if code_type == 'int' else string.ascii_lowercase
    code = random.sample(alpha, length)
    code = ''.join(code)
    return code


def get_time():
    """ 获取时间戳"""
    return int(time.time())


def to_bytes(text):
    """ 转成bytes"""
    if isinstance(text, str):
        text = text.encode('utf8')
    return text


def to_string(text):
    """ 转成string"""
    if isinstance(text, bytes):
        text = text.decode('utf8', 'ignore')
    return text


def line_to_camel(text):
    """ 驼峰"""
    pattern = re.compile(r'(_\w)')
    sub = re.sub(pattern, lambda _map: _map.group(1)[1].upper(), text)
    return sub


def camel_to_line(text):
    """ 下划线"""
    pattern = re.compile(r'([a-z]|\d)([A-Z])')
    sub = re.sub(pattern, r'\1_\2', text).lower()
    return sub


def make_excel(title, headers, datas, filename='info.xls'):
    """ 创建excel"""
    wb = xlwt.Workbook()
    ws = wb.add_sheet(title)
    for idx, header in enumerate(headers):
        ws.write(0, idx, header)

    for row, data in enumerate(datas, 1):
        for col, d in enumerate(data):
            ws.write(row, col, d)
    
    if not os.path.exists(DOWN_DIR):
        os.mkdir(DOWN_DIR)
    path = os.path.join(DOWN_DIR, filename)
    wb.save(path)
    return path
    

if __name__ == '__main__':
    print(camel_to_line('hello'))
