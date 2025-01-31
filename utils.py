import json



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