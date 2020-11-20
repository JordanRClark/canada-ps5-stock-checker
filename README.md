# canada-ps5-stock-checker
Stock checker for ps5 drops

To begin:

Requirements:
python3.5 +

Installing:
Make a virtual environment for python and install the requirements.
cd ps5-stock-checker/requirements
pip install -r base.txt

Settings:
There's some settings which need to be set in order to post alerts.
Right now the only alerts that are posted are to discord.
You will need to create a bot, create a guild (If you don't have one),
and Oauth the bot into the guild.
More details here: https://realpython.com/how-to-make-a-discord-bot-python/

Once that is live, you will need to take IDs of the channel / UserId to
post messages to


Running:
Run the main program to start checking prices!
cd ps5-stock-checker
chmod +x main.py
./main.py

Contributing:
Install pre-commit hooks so code is correctly formatted and checked
pre-commit install

Create PRs for review
