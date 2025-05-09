from flask import Flask, render_template
from sniff import start_sniff
from model import detect_threat
import threading, time

app = Flask(__name__)

def continuous_sniff_and_detect():
    while True:
        start_sniff()
        detect_threat()
        time.sleep(5)

@app.route("/")
def dashboard():
    df = detect_threat()
    threats = df[df['threat'] == 1]
    return render_template("dashboard.html", threats=threats.to_dict(orient='records'))

if __name__ == "__main__":
    t = threading.Thread(target=continuous_sniff_and_detect)
    t.daemon = True
    t.start()
    app.run(debug=True)