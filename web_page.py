import machine

led = machine.Pin(2, machine.Pin.OUT)
isLedBlinking = False
def get_led_state():
    if isLedBlinking:
        return 'Blinking'
    elif led.value() == 1:
        return 'ON'
    elif led.value() == 0:
        return 'OFF'

def web_page():
    led_state = get_led_state()

    html_page = f"""
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <meta
      name="description"
      content="Control your ESP32 using a web interface."
    />
    <title>ESP32 Web Server</title>
    <meta
      name="favicon"
      href="https://omshingare.me/assets/logo-12777f7b.svg"
    />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">

    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css"
    />
    <style>
      body {{
        background-color: #070303;
        color: #ffffff;
        font-family: "Roboto", sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
      }}

      .container {{
        background-color: #1e1e1e;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        padding: 20px;
        text-align: center;
      }}

      h2 {{
        color: #03a9f4;
      }}

      button {{
        font-size: 18px;
        padding: 12px 24px;
        margin: 5px;
      }}

      button.btn-success {{
        background-color: #4caf50;
      }}

      button.btn-danger {{
        background-color: #f44336;
      }}

      button.btn-warning {{
        background-color: #ff9800;
      }}

      p {{
        font-size: 20px;
        color: #ccc;
      }}
    </style>
  </head>
  <body>
    
    <div class="container">
      <h2 class="mt-4">Probots</h2>
      <p>Powered By : Prosol Technologies.</p>
      <!-- <form id="dropdownForm" action="/submit" method="POST"> -->
        <form class="mt-4" >
      <div class="dropdown">
        <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
            Select The Project         
         </button>

         <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('01 Fun with LED Lights')">01 Fun with LED Lights</a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('02 Sensor-controlled street light')">02 Sensor-controlled street light</a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('03 Self-opening gate')">03 Self-opening gate</a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('04 Student headcount Tracker')">04 Student headcount Tracker</a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('05 Automatic fire detection system')">05 Automatic fire detection system</a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('06 Temperature measurement device')">06 Temperature measurement device</a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('07 Digital distance measurement')">07 Digital distance measurement</a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('08 Touchless dustbin')">08 Touchless dustbin</a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('09 Touch operated fan')">09 Touch operated fan </a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('10 Smart fan ')">10 Smart fan </a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('11 Automated Solar tracking system')">11 Automated Solar tracking system </a></li>
            <li><a class="dropdown-item" href="#" onclick="changeButtonText('12 Line follower robot')">12 Line follower robot </a></li>
          </ul>
       
      </div>
      <img src="data:image/jpeg;base64,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" class="img-fluid" alt="Responsive image">
      <!-- Hidden input to store the selected value -->
      <input type="hidden" name="selectedItem" id="selectedItem">
      
      <!-- Submit button (optional) -->
      <button type="submit" class="btn btn-success mt-3">Submit</button>
    </form>
      <script>
        function changeButtonText(text) {{
          // Change the button text
          document.getElementById('dropdownMenuButton').innerText = text;
           // Set the hidden input value to the selected option
          document.getElementById('selectedItem').value = text;
          document.getElementById('selectedItem').innerText = text;
         
    
          // Close the dropdown menu by removing the expanded class
          var dropdownMenu = new bootstrap.Dropdown(document.getElementById('dropdownMenuButton'));
          dropdownMenu.hide();
        }}
      </script>
<!-- 
      <form class="mt-4">
        <label for="cars">Select Project:</label>
        <select name="cars" id="cars">
          <option value="volvo">Volvo</option>
          <option value="saab">Saab</option>
          <option value="opel">Opel</option>
          <option value="audi">Audi</option>
        </select>
        <br><br>
        <input type="submit" value="Submit">
      </form>
      </div>


      <form class="mt-4">
        <div class="row"></div>
        <button class="btn btn-success" name="LED" type="submit" value="1">
          LED ON
        </button>
        <button class="btn btn-danger" name="LED" type="submit" value="0">
          LED OFF
        </button>
        <button class="btn btn-warning" name="LED" type="submit" value="2">
          LED BLINK
        </button>
      </form>
      <p class="mt-4">LED is currently <strong>{led_state}</strong>.</p> -->
    <!-- </div> -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>    
</body>
</html>
"""

    return html_page
