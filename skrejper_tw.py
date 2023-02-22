import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "ММР (богиње OR епидемија OR епидемије OR епидемији OR епидемију OR епидемијом OR заражено OR заражених OR заражени OR зараженима OR оболело OR оболели OR оболелих OR оболелим) until:2023-02-22 since:2023-01-01"
tweets = []
limit = 10000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv('morbili_jan_feb_cir.csv')
