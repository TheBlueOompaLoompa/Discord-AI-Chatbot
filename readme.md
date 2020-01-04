# Discord-AI-Chatbot
Chatbot part created by Tech With Tim https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
The rest of it was done by me plus some improvements.

Requires-
Python 3.6 due to Tensorflow
Windows

Run pip install -r requirements.txt when you are in the directory in your terminal or command prompt

# Setup
1. Go to https://discordapp.com/developers/applications
2. Create an application with any name
3. Go to the Bot tab and create a bot
4. Copy the token
5. Paste the token as the client token in the discordai.py python file
6. Add any users you want to be admins into the file (User format: username#userid)
7. Go back to the discord developer website and click on the general information tab
8. https://discordapp.com/api/oauth2/authorize?client_id=clientidnumber&scope=bot&permissions=1 Replace clientidnumber with the client id on the general information page and go to that link
9. Fill out the information on that page to add the bot to your discord server
10. Open command prompt and type in cd *space* then drag in the folder of the python file then press enter
11. Run the command python discordai.py
12. You now have a working discord chatbot

# How to start a conversation
Use $ to start a conversation with the AI, and $ ends the conversation too.

# Test out a fully setup version

https://discord.gg/8UwBKRn

# Commands (In discord)
Admin:

Quit
Exit
Stop

Other-
To view a full list of all the paths open the intents.json file to view current setups and maybe create new ones.
