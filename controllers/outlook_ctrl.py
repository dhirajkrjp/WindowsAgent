import webbrowser
import urllib.parse

def draft_email(to_address, subject, body):
    """Fallback method using system default email client (mailto)."""
    print(f"--> [Email] Requesting system to draft email to {to_address}")
    
    # URL encode the subject and body to handle spaces and newlines
    subject_enc = urllib.parse.quote(subject)
    body_enc = urllib.parse.quote(body)
    
    # Create the mailto string
    mailto_url = f"mailto:{to_address}?subject={subject_enc}&body={body_enc}"
    
    try:
        webbrowser.open(mailto_url)
        print("--> [Email] Draft opened via default system client.")
        return True
    except Exception as e:
        print(f"--> [Email] Failed to open email client: {e}")
        return False