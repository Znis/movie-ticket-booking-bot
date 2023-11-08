from discord_webhooks import DiscordWebhooks
webhook_url = 'https://discord.com/api/webhooks/' #discord webhook api


def send_msg(movie_name,status,datee):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    # Attaches a footer
    webhook.set_footer(text='-- QFX Bot')

    if(status=="coming-soon"):

      webhook.set_content(title=movie_name,
                          description="Its COMING SOON! :star_struck:")

      # Appends a field
      webhook.add_field(name='Movie', value=movie_name)
      webhook.add_field(name='Status', value='Coming Soon')

    elif(status=="booked"):
      webhook.set_content(title = movie_name,
                          description="Seats Booked!! :heart: ")

      # Appends a field
      webhook.add_field(name='Movie', value= movie_name)
      webhook.add_field(name='Status', value= 'Seats Booked')
      webhook.add_field(name='Time', value = datee)
      webhook.add_field(name='Message', value = 'PAY THE BILL ASAP!!')

    elif(status=="available"):
      webhook.set_content(title = movie_name,
                          description="Movie Available!! :sunglasses: ")

      # Appends a field
      webhook.add_field(name='Movie', value= movie_name)
      webhook.add_field(name='Status', value= 'Available on NOW SHOWING')
      webhook.add_field(name='Message', value = 'Searching for available seats ...')

    elif(status=="not-available"):
      webhook.set_content(title = movie_name,
                          description="Valid Shift Not Found :sob:")

      # Appends a field
      webhook.add_field(name='Movie', value= movie_name)
      webhook.add_field(name='Status', value= 'Available on NOW SHOWING')
      webhook.add_field(name='Message', value = 'Could not find valid shift')
    




    webhook.send()

    print("Message Sent To Discord", end = '\n\n')