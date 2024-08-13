def show_messages(messages):
    
    print("--- MOTIVATIONAL PHRASES ---\n")
    for message in messages:    
        print(f'-> "{message}."')
        
messages = ["If you judge people you have no time to love them", 
            "Happiness is not by chance, but by choice", 
            "Try to be a rainbow in someone's cloud", 
            "A problem is a chance for you to do your best",
            "Talk to yourself like someone you love"]

show_messages(messages)