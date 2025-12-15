import discum
import json
import Vars
import time

bot = discum.Client(token=Vars.token, log=False)
botID = '432610292342587392'

def check_message(resp):
    if resp.event.message:
        m = resp.parsed.auto()
        
        if m['channel_id'] != Vars.channelId:
            return

        if m['author']['id'] != botID:
            return

        try:
            if not m['embeds']:
                return
                
            embed = m['embeds'][0]
            
            if 'author' in embed and 'name' in embed['author']:
                cardName = embed['author']['name']
            else:
                return

            if 'description' in embed:
                description_parts = embed['description'].replace('\n', '**').split('**')
                cardSeries = description_parts[0]
                try:
                    cardPower = int(description_parts[1])
                except (IndexError, ValueError):
                    cardPower = 0
            else:
                return

            is_claimed = False
            if 'footer' in embed and 'icon_url' in embed['footer']:
                is_claimed = True
            
            emoji = '🐿️' 
            
            if not is_claimed:
                print(f"Detected: {cardName} - {cardSeries} ({cardPower})")
                if cardSeries in Vars.desiredSeries or cardName in Vars.desiredCharacters:
                    print(f'Trying to Claim {cardName}')
                    
                    button_clicked = False
                    if 'components' in m:
                        for row in m['components']:
                            for component in row['components']:
                                if component.get('type') == 2:
                                    print(f"Clicking claim button: {component.get('custom_id')}")
                                    bot.click(
                                        m['author']['id'], 
                                        channelID=m['channel_id'], 
                                        guildID=Vars.serverId, 
                                        messageID=m['id'], 
                                        messageFlags=m['flags'], 
                                        data={'component_type': 2, 'custom_id': component['custom_id']}
                                    )
                                    button_clicked = True
                                    break
                            if button_clicked:
                                break
                    
                    if not button_clicked:
                        print("No button found to claim!")
            else:
                print(f"Detected (Claimed): {cardName} - {cardSeries} ({cardPower})")

            if 'components' in m and len(m['components']) > 0:
                for component_row in m['components']:
                    for component in component_row['components']:
                        if 'emoji' in component and 'name' in component['emoji']:
                            cardsKakera = component['emoji']['name']
                            if cardsKakera in Vars.desiredKakeras:
                                print(f'Trying to react to {cardsKakera} of {cardName}')
                                bot.click(
                                    m['author']['id'], 
                                    channelID=m['channel_id'], 
                                    guildID=Vars.serverId, 
                                    messageID=m['id'], 
                                    messageFlags=m['flags'], 
                                    data={'component_type': 2, 'custom_id': component['custom_id']}
                                )

        except Exception as e:
            print(f"Error processing message: {e}")

print(f"Listening for Mudae rolls in channel {Vars.channelId}...")
bot.gateway.command(
    {
        "function": check_message
    }
)
bot.gateway.run(auto_reconnect=True)
