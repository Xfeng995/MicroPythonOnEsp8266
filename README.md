# MicroPython的启动流程

## boot.py 文件
当我们启动NodeMCU后，MicroPython系统将会依次执行一系列存放在NodeMCU开发板根目录下的的程序文件。
首先执行的是boot.py文件。该文件是由MicroPython系统创建的。因此您无需自己创建该文件就可以在刚刚刷好固件的NodeMCU开发板根目录下找到它。
我不建议MicroPython的初学者对该文件进行修改，因为boot.py文件出现问题能会导致MicroPython无法正常启动，严重的会导致系统崩溃。要修复可能只有重新刷固件才行。
所以除非您很了解MicroPython，否则请不要自行修改该文件。
## main.py 文件
执行完boot.py以后，启动中的NodeMCU接下来将会执行main.py文件。
如果您希望NodeMCU在每次启动后都执行一系列操作的话，可以将您的指令代码写入该文件。

由于main.py文件是用户自己建立的而不是MicroPython系统建立的，因此在刚刚刷好固件的开发板根目录下是不存在该文件的。
假如您需要MicroPython系统在启动时执行一系列操作，请不要将大量程序代码写入main.py文件，而应该对需要执行的启动任务以模块化的方式分别存储于多个文件中。这样可便于您对启动模块的管理。
