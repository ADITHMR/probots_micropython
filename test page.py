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
    body {
      background-color: #070303;
      color: #ffffff;
      font-family: "Roboto", sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      height: 100vh;
    }

    /* Sidebar Style */
    .sidebar {
      width: 250px;
      background-color: #1e1e1e;
      padding: 20px;
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      box-shadow: 4px 0 6px rgba(0, 0, 0, 0.3);
    }

    .sidebar h2 {
      color: #03a9f4;
    }

    .form-group {
      margin-top: 20px;
      text-align: left;
    }

    .sidebar select,
    .sidebar button {
      width: 100%;
    }

    /* Main content (image) */
    .main-content {
      margin-left: 250px; /* Space for the sidebar */
      padding: 20px;
      flex: 1;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #070303;
    }

    img {
      max-width: 100%;
      height: auto;
    }

    button {
      font-size: 18px;
      padding: 12px 24px;
      margin: 5px;
    }

    button.btn-success {
      background-color: #4caf50;
    }

    button.btn-danger {
      background-color: #f44336;
    }

    button.btn-warning {
      background-color: #ff9800;
    }
  </style>
</head>

<body>
  <!-- Sidebar -->
  <div class="sidebar">
    <h2 class="mb-4">Probots</h2>
    <form method="POST">
      <div class="mb-3">
        <label for="exampleDropdown" class="form-label">Powered By: Prosol Technologies.</label>
        <select id="exampleDropdown" name="selectedItem" class="form-select" required>
          <option value="01 Fun with LED Lights">01 Fun with LED Lights</option>
          <option value="02 Sensor-controlled street light">02 Sensor-controlled street light</option>
          <option value="03 Self-opening gate">03 Self-opening gate</option>
          <option value="04 Student headcount Tracker">04 Student headcount Tracker</option>
          <option value="05 Automatic fire detection system">05 Automatic fire detection system</option>
          <option value="06 Temperature measurement device">06 Temperature measurement device</option>
          <option value="07 Digital distance measurement">07 Digital distance measurement</option>
          <option value="08 Touchless dustbin">08 Touchless dustbin</option>
          <option value="09 Touch operated fan">09 Touch operated fan</option>
          <option value="10 Smart fan">10 Smart fan</option>
          <option value="11 Automated Solar tracking system">11 Automated Solar tracking system</option>
          <option value="12 Line follower robot">12 Line follower robot</option>
        </select>
      </div>

      <!-- Placeholder for sub options (dynamic) -->
      <div id="subOptionsContainer"></div>

      <!-- Submit button (optional) -->
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>

  <!-- Main content (Image) -->
  <div class="main-content">
    <div class="image-container">
      <img id="image" src="https://raw.githubusercontent.com/ADITHMR/probot_Images/refs/heads/main/01FunwithLEDLights.jpeg" alt="Selected Image" width="400">
    </div>
  </div>

  <script>
    const subOptions = {
      "01 Fun with LED Lights": {
        "Sub Option 1": ["LED Color Patterns", "Brightness Control"],
        "Sub Option 2": ["LED Animation", "Random Lighting"]
      },
      "02 Sensor-controlled street light": {
        "Sub Option 1": ["Daylight Sensors", "Motion Sensors", "Auto ON/OFF Control"],
        "Sub Option 2": ["Dusk to Dawn", "Light Sensitivity Adjustment", "Manual Override"],
        "Sub Option 3": ["Solar Panel", "Battery Backup", "Smart Control"]
      },
      "03 Self-opening gate": {
        "Sub Option 1": ["Servo Motor Control", "RFID-based Access"],
        "Sub Option 2": ["Automated Timer Control", "Bluetooth Access"]
      },
      "04 Student headcount Tracker": {
        "Sub Option 1": ["Real-time Count", "Log Students", "Alert System"],
        "Sub Option 2": ["Automated Entry", "QR Code Scanning", "Facial Recognition"],
        "Sub Option 3": ["Attendance Report", "Mobile Notifications", "Web Dashboard"]
      },
      // Additional options can be added here
    };

    // Event listener to update image and form elements based on selected item
    document.getElementById('exampleDropdown').addEventListener("change", function () {
      var selectedValue = this.value;
      var image_name = selectedValue.replace(/\s+/g, '');
      var imgSrc = "https://raw.githubusercontent.com/ADITHMR/probot_Images/refs/heads/main/" + image_name + ".jpeg";
      document.getElementById('image').src = imgSrc;

      // Get the sub-options for the selected project
      const subOptionsContainer = document.getElementById('subOptionsContainer');
      subOptionsContainer.innerHTML = ''; // Clear previous sub options

      if (subOptions[selectedValue]) {
        let options = subOptions[selectedValue];

        // Create form elements for each Sub Option
        for (let subOption in options) {
          // Create a group for each sub-option (heading + options)
          const groupDiv = document.createElement('div');
          groupDiv.classList.add('form-group');
          
          const title = document.createElement('h5');
          title.innerText = subOption; // Sub Option heading
          groupDiv.appendChild(title);
          
          options[subOption].forEach((option, index) => {
            const label = document.createElement('label');
            label.classList.add('form-check-label');
            label.innerText = option;

            const input = document.createElement('input');
            input.type = 'radio'; // Use radio buttons for single selection
            input.name = subOption; // Group radio buttons by sub-option heading
            input.value = option;
            input.classList.add('form-check-input');

            // Set the first option in each sub-option group as the default selection
            if (index === 0) {
              input.checked = true; // First option is selected by default
            }

            const div = document.createElement('div');
            div.classList.add('form-check');
            div.appendChild(input);
            div.appendChild(label);
            groupDiv.appendChild(div);
          });

          subOptionsContainer.appendChild(groupDiv);
        }
      }
    });
  </script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
    crossorigin="anonymous"></script>
</body>

</html>
