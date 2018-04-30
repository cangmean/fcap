# -*- coding: UTF-8 -*-
# 加密

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

KEY = b'ZTJmODExOThhMTM5OTgwZDljYjQ0MTA5ZWZkNDk5OGY='


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


def wrap_encode(input_func=None, output_func=None):
    """
    :param input_func: 输入时候的字符编码
    :param output_func: 输出时候的字符编码
    :return: 编码后的密码
    """
    def wrap_func(func):

        def deco(*args, **kw):
            # 指定输入编码
            text = input_func(args[0]) if input_func else args[0]
            args = (text, ) + args[1:]
            # 返回结果
            ret = func(*args, **kw)
            # 指定返回编码
            ret = output_func(ret) if output_func else ret
            return ret
        return deco
    return wrap_func


@wrap_encode(input_func=to_bytes)
def valid_key(text):
    """ 有效的密钥"""
    length, count = 16, len(text)
    add = length - (count % length)
    text += b'\0' * add
    return text


@wrap_encode(to_bytes, to_string)
def encrypt(text, salt=None):
    """ 加密"""
    text = valid_key(text)
    salt = valid_key(salt) if salt else KEY[:16]
    crypt = AES.new(KEY[:16], AES.MODE_CBC, salt)
    plain_text = crypt.encrypt(text)
    return b2a_hex(plain_text)


@wrap_encode(to_bytes, to_string)
def decrypt(text, salt=None):
    """ 解密"""
    salt = valid_key(salt) if salt else KEY[:16]
    crypt = AES.new(KEY[:16], AES.MODE_CBC, salt)
    plain_text = crypt.decrypt(a2b_hex(text))
    plain_text = plain_text.rstrip(b'\0')
    return plain_text


if __name__ == '__main__':
    x = encrypt('123123', salt='hello')
    print(x)
    d = decrypt('bc9c65472eafec58a40b5b699d784cbe', salt="896351")
    print(d)
