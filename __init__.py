# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Twitter" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from twitter_service import TwitterService

"""
    Obtengo el modulo que fue invocado
"""
global twitter_service
module = GetParams("module")

if module == "connect":
    api_key = GetParams("api_key")
    api_key_secret = GetParams("api_key_secret")
    access_token = GetParams("access_token")
    access_token_secret = GetParams("access_token_secret")
    res = GetParams("res")
    try:
        twitter_service = None
        twitter_service = TwitterService(api_key, api_key_secret, access_token, access_token_secret)
        twitter_api = twitter_service.auth_login()
        if twitter_api:
            SetVar(res, True)
        if not twitter_api:
            SetVar(res, False)
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "send_tweet":
    message = GetParams("message")
    id_tweet = GetParams("id_tweet")
    res = GetParams("res")
    try:
        if twitter_service is None:
            raise Exception("No se ha iniciado la conexión con Twitter")
        if id_tweet:
            tweet_data = twitter_service.update_status(message, id_tweet)
        if not id_tweet:
            tweet_data = twitter_service.update_status(message)
        link_tweet = 'https://twitter.com/twitter/statuses/{id}'.format(id=tweet_data.id)
        SetVar(res, link_tweet)
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "get_tweets":
    q = GetParams("q")
    count = GetParams("count")
    lang = GetParams("lang")
    result_type = GetParams("result_type")
    res = GetParams("res")
    try:
        if twitter_service is None:
            raise Exception("No se ha iniciado la conexión con Twitter")
        params = {}
        if count:
            params["count"] = int(count)
        if lang:
            params["lang"] = lang
        if result_type:
            params["result_type"] = result_type
        result_search = twitter_service.get_tweets(q, **params)
        list_links_tweets = []
        print(result_search)
        print(type(result_search))
        for tweet in result_search:
            tweet_info = {
                'link': 'https://twitter.com/twitter/statuses/{id}'.format(id=tweet.id),
                'text': tweet.text,
                'author': tweet.author.name,
            }
            print(tweet_info)
            list_links_tweets.append(tweet_info)
        SetVar(res, list_links_tweets)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "get_mentions":
    count = GetParams("count")
    res = GetParams("res")
    try:
        if twitter_service is None:
            raise Exception("No se ha iniciado la conexión con Twitter")
        mentions = twitter_service.get_mentions(count)
        list_links_tweets = []
        for tweet in mentions:
            tweet_info = {
                'link': 'https://twitter.com/twitter/statuses/{id}'.format(id=tweet.id),
                'text': tweet.text,
                'author': tweet.author.name,
            }
            list_links_tweets.append(tweet_info)
        SetVar(res, list_links_tweets)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e