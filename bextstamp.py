#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import datetime
import time
import sys

def get_string(data, offset, maxlen):
    res = ""
    p = offset
    while maxlen > 0:
        d = ord(data[p])
        if d == 0:
            break
        res += chr(d)
        maxlen -= 1
        p += 1
    return res


if __name__ == "__main__":
   try:
      filename = sys.argv[1]  # "190401_004.WAV"
   except IndexError:
      print("parameter missing")
      sys.exit(1)

   try:
      fin = open(filename, "rb").read(358)
   except:
      print("file open error")
      sys.exit(2)

   try:
      assert get_string(fin, 0, 4) == "RIFF"
      assert get_string(fin, 8, 4) == "WAVE"
      assert get_string(fin, 12, 4) == "bext"

      dat = get_string(fin, 340, 10)
      clock = get_string(fin, 350, 8)
      mad = re.match("^(\d+)\D(\d+)\D(\d+)", dat)
      assert mad is not None, "wrong date format"
      mac = re.match("^(\d+)\D(\d+)\D(\d+)", clock)
      assert mac is not None, "wrong time format"

      bdate = datetime.datetime(
         year=int(mad.group(1)),
         month=int(mad.group(2)),
         day=int(mad.group(3)),
         hour=int(mac.group(1)),
         minute=int(mac.group(2)),
         second=int(mac.group(3)),
      )
   except:
      print("conversion error")
      sys.exit(3)

   bstamp = time.mktime(bdate.timetuple())
   now = time.time()

   try:
      os.utime(filename, (now, bstamp))
   except:
      print("error on setting date")
      sys.exit(4)
