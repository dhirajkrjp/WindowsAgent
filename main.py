from controllers import windows_ctrl, chrome_ctrl, outlook_ctrl

def execute_command(command_text):
    """A dumb, hardcoded router to test our tools before adding AI."""
    parts = command_text.lower().strip().split(" ", 1)
    action = parts[0]
    argument = parts[1] if len(parts) > 1 else ""

    if action == "search":
        chrome_ctrl.search_google(argument)
        
    elif action == "notepad":
        windows_ctrl.open_application("Notepad", "notepad.exe")
        
    elif action == "email":
        # Hardcoding a test scenario for email
        # Expected command format: "email [name]"
        if "rahul" in argument:
            outlook_ctrl.draft_email(
                to_address="rahul@example.com",
                subject="Meeting Update",
                body="I will join the meeting in 10 minutes.\n\nRegards,"
            )
        else:
            print("--> [Router] Contact not recognized in test database.")
            
    elif action == "exit":
        print("Shutting down agent.")
        exit()
        
    else:
        print("--> [Router] Unknown command. Available: search [query], notepad, email rahul, exit")

def main():
    print("=== Windows Agent Prototype (Non-AI Mode) ===")
    print("Type a command to test the controllers.")
    
    while True:
        try:
            cmd = input("\nEnter command: ")
            execute_command(cmd)
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()