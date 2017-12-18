import requests
from bs4 import BeautifulSoup
url = "http://m.tieba.com"
url2 = "http://www.baidu.com"
url3="http://r.cnews.qq.com/getSubNewsInterest?hw_fp=HUAWEI%2FNXT-AL10%2FHWNXT%3A7.0%2FHUAWEINXT-AL10%2FC00B592%3Auser%2Frelease-keys&mid=7e6743b297a502e841eb9e21f36aa2d24d1f6dc6&devid=869906027804333&mac=48%3Adb%3A50%3A2b%3A7d%3A5f&store=413&screen_height=1830&apptype=android&origin_imei=869906027804333&hw=HUAWEI_HUAWEINXT-AL10&appversion=4.5.45&appver=24_areading_4.5.45&uid=fa0acc0665c80123&screen_width=1080&sceneid=&android_id=fa0acc0665c80123&ssid=HUAWEI-ylq_5G&forward=0&IronThroneBuildTime=1513007060955&omgid=9f3e9d273cf1954fb06a745881e371abeead0010211213&IronThroneRelBuildTime=919594686&refreshType=normal&qqnetwork=wifi&commonGray=1_3%7C2_0&currentTab=kuaibao&manualRefresh=1&is_wap=0&omgbizid=d5f8fa2d472dab43d5296ea324c7a0462d6f0080211402&imsi=460011220109863&newPage=3651&uin=oijc7uKHvRFj-QiH1Ml6mbeMnlRg&bssid=94%3A77%3A2b%3A67%3Acd%3A70&IronThroneRelExecTime=919594688&muid=32060023681480524&viewsub_time=1513007054&activefrom=icon&logfrom=2&luin=&qimei=869906027804333&direction=0&lastPushTurnOffTime=0&Cookie=%20access_token%3DQi3StAHYa30dtVh1AN3_tbvTZl6LggrwC7ZV9aNQSNZ7__ixmWVTVW0hidDZ0xqpzuVg-aJP9YYc0zOg9hcli1EXAHlh2uQTLqAe7ba1i_w%3B%20openid%3Doijc7uKHvRFj-QiH1Ml6mbeMnlRg%3B%20refresh_token%3DQi3StAHYa30dtVh1AN3_tfg2F1lJc1JU34NikJSk2jMmKK_PPjRrILdwaNnXn7M_Jeui7TzWj-aj40ZNxzSlxF7p38MAkq1cnSEltLdFgjA%3B%20appid%3Dwxe90c9765ad00e2cd%3B%20unionid%3DonCs1uJf7w9a2BS3vUMWRapP-DYk%3B%20logintype%3D1%3B&sessionid=&chRefreshTimes=0&chlid=daily_timeline&oldadcode=310115&IronThroneExecTime=1513007060958&imsi_history=460011220109863&qn-sig=3173cbc20471ebcf8d5f6f7e4d3baaf6&qn-rid=df4aa651-a374-4d35-88e3-66ed4babb20a&lastPushTime=0&openPush=0"
headers = {
'Host': 'm.tieba.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'BDUSS=swZGs2akFCbUdYaE1MT1RtSHNsOFFWTVIzU2hEMGwwSERMYnBaRUNuSjhoVTlhQVFBQUFBJCQAAAAAAAAAAAEAAAAsolsGNjM0NzM5MjQyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHz4J1p8-CdaM0; BAIDUID=F574103DAB4AA9F90B2E39BA57973EEA:FG=1; BIDUPSID=F574103DAB4AA9F90B2E39BA57973EEA; PSTM=1512909144; BDRCVFR[i7zL5H8GeBs]=mk3SLVN4HKm; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; bd_traffictrace=112219_112222; plus_lsv=58828f347bbfb0b1; plus_cv=1::m:21732389; BDICON=10123156; H_WISE_SIDS=102570_106305_116520_115652_103342_120145_120783_119138_118892_118874_118849_118826_118797_107316_120773_118970_120667_117579_117334_117236_120634_117435_120591_121035_120943_118967_118103_117558_116145_121014_120851_120873_116407_120843_120896_110085_120502_121065; BDSVRTM=33; lsv=globalTjs_c53e474-wwwTcss_a27bd85-wwwBcss_08e0ba1-framejs_68c2a88-globalBjs_ca93ca6-sugjs_ddc6e70-wwwjs_5985198; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695' }
r = requests.get(url3)
js = r.json()
print(js['changeInfo'])
print(js['newslist'])
r = requests.get("https://kuaibao.qq.com/s/20171209A0QLN400?refer=kb_news&coral_uin=ec5f3062305f12d27cb08ad4cfdc52d94437c97a8de2d7076536c9460c360be312")
#print(r.text)
soup = BeautifulSoup(r.text,'html.parser')
alls = soup.find_all("p", {"class":['text']})
for ap in alls:
    print(ap.get_text(), end='')

while True:
    r_js = requests.get(url3).json()
    i = 0
    for art in js['newslist']:
        print("#",i,"#:",art['abstract'])
        #print(art['short_url'])
        r = requests.get(art['short_url'])
        print(r.content)