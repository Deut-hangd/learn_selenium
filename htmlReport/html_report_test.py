import unittest
import os, sys
import time
import HTMLTestRunner

def createsuite():
   discover = unittest.defaultTestLoader.discover('./seleniumT/seleniumT01/unittestTests', pattern='unittestT*.py', top_level_dir=None)
   print(discover)
   return discover

if __name__ == '__main__':
    curpath = sys.path[0]
    now = time.strftime('%Y-%m-%d-%H %M %S', time.localtime(time.time()))
    if not os.path.exists(curpath+'/resultreport'):
        os.makedirs(curpath+'/resultreport')

    filename=curpath+'/resultreport/'+now+'resultreport.html'
    with open(filename, 'wb') as fp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况',verbosity=2)
        suite=createsuite()
        runner.run(suite)