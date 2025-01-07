import machine
from  projectList import  *




# Generate HTML for the dropdown
html_dropdown =  '<ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">'
i=1;
for proj in project_topic_list:
    html_dropdown += f"<li><a class=\"dropdown-item\" onclick=\"changeButtonText('{proj}')\">{i} {proj}</a></li>\n"
#     html_dropdown += f"<li><a class=\"dropdown-item\" href=\"\" onclick=\"changeButtonText('{proj}')\">{i} {proj}</a></li>\n"
    
#      <li><a class="dropdown-item" href="#" onclick="changeButtonText('Apple')">1 Apple</a></li>
    i+=1
    
            
html_dropdown += '</ul>'


def web_page():
    

    html_page =website_style+ f"""

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
        {html_dropdown}
        
       
      </div>
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
          //var dropdownMenu = new bootstrap.Dropdown(document.getElementById('dropdownMenuButton'));
          //dropdownMenu.hide();
        }}
      </script>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>    
</body>
</html>
"""
    return html_page
def successProjectPage(data):
    success_page=website_style+f"""
                          <body>
                            <div class="container"><h1>Project Selection Successful!</h1>
                            <p>You selected: {data}</p>
                            
                            <a href="/reset">Click here to restart the device.</a>
                        </div>
                          </body>
                        </html>
                       """
    return success_page
def errorPage():
    error_page=website_style+f"""
                          <body>
                            <div class="container"><h1>ERROR!</h1>
                
                            
                            <a href="/reset">Click here to restart the device.</a>
                        </div>
                          </body>
                        </html>
                       """
    return error_page
def restartSuccessPage():
    error_page=website_style+f"""
                          <body>
                            <div class="container"><h1>Restarted Successfully!</h1>
                        </div>
                          </body>
                        </html>
                       """
    return error_page
    
website_style=f"""

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
      href="https://img.icons8.com/?size=80&id=dxoYK8bxqiJr&format=png"
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
  """
