import edge_tts
import asyncio
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Define the available voices
voices = {
    'Emma': 'en-US-EmmaMultilingualNeural',
    'Guy': 'fr-FR-VivienneMultilingualNeural',
    'Serafina': 'de-DE-SeraphinaMultilingualNeural',
    'Florian': 'de-DE-FlorianMultilingualNeural',
    'swara': 'hi-IN-SwaraNeural',
    'Remy': 'fr-FR-RemyMultilingualNeural',
    'Ava': 'en-US-AvaMultilingualNeural',
    'Andrew': 'en-US-AndrewMultilingualNeural',
    'Brian': 'en-US-BrianMultilingualNeural',
    'Pallavi[tamil]': 'ta-IN-PallaviNeural',
    'Valluvar[tamil]': 'ta-IN-ValluvarNeural',
    'Kumar[tamil]': 'ta-LK-KumarNeural',
    'Saranya[tamil]': 'ta-LK-SaranyaNeural',
    'Kani[tamil]': 'ta-MY-KaniNeural',
    'Surya[tamil]': 'ta-MY-SuryaNeural',
    'Anbu[tamil]': 'ta-SG-AnbuNeural',
    'Venba[tamil]': 'ta-SG-VenbaNeural'
}

# Store user IDs for broadcasting
user_ids = set()

def save_user_ids():
    with open('user_ids.json', 'w') as file:
        json.dump(list(user_ids), file)

def load_user_ids():
    try:
        with open('user_ids.json', 'r') as file:
            return set(json.load(file))
    except FileNotFoundError:
        return set()

async def tts(file_name: str, toConvert: str, voice: str):
    communicate = edge_tts.Communicate(toConvert, voice=voice)
    await communicate.save(file_name)

