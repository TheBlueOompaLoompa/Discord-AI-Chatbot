# Discord-AI-Chatbot
Chatbot part created by Tech With Tim https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg with extra modifications to add branched speech
The rest of it was done by me plus some improvements.

Requires-
Python 3.6 due to Tensorflow
Windows

# Test out a fully setup version

https://discord.gg/8UwBKRn

# Setup
1. Run pip install -r requirements.txt when you are in the directory in your terminal or command prompt
2. Go to https://discordapp.com/developers/applications
3. Create an application with any name
4. Go to the Bot tab and create a bot
5. Copy the token
6. Paste the token as the client token in the discordai.py python file
7. Add any users you want to be admins into the file (User format: username#userid)
8. Go back to the discord developer website and click on the general information tab
9. https://discordapp.com/api/oauth2/authorize?client_id=clientidnumber&scope=bot&permissions=1 Replace clientidnumber with the client id on the general information page and go to that link
10. Fill out the information on that page to add the bot to your discord server
11. Open command prompt and type in cd *space* then drag in the folder of the python file then press enter
12. Run the command python discordai.py
13. You now have a working discord chatbot

# How to start a conversation
Use $ to start a conversation with the AI, and $ ends the conversation too.

# Commands (In discord)
Admin:

1. Quit
2. Exit
3. Stop

Other-
To view a full list of all the paths open the intents.json file to view current setups and maybe create new ones.
