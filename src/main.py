#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  : Hatanezumi
@Contact : Hatanezumi@chunshengserver.cn
'''
import os
import sys
import json
import py7zr
import requests
import webbrowser
from PySide6.QtWidgets import QApplication, QMessageBox, QFileDialog, QInputDialog, QMainWindow, QComboBox
from PySide6.QtCore import Qt, QStringListModel, Signal, QObject
from PySide6.QtGui import QColor,QIcon, QTextCursor
from ui.MainWindow import Ui_MainWindow
from threading import Thread
from src import AutoProcess

#常量
INIT = 100
REFRESH = 101
GETMODS = 200
GETMODINFO = 201
GETNEWVERSION = 202
GETUPDATELOG = 203
GETOTHER = 210
INFO = 300
WARNING = 301
CRITICAL = 302

class CustomizeSingals(QObject):
    message_box = Signal(tuple)
    set_network_page = Signal(dict)
    set_listView_Network = Signal(dict)
    set_Status_Tip = Signal(str)
    set_progressBar_Download = Signal(int)
    download_finished = Signal(str,dict)
    download_err = Signal(Exception)
    set_new_version = Signal(str)
    get_new_version_err = Signal(str)
    set_plainTextEdit_updatelog = Signal(str)
class Process():
    @staticmethod
    def set_comboBox(comboBox:QComboBox, texts:list):
        comboBox.clear()
        comboBox.addItems(texts)
    @staticmethod
    def get_cloud_data(arg, state:bool, res):
        '''
        arg:(窗口,模式,获取的内容)
        '''
        try:
            window, mode, source = arg
            singals = CustomizeSingals()
            singals.message_box.connect(window.message_box)
            singals.set_listView_Network.connect(window.set_listView_Network)
            singals.set_network_page.connect(window.set_network_page)
            singals.set_Status_Tip.connect(window.set_Status_Tip)
            singals.set_new_version.connect(window.set_new_version)
            singals.get_new_version_err.connect(window.get_new_version_err)
            singals.set_plainTextEdit_updatelog.connect(window.set_plainTextEdit_updatelog)
            if not state:
                if mode == INIT:
                    if source == GETMODS:
                        singals.set_Status_Tip.emit('获取云AR信息失败:{}'.format(res))
                    elif source == GETNEWVERSION:
                        singals.get_new_version_err.emit(res)
                    elif source == GETUPDATELOG:
                        singals.set_plainTextEdit_updatelog.emit('获取更新日志失败:{}'.format(res))
                    return    
                elif mode == REFRESH:
                    if source == GETMODS:
                        singals.message_box.emit(WARNING,'出现错误',"获取云AR信息失败:{}".format(res),QMessageBox.Ok,QMessageBox.Ok)
                    elif source == GETMODINFO:
                        singals.message_box.emit(WARNING,'出现错误',"获取mod信息失败:{}".format(res),QMessageBox.Ok,QMessageBox.Ok)
            if source == GETMODS:
                singals.set_listView_Network.emit(json.loads(res))
            elif source == GETMODINFO:
                singals.set_network_page.emit(json.loads(res))
            elif source == GETNEWVERSION:
                singals.set_new_version.emit(json.loads(res)['version'])
            elif source == GETUPDATELOG:
                singals.set_plainTextEdit_updatelog.emit(res.decode())
        except Exception as err:
            singals.message_box.emit((WARNING,'出现错误',"获取信息失败:{}".format(err),QMessageBox.Ok,QMessageBox.Ok))
    @staticmethod
    def download(window:QMainWindow,url:str,path:str,info:dict):
        signals = CustomizeSingals()
        signals.set_progressBar_Download.connect(window.set_progressBar_Download)
        signals.download_finished.connect(window.download_finished)
        signals.download_err.connect(window.download_err)
        if not os.path.exists(os.path.split(path)[0]):
            signals.download_err.emit('目录不存在:{}'.format(os.path.split(path)[0]))
            return
        try:
            res = requests.get(url, stream=True,headers={"Accept-Encoding":"identity"},timeout=10)
            size = 0#初始化已下载大小
            chunk_size = 1024#单次下载量
            content_size = int(res.headers['content-length'])#总大小
            if res.status_code == 200:
                with open(path,'wb') as file:
                    for data in res.iter_content(chunk_size=chunk_size):
                        if window.isdownloading is False:
                            file.close()
                            os.remove(path)
                            signals.set_progressBar_Download.emit(0)
                            return
                        file.write(data)
                        size += len(data)
                        signals.set_progressBar_Download.emit(int(size / content_size * 100))
            signals.download_finished.emit(path,info)
        except Exception as err:
            signals.download_err.emit(err)
    @staticmethod
    def clear_localPage_everything(window:QMainWindow):
        '''
        清除本地页面中能显示的所有的物体的内容
        '''
        window.comboBox_mods.clear()
        window.listView_local_qsl.setStringList([])
        window.listView_loaded_qsl.setStringList([])
        window.lineEdit_nowpath.setText('')
        window.label_nowdir.setText('')
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        #基础设置
        super().__init__(parent)
        self.setupUi(self)
        if os.path.exists(os.path.join(os.getcwd(),'ui','ra3.ico')):
            self.icon = QIcon(os.path.join(os.getcwd(),'ui','ra3.ico'))
            self.setWindowIcon(self.icon)
        self.version = '1.1.0'
        #--------------------------
        #连接信号
        self.comboBox_mods.currentIndexChanged.connect(self.__comboBox_mods_changed)#下拉框内容改变
        self.pushButton_R.clicked.connect(self.__on_pushButton_R_clicked)#右移按钮被按下
        self.pushButton_L.clicked.connect(self.__on_pushButton_L_clicked)#左移按钮被按下
        self.pushButton_up.clicked.connect(self.__on_pushButton_up_clicked)#上移按钮被按下
        self.pushButton_down.clicked.connect(self.__on_pushButton_down_clicked)#下移按钮被按下
        self.pushButton_save.clicked.connect(self.__on_pushButton_save_clicked)#保存按钮被按下
        self.pushButton_nowpath.clicked.connect(self.__on_pushButton_nowpath_clicked)#选择当前目录按钮被按下
        self.pushButton_add.clicked.connect(self.__on_pushButton_add_clicked)#添加文件按钮被按下
        self.pushButton_savedir.clicked.connect(self.__on_pushButton_savedir_clicked)#保存到按钮被按下
        self.listView_Network.clicked.connect(self.__on_listView_Network_clicked)#网络列表被按下
        self.pushButton_refresh.clicked.connect(self.__on_pushButton_refresh_clicked)#刷新按钮被按下
        self.pushButton_Download.clicked.connect(self.__on_pushButton_Download_clicked)#下载按钮被按下
        self.pushButton_release.clicked.connect(self.__on_pushButton_release_clicked)#发布页按钮被按下
        self.pushButton_changeDir_RA3.clicked.connect(self.__on_pushButton_changeDir_RA3_clicked)#切换到RA3目录按钮被按下
        self.pushButton_changeDir_mod.clicked.connect(self.__on_pushButton_changeDir_mod_clicked)#切换到mod目录被按下
        self.pushButton_localRefresh.clicked.connect(self.__on_pushButton_localRefresh_clicked)#本地刷新按钮被按下
        self.pushButton_changeDir_ARModLauncher.clicked.connect(self.__on_pushButton_changeDir_ARModLauncher_clicked)#切换到AR启动器目录按钮被按下
        #--------------------------
        #变量注册(全局变量)
        self.select_mod = ''
        self.listView_loaded_qsl = QStringListModel()
        self.listView_local_qsl = QStringListModel()
        self.listView_Network_qsl = QStringListModel()
        self.fileDialog = QFileDialog(self)
        self.documents_path, self.base_mod_path = AutoProcess.get_mod_path()
        self.cloud_mods = {}
        self.cloud_mod_source = (None,{})
        self.isdownloading = False
        self.selected_mod_info = {}
        self.download_info = (None,None)#第一个参数为线程,第二个参数为保存地址
        self.ra3_path = AutoProcess.get_ra3_path()
        if self.ra3_path[0] is False:
            self.ra3_path = ''
            self.pushButton_changeDir_RA3.setEnabled(False)
            QMessageBox.warning(self,'获取RA3目录失败','无法获取RA3目录,原因:{}'.format(self.ra3_path[1]),QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        else:
            self.ra3_path = self.ra3_path[1]
        self.ARModLauncher_path = AutoProcess.get_ARModLauncher_path()
        if self.ARModLauncher_path[0] is False:
            self.ARModLauncher_path = ''
            self.pushButton_changeDir_ARModLauncher.setEnabled(False)
        else:
            self.ARModLauncher_path = os.path.join(self.ARModLauncher_path[1],'Resources','CustomContent')
        #--------------------------
        #初始化内容
        self.mods = AutoProcess.get_mods(self.base_mod_path)
        if self.mods[0] is False:
            QMessageBox.warning(self,'获取mod列表失败',self.mods[1],QMessageBox.Ok,QMessageBox.Ok)
        else:
            Process.set_comboBox(self.comboBox_mods,[os.path.splitext(os.path.split(mod_name)[1])[0] for mod_name in self.mods[1]])
        self.label_about_verison.setText('当前版本:{}'.format(self.version))
        #绑定模型
        self.listView_local.setModel(self.listView_local_qsl)
        self.listView_loaded.setModel(self.listView_loaded_qsl)
        self.listView_Network.setModel(self.listView_Network_qsl)
        #显示当前目录
        self.lineEdit_nowpath.setText(self.base_mod_path)
        #获取云信息
        t = Thread(target=AutoProcess.get_cloud,args=('https://cloud.armorrush.com/Hatanezumi/RA3_affiliated_mods/raw/branch/master/mods.json',Process.get_cloud_data,(self,INIT,GETMODS)),daemon=True)
        t.start()
        #获取更新信息
        t = Thread(target=AutoProcess.get_cloud,args=('https://www.chunshengserver.cn/files/RA3mods/RA3_affiliated_mod_downloader.json',Process.get_cloud_data,(self,INIT,GETNEWVERSION)),daemon=True)
        t.start()
        #获取更新日志
        t = Thread(target=AutoProcess.get_cloud,args=('https://www.chunshengserver.cn/files/RA3mods/更新日志.txt',Process.get_cloud_data,(self,INIT,GETUPDATELOG)),daemon=True)
        t.start()
    def __comboBox_mods_changed(self):
        if self.mods[0] is False:
            return
        #显示本地列表内容
        currentIndex = self.comboBox_mods.currentIndex()#因为有重复的名称,所以采用索引匹配
        mod_path = self.mods[1][currentIndex]
        files = os.listdir(os.path.split(mod_path)[0])
        files_big = [file for file in files if os.path.splitext(file)[1] == '.big' or os.path.splitext(file)[1] == '.lyi']
        self.listView_local_qsl.setStringList(files_big)
        #显示skudef文件内容
        with open(mod_path,'r',encoding='utf-8') as file:
            file_text = file.readlines()
        file_loads = []
        for text in file_text:
            if text.startswith('add-big'):
                file_loads.append(text.split(' ',1)[1].removesuffix('\n'))
        self.listView_loaded_qsl.setStringList(file_loads)
        #显示当前文件夹
        self.label_nowdir.setText('当前文件夹:{}'.format(os.path.split(os.path.split(mod_path)[0])[1]))
        #显示保存到文件夹
        self.lineEdit_savedir.setText(os.path.split(mod_path)[0])
    def __on_pushButton_R_clicked(self):
        currentIndex = self.listView_local.currentIndex().row()
        if currentIndex == -1:
            return
        select_mod_name = self.listView_local_qsl.stringList()[currentIndex]
        if select_mod_name in self.listView_loaded_qsl.stringList():
            return
        new_listView_loaded_qsl = self.listView_loaded_qsl.stringList()
        new_listView_loaded_qsl.insert(0,select_mod_name)
        self.listView_loaded_qsl.setStringList(new_listView_loaded_qsl)
    def __on_pushButton_L_clicked(self):
        currentIndex = self.listView_loaded.currentIndex().row()
        if currentIndex == -1:
            return
        new_listView_loaded_qsl = self.listView_loaded_qsl.stringList()
        new_listView_loaded_qsl.pop(currentIndex)
        self.listView_loaded_qsl.setStringList(new_listView_loaded_qsl)
    def __on_pushButton_up_clicked(self):
        currentIndex = self.listView_loaded.currentIndex().row()
        if currentIndex == -1 or currentIndex == 0:
            return
        new_listView_loaded_qsl = self.listView_loaded_qsl.stringList()
        mod_name = new_listView_loaded_qsl.pop(currentIndex)
        new_listView_loaded_qsl.insert(currentIndex - 1,mod_name)
        self.listView_loaded_qsl.setStringList(new_listView_loaded_qsl)
    def __on_pushButton_down_clicked(self):
        currentIndex = self.listView_loaded.currentIndex().row()
        if currentIndex == -1 or currentIndex == len(self.listView_loaded_qsl.stringList()) - 1:
            return
        new_listView_loaded_qsl = self.listView_loaded_qsl.stringList()
        mod_name = new_listView_loaded_qsl.pop(currentIndex)
        new_listView_loaded_qsl.insert(currentIndex + 1,mod_name)
        self.listView_loaded_qsl.setStringList(new_listView_loaded_qsl)
    def __on_pushButton_save_clicked(self):
        mods = self.listView_loaded_qsl.stringList()
        currentIndex = self.comboBox_mods.currentIndex()
        skudef_path = self.mods[1][currentIndex]
        res = AutoProcess.save_skudef(skudef_path,mods)
        if res[0]:
            QMessageBox.information(self,'保存成功','保存成功',QMessageBox.Ok,QMessageBox.Ok)
        else:
            select = QMessageBox.critical(self,'保存失败','保存失败:{}'.format(res[1]),QMessageBox.Ok|QMessageBox.Retry,QMessageBox.Ok)
            if select == QMessageBox.Retry:
                self.__on_pushButton_save_clicked()
    def __on_pushButton_nowpath_clicked(self):
        currentIndex = self.comboBox_mods.currentIndex()
        mod_path = self.mods[1][currentIndex]
        select_path = self.fileDialog.getExistingDirectory(self,dir=os.path.split(os.path.split(mod_path)[0])[0])
        if select_path == '':
            return
        mods = AutoProcess.get_mods(select_path)
        if mods[0] is False:
            QMessageBox.warning(self,'获取mod列表失败',mods[1],QMessageBox.Ok,QMessageBox.Ok)
        else:
            self.base_mod_path = select_path
            self.mods = mods
            Process.set_comboBox(self.comboBox_mods,[os.path.splitext(os.path.split(mod_name)[1])[0] for mod_name in mods[1]])
            #显示当前目录
            self.lineEdit_nowpath.setText(select_path)
    def __on_pushButton_add_clicked(self):
        add_file_name, select = QInputDialog.getText(self,'请输入要添加的big文件名','请输入要添加的big文件名,要带".big"后缀\n如果不了解请勿随意添加')
        if not select:
            return
        if add_file_name == '':
            QMessageBox.warning(self,'错误的输入','输入内容不能为空!',QMessageBox.Ok,QMessageBox.Ok)
            return
        self.listView_loaded_qsl.setStringList([add_file_name]+self.listView_loaded_qsl.stringList())
    def __on_pushButton_savedir_clicked(self):
        now_path = self.lineEdit_savedir.text()
        if not os.path.exists(now_path):
            now_path = self.base_mod_path
        select_path = self.fileDialog.getExistingDirectory(self,dir=now_path)
        if select_path == '':
            return
        self.lineEdit_savedir.setText(select_path)
    def __on_listView_Network_clicked(self):
        currentIndex = self.listView_Network.currentIndex().row()
        select_mod_name = self.listView_Network_qsl.stringList()[currentIndex]
        if select_mod_name not in self.cloud_mods.keys():
            return
        t = Thread(target=AutoProcess.get_cloud,args=(self.cloud_mods[select_mod_name],Process.get_cloud_data,(self,REFRESH,GETMODINFO)),daemon=True)
        t.start()
    def message_box(self,arg):
        mode, title, text, Button, defaultButton = arg
        self.__message_box(mode,title,text,Button,defaultButton)
    def __message_box(self,mode:int,title:str,text:str,Button:QMessageBox.StandardButton,defaultButton:QMessageBox.StandardButton):
        if mode == INFO:
            QMessageBox.information(self,title,text,Button,defaultButton)
        elif mode == WARNING:
            QMessageBox.warning(self,title,text,Button,defaultButton)
        elif mode == CRITICAL:
            QMessageBox.Critical(self,title,text,Button,defaultButton)
    def set_network_page(self,res:dict):
        self.selected_mod_info = res
        self.label_name.setText('名称:'+res['name'])
        self.label_author.setText('作者:'+res['author'])
        self.label_version.setText('版本:'+res['version'])
        self.plainTextEdit_introduce.setPlainText(res['introduce'])
        self.cloud_mod_source = (res['name'],res['source'])
        Process.set_comboBox(self.comboBox_download,[i['name'] for i in res['source']])
    def set_listView_Network(self,res:dict):
        self.listView_Network_qsl.setStringList(res.keys())
        self.cloud_mods = res
    def set_Status_Tip(self,text:str):
        self.setStatusTip(text)
    def __on_pushButton_refresh_clicked(self):
        t = Thread(target=AutoProcess.get_cloud,args=('https://cloud.armorrush.com/Hatanezumi/RA3_affiliated_mods/raw/branch/master/mods.json',Process.get_cloud_data,(self,REFRESH,GETMODS)),daemon=True)
        t.start()
    def __on_pushButton_Download_clicked(self):
        if self.isdownloading:
            select = QMessageBox.question(self,'是否终止','确定要终止下载?已下载的进度不会被保存',QMessageBox.Yes|QMessageBox.Cancel,QMessageBox.Cancel)
            if select == QMessageBox.Yes:
                self.isdownloading = False
                self.pushButton_Download.setText('下载')
            return
        currentText = self.comboBox_download.currentText()
        if self.cloud_mod_source[0] != self.listView_Network_qsl.stringList()[self.listView_Network.currentIndex().row()]:
            return
        link = ''
        for source in self.cloud_mod_source[1]:
            if source['name'] == currentText:
                link = source['link']
        if link == '':
            return
        file_name = link.split('/')[-1]
        save_path = self.lineEdit_savedir.text()
        self.isdownloading = True
        self.pushButton_Download.setText('终止')
        t = Thread(target=Process.download,args=(self,link,os.path.join(save_path,file_name),self.selected_mod_info),daemon=True)
        self.download_info = (t,os.path.join(save_path,file_name))
        t.start()
    def set_progressBar_Download(self,value:int):
        self.progressBar_Download.setValue(value)
    def download_finished(self,path:str,info:dict):
        self.isdownloading = False
        self.progressBar_Download.setValue(0)
        in_ARModLauncher_path = False
        self.pushButton_Download.setText('下载')
        outpath = os.path.split(path)[0]
        if os.path.split(path)[0] == self.ARModLauncher_path:
            in_ARModLauncher_path = True
            outpath = os.path.join(outpath,os.path.split(path)[1].split('.')[0])
        select = QMessageBox.question(self,'下载成功','下载成功,是否自动解压?',QMessageBox.Yes|QMessageBox.Cancel,QMessageBox.Yes)
        if select == QMessageBox.Yes:
            try:
                if not os.path.exists(outpath):
                    os.mkdir(outpath)
                with py7zr.SevenZipFile(file=path,mode='r') as file:
                    file.extractall(path=outpath)
            except Exception as err:
                QMessageBox.warning(self,'解压失败','解压失败,原因:{}'.format(err),QMessageBox.Ok,QMessageBox.Ok)
                return
            else:
                QMessageBox.information(self,'解压成功','解压成功',QMessageBox.Ok,QMessageBox.Ok) 
        if in_ARModLauncher_path:
            select = QMessageBox.question(self,'是否生成配置文件','检测到当前位于AR启动器的目录中,是否生成可以被AR启动器识别的附属mod配置文件?',QMessageBox.Yes|QMessageBox.Cancel,QMessageBox.Yes)
            if select == QMessageBox.Yes:
                try:
                    mods = [i for i in os.listdir(outpath) if os.path.splitext(i)[-1].lower() == '.skudef']
                    info_keys = info.keys()
                    mod_info = {}
                    mod_info['Id'] = os.path.split(path)[1].split('.')[0]
                    mod_info['Version'] = info['version'] if 'version' in info_keys else 'None'
                    mod_info['DisplayName_CN'] = info['name'] if 'name' in info_keys else 'None'
                    mod_info['DisplayName_EN'] = info['name_EN'] if 'name_EN' in info_keys else 'None'
                    mod_info['FilePath'] = os.path.join(os.path.split(path)[1].split('.')[0],mods[0])#仅添加第一个找到的skudef文件
                    mod_info['Desc_CN'] = info['introduce'] if 'introduce' in info_keys else 'None'
                    mod_info['Desc_EN'] = info['introduce_EN'] if 'introduce_EN' in info_keys else 'None'
                    with open(os.path.join(outpath,'config.json'),'w') as file:
                        json.dump(mod_info,file)
                except Exception as err:
                    QMessageBox.warning(self,'生成失败','生成失败,原因:{}'.format(err),QMessageBox.Ok,QMessageBox.Ok)
                    return 
                else:
                    QMessageBox.information(self,'生成成功','生成成功',QMessageBox.Ok,QMessageBox.Ok) 
    def download_err(self,err:Exception):
        self.isdownloading = False
        os.remove(self.download_info[1])
        self.progressBar_Download.setValue(0)
        self.pushButton_Download.setText('下载')
        QMessageBox.warning(self,'下载失败','下载失败,原因:{}'.format(err),QMessageBox.Ok,QMessageBox.Ok)
    def set_new_version(self,version:str):
        self.label_about_newverison.setText("最新版本:"+version)
        version_int = int(version.replace('.',''))
        self_version = int(self.version.replace('.',''))
        if version_int > self_version:
            self.label_about_newverison.setText("<font color=red>最新版本:"+version+"(有更新!请点击发布页下载)</font>")
            self.setStatusTip('有新版本!({})'.format(version))
    def get_new_version_err(self,err:str):
        self.label_about_newverison.setText("<font color=red>最新版本:连接到纯世蜉生失败,原因:{}</font>".format(err))
    def __on_pushButton_release_clicked(self):
        webbrowser.open('https://cloud.armorrush.com/Hatanezumi/RA3_affiliated_mod_downloader/releases')
    def set_plainTextEdit_updatelog(self,text:str):
        self.plainTextEdit_updatelog.setPlainText(text)
    def __on_pushButton_changeDir_RA3_clicked(self):
        if self.ra3_path == '':
            self.pushButton_changeDir_RA3.setEnabled(False)
            return
        mods = AutoProcess.get_mods(self.ra3_path)
        if mods[0] is False:
            QMessageBox.warning(self,'获取mod列表失败',mods[1],QMessageBox.Ok,QMessageBox.Ok)
        else:
            self.base_mod_path = self.ra3_path
            self.mods = mods
            Process.set_comboBox(self.comboBox_mods,[os.path.splitext(os.path.split(mod_name)[1])[0] for mod_name in mods[1]])
            #显示当前目录
            self.lineEdit_nowpath.setText(self.ra3_path)
    def __on_pushButton_changeDir_mod_clicked(self):
        self.documents_path, self.base_mod_path = AutoProcess.get_mod_path()
        mods = AutoProcess.get_mods(self.base_mod_path)
        if mods[0] is False:
            QMessageBox.warning(self,'获取mod列表失败',mods[1],QMessageBox.Ok,QMessageBox.Ok)
        else:
            self.mods = mods
            Process.set_comboBox(self.comboBox_mods,[os.path.splitext(os.path.split(mod_name)[1])[0] for mod_name in mods[1]])
            #显示当前目录
            self.lineEdit_nowpath.setText(self.base_mod_path)
    def __on_pushButton_localRefresh_clicked(self):
        currentIndex = self.comboBox_mods.currentIndex()
        now_path = self.lineEdit_nowpath.text()
        if os.path.exists(now_path) is False:
            self.__on_pushButton_changeDir_mod_clicked()
            return
        mods = AutoProcess.get_mods(now_path)
        if mods[0] is False:
            QMessageBox.warning(self,'获取mod列表失败',mods[1],QMessageBox.Ok,QMessageBox.Ok)
        else:
            self.base_mod_path = now_path
            self.mods = mods
            Process.set_comboBox(self.comboBox_mods,[os.path.splitext(os.path.split(mod_name)[1])[0] for mod_name in mods[1]])
            #显示当前目录
            self.lineEdit_nowpath.setText(now_path)
            if currentIndex + 1  > self.comboBox_mods.count():
                return
            else:
                self.comboBox_mods.setCurrentIndex(currentIndex)
    def __on_pushButton_changeDir_ARModLauncher_clicked(self):
        if self.ARModLauncher_path == '':
            self.pushButton_changeDir_ARModLauncher.setEnabled(False)
            return
        self.lineEdit_savedir.setText(self.ARModLauncher_path)
def init():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
