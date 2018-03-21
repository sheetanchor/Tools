#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/17 下午4:53
# @Author  : Anchor
# @File    : encode.py
# @Des     : 加密

from Crypto.Cipher import AES
from binascii import b2a_hex

#补全字符
def align(str,isKey=False):
    #如果接受的字符串是密码，需要确保其长度为16
    if isKey:
        if len(str) > 16:
            return str[1:16]
        else:
            return align(str)
    #如果接受的字符串是明文或长度不足的密码，确保其长度为16的整数倍
    else:
        zerocount = 16 - len(str) % 16
        for i in range(0,zerocount):
            str = str + '\0'
        return str

#CBC模式加密
def encrypt_CBC(str,key):
    #补全字符串
    str = align(str)
    key = align(key,True)
    #初始化AES，引入初始向量
    AESCipher = AES.new(key,AES.MODE_CBC,'1234567890123456')
    #加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)




if __name__ == '__main__':
    print(encrypt_CBC('aaa','bbb'))