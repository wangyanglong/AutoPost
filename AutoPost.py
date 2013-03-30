#!/usr/bin/env python
#encoding=utf-8
from re import *
import urllib
import urllib2
import cookielib
import datetime
import time
import getpass
class AutoPost():
	def __init__(self,email,password):
		self.email=email
		self.password=password
		self.domain='renren.com'
		try:
			cookie=cookielib.CookieJar()  
			cookieProc=urllib2.HTTPCookieProcessor(cookie)  
		except:
			raise
		else:
			opener=urllib2.build_opener(cookieProc)  
			urllib2.install_opener(opener) 

	def Login(self):
		print 'Login...'
		url='http://www.renren.com/PLogin.do'  
		postdata={  
          	  'email':self.email, 
                 'password':self.password,  
                 'domain':self.domain,  
                 }  
		req=urllib2.Request(  
                           url,  
                           urllib.urlencode(postdata)             
                           )  
          
		PreContent=urllib2.urlopen(req).read()
		self._rtk=(split(',',split(':',split('get_check_x',PreContent,1)[1],1)[1],1)[0])[1:9]
		self.ids=(split(',',split("'id':",PreContent,1)[1],1)[0])[1:10]
		self.RequestToken=(split(',',split('get_check:',PreContent,1)[1],1)[0])[1:10]
		print 'Login succeed!'

	def Publish(self,content):
		url='http://shell.renren.com/'+self.ids+'/status'
		postdata={
					'_rtk':self._rtk,
					'channel':'renren',
					'content':content,
					'hostid':self.ids,
					'requestToken':self.RequestToken,
					
		}
		req=urllib2.Request(url,urllib.urlencode(postdata))
		self.result=urllib2.urlopen(req).read()
		print '%s:\n帐号为%s的人人网用户发了一条状态\n内容为：(%s)'%(datetime.datetime.now(),self.email,postdata.get('content',''))
if __name__ =='__main__':
	email=raw_input('请输入您的人人网登录帐号，按回车键结束：')
	password=getpass.getpass('请输入您的人人网登录密码，按回车键结束：')
	renrenAutoPost=AutoPost(email,password)
	renrenAutoPost.Login()
	content=raw_input('请输入您需要发布的状态，按回车键结束：')
	renrenAutoPost.Publish(content)
