import requests  # Library used to send HTTP requests to the API

def sherlock_scan(mac_address):
    print("\n[🔎] Sherlock is scanning the network database...")
    
    # API URL targeting the user's input MAC address
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        # Sending the GET request to the MacVendors API
        response = requests.get(url)

        # HTTP Status 200 means success (OUI found)
        if response.status_code == 200:
            print("[+] TARGET IDENTIFIED!")
            print(f"Device Vendor: {response.text}")
            
        # HTTP Status 404 means the MAC prefix wasn't found
        elif response.status_code == 404:
            print("[-] Vendor not found.")
            print("Note: This device might be using a randomized/spoofed MAC address!")
            
    except requests.ConnectionError:
        # Error handling if there is no internet connection
        print("\n[!] Error: Connection failed. Please check your internet connection.")

# --- MAIN PROGRAM INTERFACE ---
print("=" * 35)
print("       MAC_SHERLOCK v1.0       ")
print("  Investigating Device Vendors  ")
print("=" * 35)

# Getting the MAC address input from the user
user_input = input("Enter the MAC address to investigate (e.g., 00:1A:2B:3C:4D:5E): ")

# Running the function with the provided MAC address
sherlock_scan(user_input)
print("\n[🔍] Scan complete. Stay safe and keep investigating!")
