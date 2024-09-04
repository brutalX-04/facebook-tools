# MODULE
import os
import re
import sys
import uuid
import time
import requests
from bs4 import BeautifulSoup as bs


# COLOR
p  = '\33[m'        # DEFAULT
m  = '\x1b[0;91m'   # RED 
k  = '\033[0;93m'   # KUNING 
h  = '\x1b[0;92m'   # HIJAU 


# CALLING
ok = 0
fl = 0
loop = 0
rs = requests.Session()


# CLEAR
def clear():
    if "win" in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


# CLASS BANNER
class banner:
    def __init__(self):
        self.banner()

    def banner(self):
        clear()
        print('┏┓┏┓┳┳┓   ┓\n ┃┃ ┃┃┃┏┓┏┫       © 2023\n┗┛┗┛┛ ┗┗┛┗┻       by%s XMod%s'%(h,p))
        print('*' * 25)
        



class coment:
    def __init__(self):
        pass

    def getPost(self):
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,id;q=0.8',
            'cache-control': 'no-cache',
            'dpr': '1',
            'pragma': 'no-cache',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '"6.4.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }


        get = bs(rs.get('https://www.facebook.com/?filter=friends&sk=h_chr', cookies=cookies, headers=headers).text, 'html.parser')
        cursor = re.search('cursor":"(.*?)"', str(get)).group(1)
        self.user = re.search('"ACCOUNT_ID":"(.*?)"', str(get)).group(1);self.haste = re.search('"haste_session":"(.*?)"', str(get)).group(1);self.client = re.search('"client_revision"\:(.*?)\,', str(get)).group(1);self.spin_r = re.search('"__spin_r"\:(.*?)\,', str(get)).group(1);self.spin_t = re.search('"__spin_t"\:(.*?)\,', str(get)).group(1);self.hsi = re.search('"hsi":"(.*?)"', str(get)).group(1);self.dtsg = re.search('"DTSGInitialData"\,\[\]\,{"token":"(.*?)"', str(get)).group(1);self.lsd = re.search('"LSD"\,\[\]\,{"token":"(.*?)"', str(get)).group(1);self.jazoest = re.search('jazoest=(.*?)"', str(get)).group(1);self.client_id = re.search('"clientID":"(.*?)"', str(get)).group(1)
        self.getPostGraphql(cursor)


    def getPostGraphql(self, cursor):
        global loop, ok, fl
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,id;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'origin': 'https://www.facebook.com',
            'pragma': 'no-cache',
            'referer': 'https://www.facebook.com/?filter=friends&sk=h_chr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '"6.4.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-asbd-id': '129477',
            'x-fb-friendly-name': 'CometNewsFeedPaginationQuery',
            'x-fb-lsd': self.lsd
        }

        data = {
            'av': self.user,
            '__user': self.user,
            '__a': '1',
            '__req': '15',
            '__hs': self.haste,
            'dpr': '1',
            '__ccg': 'UNKNOWN',
            '__rev': self.client,
            '__s': '',
            '__hsi': self.hsi,
            '__dyn': '',
            '__comet_req': '15',
            'fb_dtsg': self.dtsg,
            'jazoest': '25315',
            'lsd': self.lsd,
            '__spin_r': self.spin_r,
            '__spin_b': 'trunk',
            '__spin_t': self.spin_t,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometNewsFeedPaginationQuery',
            'variables': '{"RELAY_INCREMENTAL_DELIVERY":true,"UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery","clientQueryId":"%s","connectionClass":"UNKNOWN","count":5,"cursor":"%s","displayCommentsContextEnableComment":null,"displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"displayCommentsFeedbackContext":null,"experimentalValues":null,"feedLocation":"NEWSFEED","feedStyle":"MOST_RECENT_FRIENDS_FEED","feedbackSource":1,"focusCommentID":null,"orderby":["MOST_RECENT"],"privacySelectorRenderLocation":"COMET_STREAM","recentVPVs":[],"refreshMode":"COLD_START","renderLocation":"homepage_stream","scale":1,"useDefaultActor":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__StoriesRingrelayprovider":false}'%(uuid.uuid4(), cursor),
            'server_timestamps': 'true',
            'doc_id': '7396744383674405',
        }

        post = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
        data = re.findall('{"brs_content_label"(.*?)}}}}', post.text)
        for data in data:
            if loop == int(jumlah):
                print('Program Succes')
                exit()
            else:
                loop+=1
                print('\r- Running [%s/%s] Succes : %s%s%s, Failled : %s%s%s '%(loop, jumlah, h, ok, p, m, fl, p), end='')
                time.sleep(10)
            
            try:
                name = re.search('"name":"(.*?)"', str(data)).group(1)
                fedback = re.search('"story":{"feedback":{"id":"(.*?)"', str(data)).group(1)
                tracking = re.search('"encrypted_tracking":"(.*?)"', str(data)).group(1)
                session = re.search('"session_id(.*?)"type', str(data)).group(1).split('"')[2].replace('\\','')
                cursor = re.search('"cursor":"(.*?)"', str(data)).group(1)
                actor_id = re.search('{"viewer_actor":{"__typename":"User","id":"(.*?)"', str(data)).group(1)
                self.sendComent(fedback, tracking, session, actor_id, name)

            except:
                name = re.search('"name":"(.*?)"', str(data)).group(1)
                print('\rFailled Comment In Post : %s%s%s'%(m, name, p))
                print('*' * 25)
                fl+=1

        self.getPostGraphql(cursor)



    def sendComent(self, fedback, tracking, session, actor_id, name):
        global loop, ok, fl
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,id;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'origin': 'https://www.facebook.com',
            'pragma': 'no-cache',
            'referer': 'https://www.facebook.com/?filter=friends&sk=h_chr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '"6.4.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-asbd-id': '129477',
            'x-fb-friendly-name': 'CometUFICreateCommentMutation',
            'x-fb-lsd': self.lsd,
        }

        data = {
            'av': self.user,
            '__user': self.user,
            '__a': '1',
            '__req': '1w',
            '__hs': self.haste,
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': self.client,
            '__s': '',
            '__hsi': self.hsi,
            '__dyn': '',
            '__csr': '',
            '__comet_req': '15',
            'fb_dtsg': self.dtsg,
            'jazoest': self.jazoest,
            'lsd': self.lsd,
            '__spin_r': self.spin_r,
            '__spin_b': 'trunk',
            '__spin_t': self.spin_t,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUFICreateCommentMutation',
            'variables': '{"displayCommentsFeedbackContext":null,"displayCommentsContextEnableComment":null,"displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"feedLocation":"NEWSFEED","feedbackSource":1,"focusCommentID":null,"groupID":null,"includeNestedComments":false,"input":{"attachments":null,"feedback_id":"%s","formatting_style":null,"message":{"ranges":[],"text":"%s"},"attribution_id_v2":"FeedsCometRoot.react,comet.most_recent_feed,via_cold_start,1695545722529,702527,4748854339,","is_tracking_encrypted":true,"tracking":["%s","{\\"assistant_caller\\":\\"comet_above_composer\\",\\"conversation_guide_session_id\\":null,\\"conversation_guide_shown\\":null}"],"feedback_source":"NEWS_FEED","idempotence_token":"client:%s","session_id":"%s","actor_id":"%s","client_mutation_id":"3"},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery"}'%(fedback, text, tracking, uuid.uuid4(), session, actor_id),
            'server_timestamps': 'true',
            'doc_id': '6086237478143567',
        }

        post = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
        if '<Response [200]>' in str(post):
            print('\rSucces Comment In Post : %s%s%s'%(h, name, p))
            print('*' * 25)
            ok+=1
        else:
            print('\rFailled Comment In Post : %s%s%s'%(m, name, p))
            print('*' * 25)
            fl+=1
            


banner()
jumlah = input('Input Jumlah Komentar : ')
text = input('Input Text Komentar : ')
cookie = input('Input Cookie : ')
cookies = {'cookie': cookie}
print('*' * 25)

coment().getPost()
