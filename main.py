import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6646431554:AAFU_Kcg_mty4JGaduqpN-yzZfVwzXMA5AE'
BOT_USERNAME ='@Anbu_Album_Bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am Anbu's Album Handler Bot.")
    await update.message.reply_text("Pick any of those request /photo, /video, /link, /ice_cream.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How can i asist you?")

async def icre_cream(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ice cream photos")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is custom command")

#to send file, photo, video, link
async def send_photo(update: Update, context):
    photo_path = 'D:\\anbu\\POSTER.jpg'
    await update.message.reply_text("Currently I only have the Poster of my Owner, Here it is:")
    await update.message.reply_photo(photo=open(photo_path, 'rb'))

async def send_files_from_folder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    folder_path = 'D:\work\pro images'

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        for file in files:
            with open(os.path.join(folder_path, file), 'rb') as f:
                await context.bot.send_document(chat_id=chat_id, document=f)
    else:
        response = f"Folder not found: {folder_path}"
        await update.message.reply_text("Here is some ice cream pics")
        await context.bot.send_message(chat_id=chat_id, text=response)

async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # video_path = os.path.join(FILES_FOLDER, 'video.mp4')
    #  await update.message.reply_video(video=open(video_path, 'rb'))
        await update.message.reply_text("sorry currently i have only one poster click it /photo to view it")

async def send_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # link = 'https://www.example.com'
    # await update.message.reply_text(link)
    await update.message.reply_text("sorry currently i have only one poster click it /photo to view it")

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
         return 'Hey there'
    if 'how are you' in processed:
        return 'i am good'
    if 'i love you' in processed:
        return "As I am Anbu's Bot I need access from my Owner anyway you are cute"
    
    return 'I am not Instructed to this type of question'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: {text}')

    if message_type =='group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("BOT:", response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == "__main__":
   app = Application.builder().token(TOKEN).build()

   print("Started....")
   app.add_handler(CommandHandler('start', start_command))
   app.add_handler(CommandHandler('help', help_command))
   app.add_handler(CommandHandler('custom', custom_command))
   app.add_handler(CommandHandler('photo', send_photo))
   app.add_handler(CommandHandler('video', send_video))
   app.add_handler(CommandHandler('link', send_link))
   app.add_handler(CommandHandler('ice_cream', send_files_from_folder))
   #message
   app.add_handler(MessageHandler(filters.TEXT, handle_message))

   #eroors
   app.add_error_handler(error)

   #polling
   print("polling...")
   app.run_polling(poll_interval = 3)