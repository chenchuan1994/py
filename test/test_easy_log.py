# import pytest
from log.easy_log import easyLog

def test_log():
    path = '/Users/chuan/Software/ccpy/py/test'
    elog = easyLog(path)
    l = elog.getLogger()
    l.info('info')

test_log()