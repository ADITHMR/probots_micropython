import machine
from  projectList import  *




# Generate HTML for the dropdown
html_dropdown =  """<select id="mydropdown" name="selectedItem" class="form-select" required>"""
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
    <div class="form-container">
      <h2 class="mb-4">Probots</h2>
      <form method="POST">
        <div class="mb-3">
          <label for="exampleDropdown" class="form-label">Powered By : Prosol Technologies.</label>
                    {html_dropdown}
                  </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>

    <!-- Image container on the right -->
    <div class="image-container">
      <img id="image" src="https://raw.githubusercontent.com/ADITHMR/probot_Images/refs/heads/main/01FunwithLEDLights.jpeg" alt="Selected Image">
    </div>
  </div>

  <script>
    document.getElementById('mydropdown').addEventListener("change", function() {{
      var selectedValue = this.value;
      var image_name = selectedValue.replace(/\s+/g, '');  // Remove spaces from selected value
      var imgSrc = "https://raw.githubusercontent.com/ADITHMR/probot_Images/refs/heads/main/" + image_name + ".jpeg";
      document.getElementById('image').src = imgSrc;  // Update the image source
    }});
  </script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
    crossorigin="anonymous"></script>
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
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <meta name="description" content="Control your ESP32 using a web interface." />
  <title>ESP32 Web Server</title>
  <meta name="favicon" href="https://img.icons8.com/?size=80&id=dxoYK8bxqiJr&format=png" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" />
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
      min-height: 100vh;
    }}

    .container {{
      display: flex;
      justify-content: space-between; /* Align form and image side by side */
      background-color: #1e1e1e;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
      padding: 20px;
      width: 90%; /* Adjust the width of the container */
      flex-wrap: wrap; /* Allow wrapping on small screens */
    }}

    .form-container {{
      flex: 1; /* Allow the form to take up the remaining space */
      margin-right: 20px; /* Add space between the form and image */
    }}

    .form-container h2 {{
      color: #03a9f4;
    }}

    .form-container button {{
      font-size: 18px;
      padding: 12px 24px;
      margin: 5px;
    }}

    .form-container button.btn-success {{
      background-color: #4caf50;
    }}

    .form-container button.btn-danger {{
      background-color: #f44336;
    }}

    .form-container button.btn-warning {{
      background-color: #ff9800;
    }}

    .form-container p {{
      font-size: 20px;
      color: #ccc;
    }}

    /* Responsive image */
    #image {{
      max-width: 100%; /* Image width */
      max-height: 60vh; /* Make image responsive to the height of the viewport */
      height: auto;
      border-radius: 10px;
    }}

    /* Media query for mobile screens */
    @media (max-width: 768px) {{
      .container {{
        flex-direction: column; /* Stack form and image vertically on smaller screens */
        align-items: center;
      }}

      .form-container {{
        margin-right: 0; /* Remove space between form and image on small screens */
        margin-bottom: 20px; /* Add some space below the form */
      }}
    }}
  </style>
</head>
  """
