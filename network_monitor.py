import scapy.all as scapy
import requests
import json
import os

# Configuration - Replace these with your actual values
SUBNET = "192.168.1.0/24"  # Example: 192.168.1.0/24
WEBHOOK_URL = "web_hook_url"  # Replace with your actual webhook URL
PREV_FILE = "previous_devices.json"

def scan_network(subnet):
    """Scan the network using ARP requests and return a list of devices (IP and MAC)."""
    try:
        ans, _ = scapy.arping(subnet, verbose=0)
        devices = []
        for sent, received in ans:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc.lower()})
        return devices
    except Exception as e:
        print(f"Error during network scan: {e}")
        return []

def check_new_devices(current_devices, previous_devices):
    """Check for devices that are new since the last scan."""
    previous_macs = {device['mac'] for device in previous_devices}
    new_devices = [device for device in current_devices if device['mac'] not in previous_macs]
    return new_devices

def check_arp_spoofing(devices):
    """Check for potential ARP spoofing by looking for MACs with multiple IPs."""
    mac_to_ips = {}
    for device in devices:
        mac = device['mac']
        ip = device['ip']
        if mac not in mac_to_ips:
            mac_to_ips[mac] = []
        mac_to_ips[mac].append(ip)

    suspicious = {mac: ips for mac, ips in mac_to_ips.items() if len(ips) > 1}
    return suspicious

def send_discord_notification(message):
    """Send a notification message to Discord via webhook."""
    payload = {'content': message}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code != 200 and response.status_code != 204:
            print(f"Failed to send notification: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending Discord notification: {e}")

def load_previous_devices():
    """Load previous devices from JSON file, handling empty or invalid files."""
    if os.path.exists(PREV_FILE):
        try:
            with open(PREV_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: {PREV_FILE} is corrupted. Starting fresh.")
            return []
    return []

def save_current_devices(devices):
    """Save current device list to JSON file."""
    with open(PREV_FILE, 'w') as f:
        json.dump(devices, f, indent=2)

def main():
    """Main function to run the network monitoring script."""
    previous_devices = load_previous_devices()

    # Scan the network
    current_devices = scan_network(SUBNET)

    # Check for new devices and send notifications
    new_devices = check_new_devices(current_devices, previous_devices)
    for device in new_devices:
        message = f"🔔 New Device Detected: IP `{device['ip']}`, MAC `{device['mac']}`"
        send_discord_notification(message)

    # Check for potential ARP spoofing and send notifications
    suspicious = check_arp_spoofing(current_devices)
    for mac, ips in suspicious.items():
        ips_str = ", ".join(ips)
        message = f"⚠️ Potential ARP Spoofing Detected! MAC `{mac}` is using IPs: {ips_str}"
        send_discord_notification(message)

    # Save current devices for next run
    save_current_devices(current_devices)

if __name__ == "__main__":
    main()
