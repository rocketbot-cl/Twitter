import tweepy


class TwitterService:
    def __init__(self, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        self.API_KEY = API_KEY
        self.API_KEY_SECRET = API_KEY_SECRET
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
        self.api = None
        self.auth = None

    def auth_login(self):
        self.auth = tweepy.OAuthHandler(self.API_KEY, self.API_KEY_SECRET)
        try:
            url = self.auth.get_authorization_url()
            self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
            return self.api
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            print(e)
            return None

    def update_status(self, message, in_reply_to_status_id=None):
        status_tweet = self.api.update_status(message, in_reply_to_status_id=in_reply_to_status_id, auto_populate_reply_metadata=True)
        return status_tweet

    def get_tweets(self, q, count=10, lang="es", result_type=""):
        result_search = tweepy.Cursor(self.api.search_tweets,
                            q=q,
                            lang=lang,
                            result_type=result_type,
                            count=count
        ).items(count)
        return result_search

    def get_mentions(self, count=10):
        mentions = self.api.mentions_timeline(count=count)
        return mentions
