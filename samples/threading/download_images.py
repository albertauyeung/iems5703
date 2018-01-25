import threading
import time
from urllib import request 

images = [
    "http://www.gardenhostel.com.hk/images/StarFerry.jpg",
    "https://res.klook.com/images/fl_lossy.progressive,q_65/c_fill,w_1295,h_720,f_auto/w_80,x_15,y_15,g_south_west,l_klook_water/activities/ncewed1hbddovlflaop3/StarFerryRoundtripDisneylandTransfer.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/0/01/Golden_star_ferry_at_Hong_Kong.jpg",
    "https://i.ytimg.com/vi/oq16X5hL3Z4/maxresdefault.jpg",
    "http://www.exploitrip.com/destinations/wp-content/uploads/2015/01/star-Ferry-Hong-Kong.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/c9/Star_Ferry%27s_Harbour_Tour%2C_Shining_Star_%28Hong_Kong%29.jpg"
]

def download(url, i):
    print("Downloading image %d..." % i)
    file_name = "%d.jpg" % i
    request.urlretrieve(url, file_name)


start_time = time.time()

for i, url in enumerate(images):
    t = threading.Thread(target=download, args=(url, i))
    t.start()

for t in threading.enumerate():
    if t != threading.main_thread():
        t.join()

print(time.time() - start_time)
