# Network Monitor & ARP Spoofing Detector

This project is a Python-based **network monitoring script** that scans your local network for connected devices and checks for potential **ARP spoofing attacks**. It sends notifications to a configured **Discord Webhook** if any suspicious activity is detected.

---

## 🚀 Features

✅ Scans your local network for devices (IP and MAC addresses) using `arp -a`  
✅ Filters results for a specified subnet (default: `192.168.1.x`)  
✅ Detects potential **ARP spoofing** by identifying when multiple IPs share the same MAC as the gateway (default: `192.168.1.1`)  
✅ Sends real-time **Discord notifications** for ARP table updates and spoofing alerts  
✅ Supports both Windows and Linux/macOS ARP output formats

![Screenshot 2025-03-08 021159](https://github.com/user-attachments/assets/4b555f88-8ef7-43d3-9c08-996333475ad9)

---

## 🛠️ Requirements

To run this script, you need:

- **Python 3.x**

- Required Python packages:
  - `requests`

You can install the required package using:

```bash
pip install requests
```

---

## ⚙️ Configuration

1. **Subnet Filtering**  
   Edit the `SUBNET_PREFIX` variable in the script to match your network. For example:

   ```python
   SUBNET_PREFIX = "192.168.1."
   ```

2. **Gateway IP**  
   Set the `GATEWAY_IP` variable to your network's gateway IP address for spoofing checks:

   ```python
   GATEWAY_IP = "192.168.1.1"
   ```

3. **Discord Webhook URL**  
   Replace the `WEBHOOK_URL` variable with your actual Discord Webhook URL:

   ```python
   WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_here"
   ```

4. **Scan Interval**  
   Modify the `SCAN_INTERVAL` variable to adjust how frequently the script scans the network (in seconds):

   ```python
   SCAN_INTERVAL = 60
   ```

---

## ▶️ Usage

Run the script directly from the command line:

```bash
python network_monitor.py
```

You can also set this up as a cron job (Linux) or Task Scheduler job (Windows) for continuous monitoring.

---

## 🔔 Example Notifications

**ARP Table Notification:**

```
📋 **ARP Table (192.168.1.0/24):**
Interface: 192.168.1.10 --- 0x13
192.168.1.1          58-11-22-e0-67-4f     dynamic
192.168.1.100        00-50-56-c0-00-08     dynamic
```

**ARP Spoofing Alert:**

```
🔔 ALERT: Possible ARP spoofing detected!
Another IP shares the same MAC as the gateway.
```

---

## ⚠️ Security Note

This is a basic detection script and may produce false positives in environments with:

- Load balancers  
- VPN gateways  
- Misconfigured DHCP servers  

Use this as an early warning tool — not a comprehensive security system.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

Created with 💻 by c!ph3r1337
