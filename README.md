# mensa-bot
A python script that connects an https://dash.import.io/ extractor with a telegram bot and posts messages.

## Preparation

You'll need some data that you want to share and push, a telegram bot and possibly one or many channels that you want to broadcast to.

#### Libraries

Install [requests](http://docs.python-requests.org/en/master/user/install/#install).

#### Extractor

We used https://dash.import.io/ to quickly and easily create an extractor for the website that holds our desired data. As a result, you'll be able to send `GET`-Requests to a REST-API made available by import.io. They also offer an RSS-Feed in case you want to skip telegram. Make sure that they have the correct data by testing the REST-call.

Once you're done, you should have:
- EXTRACTOR_ID
- EXTRACTOR_API_KEY
- (EXTRACTOR_RSS - optional)

#### Telegram Bot

The telegram team made it ridiculously easy to create a new telegram bot. Simply follow [these instructions](https://core.telegram.org/bots#3-how-do-i-create-a-bot). 

Once you're done, you should have:
- BOT_ID
- BOT_TOKEN

#### Broadcasts

Create one or multiple Broadcast Channels on telegram [(find out how)](https://telegram.org/faq_channels#q-what-39s-a-channel).

You chould get:
- [BROADCAST_ID] `// a list of broadcast ids`

## Usage

Change the file to fit your needs. Run it to get the data and send it. Trigger it by RSS or manually. (See next part for more information.) 

```bash
python main.py "EXTRACTOR_ID" "EXTRACTOR_API_KEY" "BOT_ID BOT_TOKEN" "TARGET_URL"
```

## Integration

#### RSS-triggered Terminal

Install [this lib](http://python-rsstail.readthedocs.io/en/latest/) and use it as described in [this example](http://stackoverflow.com/a/25351065/5299750) to trigger script whenever there is an rss update on the RSS Feed of your import.io extractor. (You can define how often there should be an update in the import.io settings.

#### Docker Cronejob

Explanation to follow soon.
