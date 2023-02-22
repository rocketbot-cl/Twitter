# Twitter
  
Connect to Twitter, list tweets from timeline, update status, and search words  

*Read this in other languages: [English](Manual_Twitter.md), [Español](Manual_Twitter.es.md).*
  
![banner](imgs/Banner_Twitter.png)

## How to use this module
### First we must be clear that the Twitter account to be used must have the profile with complete data and have been using it for some time, otherwise it will be a little more complicated to apply to have enabled the use of the API. Check the following link for more information: https://developer.twitter.com/en/apply-for-access
1. Login to your Twitter account and then go to the following link: https://developer.twitter.com/en/docs/twitter-api
2. Inside the main screen, in the "Twitter API" section we will click on the button called "Sign Up".
3. Then in the dashboard, we must create a project by clicking on "Create Project". We will have to put title, description and other data to create the project.
4. After creating the project, we will see some keys, of which we must copy and save the ones that say API Key and API Secret Key.
5. As last step, we must generate the tokens. For it it is necessary to go to the section of Project App and to click in the icon with form of key that has of name "Keys and Tokens". 
6. We generate the Access Token and the Access Token Secret, copy them and save them.


## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  






## Description of the commands

### Connect to Twitter
  
Connect to your Twitter account using your credentials
|Parameters|Description|example|
| --- | --- | --- |
|API KEY|Enter the API KEY that we generated in our account|eYSmJLqazCAXxFOrMogNa1322|
|API KEY Secret|Enter the API KEY Secret that we generated in our account|Qvi0tuylMfrzJOJxO5Rp2Y5cSGWMHevITBwG0Oj2199Vo5Tdbr|
|Access Token|Enter the Access Token that we generated in our account|Jc7bsx5UaQFewwvKHava6PBGkaZqdn0HSvp7Jg30dBQyy5ZZOB|
|Access Token Secret|Enter the Access Token Secret that we generated in our account|Qvi0tuylMfrzJOJxO5Rp2Y5cSGWMHevITBwG0Oj2199Vo5Tdbr|
|Result|Variable where we will store our result. If the connection is successful, it will return True, otherwise it will return False|result|

### Send tweet
  
Send a tweet using a message and optional an ID from a tweet to reply
|Parameters|Description|example|
| --- | --- | --- |
|Message|In this field we must put the message to send|Hello World! I'm sending a tweet from Rocketbot|
|Tweet ID|In case we want to reply to a tweet or a thread, we must put the ID of that tweet|1461077245825531907|
|Result|Variable where we will save our result. Returns the link of the tweet sent|result|

### Search tweets
  
Given a word or text, with or without filters, search for it using the Twitter API
|Parameters|Description|example|
| --- | --- | --- |
|Search|Must be the text or word to search|Noticias importantes|
|Count|Indicate the amount of tweets to return. By default returns 10|10|
|Lang|Indicate the language in which you want to perform the search|es|
|Result type|Can be recent, mixed or popular. Leave empty to get by default|recent|
|Result|Variable where we will store our result. Returns a list of dictionaries that have link, author and message of the tweet|result|

### Get mentions
  
Get a list of mentions that have been made to the account
|Parameters|Description|example|
| --- | --- | --- |
|Count|Indicate the amount of tweets to return. By default returns 10|10|
|Result|Variable where we will store our result. Returns a list of dictionaries that have link, author and message of the tweet|result|

### Get user ID
  
Gets the ID of a user
|Parameters|Description|example|
| --- | --- | --- |
|Twitter user|Indicates the Twitter user from which we want to obtain the ID|rocketbot_es|
|Result|Variable where we will store our result. Returns a list of dictionaries that have link, author and message of the tweet|result|

### Get user timeline
  
Get the timeline of a user
|Parameters|Description|example|
| --- | --- | --- |
|User ID|Indicate the ID of the user whose timeline we want to obtain|1234567890|
|Count|Indicate the amount of tweets to return. By default returns 10|10|
|Include retweets|Indicate if we want to include retweets in the result|True|
|Result|Variable where we will store our result. Returns a list of dictionaries that have link, author and message of the tweet|result|

### Retweet
  
Retweets a tweet
|Parameters|Description|example|
| --- | --- | --- |
|Tweet ID|Indicate the ID of the tweet you want to retweet|1461077245825531907|

### Get tweet information
  
Get information from a tweet from its ID
|Parameters|Description|example|
| --- | --- | --- |
|Tweet ID|Indicate the ID of the tweet you want to retweet|1461077245825531907|
|Variable |Variable where the result will be stored|result|
