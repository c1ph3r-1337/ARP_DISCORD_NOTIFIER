import scapy.all as scapy
import requests
import json
import os

# Configuration - Replace these with your values
SUBNET = "192.168.1.0/24"  # Your network subnet (e.g., 192.168.1.0/24)
WEBHOOK_URL = "my_weekhook_url" 
PREV_FILE = "previous_devices.json"

def scan_network(subnet):
    """Scan the network using ARP requests and return a list of devices (IP and MAC)."""
    ans, _ = scapy.arping(subnet, verbose=0)
    devices = [{'ip': received.psrc, 'mac': received.hwsrc} for sent, received in ans]
    return devices

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
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code != 204:
        print(f"Failed to send notification: {response.status_code}")

def main():
    """Main function to run the network monitoring script."""
    # Load previous devices from file if it exists
    if os.path.exists(PREV_FILE):
        with open(PREV_FILE, 'r') as f:
            previous_devices = json.load(f)
    else:
        previous_devices = []

    # Scan the network
    current_devices = scan_network(SUBNET)

    # Check for new devices and send notifications
    new_devices = check_new_devices(current_devices, previous_devices)
    for device in new_devices:
        message = f"Device connected: IP {device['ip']} MAC {device['mac']}"
        send_discord_notification(message)

    # Check for potential ARP spoofing and send notifications
    suspicious = check_arp_spoofing(current_devices)
    for mac, ips in suspicious.items():
        ips_str = ", ".join(ips)
        message = f"Potential ARP spoofing detected: MAC {mac} with IPs {ips_str}"
        send_discord_notification(message)

    # Save current devices to file for the next run
    with open(PREV_FILE, 'w') as f:
        json.dump(current_devices, f)

if __name__ == "__main__":
    main()
