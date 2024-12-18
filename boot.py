# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
webrepl.start()
gc.collect()
#连接wifi
from hyftools.wifi_connect import do_wifi_connect
do_wifi_connect('hu_mi8_8888','qwerasdf1234')
#设置热点ap
from hyftools.ap_config import config_ap
config_ap('esp_ap', '12345678')
