import requests
import socket
import whois
import dns.resolver
from bs4 import BeautifulSoup
import nmap
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from geopy.geocoders import Nominatim

def fetch_website_content(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as req_exception:
        print(f"Request Exception: {req_exception}")
    except Exception as e:
        print(f"Error fetching website content: {e}")
    return None

def extract_technologies(html_content):
    if html_content:
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            technologies_used = [tech.text for tech in soup.find_all('technology-selector')]
            return technologies_used
        except Exception as e:
            print(f"Error extracting technologies: {e}")
    return None

def get_application_info(url):
    try:
        html_content = fetch_website_content(url)
        if html_content:
            technologies_used = extract_technologies(html_content)
            if technologies_used:
                print(f"Technologies Used: {technologies_used}")
            else:
                print("No technologies found.")
        else:
            print("Failed to fetch website content.")

    except Exception as e:
        print(f"Error: {e}")

def perform_reconnaissance(target_domain):
    try:
        ip_addresses = socket.gethostbyname_ex(target_domain)
        print(f"IP Addresses for {target_domain}: {ip_addresses}")

        domain_info = whois.whois(target_domain)
        print("Domain Registration Details:")
        print(domain_info)

        subdomains = perform_dns_enum(target_domain)
        print(f"Subdomains: {subdomains}")

        banner = perform_banner_grabbing(target_domain)
        print(f"Banner Grabbing: {banner}")

        additional_urls = perform_web_crawling(target_domain)
        print(f"Additional URLs: {additional_urls}")
        
        ssl_info = get_ssl_certificate_info(target_domain)
        print(f"SSL Certificate Information: {ssl_info}")

        # Additional functionalities
        perform_traceroute(target_domain)
        perform_geoip_lookup(target_domain)
        perform_whois_for_ips(ip_addresses[2])
        check_security_headers(target_domain)
        # perform_vulnerability_scanning(target_domain)
        analyze_robots_txt(target_domain)
        capture_screenshots(target_domain)

    except Exception as e:
        print(f"Error: {e}")

def perform_dns_enum(target_domain):
    subdomains = []
    try:
        answers = dns.resolver.resolve(target_domain, 'A')
        subdomains = [answer.address for answer in answers]
    except dns.exception.DNSException as e:
        print(f"DNS Enumeration Error: {e}")
    return subdomains

def perform_banner_grabbing(target_domain):
    try:
        response = requests.get(f"http://{target_domain}")
        return response.headers.get('server')
    except requests.RequestException as e:
        print(f"Banner Grabbing Error: {e}")
        return None

def perform_web_crawling(target_domain):
    try:
        response = requests.get(f"http://{target_domain}")
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except requests.RequestException as e:
        print(f"Web Crawling Error: {e}")
        return []

def get_ssl_certificate_info(target_domain):
    try:
        import ssl
        cert = ssl.get_server_certificate((target_domain, 443))

        # Assuming cert_data contains the binary certificate data
        cert_data = ssl.PEM_cert_to_DER_cert(cert)

        # Load the DER-encoded certificate using cryptography
        certificate = x509.load_der_x509_certificate(cert_data, default_backend())

        # Extract subject and issuer
        subject = certificate.subject
        issuer = certificate.issuer

        print(f"SSL Certificate Subject: {subject}")
        print(f"SSL Certificate Issuer: {issuer}")

        # Return the DER-encoded certificate if needed
        return cert_data

    except Exception as e:
        print(f"SSL Certificate Information Error: {e}")
        return None
        
def get_certificate(target_domain):
    try:
        import ssl
        cert = ssl.get_server_certificate((target_domain, 443))
        return ssl.PEM_cert_to_DER_cert(cert)
    except Exception as e:
        print(f"SSL Certificate Retrieval Error: {e}")
        return None


def perform_traceroute(target_domain):
    try:
        import subprocess
        result = subprocess.run(['traceroute', target_domain], stdout=subprocess.PIPE)
        print(f"Traceroute:\n{result.stdout.decode('utf-8')}")

    except Exception as e:
        print(f"Traceroute Error: {e}")

def perform_geoip_lookup(target_domain):
    try:
        # Use Nominatim geocoder for GeoIP lookup
        geolocator = Nominatim(user_agent="geoip_lookup_script")
        location = geolocator.geocode(target_domain, timeout=10)

        if location:
            print(f"GeoIP Information for {target_domain}:")
            print(f"Country: {location.address}")
            print(f"Latitude: {location.latitude}")
            print(f"Longitude: {location.longitude}")
        else:
            print(f"No GeoIP information found for {target_domain}")

    except Exception as e:
        print(f"GeoIP Lookup Error: {e}")

def perform_whois_for_ips(ip_addresses):
    try:
        for ip in ip_addresses:
            ip_info = whois.whois(ip)
            print(f"WHOIS Information for IP {ip}:")
            print(ip_info)

    except Exception as e:
        print(f"WHOIS Lookup Error: {e}")

def check_security_headers(target_domain):
    try:
        response = requests.get(f"http://{target_domain}")
        security_headers = response.headers.get('Strict-Transport-Security'), response.headers.get('Content-Security-Policy')
        print(f"Security Headers:\nStrict-Transport-Security: {security_headers[0]}\nContent-Security-Policy: {security_headers[1]}")

    except requests.RequestException as e:
        print(f"Security Headers Check Error: {e}")



def analyze_robots_txt(target_domain):
    try:
        response = requests.get(f"http://{target_domain}/robots.txt")
        print(f"Robots.txt Content:\n{response.text}")

    except requests.RequestException as e:
        print(f"Robots.txt Analysis Error: {e}")

def capture_screenshots(target_domain):
    try:
        # Set up a headless Chrome browser
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        # Navigate to the target domain
        driver.get(f'http://{target_domain}')

        # Capture a screenshot and save it to a file
        screenshot_filename = f"screenshot_{target_domain}.png"
        driver.save_screenshot(screenshot_filename)
        print(f"Screenshot captured for {target_domain}. Saved as {screenshot_filename}")

        # Close the browser
        driver.quit()

    except Exception as e:
        print(f"Screenshots Capture Error: {e}")


if __name__ == "__main__":
    # User input for target URL and domain
    target_url = input("Enter the target application URL (e.g., http://example.com): ")
    target_domain = input("Enter the target domain (e.g., example.com): ")

    # Perform reconnaissance
    get_application_info(target_url)
    perform_reconnaissance(target_domain)
