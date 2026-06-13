🕵️‍♂️ mac_sherlock
mac_sherlock is a lightweight, efficient OSINT and network analysis tool designed to identify hardware vendors (e.g., Apple, Samsung, Intel, Espressif) using Wi-Fi or Bluetooth MAC addresses.

Developed by a 12-year-old aspiring developer(Made By ahmetchimp) during my Python learning journey to better understand network protocols, API integration, and HTTP request handling.

🚀 Features
Validates user-inputted MAC addresses.

Fetches real-time vendor data using the macvendors.com API.

Gracefully handles invalid, unrecognized, or spoofed MAC addresses.

Clean, minimal, and scannable terminal interface.

🛠️ Installation & Usage
Clone or download this repository to your local machine:
git clone https://github.com/ahmetchimp/mac_sherlock.git
cd mac_sherlock

Install the required dependency:
pip install -r requirements.txt

Run the investigator:
python mac_sherlock.py

⚖️ Legal Disclaimer
This tool is strictly developed for educational purposes, network administration, and cybersecurity awareness.

mac_sherlock only analyzes MAC addresses that are publicly broadcasted by devices in unencrypted wireless frames.

It does not perform any network intrusion, exploit vulnerabilities, or intercept private data traffic.

The developer assumes no liability and is not responsible for any misuse or damage caused by this program. Users are entirely responsible for complying with local laws and regulations.