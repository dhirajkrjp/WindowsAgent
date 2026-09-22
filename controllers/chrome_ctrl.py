import webbrowser
import urllib.parse

def search_google(query):
    """Opens your default existing browser and searches Google."""
    print(f"--> [Chrome] Searching Google for: '{query}'")
    
    # URL encode the query (e.g., "best laptops" -> "best+laptops")
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    
    # This automatically opens a new tab in your EXISTING Chrome window
    webbrowser.open(url)
    return True

def open_url(url):
    """Opens a specific URL in your existing browser."""
    print(f"--> [Chrome] Opening URL: {url}")
    webbrowser.open(url)
    return True