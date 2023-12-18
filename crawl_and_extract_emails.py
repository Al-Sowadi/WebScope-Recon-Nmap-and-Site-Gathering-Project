from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

def crawl_and_extract_emails(target_url, max_pages):
    urls = deque([target_url])
    scraped_urls = set()
    emails = set()
    count = 0

    try:
        while len(urls):
            count += 1
            if count == max_pages:
                break
            url = urls.popleft()
            scraped_urls.add(url)

            parts = urllib.parse.urlsplit(url)
            base_url = '{0.scheme}://{0.netloc}'.format(parts)
            path = url[:url.rfind('/') + 1] if '/' in parts.path else url

            print('[%d] Processing %s' % (count, url))
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                continue

            new_emails = set(re.findall(r"[a-z0-9\.\-+]+@[a-z0-9\.\-+]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, features="lxml")

            for anchor in soup.find_all("a"):
                link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                if link not in urls and link not in scraped_urls:
                    urls.append(link)
    except KeyboardInterrupt:
        print('[-] Closing!')

    return emails

if __name__ == "__main__":
    user_url = str(input('[+] Enter Target URL To Scan (e.g., https://www.example.com): '))
    max_pages = int(input('[+] Enter the maximum number of pages to crawl: '))

    extracted_emails = crawl_and_extract_emails(user_url, max_pages)

    print("\nExtracted Emails:")
    for mail in extracted_emails:
        print(mail)
