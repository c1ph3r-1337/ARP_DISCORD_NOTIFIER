# Network Monitor & ARP Spoofing Detector

This project is a Python-based **network monitoring script** that scans your local network for connected devices, detects new devices, and checks for potential **ARP spoofing attacks**. It also sends notifications to a configured **Discord Webhook** if any new devices are detected or suspicious activity is found.

---

## Features

✅ Scans your local network for devices (IP and MAC addresses)  
✅ Detects new devices that were not present in the previous scan  
✅ Detects potential **ARP Spoofing** by checking if a single MAC address has multiple IP addresses  
✅ Sends **Discord notifications** via a webhook for new devices and suspicious activity  
✅ Saves the list of devices to a JSON file (`previous_devices.json`) for persistence between runs  

---

## Requirements

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

## Configuration

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
This file is automatically created and updated. You can change the name if needed.

---

## Usage

Run the script directly:

```bash
python network_monitor.py
```

You can also set this up as a cron job or scheduled task for continuous monitoring.

---

## Notifications

### Example New Device Notification
```
Device connected: IP 192.168.1.50 MAC aa:bb:cc:dd:ee:ff
```

### Example ARP Spoofing Notification
```
Potential ARP spoofing detected: MAC aa:bb:cc:dd:ee:ff with IPs 192.168.1.50, 192.168.1.51
```

---

## Security Note

This is a **basic detection script** and may produce **false positives** in some networks, such as networks with load balancers, VPNs, or DHCP issues. It’s recommended to use this as an **early warning system** rather than a definitive security tool.

---

## License

This project is licensed under the MIT License.

---

## Author

👤 Created by c!ph3r1337 
