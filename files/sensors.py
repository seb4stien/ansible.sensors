#!/usr/bin/env python2

from collections import defaultdict

import re
import rfxcom
import time

my_sensors = {
  'thr128.04': {
     'name': 'salon'
  },
  'thgr228n.ec': {
     'name': 'chambre'
  },
  'thgr228n.a3': {
     'name': 'suite'
  },
  'thn132n.c5': {
     'name': 'terrasse'
  }
}

def test():
    msg = "topic: temp, battery: 90, source: thgr228n.a3, sensor: thgr228n.a3, temp: 22.5, humidity: 37"
    res = on_message(msg)
    assert res['topic'] == "temp"
    assert res['battery'] == 90
    assert res['source'] == "thgr228n.a3"
    assert res['sensor'] == "thgr228n.a3"
    assert res['temp'] == 22.5
    assert res['humidity'] == 37


def on_message(message):

    message = str(message)
    res = defaultdict(None)

    m = re.match(".*topic: ([^,]+)", message)
    if m:
        res['topic'] = m.group(1)

    m = re.match(".*battery: ([^,]+)", message)
    if m:
        res['battery'] = float(m.group(1))

    m = re.match(".*source: ([^,]+)", message)
    if m:
        res['source'] = m.group(1)

    m = re.match(".*sensor: ([^,]+)", message)
    if m:
        res['sensor'] = m.group(1)

    m = re.match(".*temp: ([^,]+)", message)
    if m:
        res['temp'] = float(m.group(1))

    m = re.match(".*humidity: ([^,]+)", message)
    if m:
        res['humidity'] = float(m.group(1))

    if res['source']:
        if res['source'] in my_sensors:
            res['room'] = my_sensors[res['source']]['name']
        else:
            res['room'] = 'unknown'
        
    ts = int(time.time())
    res['ts'] = ts

    print(res)
    with open("/srv/sensors/%s.log" % res['room'], "a+") as fh:
        fh.write("ts: %d, %s\n" % (ts, message))
    return res


if __name__ == "__main__":
    rfx = rfxcom.RFXCom(on_message)
    rfx.setup()
    rfx.run()
    #test()
