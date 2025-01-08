import machine
from  projectList import  *




# Generate HTML for the dropdown
html_dropdown =  """<select id="exampleDropdown" name="selectedItem" class="form-select" required>"""
#         <option value="" disabled selected>Select the Project</option>"""

for proj in project_topic_list:
    html_dropdown += f"<option value=\"{proj}\">{proj}</option>\n"
#     <li><a class=\"dropdown-item\" onclick=\"changeButtonText('{proj}')\">{proj}</a></li>\n"
#     html_dropdown += f"<li><a class=\"dropdown-item\" href=\"\" onclick=\"changeButtonText('{proj}')\">{i} {proj}</a></li>\n"
    
#      <li><a class="dropdown-item" href="#" onclick="changeButtonText('Apple')">1 Apple</a></li>
   
html_dropdown+="</select>"    
            




# print(html_dropdown)
def web_page():
    

    html_page =website_style+ f"""

  <body>
    <div class="container">  
        <div class="container mt-5">
            <h2 class="mb-4">Probots</h2>
            <form  method="POST">
                <div class="mb-3">
                    <label for="exampleDropdown" class="form-label">Powered By : Prosol Technologies.</label>
                    {html_dropdown}
                  </div>
                </div>
                <!-- Submit button (optional) -->
                <button type="submit" class="btn btn-primary">Submit</button>
             
             </form>
        </div>
        

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
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
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
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
