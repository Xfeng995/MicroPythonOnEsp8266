def config_ap(ssid, passwd):
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    # 只设置ssid，默认密码为MicroPythoN
    #ap.config(essid = ssid)
    # 设置ssid，并设置密码
    ap.config(essid = ssid, password = passwd)
    # 设置ssid，不设置连接密码
    #ap.config(essid = ssid，authmode=0)
