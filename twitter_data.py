import tweepy
import pandas as pd

# Function to get Twitter API access
def get_twitter_api():
    # Replace the following strings with your own credentials obtained from the Twitter developer portal
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
    
    # Setting up the authentication and API access
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    return api

# Function to search tweets based on a query
def search_tweets(api, query, max_tweets):
    searched_tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="id").items(max_tweets):
        searched_tweets.append(tweet)
    return searched_tweets

# Get Twitter API access
api = get_twitter_api()

# Define the search query and the number of tweets to retrieve
query = "minat sains matematika Indonesia"
max_tweets = 100

# Search for tweets
tweets = search_tweets(api, query, max_tweets)

# Extract relevant information from tweets
data = []
for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text, tweet.favorite_count, tweet.retweet_count])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Timestamp', 'User', 'Tweet', 'Likes', 'Retweets'])

# Save the DataFrame to a CSV file
df.to_csv('tweets_minat_sains_matematika_indonesia.csv', index=False)

# Display the first few rows of the DataFrame
print(df.head())
