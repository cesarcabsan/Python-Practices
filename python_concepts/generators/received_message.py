def message_receiver():
    print("[Receiver]: Starting up and waiting for the first message...")

    try:
        while True:
            # The generator pauses at 'yield'. 
            # It yields "Ready" to the caller, and waits for a value from .send()
            incoming_message = yield "Ready"

            # When .send(value) is called, the generator resumes and assigns the value
            print(f"[Receiver] '{incoming_message}'")

            # Simple processing logic
            if incoming_message == 'ping':
                print('[Receiver] pong!')
        
    except GeneratorExit:
        # This block catches the exception raised when .close() is called
        print("[Receiver] And that all for today, Goodbye!")


## Using the generator
# 1. Initializing
chat = message_receiver()

# 2. "Prime" the generator (Crucial Step!)
# You MUST advance the generator to the first 'yield' before you can send data.
# You can do this with next(chat) or chat.send(None).
status = chat.send(None)
print(f"Generator status: {status}\n")

# 3. Send messages into the generator
# The string passed to .send() becomes the value of 'incoming_message'
chat.send("Hello generator!")
chat.send("ping")
chat.send("Want to start learning programming?")
chat.send("You might wanna try Python.")

# 4. Close the generator
# This triggers the GeneratorExit exception inside the while loop
print("\n[main] Closing connection....")
chat.close()

# If you try to send a message after closing, it will raise a StopIteration error.
