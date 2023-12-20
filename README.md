# WebScope-Recon-Nmap-and-Site-Gathering-Project
## Overview
WebScope Recon is a comprehensive Python toolkit designed for web reconnaissance, network scanning, and site information gathering. This project brings together three essential components:

# 1-Multi-faceted Cyber Reconnaissance Tool

The Web Reconnaissance Toolkit is a Python script that performs reconnaissance and gathers information about a target application and domain using various tools and techniques.

## Table of Contents

- [Dependencies](#dependencies)
- [Usage](#usage)
- [Features](#features)


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
python webSiteInfo.py
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


# 2-Nmap Integration Script

This Python script integrates Nmap, a powerful network scanning tool, to perform scans on a target. It provides a clean and organized output, removing unwanted lines and sections for better readability.

## Table of Contents

- [Usage](#usage)
- [Features](#features)
- [Command-line Options](#command-line-options)

## Usage

1. Ensure you have Nmap installed on your system.
2. Run the script using the following command:

```bash
python NmapLike.py <target> [-o <output_file>]

```
Install the requirements using:

```bash
pip install -r requirements2.txt
```
## Features
- Integrates Nmap for network scanning.
- Provides a clean and organized output by removing unwanted lines and sections.
- Supports saving scan results to an output file.
  
### Command-line Options

<target>: Specify the target IP address or domain for the Nmap scan.
-o <output_file>: Specify an output file for saving the scan results.

# 3-Web Scraper for Email Addresses

This Python script is a simple web scraper that extracts email addresses from a given target URL by crawling through its pages.

## Features

- Crawls a specified target URL and extracts email addresses.
- Uses BeautifulSoup for HTML parsing and requests for making HTTP requests.
- Allows users to specify the maximum number of pages to crawl.

## Requirements

- Python 3.x
- BeautifulSoup 4
- requests

Install the required dependencies using:

```bash
pip install beautifulsoup4 requests

```
## Usage
- Run the script:
```bash
python crawl_and_extract_emails.py
```
- Enter the target URL and the maximum number of pages to crawl as prompted.
- The script will display the extracted email addresses.

## Disclaimer
Use this script responsibly and in compliance with the terms of service of the websites you are scraping.
Be aware that web scraping may be against the terms of service of some websites.
