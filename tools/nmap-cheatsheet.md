# Nmap Cheatsheet — 2025-09-24
# Educational / Lab Only

## Basic Scans
- `nmap <IP>` → simple scan
- `nmap -sV <IP>` → detect service version
- `nmap -p 22,80,443 <IP>` → scan specific ports
- `nmap -A <IP>` → aggressive scan (OS + services + scripts)

## Tips
- Use `-oN <file>` to save output: `nmap -sV <IP> -oN result.txt`
- Combine with Wireshark to analyze traffic
- Always scan your own lab or authorized targets only
