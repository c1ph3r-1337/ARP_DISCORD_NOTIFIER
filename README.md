
```markdown
# Network Monitor & ARP Spoofing Detector

This project is a Python-based **network monitoring script** that scans your local network for connected devices, detects new devices, and checks for potential **ARP spoofing attacks**. It also sends notifications to a configured **Discord Webhook** if any new devices are detected or suspicious activity is found.

---

## 🚀 Features

✅ Scans your local network for devices (IP and MAC addresses)  
✅ Detects **new devices** that appear on the network since the last scan  
✅ Detects potential **ARP Spoofing** by identifying MAC addresses using **multiple IPs**  
✅ Sends real-time **Discord notifications** for new devices and suspicious activity  
✅ Saves a list of detected devices to `previous_devices.json` for comparison in future scans  

---

## 🛠️ Requirements

To run this script, you need:

- Python 3.x
- Required Python packages:
    - `scapy`
    - `requests`

You can install them using:

```bash
pip install scapy requests
```

---

## ⚙️ Configuration

### 1. Subnet
Edit the `SUBNET` variable in the script to match your network, e.g.:
```python
SUBNET = "192.168.1.0/24"
```

### 2. Discord Webhook URL
Replace `WEBHOOK_URL` with your actual Discord Webhook URL:
```python
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_here"
```

### 3. Previous Devices File
By default, the script uses:
```python
PREV_FILE = "previous_devices.json"
```
This file is automatically created and updated each time the script runs.

---

## ▶️ Usage

Run the script directly:

```bash
python network_monitor.py
```

You can also set this up as a **cron job** (Linux) or **Task Scheduler job** (Windows) for continuous monitoring.

---

## 🔔 Example Notifications

### New Device Detected
```
🔔 New Device Detected: IP 192.168.1.50, MAC aa:bb:cc:dd:ee:ff
```

### ARP Spoofing Detected
```
⚠️ Potential ARP Spoofing Detected! MAC aa:bb:cc:dd:ee:ff is using IPs: 192.168.1.50, 192.168.1.51
```

---

## ⚠️ Security Note

This is a **basic detection script** and may produce **false positives** in some environments, such as networks with:

- Load balancers
- VPN gateways
- Misconfigured DHCP servers

Treat this as an **early warning tool** — not a comprehensive security system.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

Created with 💻 by **c!ph3r1337**

---
