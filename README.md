# Thumbot
![thumb](http://i.giphy.com/I83tvEbSgRy8M.gif)

**Thumbot** is a :thumbsup: :thumbsdown: counter keyboard for Telegram bots and channels.

![photo31331718161082944](https://cloud.githubusercontent.com/assets/431892/21070814/1a44c100-be75-11e6-9995-06a82bce7e41.jpg)


## Requirements
- Python;
- Your bot/channel must be created with [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI);
- MongoDB;


## Running

- Your're going to need to run an instance of [MongoDB](https://mongodb.com). For tests porpuse (or even production, but with some concerns) you can run the command below to get  a [Docker](https://docker.com/) container running:

  `$ docker run -d -p 27017:27017 mongo`

- To install Thumbot is pretty easy:

  `$ pip install thumbot`

- Now, you're ready to include the Thumbot keyboard in your bot or channel!


## Usage
```py
from thumbot import Thumbot

# Create a new instance of Thumbot passing chat and message ids:
thumbot = Thumbot(chat_id, message_id)

# Now you can vote up and down with the methods .up() and .down(),
# always passing the id of the user that is voting:
thumbot.up(user_id)
thumbot.down(user_id)
```

Check out the [example.py](https://github.com/rougeth/thumbot/blob/master/example.py) to see a full working bot using Thumbot.


### Bots and Channels using Thumbot:
- [@on_sale](https://telegram.me/on_sale)
