# 演習プロジェクト 18.10.3  自動退会機

import imaplib
imaplib._MAXLINE = 10000000
import imapclient
from backports import ssl
import pyzmail
import bs4
import webbrowser

IMAP_SERVER = 'IMAP_SERVER' # IMAPサーバーのアドレスを設定してください
MY_ADDRESS = 'YOUR_ID' # アカウントを設定してください
MY_PASSWORD = 'YOUR_PASSWORD' # パスワードを設定してください

print('接続中')

# IMAPで接続する
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
imap_obj = imapclient.IMAPClient(IMAP_SERVER, ssl=True, ssl_context=context)
imap_obj.login(MY_ADDRESS, MY_PASSWORD)

# INBOXから本文にunsubscribeが含まれるメールを探す
imap_obj.select_folder('INBOX', readonly=True)
UIDs = imap_obj.search(['BODY', 'unsubscribe'])
count = len(UIDs)
print('{}件見つかりました'.format(count))

n = 0
for uid in UIDs:
    n += 1
    print('{}/{}件目のメールを取得中'.format(n, count))

    # IMAPでメール本文を取得する
    raw_message = imap_obj.fetch([uid], ['BODY[]'])
    message = pyzmail.PyzMessage.factory(raw_message[uid][b'BODY[]'])
    print('件名：', message.get_subject())
    print('From：', message.get_addresses('from'))
    if not message.html_part:
        print('HTMLメールではありません。スキップします。')
        continue

    html = message.html_part.get_payload().decode(message.html_part.charset)

#    #解析用に、htmlを保存する
#    with open(str(uid) + '.html', 'w', encoding='utf-8') as f:
#        f.write(html)

    # HTMLから<a>タグを探す
    soup = bs4.BeautifulSoup(html, 'lxml')
    links = soup.select('a')
    for link in links:
        # リンクテキストにunsubscribeが含まれているものを探す
        if 'unsubscribe' in link.getText().lower():
            href = link.attrs['href']
            print('退会リンク：', href)
            while True:
                print('リンクを開きますか？(y/n)：', end='', flush=True)
                yn = input().lower()
                if yn == 'y':
                    webbrowser.open(href)
                    break
                elif yn == 'n':
                    print('スキップします。')
                    break
                else:
                    print('yかnで答えてください。')

print('終了')
