# ImitateBot
This bot utilizes [this MarkovBot code](https://github.com/esdalmaijer/markovbot) and the [Twitter API](https://developer.twitter.com/en/docs) to create a TwitterBot that is capable of "imitating" any Twitter user with the Markov text analysis of that user's tweets. The bot reads tweets with [this get_all_tweets method](https://gist.github.com/yanofsky/5436496). 

In order to utilize this bot code, in addition to the code mentions above, consumer and access keys must be generated, as explained in [this great how-to](https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/). 

A future update to this bot will allow the bot to imitate a user as long as the mention has a valid handle in it, rather than requiring the "@imitatebot string @handle..." format. 
