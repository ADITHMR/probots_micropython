from machine_id import get_serial_no

def web_page_AP():
    # Get the serial number
    serial_no = get_serial_no()
    
    # HTML page content with dynamic serial number insertion
    html_page = f"""
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SSID and Password Form</title>
  
  <style>
    body {{
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #f4f4f4;
    }}
    .form-container {{
      background-color: white;
      padding: 50px;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      width: 100%;
      max-width: 400px;
    }}
    h4 {{
      margin-bottom: 20px;
      text-align: center;
    }}
    .form-group {{
      margin-bottom: 15px;
    }}
    label {{
      font-size: 14px;
      font-weight: bold;
      display: block;
      margin-bottom: 5px;
    }}
    input {{
      width: 100%;
      padding: 10px;
      font-size: 14px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }}
    button {{
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
      transition: background-color 0.3s;
    }}
    button:hover {{
      background-color: #0056b3;
    }}
  </style>

  <script>
    // Function to replace spaces with %20 in form inputs
    function replaceSpaces(event) {{
      const form = event.target;
      const ssidField = form.querySelector('#ssid');
      const passwordField = form.querySelector('#password');
      
      // Replace spaces in SSID and Password fields with %20
      ssidField.value = ssidField.value.replace(/ /g, '@@!##');
      passwordField.value = passwordField.value.replace(/ /g, '@@!##');
    }}
  </script>
</head>
<body>

<div class="form-container">

  <h4>Submit SSID and Password</h4>
  <h1 class="page-heading">S/N: {serial_no}</h1>
  <!-- Form to collect SSID and password -->
  <form action="your-server-endpoint" method="POST" onsubmit="replaceSpaces(event)">
    <div class="form-group">
      <label for="ssid">SSID</label>
      <input type="text" id="ssid" name="ssid" placeholder="Enter SSID" required>
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" id="password" name="password" placeholder="Enter Password" required>
    </div>
    <button type="submit">Submit</button>
  </form>
</div>

</body>
</html>
"""
    return html_page
