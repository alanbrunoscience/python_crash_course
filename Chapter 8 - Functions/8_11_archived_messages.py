def send_messages(messages, sent_messages):
    
    print("--- MOTIVATIONAL PHRASES ---\n")
    while messages:
        current_message = messages.pop()
        print(f'-> "{current_message}."')
        sent_messages.append(current_message)
        
messages = ["If you judge people you have no time to love them", 
            "Happiness is not by chance, but by choice", 
            "Try to be a rainbow in someone's cloud", 
            "A problem is a chance for you to do your best",
            "Talk to yourself like someone you love"]
sent_messages = []

send_messages(messages[:], sent_messages)
print(f"\n- Messages list: {messages}")
print(f"- Sent messages list: {sent_messages}")