import win32com.client

def draft_email(to_address, subject, body):
    """Opens the local Outlook app and creates a visible email draft."""
    print(f"--> [Outlook] Drafting email to {to_address}")
    
    try:
        # Connect to the installed Outlook application
        outlook = win32com.client.Dispatch("Outlook.Application")
        
        # Create a new mail item (0 = MailItem)
        mail = outlook.CreateItem(0)
        
        mail.To = to_address
        mail.Subject = subject
        mail.Body = body
        
        # Display the email on screen so you can review and click Send manually
        mail.Display()
        print("--> [Outlook] Draft created and displayed on screen.")
        return True
        
    except Exception as e:
        print(f"--> [Outlook] Failed to connect to Outlook: {e}")
        return False