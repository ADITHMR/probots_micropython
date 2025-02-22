_A=None
import sys
CRITICAL=50
ERROR=40
WARNING=30
INFO=20
DEBUG=10
NOTSET=0
_level_dict={CRITICAL:'CRIT',ERROR:'ERROR',WARNING:'WARN',INFO:'INFO',DEBUG:'DEBUG'}
_stream=sys.stderr
class Logger:
	level=NOTSET
	def __init__(A,name):A.name=name
	def _level_str(C,level):
		A=level;B=_level_dict.get(A)
		if B is not _A:return B
		return'LVL%s'%A
	def setLevel(A,level):A.level=level
	def isEnabledFor(A,level):return level>=(A.level or _level)
	def log(A,level,msg,*C):
		B=level
		if B>=(A.level or _level):
			_stream.write('%s:%s:'%(A._level_str(B),A.name))
			if not C:print(msg,file=_stream)
			else:print(msg%C,file=_stream)
	def debug(A,msg,*B):A.log(DEBUG,msg,*B)
	def info(A,msg,*B):A.log(INFO,msg,*B)
	def warning(A,msg,*B):A.log(WARNING,msg,*B)
	def error(A,msg,*B):A.log(ERROR,msg,*B)
	def critical(A,msg,*B):A.log(CRITICAL,msg,*B)
	def exc(A,e,msg,*B):A.log(ERROR,msg,*B);sys.print_exception(e,_stream)
	def exception(A,msg,*B):A.exc(sys.exc_info()[1],msg,*B)
_level=INFO
_loggers={}
def getLogger(name):
	A=name
	if A in _loggers:return _loggers[A]
	B=Logger(A);_loggers[A]=B;return B
def info(msg,*A):getLogger(_A).info(msg,*A)
def debug(msg,*A):getLogger(_A).debug(msg,*A)
def basicConfig(level=INFO,filename=_A,stream=_A,format=_A):
	A=stream;global _level,_stream;_level=level
	if A:_stream=A
	if filename is not _A:print('logging.basicConfig: filename arg is not supported')
	if format is not _A:print('logging.basicConfig: format arg is not supported')