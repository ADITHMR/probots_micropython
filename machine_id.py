
import network
import json

def get_serial_no():
    try:
        # Create a station interface (STA_IF) to get the MAC address of the ESP32
        sta_if = network.WLAN(network.STA_IF)
        # Get the MAC address
        mac_address = sta_if.config('mac')
        # Extract the last 24 bits (last 3 bytes)
        last_24bits = mac_address[3:]  # The last 3 bytes of the MAC address
        # Convert to a readable format (hex) without colons
        last_24bits_str = ''.join('%02x' % b for b in last_24bits) 
        with open('schema.dat', 'r') as f:
            data = json.load(f)
            
        serial_number=f"{data['serial_prefix']}{last_24bits_str}{data['serial_suffix']}"
        return (serial_number)
    except Exception as e:
        print("Error: on get_serial_no()", e)
        return("Serial Number ERROR")
       

def get_version():
    with open('version.dat', 'r') as f:
        data = json.load(f)
            
        version=f"{data['version']}"
        return (version)

def get_update_flag():
    try:
        with open('schema.dat', 'r') as f:
            data = json.load(f)
        if data["update_flag"]=="enabled":
            return True
        elif data["update_flag"]=="disabled":
            return False
        else:
            return "Error"
    except Exception as e:
        print("Error: on get_serial_no()", e)
        return("ERROR")
        
  