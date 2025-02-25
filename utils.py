import json
import os
import esp32

def set_wifi_credentials(SSID,PASSWORD):
    try:
        ssid=SSID
        password=PASSWORD
        
        ssid_len=len(ssid)
        password_len=len(password)

        wifi = esp32.NVS('WIFI')
        
        wifi.set_blob('ssid', ssid)
        wifi.set_i32('ssid_len', ssid_len)
        
        wifi.set_blob('password', password)
        wifi.set_i32('password_len', password_len)
        wifi.commit()
        return True
    except Exception as e:
        print("Error: on set_wifi_credentials()", e)
        return False
        
# set_wifi_credentials("RoboNinjaz","Ariyilla")
def get_wifi_credentials():
    try:
        wifi = esp32.NVS('WIFI')
        
        ssid = bytearray(wifi.get_i32('ssid_len'))
        wifi.get_blob('ssid', ssid)
        
        password = bytearray(wifi.get_i32('password_len'))
        wifi.get_blob('password', password)
        print(f"{ssid.decode()}   {password.decode()}")
        return ssid.decode(),password.decode()
    except Exception as e:
        print("Error: on get_wifi_credentials()", e)
        return False
    

    
def file_exists(file_name):
    try:
        os.stat(file_name)
        return True  # File exists
    except OSError:
        return False  # File does not exist
def get_jsonvalue_from_file(file_path,key):
    try:
        if file_exists(file_path):
            with open(file_path, 'r') as f:
                    conf_data = json.load(f)
                    return conf_data[key]
        else:
            return "error"
    except Exception as e:
        return "error"
        print("Error on 'get_jsonvalue_from_file()':", e)
        
def put_jsonvalue_to_file(file_path,key,value):
    try:
        if file_exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
            data[key]=value
            with open(file_path, 'w') as f:
                    json.dump(data, f)
        else:
            return "error"
    except Exception as e:
        return "error"
        print("Error on 'put_jsonvalue_to_file()':", e)
def read_file(file_path):
    try:
        if file_exists(file_path):
            with open(file_path, 'r') as f:
                file_data = f.read()
            return file_data
    
    except Exception as e:
        print("Error on 'getData_from_file()':", e)
        return "error"
def write_file(file_path,data):
    try:
        with open(file_path, "w") as f:
            f.write(data)
        return True
    except Exception as e:
        print("Error on 'getData_from_file()':", e)
        return "error" 
    


def get_activity_params(activity):
    path=f"{activity}/config.txt"
    with open(path, 'r') as f:
         data = json.load(f)
    params=data['params']
    return (params)
    
def get_params(str_data):
    params={}
    try:
        query_string = str_data.split("GET /")[1].split(" HTTP")[0]
        if "?" in query_string:
            query_string = query_string.split("?")[1]
            pairs = query_string.split("&")
            for pair in pairs:
                key, value = pair.split("=")
                params[key] = value
            return params
    except Exception as e:
            print(f"An error occurred: {e}")
            return 0
def url_decode(encoded_str):

     # First, replace '+' with space to reverse URL encoding of spaces
    decoded_str = encoded_str.replace('+', ' ')  # Convert '+' to space
    # Simple replacement for common encoded characters
    decoded_str = decoded_str.replace('%20', ' ') \
                             .replace('%21', '!') \
                             .replace('%22', '"') \
                             .replace('%23', '#') \
                             .replace('%24', '$') \
                             .replace('%25', '%') \
                             .replace('%26', '&') \
                             .replace('%27', "'") \
                             .replace('%28', '(') \
                             .replace('%29', ')') \
                             .replace('%2A', '*') \
                             .replace('%2B', '+') \
                             .replace('%2C', ',') \
                             .replace('%2D', '-') \
                             .replace('%2E', '.') \
                             .replace('%2F', '/') \
                             .replace('%3A', ':') \
                             .replace('%3B', ';') \
                             .replace('%3C', '<') \
                             .replace('%3D', '=') \
                             .replace('%3E', '>') \
                             .replace('%3F', '?') \
                             .replace('%40', '@') \
                             .replace('%5B', '[') \
                             .replace('%5C', '\\') \
                             .replace('%5D', ']') \
                             .replace('%5E', '^') \
                             .replace('%5F', '_') \
                             .replace('%60', '`') \
                             .replace('%7B', '{') \
                             .replace('%7C', '|') \
                             .replace('%7D', '}') \
                             .replace('%7E', '~')

    return decoded_str