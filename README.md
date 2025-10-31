# Simple Port Scanner

A lightweight Python project that demonstrates basic cybersecurity and networking concepts.  
It scans a target host for open ports and attempts simple banner grabbing on common services.

## Features
- Scans a range of ports on a given host (default: 20–101).
- Reports which ports are open.
- Performs basic banner grabbing on common ports (21, 22, 80, 443).
- Measures and displays total scan time.
- Command‑line or interactive input supported.

## Usage
Run the script with a host as an argument:

```bash
python simple_port_scanner.py 127.0.0.1
