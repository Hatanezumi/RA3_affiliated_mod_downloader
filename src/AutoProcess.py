#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  : Hatanezumi
@Contact : Hatanezumi@chunshengserver.cn
'''
import os
import winreg
import requests
import ctypes.wintypes

def get_mods(base_path:str) -> tuple[bool,str|list[str]]:
    if os.path.exists(base_path) is False:
        return (False,'未找到{}'.format(base_path))
    mod_dirs = [os.path.join(base_path,i) for i in os.listdir(base_path) if os.path.isdir(os.path.join(base_path,i))]
    mods = [os.path.join(base_path,i) for i in os.listdir(base_path) if os.path.splitext(i)[-1].lower() == '.skudef']
    if len(mod_dirs) == 0 and len(mods) == 0:
        return (False,'mod文件夹下无mod')
    for mod_dir in mod_dirs:
        mod = [os.path.join(mod_dir,i) for i in os.listdir(mod_dir) if os.path.splitext(i)[-1].lower() == '.skudef']
        mods += mod
    if len(mods) == 0:
        return (False,'mod文件夹下无mod')
    else:
        return (True,mods)
def save_skudef(skufile_path:str,mods:list) -> tuple[bool,str|None]:
    try:
        with open(skufile_path,'r',encoding='utf-8') as file:
            texts = file.readlines()
        texts = [text for text in texts if not text.startswith('add-big')]
        mods = ['add-big {}\n'.format(mod) for mod in mods]
        first_text = texts.pop(0)
        texts = mods + texts
        texts.insert(0,first_text)
        texts[-1] = texts[-1].removesuffix('\n')
        with open(skufile_path,'w',encoding='utf-8') as file:
            file.writelines(texts)
        return (True,None)
    except Exception as err:
        return (False,err)
def get_cloud(path:str, target, arg):
    try:
        req = requests.get(path)
        if req.status_code != 200:
            target(arg,False,"返回值为:{}".format(req.status_code))
            return
        res = req.content
        target(arg,True,res)
    except Exception as err:
        target(arg,False,err)
def get_ra3_path(base_reg_path:str = None) -> tuple[bool,str]:
    try:
        if base_reg_path is None:
            base_reg_path = 'SOFTWARE\\WOW6432Node'
        key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,base_reg_path + '\\Electronic Arts\\Electronic Arts\\Red Alert 3')
        dir = winreg.QueryValueEx(key,'Install Dir')
        return (True,dir[0])
    except FileNotFoundError:
        if base_reg_path == 'SOFTWARE\\WOW6432Node':
            return get_ra3_path('SOFTWARE\\')
        else:
            return (False,'未找到RA3根目录,你确定安装了吗?或尝试修复注册表')
    except Exception as err:
        return (False,err)
def get_mod_path() -> tuple[str,str]:
    '''
    返回文档路径和mod路径
    '''
    try:
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
        if buf == '':
            raise Exception('目录获取失败')
        documents_path = buf.value
    except:
        documents_path = os.path.join(os.path.splitdrive(os.environ['systemroot'])[0],os.environ['homepath'],'Documents')
    base_mod_path = os.path.join(documents_path,'Red Alert 3','Mods')
    return (documents_path,base_mod_path)