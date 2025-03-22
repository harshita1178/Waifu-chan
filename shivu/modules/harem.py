from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from itertools import groupby
import random
import math
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler, filters
from shivu import collection, user_collection, application

async def harem(update: Update, context: CallbackContext, page=0) -> None:
    user_id = update.effective_user.id  
    user = await user_collection.find_one({'id': user_id})

    if not user:
        message = '<b>ʏᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ɢʀᴀʙʙᴇᴅ ᴀɴʏ ᴄʜᴀʀᴀᴄᴛᴇʀs ʏᴇᴛ.</b>'
        if update.message:
            await update.message.reply_html(message)
        else:
            await update.callback_query.edit_message_text(message, parse_mode='HTML')
        return

    selected_rarity = user.get('selected_rarity', 'Default')
    characters = sorted(user['characters'], key=lambda x: (x['anime'], x['id']))
    
    if selected_rarity and selected_rarity != 'Default':
        characters = [char for char in characters if char['rarity'][0] == selected_rarity[0]]

    character_counts = {k: len(list(v)) for k, v in groupby(characters, key=lambda x: x['id'])}
    unique_characters = list({char['id']: char for char in characters}.values())
    total_pages = math.ceil(len(unique_characters) / 15)

    page = max(0, min(page, total_pages - 1))
    harem_message = f"{update.effective_user.first_name}'s ʜᴀʀᴇᴍ - ᴘᴀɢᴇ {page+1}/{total_pages}\n"
    
    current_chars = unique_characters[page*15:(page+1)*15]
    current_grouped = {k: list(v) for k, v in groupby(current_chars, key=lambda x: x['anime'])}

    for anime, chars in current_grouped.items():
        anime_count = await collection.count_documents({"anime": anime})
        harem_message += f'\n𖤍 <b>{anime}</b> ｛{len(chars)}/{anime_count}｝\n⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n'
        for char in chars:
            count = character_counts[char['id']]
            harem_message += f'𒄬 {char["id"]} [ {char["rarity"][0]} ] {char["name"]} ×{count}\n'
        harem_message += '⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋⚋\n'

    total_count = len(user['characters'])
    keyboard = [
        [InlineKeyboardButton(f"sᴇᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ({total_count})", switch_inline_query_current_chat=f"collection.{user_id}")],
        [InlineKeyboardButton(f"{page+1}/{total_pages}", callback_data="ignore")]
    ]
    
    if total_pages > 1:
        nav_buttons = []
        if page > 0:
            nav_buttons.append(InlineKeyboardButton("⬅️1x", callback_data=f"harem:{page-1}:{user_id}"))
        if page < total_pages - 1:
            nav_buttons.append(InlineKeyboardButton("1x➡️", callback_data=f"harem:{page+1}:{user_id}"))
        keyboard.append(nav_buttons)

    reply_markup = InlineKeyboardMarkup(keyboard)
    random_character = random.choice(user['characters']) if user['characters'] else None

    if random_character and 'img_url' in random_character:
        if update.message:
            await update.message.reply_photo(photo=random_character['img_url'], caption=harem_message, reply_markup=reply_markup, parse_mode='HTML')
        else:
            await update.callback_query.edit_message_media(
                media=InputMediaPhoto(media=random_character['img_url'], caption=harem_message, parse_mode='HTML'),
                reply_markup=reply_markup
            )
    else:
        if update.message:
            await update.message.reply_text(harem_message, reply_markup=reply_markup, parse_mode='HTML')
        else:
            await update.callback_query.edit_message_text(harem_message, reply_markup=reply_markup, parse_mode='HTML')

async def harem_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    _, page, user_id = query.data.split(':')
    page, user_id = int(page), int(user_id)

    if query.from_user.id != user_id:
        await query.answer("ᴅᴏɴ'ᴛ sᴛᴀʟᴋ ᴏᴛʜᴇʀ ᴜsᴇʀ's ʜᴀʀᴇᴍ..  OK", show_alert=True)
        return

    await harem(update, context, page)

application.add_handler(CommandHandler("harem", harem, block=False))
application.add_handler(CallbackQueryHandler(harem_callback, pattern='^harem', block=False))
