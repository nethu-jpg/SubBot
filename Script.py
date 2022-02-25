class script(object):
    START_TXT = """<b>කොහොමද ඉතින්  {},
මන් සිංහල උපසිරැසි දෙන බොට් කෙනෙක් 🙂❤️. ඔයාගෙ Group එකටත් මාව ඇඩ් කරල මට ඇඩ්මින් දෙන්න 🤗.</b>"""
    HELP_TXT = """ <b>හායි {}
බොට්ව පාවිච්චි කරන හැටි සිංහලෙන්ම තියෙනවා ඕන්.</b>"""
    MORE_TXT = """ <b>More help for group managment </b>"""
    ABOUT_TXT = """
    <b>○ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/sinhala_subtitles_bot>සිංහල සබ් බොට්</a>
    ○ ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ
    ○ ғʀᴀᴍᴇᴡᴏʀᴋ: ᴘʏʀᴏɢʀᴀᴍ
    ○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :🔐
    ○ ᴠᴇʀsɪᴏɴ : 2.7.7
    ○ ᴄʀᴇᴀᴛᴏʀ : ᴇᴠᴀ ᴍᴀʀɪᴀ ᴄʀᴇᴀᴛᴇʀꜱ</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    GRUPAK_TXT = """<b><u>Sinahala Subtitle Groups</b></u>

- <code>Sinahala Sub Groups In Sri Lanka.</code>
<b>• @SubsInfinity_Subtitles_Sinhala - </b><code>{2K+}</code>
<b>• 
• 
• </b>

<b>★ ඔයාගෙ එකත් මෙතනට දාගන්න <a href=https://t.me/Pokemon_Academy_ContactBot>ඇඩ්මින් කෙනෙක්</a> කන්ටැක්ට් කරගන්න 😄👌.</b>
"""
    HOWTOGIVE_TXT = """<u><b>❗️ ඔයාගෙ සබ් බොට්ට ඇඩ් කරන්නෙ කොහොමද?</b></u>

<b>NOTE:</b>
1. ඔයාගෙ සබ් තියෙන චැනල් එක privet චැනල් එකක් නම් බොට්ව ඒකෙ ඇඩ්මින් කරන්න.
2. අනේ ඉතින් සිංහල සබ් ඇර වෙන එකේක එව්ව තියෙන ඒව නම් එපා සාන්ත 🙂.
3. සාමාන්‍ය විදිහට චැනල් එකේ අන්තිමට දාල තියෙන මැසේජ් එක බොට්ට ෆෝවර්ඩ් කරන්න 😇.
ඉතිරි හරිය මන් බලාගන්නම් 😎👌 ."""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mewtwo_pabot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message, You should use @MEWTEO_PAbot to get tv series )</code>"""
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
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
★ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱
★ ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱"""
    HOWTOFIND_TXT = """<b><u>❗️ සබ් බොට්ගෙන් සබ් ගන්නෙ කොහොමද ? </b></u>

- <i>බොට්ගෙන් සබ් ගන්න කලින් ඔයා අනිවාර්‍යෙන්ම බොට් ඉන්න group එකක මෙම්බර් කෙනෙක් වෙලා ඉන්න ඔනෙ😗, එහෙම නැතුව botට මැසේජ් දැම්මට වැඩක් නැහැ 🥲</i>

<b>NOTE:</b>
1. මේ bot ඉන්න group එකක මෙම්බර් කෙනෙක් වෙලා ඉන්න ඔනෙ 🤗.
2. ඔයාට ඕනෙ සබ් එකේ නම group එකට දාන්න, ඔයා හොයන්නෙ ෆිල්ම් එකක් නම් රිලීස් කරපු අවුරැද්දත් එක්ක දාන්න💆.
3. අපේ ඩේටබේස් එකේ ඔයා හොයන දේ තියෙනවනම් ඉක්මනට හොයාගන්න පුලුවන්😗🔥.

<b>• සබ් group නැත්තන් පහල එකට join වෙන්න.</b> """
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
