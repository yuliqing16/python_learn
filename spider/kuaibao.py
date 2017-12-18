import requests
from bs4 import BeautifulSoup

#url3="http://r.cnews.qq.com/getSubNewsInterest?hw_fp=HUAWEI%2FNXT-AL10%2FHWNXT%3A7.0%2FHUAWEINXT-AL10%2FC00B592%3Auser%2Frelease-keys&mid=7e6743b297a502e841eb9e21f36aa2d24d1f6dc6&devid=869906027804333&mac=48%3Adb%3A50%3A2b%3A7d%3A5f&store=413&screen_height=1830&apptype=android&origin_imei=869906027804333&hw=HUAWEI_HUAWEINXT-AL10&appversion=4.5.45&appver=24_areading_4.5.45&uid=fa0acc0665c80123&screen_width=1080&sceneid=&android_id=fa0acc0665c80123&ssid=HUAWEI-ylq_5G&forward=0&IronThroneBuildTime=1513007060955&omgid=9f3e9d273cf1954fb06a745881e371abeead0010211213&IronThroneRelBuildTime=919594686&refreshType=normal&qqnetwork=wifi&commonGray=1_3%7C2_0&currentTab=kuaibao&manualRefresh=1&is_wap=0&omgbizid=d5f8fa2d472dab43d5296ea324c7a0462d6f0080211402&imsi=460011220109863&newPage=3651&uin=oijc7uKHvRFj-QiH1Ml6mbeMnlRg&bssid=94%3A77%3A2b%3A67%3Acd%3A70&IronThroneRelExecTime=919594688&muid=32060023681480524&viewsub_time=1513007054&activefrom=icon&logfrom=2&luin=&qimei=869906027804333&direction=0&lastPushTurnOffTime=0&Cookie=%20access_token%3DQi3StAHYa30dtVh1AN3_tbvTZl6LggrwC7ZV9aNQSNZ7__ixmWVTVW0hidDZ0xqpzuVg-aJP9YYc0zOg9hcli1EXAHlh2uQTLqAe7ba1i_w%3B%20openid%3Doijc7uKHvRFj-QiH1Ml6mbeMnlRg%3B%20refresh_token%3DQi3StAHYa30dtVh1AN3_tfg2F1lJc1JU34NikJSk2jMmKK_PPjRrILdwaNnXn7M_Jeui7TzWj-aj40ZNxzSlxF7p38MAkq1cnSEltLdFgjA%3B%20appid%3Dwxe90c9765ad00e2cd%3B%20unionid%3DonCs1uJf7w9a2BS3vUMWRapP-DYk%3B%20logintype%3D1%3B&sessionid=&chRefreshTimes=0&chlid=daily_timeline&oldadcode=310115&IronThroneExecTime=1513007060958&imsi_history=460011220109863&qn-sig=3173cbc20471ebcf8d5f6f7e4d3baaf6&qn-rid=df4aa651-a374-4d35-88e3-66ed4babb20a&lastPushTime=0&openPush=0"
url3="http://r.cnews.qq.com/getSubNewsInterest"

while True:
    r_js = requests.get(url3).json()
    i = 0
    select_no = 0
    while select_no != 99:
        try:
            i = 0
            for art in r_js['newslist']:
                print("#",i,"#:",art['commentShareTitle'])
                i = i + 1
            select_no = int(input("Put Index(99 Refresh)>"))
            if select_no == 99:
                continue
            r = requests.get(r_js['newslist'][select_no]['short_url'])
            soup = BeautifulSoup(r.text, 'html.parser')
            alls = soup.find_all("p", {"class": ['text']})
            for ap in alls:
                print(ap.get_text(), end='')
            print("")
            input("")
        except:
            continue