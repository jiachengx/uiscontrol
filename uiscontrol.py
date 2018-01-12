#!/usr/bin/env python
# -*- coding: utf-8 -*-
# UIS-522b control

import requests, sys

outlet = {1: 'Outlet 1', 2: 'Outlet 2', 3:'Outlet all'}
control = {0: 'off', 1: 'on', 2: 'Switch', 3: 'reset'}


def send_control_to_uis(ipaddr, val_target, val_control):
    try:
        res = requests.request('GET', 'http://%s/cgi-bin/control2.cgi' % (ipaddr))
        payload = {'user': 'admin', 'passwd': 'admin', 'target': None, 'control': None}
        payload['target'] = val_target
        payload['control'] = val_control
        r = requests.get('http://%s/cgi-bin/control2.cgi' % (ipaddr), params=payload)
    except:
        print "[UIS] Connection Failed"
        return False
    return r.text


def dict_search(key, dct):
    for idx, value in dct.iteritems():
        if idx == key:
            return value


def main():
    uisstatus = ''
    if len(sys.argv) < 4:
        print "Usage: \n\tpython %s IP target=[1:Switch 1|2: Switch 2|3:All] control=[0:OFF|1:ON|2:Reset] \n" \
              "\ti.e. python %s '192.168.1.3' 1 1" % (sys.argv[0], sys.argv[0])
        sys.exit(0)

    ipaddr = sys.argv[1]
    target = int(sys.argv[2])
    control_flag = int(sys.argv[3])
    # uisstatus = send_control_to_uis(sys.argv[1],sys.argv[2],sys.argv[3])
    uisstatus = send_control_to_uis(ipaddr, target, control_flag)
    if uisstatus != False:
        print "[UIS] IP:%s Target: %s Status: %s" \
              % (ipaddr, dict_search(target, outlet), dict_search(control_flag, control))
        # print "Status: %s, %s" % (dict_search(int(uisstatus[45]), outlet), dict_search(int(uisstatus[47]), control))


if __name__ == '__main__':
    main()
