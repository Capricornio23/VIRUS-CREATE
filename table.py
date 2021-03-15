#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
def force_to_unicode(text): 
        "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding" 
        return text if isinstance(text, unicode) else text.decode('utf8')

print
print (""+R+"          ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print (""+R+"          ┃"+B+"0."+G+"        DroidXAntivirus"+R+"        ┃")
print (""+R+"          ┃"+B+"I."+G+"        Android Freezen"+R+"        ┃")
print (""+R+"          ┃"+B+"II."+G+"         Android Ransn"+R+"        ┃")
print (""+R+"          ┃"+B+"III."+G+"        Android Malware"+R+"      ┃")
print (""+R+"          ┃"+B+"IV."+G+"       Android Decryptor"+R+"      ┃")
print (""+R+"          ┃"+B+"V."+G+"       Android Decryptor2"+R+"      ┃")
print (""+R+"          ┃"+B+"VI."+G+"        Android SMS Tief"+R+"      ┃")
print (""+R+"          ┃"+B+"VII."+G+"   Android Dangerous Malware"+R+" ┃")
print (""+R+"          ┃"+B+"VIII."+G+"      Android ENC Malware"+R+"   ┃")
print (""+R+"          ┃"+B+"IX."+G+"      Android Door Trojan"+R+"     ┃")
print (""+R+"          ┃"+B+"X."+R+"             EXIT              ┃")
print (""+R+"          ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
print
