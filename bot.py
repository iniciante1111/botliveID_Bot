from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Definir uma função para o comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! O que você deseja fazer?")

# Definir uma função para o comando /hello
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá!")

# Definir uma função para mensagens de texto
def text_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Desculpe, não entendi o que você quis dizer.")

# Criar um objeto Updater e passar o token do seu bot do Telegram
updater = Updater(token='6233432014:AAEOvoKtu6z2R9uZHjek4B8T5JJXwGIXDIA', use_context=True)

# Obter o objeto dispatcher do updater
dispatcher = updater.dispatcher

# Adicionar um handler para o comando /start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Criar os handlers para os comandos e as mensagens de texto
hello_handler = CommandHandler('hello', hello)
text_handler = MessageHandler(Filters.text & (~Filters.command), text_message)

# Adicionar os handlers ao dispatcher
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(text_handler)

# Iniciar o loop do Updater
updater.start_polling()

# Manter o bot em execução
updater.idle()
