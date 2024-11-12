from flask import Flask
import os
import subprocess
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the system username
    username = os.getlogin()
    
    # Get server time in IST
    ist = timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z%z")
    
    # Execute the top command and capture the output
    top_output = subprocess.getoutput("top -bn 1 | head -n 10")

  # Adjusted to show top 10 lines
    
    # Your name
    name = "Isha Rathore"
    
    # HTML content to display on the /htop endpoint
    html_content = f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><b>Name:</b> {name}</p>
            <p><b>Username:</b> {username}</p>
            <p><b>Server Time (IST):</b> {server_time}</p>
            <pre><b>Top Output:</b>\n{top_output}</pre>
        </body>
    </html>
    """
    
    return html_content

if __name__ == '__main__':
    # Run the app on the default port 5000, accessible publicly
    app.run(host="0.0.0.0", port=5000)
