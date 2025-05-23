pip install flask pytz
from flask import Flask
import getpass
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Full name
    full_name = "Praveen"  # Replace with your actual full name

    # Username
    username = getpass.getuser()

    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    # Top output (first 20 lines for readability)
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
        top_output = '\n'.join(top_output.split('\n')[:20])
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    html_output = f"""
    <pre>
    Name: {full_name}
    User: {username}
    Server Time (IST): {server_time}
    Top Output:
    {top_output}
    </pre>
    """
    return html_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

