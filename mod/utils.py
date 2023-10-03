import math
import random
from datetime import datetime as dt
import os

def mt_sqrt(x):
    return math.sqrt(x)

def mt_sinpi():
    return math.sin(math.pi / 2)

def mt_log():
    return math.log(math.e)

def mt_exp(x):
    return math.exp(x)

def mt_pi():
    return math.pi
#==========================================

def rd_int(x, y) :
    return random.randint(x, y)

def rd_list(this) :
    return random.choice(this)

def rd_rd() :
    return random.random()

def rd_nmvar() :
    return random.normalvariate(0, 1)
#===========================================

def get_dtnow():
    return dt.now()

def cvt_time2str(objtime):
    return dt.strptime(objtime, "%Y-%m-%d")
                       
def cvt_str2time():
    obj = dt.now()
    return obj.strftime("%Y-%m-%d")

#============================================

def get_curdir():
    return os.getcwd()

def os_mkdir(pname):
    return os.mkdir('pname')

def os_rmdir(pname):
    return os.rmdir('pname')
    
    
    
    
""" date_string = '2021-07-00'
date_object = dt.strptime(date_string, '%Y-%n-%d')
print(date_object)

#날짜를 문자열로 변환
date_object = dt.now()
date_string = date_object.strftime('%Y-%n-%d')
print(date_string)
 """
