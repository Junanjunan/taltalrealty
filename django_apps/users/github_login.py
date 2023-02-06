from config.taltalrealty_local_settings.local_settings import LOCAL_URL, GH_ID_LOCAL, GH_SECRET_LOCAL

GH_OATH_API_URL = "https://api.github.com/user"
GH_LOGIN_BASE_URL = "https://github.com/login/oauth"
GH_REDIRECT_LOCAL_URL = f"{LOCAL_URL}/login/github/callback"
GH_AUTHORIZE_URL = f"{GH_LOGIN_BASE_URL}/authorize?client_id={GH_ID_LOCAL}&redirect_uri={GH_REDIRECT_LOCAL_URL}&scope=read:user"