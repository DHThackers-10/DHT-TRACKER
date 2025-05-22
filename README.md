# DHT-LOCATION

![DHT-TRACKER](https://img.shields.io/badge/DHT-HACKERS-red?style=for-the-badge)
The most powerful **location phishing** tool for **educational purposes only**.

---

# 🎯 DHT-Phisher – Track with Style!

Welcome to DHT-Phisher — a sleek and educational location phishing tool powered by Python, Flask, and Rich. Ideal for demonstrating how location capture works in a secure and ethical environment.

---

# ⚠️ Disclaimer

> This tool is made strictly for **educational** and **ethical hacking** purposes.  
> Do **not** use this tool for any unauthorized or malicious activity.  
> Use it only in environments where you have permission.

---

# 🚀 Installation Guide

Fire up your terminal and execute the following commands:

```bash
apt update && apt upgrade -y
pkg update && pkg upgrade -y
pkg install git python python3 wget cloudflared -y
pip install flask rich pyfiglet
git clone https://github.com/DHThackers-10/DHT-TRACKER.git
cd DHT-TRACKER
python3 DHT-TRACKER.py
```

# Screenshot 

![Screenshot_20250522-121939](https://github.com/user-attachments/assets/eb5febaf-b3fd-40b4-9dbf-8520f1b80b36)

# ⚙️ How It Works?

Runs a lightweight Flask server to host a fake location verification page

Uses JavaScript Geolocation API to capture:
• Latitude

• Longitude

• Accuracy

• Platform

• Language

• IP

• User Agent


Stores all captured data in a structured JSON file

Displays all data in a beautiful Rich table

Provides a Google Maps link based on the captured coordinates


# 🌐 Make It Public

To share your phishing page with the internet using Cloudflared, run:
```
cloudflared tunnel --url http://localhost:5000
```
You’ll get a public https:// link you can send to targets (for demo/educational use).


# ✅ Features

*Fast & Lightweight*

*Stylish Terminal Output (Rich)*

*Google Maps Integration*

*JSON Logging*

*One-Command Start*

*Beginner Friendly*

*Ethical by Design*


# 👨‍💻 Credits

Created by the DHT Hackers Team
**GitHub profile**:[GitHub](https://github.com/DHThackers-10)

**channel**:[YouTube](https://youtube.com/@dht-hackers_10)

**Group**:[WhatsApp Community](https://chat.whatsapp.com/G2hCkCzylra2OENEfhH8Os)
