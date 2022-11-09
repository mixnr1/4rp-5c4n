# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import config
import time
from scapy.all import ARP, Ether, srp
ip_range=config.ip_range
open_file = open(ip_range, "r")
for line in open_file:
    mytime=time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
    target_ip=line.rstrip()
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'time': mytime,'mac': received.hwsrc})
    for client in clients:
        print("{},{},{}".format(client['ip'], client['time'], client['mac']))
#######MySQL########
# import config
# import os
# from sqlite3 import Timestamp
# import mysql.connector
# import time
# from scapy.all import ARP, Ether, srp
# mysql_user=os.environ['DBUSER']
# mysql_pass=os.environ['DBPASS']
# mysql_host=os.environ['DBHOST']
# mysql_db=os.environ['DBNAME']
# mydb=mysql.connector.connect(
#     host=mysql_host,
#     user=mysql_user,
#     passwd=mysql_pass,
#     database=mysql_db
# )
# mycursor=mydb.cursor()
# ip_range=config.ip_range
# open_file = open(ip_range, "r")
# for line in open_file:
#     mytime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     target_ip=line.rstrip()
#     arp = ARP(pdst=target_ip)
#     ether = Ether(dst="ff:ff:ff:ff:ff:ff")
#     packet = ether/arp
#     result = srp(packet, timeout=3, verbose=0)[0]
#     clients = []
#     for sent, received in result:
#         clients.append({'ip': received.psrc, 'time': mytime,'mac': received.hwsrc})
#     for client in clients:
#         sql = "INSERT INTO mac (ipaddr, timestamp, macaddr) VALUES (%s, %s, %s)"
#         val = (client['ip'], client['time'], client['mac'])
#         mycursor.execute(sql, val)
#         mydb.commit()
