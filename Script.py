class script(object):
    START_TXT = """<b>HOW ARE YOU {} DUDE ๐คฉ,Nice To Meet You๐</b>
\n<i>๐จ'๐ ๐๐๐๐ ๐บ ๐๐๐๐๐๐พ ๐๐๐พ - ๐ฟ๐๐๐ผ๐๐๐๐๐พ๐ฝ ๐บ๐๐๐๐ฟ๐๐๐๐พ๐ ๐ป๐๐</i>
<b><i>Its Simple To Use Me..โบ๏ธ,Just Add Me To Your Group As Admin,Thats All I Will Provide Movies There..๐ฅฐ</i></b>"""
    HELP_TXT = """<b>HEY {} DUDE ๐โโ๏ธ</b>
\n<b>Just Add To Your Group As Admin Its All.โบ๏ธ,</b> \n<i>I Will Provide Movies There...โก๏ธ</i>"""
    ABOUT_TXT = """ <code> IAM JUST A  Auto-Filter-Bot </code>๐ถโโ๏ธโ ๏ธ

โช ๐ด๐ ๐๐๐๐ : ๐นแดxษชแด
โช <b>๐ช๐๐๐๐๐๐ : <a href='https://t.me/OGGY123kph'>๐บสษชแด แด ๐ต๏ธโโ๏ธ</a>
โช ๐ช๐๐๐๐๐๐ : <code>Everyone in this journey</code>
โช ๐ณ๐๐๐๐๐๐ : <a href='https://docs.pyrogram.org/'>๐ทสสแดษขสแดแด ๐</a>
โช ๐ณ๐๐๐๐๐๐๐ : <code>๐ทสแดสแดษด 3</code>
โช ๐ซ๐๐๐ ๐๐๐๐ : <a href='https://www.mongodb.com/'>๐ดแดษดษขแด ๐ซส</a>
โช ๐ฉ๐๐ ๐๐๐๐๐๐ : <a href='https://dashboard.heroku.com/apps'>๐ฏแดสแดแดแด</a>
โช ๐บ๐๐๐๐๐ ๐ช๐๐๐ : <a href='https://t.me/joinchat/aYbIjDgZqY9lYjQ9'>๐ ๐ชสษชแดแด ๐ฏแดสแด</a>
โช ๐ฉ๐๐๐๐ ๐บ๐๐๐๐๐ : <code>v1.0.1 [ ๐ฉแดแดแด ]</code>
\n\n๐ ๐ธ๐๐๐๐ : <code>เดเดฐเตเด เดชเตเดเดฟเดเตเดเตเดฃเตเด เดเดฒเตเดฒเดพเดตเตผเดเตเดเตเด เดเดฟเดเตเดเตเด</code></b>"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>๐ณ๐๐๐ ๐ก๐๐ ๐ถ๐บ๐ ๐ฌ๐บ๐๐พ๐ฝ ๐ณ๐บ๐๐๐๐ ๐ฒ๐๐๐บ๐๐ ๐ฑ๐พ๐๐๐ ๐ฎ๐ฟ ๐ฎ๐๐๐พ๐ ๐ช๐๐๐ฝ ๐ก๐๐๐

๐ฒ๐ฎ๐ด๐ฑ๐ข๐ค ๐ข๐ฎ๐ฃ๐ค ~ ๐ญ๐ฎ๐ณ ๐ ๐ต๐ ๐จ๐ซ๐ ๐ก๐ซ๐ค ๐ฑ๐จ๐ฆ๐ง๐ณ ๐ญ๐ฎ๐ถ</b>

<b>๐ฎ๐ณ๐ง๐ค๐ฑ ๐ช๐จ๐ญ๐ฃ ๐ก๐ฎ๐ณ๐ฒ:</b>
<b>๐ ๐ด๐ณ๐ฎ ๐ฅ๐จ๐ซ๐ณ๐ค๐ฑ</b> : <a href='https://github.com/EvamariaTG/EvaMaria'>๐ค๐๐บ ๐ฌ๐บ๐๐๐บ</a>

<b>๐ฒ๐ฎ๐ญ๐ฆ</b> :  <a href='https://github.com/AsmSafone/RadioPlayerV2'>๐ ๐๐๐ฒ๐บ๐ฟ๐๐๐พ</a>

<b>๐ฅ๐จ๐ซ๐ณ๐ค๐ฑ</b> : <a href='https://github.com/TroJanzHEX/Unlimited-Filter-Bot'>๐ด๐๐๐๐๐๐๐พ๐ฝ ๐ฅ๐๐๐๐พ๐ ๐ก๐๐</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
<b>Extra ๐ถ Show Commands</b>

<b>๐ญ๐ฎ๐ณ๐ค: ๐๐๐พ๐๐พ ๐บ๐๐พ ๐๐๐พ ๐พ๐๐๐๐บ ๐ฟ๐พ๐บ๐๐๐๐พ๐ ๐๐ฟ Rexie</b>
โข /id - <code>get id of a specifed user.</code>

โข /info  - <code>get information about a user.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """๐ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โก TOTAL USERS : <code>{}</code>
๐ TOTAL CHATS : <code>{}</code>
๐ USED STORAGE: <code>{}</code> MB
๐ญ FREE STORAGE: <code>{}</code> MB"""
    LOG_TEXT_G = """#NewGroup
โก Group = {}(<code>{}</code>)
๐ณ Total Members = <code>{}</code>
๐ต๏ธโโ๏ธ Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
