#!/usr/bin/env python
# Integrating nmap

import subprocess
import argparse
from colorama import Fore, Style

def run_nmap_scan(target, output_file=None):
    # Build the Nmap command
    nmap_command = f"nmap {target}"

    # Append the output file option to the Nmap command
    if output_file:
        nmap_command += f" -oN {output_file}"

    # Run the Nmap command and capture the complete output
    result = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)

    # Process the output to remove unwanted lines and sections
    cleaned_output = process_nmap_output(result.stdout)

    # Print the cleaned output with color
    print(f"{Fore.BLUE}Nmap Output:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{cleaned_output}{Style.RESET_ALL}")
    print(f"{Fore.RED}{result.stderr}{Style.RESET_ALL}")

    # Inform the user about the saved output file
    if output_file:
        print(f"{Fore.YELLOW}Scan results saved to: {output_file}{Style.RESET_ALL}")

def process_nmap_output(output):
    # Remove unwanted lines and sections from the Nmap output
    lines = output.split('\n')
    cleaned_lines = []

    skip_lines = False
    for line in lines:
        if 'Host script results:' in line:
            skip_lines = True
        elif 'Nmap done:' in line:
            skip_lines = False
            continue

        if not skip_lines:
            cleaned_lines.append(line)

    cleaned_output = '\n'.join(cleaned_lines)
    return cleaned_output

def main():
    # Using argparse for improved command-line interface
    parser = argparse.ArgumentParser(description='Integrating Nmap')
    parser.add_argument('target', type=str, help='specify the target for the Nmap scan')
    parser.add_argument('-o', dest='output_file', type=str, help='specify output file for scan results')

    args = parser.parse_args()
    run_nmap_scan(args.target, args.output_file)

if __name__ == '__main__':
    main()
