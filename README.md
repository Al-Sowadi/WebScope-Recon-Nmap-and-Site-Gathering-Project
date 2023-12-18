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
pip install -r requirements1.txt
```
## Usage
Run the script by providing the target application URL and domain:

```bash
python script_name.py
```

## Features
Certainly! Here's the Features section
### Fetch Website Content:

Uses `requests` to make HTTP requests and retrieve the content of the target website.

### Extract Technologies:

Parses HTML content with `Beautiful Soup` to extract technologies used on the website.

### Perform Reconnaissance on a Target Domain:

#### Get IP Addresses:

Uses `socket` to get IP addresses associated with the target domain.

#### Retrieve Domain Registration Details:

Uses `whois` to obtain WHOIS information about the domain.

#### Enumerate Subdomains:

Uses `dns.resolver` to perform DNS enumeration and find subdomains.

#### Banner Grabbing and Web Crawling:

Utilizes `requests` and `BeautifulSoup` to perform banner grabbing and web crawling.

#### Obtain SSL Certificate Information:

Uses `cryptography` to retrieve and parse SSL certificate information.

#### Conduct Traceroute:

Uses `subprocess` to perform traceroute on the target domain.

#### Perform GeoIP Lookup:

Utilizes `geopy` to perform GeoIP lookup for the target domain.

#### Retrieve WHOIS Information for IP Addresses:

Uses `whois` to obtain WHOIS information for the obtained IP addresses.

#### Check Security Headers:

Retrieves and displays security headers of the target domain.

#### Analyze `robots.txt`:

Retrieves and displays the content of the `robots.txt` file for the target domain.

#### Capture Screenshots:

Uses `selenium` to capture screenshots of the target domain.

