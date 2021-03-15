
import time
import sys
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

delay_print
delay_print (""+R+"  _   _  _____ ______  _   _  _____        "+O+"  _____ ______  _____   ___   _____  _____ \n")
delay_print (""+R+" | | | ||_   _|| ___ \| | | |/  ___|       "+O+" /  __ \| ___ \|  ___| / _ \ |_   _||  ___|\n")
delay_print (""+R+" | | | |  | |  | |_/ /| | | |\ `--. "+G+" ______"+O+" | /  \/| |_/ /| |__  / /_\ \  | |  | |__ \n") 
delay_print (""+R+" | | | |  | |  |    / | | | | `--. \""+G+"|______|"+O+"| |    |    / |  __| |  _  |  | |  |  __| \n")
delay_print (""+R+" \ \_/ / _| |_ | |\ \ | |_| |/\__/ /        "+O+"| \__/\| |\ \ | |___ | | | |  | |  | |___ \n")
delay_print (""+R+"  \___/  \___/ \_| \_| \___/ \____/         "+O+"\____/ \_| \_|\____/ \_| |_/  \_/  \____/ \n")
print








