def get_token():
    try:
        token_file = open("token.txt", "r")
        TOKEN = token_file.read()
        TOKEN = TOKEN[:-1]
        token_file.close()
    except Exception:
        print("wattafuk is this??")
    return TOKEN

def get_request_kwargs():
    REQUEST_KWARGS={
        'proxy_url': 'socks5h://45.13.194.235:30001',
        # Optional, if you need authentication:
        'urllib3_proxy_kwargs': {
            'username': 'dmitlavrik_gmail_com',
            'password': 'e5f1721b99',
        }
    }
    return REQUEST_KWARGS
