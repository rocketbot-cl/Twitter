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
        self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        return self.api

    def update_status(self, message, in_reply_to_status_id=None):
        status_tweet = self.api.update_status(message, in_reply_to_status_id=in_reply_to_status_id, auto_populate_reply_metadata=True)
        return status_tweet

    def get_tweets(self, q, count=10, lang="es", result_type=""):
        print("q:", q)
        print("count:", count)
        print("lang:", lang)
        print("result_type:", result_type)
        print("Inicio")
        import json
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


if __name__ == '__main__':
    API_KEY = "d2VR8dNs0RI99KHL4yLnWFRkI"
    API_KEY_SECRET = "p2QFEKJObzSToZH9HRHsTBU6UNjgqZ35bD2VMl6r8r50uP3gOP"
    access_token = "90757624-qv7K2uCzZsuBMFALoH7UOCV3mvdO2vkBobSYHFP4d"
    access_token_secret = "5L5QpndTb5wA9aGYB5lUuGAwm7vVsnAbJNkoGLSkDngv9"
    twitter_service = TwitterService(API_KEY, API_KEY_SECRET, access_token, access_token_secret)
    twitter_service.auth_login()
    params = {}
    q = "argentina"
    count = 3
    lang = "es"
    result_type = "mixed"
    if count:
        params["count"] = count
    if lang:
        params["lang"] = lang
    if result_type:
        params["result_type"] = result_type
    
    result_search = twitter_service.get_tweets(q, **params)
    #result_search = twitter_service.get_tweets(q="argentina")
    print(result_search)
    print(type(result_search))
    #for tweet in result_search:
    #    print(tweet.text)
    #twitter_service.update_status("Test!")
