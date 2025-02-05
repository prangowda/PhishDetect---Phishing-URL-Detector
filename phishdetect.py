import re
import whois
import requests
from joblib import load

# Load pre-trained phishing detection model (Optional)
try:
    model = load("phishing_model.joblib")
    use_ml = True
except:
    use_ml = False

# Phishing detection patterns
SUSPICIOUS_KEYWORDS = ["verify", "banking", "secure", "login", "account", "update"]
IP_REGEX = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

def check_ssl(url):
    """Check if a URL has a valid SSL certificate"""
    try:
        response = requests.get(url, timeout=5)
        return response.url.startswith("https")
    except requests.exceptions.RequestException:
        return False

def get_domain_info(url):
    """Retrieve WHOIS data for domain age verification"""
    domain = re.sub(r"https?://", "", url).split("/")[0]
    try:
        w = whois.whois(domain)
        return w.creation_date
    except:
        return None

def is_phishing(url):
    """Analyze URL and return if it's suspicious"""
    if re.search(IP_REGEX, url):
        return True  # Suspicious: Uses IP instead of domain

    for word in SUSPICIOUS_KEYWORDS:
        if word in url.lower():
            return True  # Suspicious: Contains phishing keywords

    if not check_ssl(url):
        return True  # Suspicious: No SSL certificate

    if get_domain_info(url) is None:
        return True  # Suspicious: WHOIS lookup failed

    if use_ml:
        return model.predict([url])[0]  # Use ML model for final check

    return False  # Safe URL

# Example usage
if __name__ == "__main__":
    url = input("Enter URL to check: ")
    if is_phishing(url):
        print("🚨 WARNING: This URL may be a phishing site!")
    else:
        print("✅ Safe URL.")
