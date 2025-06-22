import re

def extract_emails(text):
    """Extract all email addresses from a text."""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    """
    Extract phone numbers with these assumptions:
    - Start with optional + and country code (1-3 digits)
    - Followed by 7-15 digits, possibly separated by spaces, dots, or hyphens
    """
    pattern = r'\+\d{1,3}(?:[-.\s]?\d{2,4}){2,4}(?!\.\d)'  
    return [num.strip('.- ') for num in re.findall(pattern, text)]  

def extract_urls(text):
    """Extract URLs from text."""
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

def extract_dates(text):
    """Extract dates in formats like YYYY-MM-DD, DD/MM/YYYY, MM-DD-YYYY."""
    pattern = r'\b(\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})\b'
    return re.findall(pattern, text)

def clean_price(price_str):
    """Extract numeric price value from a string, handling European decimal comma."""
    price_str = price_str.replace('.', '').replace(',', '.')
    cleaned = re.sub(r'[^\d.]', '', price_str)
    try:
        return float(cleaned)
    except ValueError:
        return None

def validate_ipv4(ip):
    """Validate IPv4 address format."""
    pattern = r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.|$)){4}$'
    return bool(re.match(pattern, ip))


text = """
Contact us at support@example.com or sales@example.co.uk.
Call +1 234-567-8900 or +44 20 7946 0958.
Visit https://www.example.com or http://example.org/page.
Important dates: 2023-06-22, 22/06/2023, 06-22-2023.
The price is $1,299.99 or €1.234,56.
Server IPs: 192.168.1.1, 256.100.50.25, 10.0.0.5
"""

print("Emails:", extract_emails(text))
print("Phone numbers:", extract_phone_numbers(text))
print("URLs:", extract_urls(text))
print("Dates:", extract_dates(text))
print("Cleaned prices:")
print(clean_price("$1,299.99"))
print(clean_price("€1.234,56"))
print("Validate IPs:")
print(validate_ipv4("192.168.1.1"))
print(validate_ipv4("256.100.50.25"))
print(validate_ipv4("10.0.0.5"))