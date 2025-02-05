# PhishDetect - Phishing URL Detector

## 🔍 Project Description
PhishDetect is a **Python-based cybersecurity tool** that helps detect phishing URLs by analyzing **domain characteristics, SSL certificates, and URL patterns**. It uses **machine learning models** and heuristic analysis to classify URLs as **safe or suspicious**, helping to prevent phishing attacks.

---

## 🛠 Features
✅ Detects **phishing URLs** using domain reputation and keyword analysis  
✅ Uses **ML models** to classify URLs (optional feature)  
✅ Checks **SSL certificate validity** for HTTPS-based domains  
✅ Verifies **domain age and WHOIS records**  
✅ Fast processing using **regex and online threat intelligence APIs**  

---

## 📜 Installation
Install the required dependencies using pip:
```sh
pip install requests whois scikit-learn joblib
```

---

## 📂 Usage
Run the tool and enter a URL:
```sh
python phishdetect.py
```
The script will analyze the URL and display whether it is **safe** or a **potential phishing site**.

---

## 📊 Example Input & Output

### 🔹 **User Input**
```
https://secure-banking-login.com
```

### 🔹 **Output**
```
🚨 WARNING: This URL may be a phishing site!
```

---

## 🚀 Future Enhancements
🔹 **Integrate Google Safe Browsing API for real-time threat detection**  
🔹 **Improve ML model accuracy with more training data**  
🔹 **Create a web-based or browser extension version**  


