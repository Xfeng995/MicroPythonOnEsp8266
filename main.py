#连接wifi
from hyftools.wifi_connect import do_wifi_connect
do_wifi_connect('hu_mi8_8888','qwerasdf1234')
#设置热点ap
from hyftools.ap_config import config_ap
config_ap('esp_ap', '12345678')