import telebot
import fal_client

# Initialize the bot with your token
bot = telebot.TeleBot('5801349508:AAHc5mrpSWaTDDpsDMQoHk6Z6i2dXQaX_iY')

# Initialize the fal_client
#fal_client = fal_client.Client()

# Define the /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Send me a prompt and I will generate an image for you.")

# Define the message handler for text messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    handler = fal_client.submit(
        "fal-ai/flux-pro",
        arguments={
            "prompt": user_input
        },
    )
    result = handler.get()
    
    # Print the result in the interpreter
    print(result)
    
    # Extract the image URL from the result
    image_url = result['images'][0]['url']
    
    # Send the image URL to the user
    bot.reply_to(message, f"Here is your generated image: {image_url}")

# Start polling
bot.polling()
