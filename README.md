---
title: 🛡️ Wi-Fi 6 AI Threat Detection Dashboard 🚀
description: Real-time AI-powered dashboard for monitoring Wi-Fi 6 traffic and detecting threats using GPU-accelerated AI.
---

# 🛡️ Wi-Fi 6 AI Threat Detection Dashboard 🚀

Real-time AI-powered dashboard that sniffs **Wi-Fi 6 packets**, detects threats using a **GPU-accelerated PyTorch model**, and displays results via a **live Flask web app**.

---

## 📁 Project Structure

wifi6_ai_dashboard/
├── app.py # Flask web server
├── model.py # GPU-based threat detection model
├── sniff.py # Wi-Fi 6 packet sniffer (monitor mode)
├── wifi6_packets.csv # Live-updating packet data
├── templates/
│ └── dashboard.html # HTML frontend dashboard

yaml
Copy
Edit

---

## 🧠 Features

- 📡 **Sniffs Wi-Fi 6 (802.11ax)** packets in monitor mode using Scapy.
- ⚙️ **Processes data in real time.**
- ⚡ **Detects threats** with a simulated PyTorch model using CUDA (GPU).
- 🌐 **Live web dashboard** (auto-refreshes every 5 seconds).
- 🎯 **Easily extendable** with more AI models or deep analytics.

---

## 🧰 Requirements

Install dependencies:

```bash
pip install flask scapy torch pandas scikit-learn
```
Ensure your Wi-Fi adapter supports monitor mode (e.g., Alfa AWUS036ACH).

Set it to monitor mode:

bash
Copy
Edit
sudo airmon-ng start wlan0
🚀 Run the Dashboard
bash
Copy
Edit
# Clone the repo
git clone https://github.com/yourname/wifi6_ai_dashboard.git
cd wifi6_ai_dashboard

# Run the Flask app
python3 app.py
Then open http://127.0.0.1:5000 in your browser.

📊 The dashboard auto-updates every 5 seconds.
