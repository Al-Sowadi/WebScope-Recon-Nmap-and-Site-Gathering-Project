# WebScope-Recon-Nmap-and-Site-Gathering-Project

# Web Reconnaissance Toolkit

The Web Reconnaissance Toolkit is a Python script that performs reconnaissance and gathers information about a target application and domain using various tools and techniques.

## Table of Contents

- [Dependencies](#dependencies)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Dependencies

Make sure you have the following dependencies installed before running the script:

- `requests`: For making HTTP requests
- `socket`: For working with sockets and getting host information
- `whois`: For retrieving WHOIS information about a domain
- `dns.resolver`: For DNS-related operations
- `bs4` (Beautiful Soup): For parsing HTML content
- `nmap`: For performing network scanning
- `cryptography`: For working with SSL certificates
- `geopy`: For performing GeoIP lookup
- `selenium`: For capturing screenshots (install ChromeDriver separately)

Install the dependencies using:

```bash
pip install -r requirements.txt

##Usage
Run the script by providing the target application URL and domain:

```bash
python script_name.py
