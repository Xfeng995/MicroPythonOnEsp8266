def do_wifi_connect(essid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(essid, password)
        #wlan.connect('hu_mi8_8888', 'qwerasdf1234')
        #wlan.connect(b'hu_mi8_8888\n','qwerasdf1234')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())