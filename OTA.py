import network
import time
import urequests
import machine

# WiFi credentials
SSID = 'Ponnus'
PASSWORD = 'Ariyilla'

# List of files on GitHub (raw URLs)
FILES = [
    "https://raw.githubusercontent.com/ADITHMR/probots_micropython/main/main.py",
    
]

# Connect to WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
        print("WiFi connected!")
    else:
        print("Already connected to WiFi.")
    return wlan

# Download files from GitHub and overwrite existing ones
def download_files(files):
    for url in files:
        filename = url.split('/')[-1]
        print(f"Downloading {filename}...")
        
        # Download file
        response = urequests.get(url)
        
        if response.status_code == 200:
            # Write content to file
            with open(filename, 'w') as f:
                f.write(response.text)
            print(f"{filename} updated successfully!")
        else:
            print(f"Failed to download {filename}.")
        response.close()

# Reboot ESP32
def reboot_esp32():
    print("Rebooting ESP32...")
    machine.reset()

# Main function
def main():
    connect_wifi()         # Connect to WiFi
    download_files(FILES)  # Download and update files from GitHub
    reboot_esp32()         # Reboot the ESP32 to apply the changes

# Run the OTA update
main()