async def convert_text_to_speech(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_input = update.message.text
    voice = context.user_data.get('voice', 'en-US-EmmaMultilingualNeural')
    try:
        print(f"Converting text: {text_input} with voice: {voice}")
        await tts(f'edge-tts.mp3', text_input, voice)
        await update.message.reply_text("Speech conversion successful")
        await update.message.reply_audio(audio=open('edge-tts.mp3', 'rb'))
    except Exception as e:
        print(f"Error during TTS conversion: {e}")
        await update.message.reply_text(f"An error occurred: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await check_subscription(update, context):
        if update.effective_chat.id not in user_ids:
            user_ids.add(update.effective_chat.id)
            save_user_ids()
            print(f"New user added: {update.effective_chat.id}")

        keyboard = [
            [InlineKeyboardButton("Emma", callback_data='Emma')],
            [InlineKeyboardButton("Guy", callback_data='Guy')],
            [InlineKeyboardButton("Serafina", callback_data='Serafina')],
            [InlineKeyboardButton("Florian", callback_data='Florian')],
            [InlineKeyboardButton("Next", callback_data='next')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Select voice model:', reply_markup=reply_markup)

'''async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'next':
        keyboard = [
            [InlineKeyboardButton("Remy", callback_data='Remy')],
            [InlineKeyboardButton("Ava", callback_data='Ava')],
            [InlineKeyboardButton("Andrew", callback_data='Andrew')],
            [InlineKeyboardButton("Next", callback_data='next2')],
            [InlineKeyboardButton("Previous", callback_data='previous')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text='Select voice model:', reply_markup=reply_markup)
    elif query.data == 'next2':
        keyboard = [
            [InlineKeyboardButton("Pallavi[tamil]", callback_data='Pallavi[tamil]')],
            [InlineKeyboardButton("Valluvar[tamil]", callback_data='Valluvar[tamil]')],
            [InlineKeyboardButton("Kumar[tamil]", callback_data='Kumar[tamil]')],
            [InlineKeyboardButton("Saranya[tamil]", callback_data='Saranya[tamil]')]
	               [InlineKeyboardButton("Previous", callback_data='previous2')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text='Select voice model:', reply_markup=reply_markup)
    elif query.data == 'previous':
        keyboard = [
            [InlineKeyboardButton("Emma", callback_data='Emma')],
            [InlineKeyboardButton("Guy", callback_data='Guy')],
            [InlineKeyboardButton("Serafina", callback_data='Serafina')],
            [InlineKeyboardButton("Florian", callback_data='Florian')],
            [InlineKeyboardButton("Next", callback_data='next')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text='Select voice model:', reply_markup=reply_markup)
    elif query.data == 'previous2':
        keyboard = [
            [InlineKeyboardButton("Remy", callback_data='Remy')],
            [InlineKeyboardButton("Ava", callback_data='Ava')],
            [InlineKeyboardButton("Andrew", callback_data='Andrew')],
            [InlineKeyboardButton("Brian", callback_data='Brian')],
            [InlineKeyboardButton("Next", callback_data='next2')],
            [InlineKeyboardButton("Previous", callback_data='previous')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text='Select voice model:', reply_markup=reply_markup)
    else:
        voice = voices[query.data]
        context.user_data['voice'] = voice
        await query.edit_message_text(text=f"Selected voice model: {query.data}")
'''
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'next':
        keyboard = [
            [InlineKeyboardButton("Remy", callback_data='Remy')],
            [InlineKeyboardButton("Ava", callback_data='Ava')],
            [InlineKeyboardButton("Andrew", callback_data='Andrew')],
            [InlineKeyboardButton("Brian", callback_data='Brian')],
            [InlineKeyboardButton("swara", callback_data='swara')],
            [InlineKeyboardButton("Next", callback_data='next2')],
            [InlineKeyboardButton("Previous", callback_data='previous')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text='Select voice model:', reply_markup=reply_markup)
    elif query.data == 'next2':
        keyboard = [
            [InlineKeyboardButton("Pallavi[tamil]", callback_data='Pallavi[tamil]')],
            [InlineKeyboardButton("Valluvar[tamil]", callback_data='Valluvar[tamil]')],
            [InlineKeyboardButton("Kumar[tamil]", callback_data='Kumar[tamil]')],
            [InlineKeyboardButton("Saranya[tamil]", callback_data='Saranya[tamil]')],
            [InlineKeyboardButton("Previous", callback_data='previous2')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text='Select voice model:', reply_markup=reply_markup)
    elif query.data == 'previous':
        keyboard = [
            [InlineKeyboardButton("Emma", callback_data='Emma')],
            [InlineKeyboardButton("Guy", callback_data='Guy')],
            [InlineKeyboardButton("Serafina", callback_data='Serafina')],
            [InlineKeyboardButton("Florian", callback_data='Florian')],
            [InlineKeyboardButton("Next", callback_data='next')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text='Select voice model:', reply_markup=reply_markup)
    elif query.data == 'previous2':
        keyboard = [
            [InlineKeyboardButton("Remy", callback_data='Remy')],
            [InlineKeyboardButton("Ava", callback_data='Ava')],
            [InlineKeyboardButton("Andrew", callback_data='Andrew')],
            [InlineKeyboardButton("Brian", callback_data='Brian')],
            [InlineKeyboardButton("Next", callback_data='next2')],
            [InlineKeyboardButton("Previous", callback_data='previous')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text='Select voice model:', reply_markup=reply_markup)
    else:
        voice = voices[query.data]
        context.user_data['voice'] = voice
        await query.edit_message_text(text=f"Selected voice model: {query.data}")
async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    channel_id = '-1002004608940'  # Replace with your channel ID
    chat_member = await context.bot.get_chat_member(channel_id, chat_id)
    if chat_member.status not in ['member', 'creator', 'administrator']:
        keyboard = [
            [InlineKeyboardButton("Subscribe", url='https://t.me/abhibot2023')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Please subscribe to our channel to use this bot:', reply_markup=reply_markup)
        return False
    return True
def main():
    application = Application.builder().token('paste_your_bot_token').build()  # Replace with your bot token

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, convert_text_to_speech))

    application.run_polling()

if __name__ == '__main__':
    main()
