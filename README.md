# ARP Monitor and Spoofing Detector

This Python script periodically runs `arp -a` to collect ARP (Address Resolution Protocol) information on your local network. It then filters for devices within a specific subnet (by default `192.168.1.x`), checks for possible ARP spoofing by comparing each device’s MAC address to your gateway’s MAC address, and sends the results (plus any alerts) to a **Discord webhook**.

## Features

- **Automated ARP Collection:** Runs `arp -a` at a fixed interval to gather IP/MAC mappings.  
- **Subnet Filtering:** Only displays entries for the specified subnet (default `192.168.1.`).  
- **ARP Spoofing Detection:** Compares each IP’s MAC address to the gateway’s MAC. If another IP has the same MAC, an alert is triggered.  
- **Discord Notifications:** Posts the ARP table (and any alerts) to a configured Discord channel via a webhook.  

## How It Works

1. **Collect ARP Table:** The script executes `arp -a` using `subprocess.run`.  
2. **Parse Entries:** It parses both **Windows**-style (`192.168.1.10 00-50-56-c0-00-08 dynamic`) and **Linux/macOS**-style (`? (192.168.1.1) at 58:11:22:e0:67:4f [ether] on eth0`) ARP output using regular expressions.  
3. **Filter by Subnet:** Only keeps ARP entries whose IP starts with the configured `SUBNET_PREFIX` (e.g., `192.168.1.`).  
4. **Check for Spoofing:**  
   - Looks up the gateway’s IP (e.g., `192.168.1.1`) in the ARP table to find its MAC address.  
   - Compares all other IPs’ MAC addresses. If any match the gateway’s MAC, it flags a **possible ARP spoof**.  
5. **Send to Discord:** Formats the ARP entries and sends them to a Discord webhook as a code block. If spoofing is detected, an alert message is appended.  
6. **Repeat at Interval:** Waits `SCAN_INTERVAL` seconds (default 60) and repeats.

## Requirements

- **Python 3**  
- **Requests Library:** Install with `pip install requests`.  
- **Ability to Run `arp -a`:** Typically works out-of-the-box on Windows, Linux, and macOS.

## Configuration

Edit the following variables at the top of the script to suit your environment:

```python
WEBHOOK_URL = "https://discord.com/api/webhooks/REPLACE_ME"  # Replace with your actual webhook URL
SUBNET_PREFIX = "192.168.1."                                 # Subnet prefix to monitor
GATEWAY_IP = "192.168.1.1"                                   # Gateway IP to compare for spoofing checks
SCAN_INTERVAL = 60                                           # Seconds between scans
```

- **WEBHOOK_URL:** Your Discord channel’s webhook URL.  
- **SUBNET_PREFIX:** The subnet you want to monitor.  
- **GATEWAY_IP:** The default gateway (router) IP address on your LAN.  
- **SCAN_INTERVAL:** How often (in seconds) to run the ARP scan and post to Discord.

## Usage

1. **Clone or Download** this script to your local machine or server.  
2. **Install Dependencies:**  
   ```bash
   pip install requests
   ```
3. **Configure** the variables in the script (`WEBHOOK_URL`, `SUBNET_PREFIX`, etc.).  
4. **Run the Script:**  
   ```bash
   python arp_monitor.py
   ```
5. **Check Discord:** You should see messages containing the filtered ARP table and any spoofing alerts.

## Example Output

A typical Discord message might look like:

```
📋 **ARP Table (192.168.1.0/24):**
```
```
Interface: 192.168.1.10 --- 0x13
192.168.1.1          58-11-22-e0-67-4f     dynamic
192.168.1.100        00-50-56-c0-00-08     dynamic
```
```
**🔔ALERT: Possible ARP spoofing detected!** Another IP shares the same MAC as the gateway.
```

## Notes & Caveats

- **Local Network Only:** ARP scans only reveal devices on the same local subnet (broadcast domain).  
- **ARP Table Expiration:** If a device is not actively communicating, it may not appear in the ARP table.  
- **Permission:** Always ensure you have permission to monitor and scan the network.  
- **Platform Differences:** The script tries to parse both Windows and Linux/macOS formats, but if your system outputs ARP data in a different format, you may need to adjust the regular expressions.

## Contributing

Feel free to open issues or submit pull requests for improvements, such as:

- Additional spoofing checks or security features.  
- Enhanced platform compatibility.  
- Improved parsing for edge cases.

## License

This script is provided as-is, with no warranty. Use at your own risk. You are free to modify and distribute it as needed.
