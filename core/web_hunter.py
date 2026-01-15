#!/usr/bin/env python3
"""
Web application analysis module
Probes web infrastructure for security vulnerabilities
"""

import subprocess
import requests
from urllib.parse import urlparse
from utils.colors import Colors

class WebHunter:
    def __init__(self, workspace, logger):
        self.workspace = workspace
        self.logger = logger

    def quick_check(self, url):
        """Rapid web application reconnaissance"""
        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}")
        print(f"{Colors.cyber_scan('WEB APPLICATION ANALYSIS PROTOCOL')}")
        print(f"{Colors.NEON_CYAN}[TARGET]{Colors.END} {Colors.NEON_GREEN}{url}{Colors.END}")
        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}\n")

        checks = {
            'robots.txt': f'{url}/robots.txt',
            'sitemap.xml': f'{url}/sitemap.xml',
            '.git/HEAD': f'{url}/.git/HEAD',
            '.env': f'{url}/.env',
            'backup.zip': f'{url}/backup.zip',
            'phpinfo.php': f'{url}/phpinfo.php',
            'config.php': f'{url}/config.php'
        }

        findings = []

        print(f"{Colors.NEON_CYAN}[PROBING]{Colors.END} Scanning web infrastructure...\n")

        for name, check_url in checks.items():
            try:
                response = requests.get(check_url, timeout=5, verify=False)
                if response.status_code == 200:
                    print(f"{Colors.cyber_success(f'Located: {name}')}")
                    findings.append(name)

                    # Save content
                    output_file = self.workspace.loot / f"{name.replace('/', '_')}.txt"
                    with open(output_file, 'w') as f:
                        f.write(response.text)

                    self.logger.log_finding("Exposed File", url, name)
                else:
                    print(f"{Colors.GRAY}[{response.status_code}] {name}{Colors.END}")
            except:
                print(f"{Colors.GRAY}[TIMEOUT] {name}{Colors.END}")

        print(f"\n{Colors.cyber_success('Web reconnaissance complete')}")
        print(f"{Colors.NEON_CYAN}[FINDINGS]{Colors.END} {Colors.NEON_GREEN}{len(findings)} vulnerable endpoints located{Colors.END}\n")

        return findings

    def directory_enum(self, url, wordlist='/usr/share/wordlists/dirb/common.txt'):
        """Directory structure enumeration"""
        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}")
        print(f"{Colors.cyber_scan('DIRECTORY ENUMERATION PROTOCOL')}")
        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}\n")

        parsed = urlparse(url)
        output_file = self.workspace.scans / f"gobuster_{parsed.netloc}.txt"

        cmd = f"gobuster dir -u {url} -w {wordlist} -x php,html,txt -o {output_file}"

        self.logger.log_command(cmd, url)

        print(f"{Colors.NEON_CYAN}[SCANNING]{Colors.END} Mapping directory structure...\n")

        try:
            subprocess.run(cmd, shell=True, timeout=300)
            print(f"\n{Colors.cyber_success('Directory mapping complete')}")
            print(f"{Colors.NEON_CYAN}[OUTPUT]{Colors.END} {Colors.NEON_GREEN}{output_file
