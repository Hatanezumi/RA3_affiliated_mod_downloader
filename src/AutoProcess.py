#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  : Hatanezumi
@Contact : Hatanezumi@chunshengserver.cn
'''
import os
import json
import requests

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
        res = json.loads(req.content)
        target(arg,True,res)
    except Exception as err:
        target(arg,False,err)