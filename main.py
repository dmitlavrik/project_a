import setup
import telegram.ext
from uuid import uuid4

TOKEN = setup.get_token()
REQUEST_KWARGS = setup.get_request_kwargs()

updater = telegram.ext.Updater(TOKEN, use_context = True,
                               request_kwargs = REQUEST_KWARGS)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = "I'm a bot, please talk to me!")

start_handler = telegram.ext.CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def set_place(update, context):
    """ Usage: /set_place @id """


def put(update, context):
    """Usage: /put value"""
    # Generate ID and seperate value from command
    key = str(uuid4())
    value = update.message.text.partition(' ')[2]

    # Store value
    context.user_data[key] = value

    update.message.reply_text(key)

dispatcher.add_handler(telegram.ext.CommandHandler('put', put))

def get(update, context):
    """Usage: /get uuid"""
    # Seperate ID from command
    key = update.message.text.partition(' ')[2]

    # Load value
    try:
        value = context.user_data[key]
        update.message.reply_text(value)

    except KeyError:
        update.message.reply_text('Not found')

dispatcher.add_handler(telegram.ext.CommandHandler('get', get))

updater.start_polling()

# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)
#
# def caps(update, context):
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
#
# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)
#
# j = updater.job_queue
#
# from telegram.ext import CallbackContext
# def callback_increasing(context: CallbackContext):
#     job = context.job
#     context.bot.send_message(chat_id='@heheeeboi',
#                              text='Sending messages with increasing delay up to 10s, then stops.')
#     job.interval += 1.0
#     if job.interval > 10.0:
#         job.schedule_removal()
#
# j.run_repeating(callback_increasing, 1)
#
# from telegram import Update
# def callback_alarm(context: CallbackContext):
#     context.bot.send_message(chat_id=context.job.context, text='BEEP')
#
# def callback_timer(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.message.chat_id,
#                              text='Setting a timer for 1 minute!')
#
#     context.job_queue.run_once(callback_alarm, 60, context=update.message.chat_id)
#
# timer_handler = CommandHandler('timer', callback_timer)
# updater.dispatcher.add_handler(timer_handler)
#
# def unknown(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
#
# unknown_handler = MessageHandler(Filters.command, unknown)
# dispatcher.add_handler(unknown_handler)
#
# from telegram.error import (TelegramError, Unauthorized, BadRequest,
#                             TimedOut, ChatMigrated, NetworkError)
#
# def error_callback(update, context):
#     error = "None"
#     try:
#         raise context.error
#     except Unauthorized:
#         # remove update.message.chat_id from conversation list
#         error = "Uno"
#     except BadRequest:
#         # handle malformed requests - read more below!
#         error = "Bad"
#     except TimedOut:
#         # handle slow connection problems
#         error = "Time"
#     except NetworkError:
#         # handle other connection problems
#         error = "Net"
#     except ChatMigrated as e:
#         # the chat_id of a group has changed, use e.new_chat_id instead
#         error = "Chat"
#     except TelegramError:
#         # handle all other telegram related errors
#         error = "Teleg"
#     context.bot.send_message(chat_id=update.effective_chat.id, text=error)
#
# dispatcher.add_error_handler(error_callback)

updater.start_polling()
