#!/usr/bin/env python3
"""
Network reconnaissance module
Scans target infrastructure using advanced protocols
"""

import subprocess
from pathlib import Path
from utils.colors import Colors

class Scanner:
    def __init__(self, workspace, logger):
        self.workspace = workspace
        self.logger = logger

    def quick_scan(self, target):
        """Rapid reconnaissance protocol"""
        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}")
        print(f"{Colors.cyber_scan('RAPID RECON PROTOCOL INITIATED')}")
        print(f"{Colors.NEON_CYAN}[TARGET]{Colors.END} {Colors.NEON_GREEN}{target}{Colors.END}")
        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}\n")

        output_file = self.workspace.get_scan_file(target, "quick")
        cmd = f"nmap -T4 -F --min-rate=1000 -oN {output_file} {target}"

        self.logger.log_command(cmd, target)

        print(f"{Colors.NEON_CYAN}[SCANNING]{Colors.END} Probing network infrastructure...")
        result = self._run_nmap(cmd)

        print(f"\n{Colors.cyber_success('Scan matrix compiled')}")
        print(f"{Colors.NEON_CYAN}[OUTPUT]{Colors.END} {Colors.NEON_GREEN}{output_file}{Colors.END}\n")

        return result

    def full_scan(self, target):
        """Comprehensive reconnaissance matrix"""
        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}")
        print(f"{Colors.cyber_scan('DEEP SCAN PROTOCOL ENGAGED')}")
        print(f"{Colors.NEON_CYAN}[TARGET]{Colors.END} {Colors.NEON_GREEN}{target}{Colors.END}")
        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}\n")

        output_file = self.workspace.get_scan_file(target, "full")
        cmd = f"nmap -sC -sV -p- --min-rate=1000 -oN {output_file} {target}"

        self.logger.log_command(cmd, target)

        print(f"{Colors.NEON_CYAN}[SCANNING]{Colors.END} Deploying comprehensive analysis protocols...")
        print(f"{Colors.NEON_CYAN}[STATUS]{Colors.END} This may take several cycles...\n")

        result = self._run_nmap(cmd)

        if result:
            self._cyber_analyze_scan(result, target)

        print(f"\n{Colors.cyber_success('Neural scan complete')}")
        print(f"{Colors.NEON_CYAN}[OUTPUT]{Colors.END} {Colors.NEON_GREEN}{output_file}{Colors.END}\n")

        return result

    def _run_nmap(self, cmd):
        """Execute reconnaissance command"""
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=600
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            print(f"{Colors.cyber_error('Scan timeout - target may be protected')}")
            return None
        except Exception as e:
            print(f"{Colors.cyber_error(f'Scan failure: {e}')}")
            return None

    def _cyber_analyze_scan(self, output, target):
        """Analyze scan results and generate attack vectors"""
        if not output:
            return

        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}")
        print(f"{Colors.NEON_CYAN}[NEURAL ANALYSIS]{Colors.END} Computing attack vectors...\n")

        suggestions = []

        # FTP Detection
        if "21/tcp" in output and "ftp" in output.lower():
            suggestions.append({
                'service': 'FTP',
                'port': '21',
                'priority': 'HIGH',
                'vectors': [
                    f'ftp {target}',
                    f'hydra -L users.txt -P pass.txt ftp://{target}'
                ]
            })

        # SSH Detection
        if "22/tcp" in output and "ssh" in output.lower():
            suggestions.append({
                'service': 'SSH',
                'port': '22',
                'priority': 'MEDIUM',
                'vectors': [
                    f'ssh root@{target}',
                    f'hydra -l root -P pass.txt ssh://{target}'
                ]
            })

        # HTTP/HTTPS Detection
        if any(port in output for port in ["80/tcp", "443/tcp", "8080/tcp"]):
            port = '80' if '80/tcp' in output else ('443' if '443/tcp' in output else '8080')
            protocol = 'https' if port == '443' else 'http'
            suggestions.append({
                'service': 'WEB',
                'port': port,
                'priority': 'CRITICAL',
                'vectors': [
                    f'curl {protocol}://{target}/robots.txt',
                    f'gobuster dir -u {protocol}://{target} -w /usr/share/wordlists/dirb/common.txt',
                    f'nikto -h {protocol}://{target}',
                    'SQL injection testing on forms',
                    'File upload exploitation'
                ]
            })

        # SMB Detection
        if "445/tcp" in output:
            suggestions.append({
                'service': 'SMB',
                'port': '445',
                'priority': 'CRITICAL',
                'vectors': [
                    f'nmap -p 445 --script smb-vuln-ms17-010 {target}',
                    f'smbclient -L //{target} -N',
                    f'enum4linux -a {target}'
                ]
            })

        # MySQL Detection
        if "3306/tcp" in output and "mysql" in output.lower():
            suggestions.append({
                'service': 'MYSQL',
                'port': '3306',
                'priority': 'HIGH',
                'vectors': [
                    f'mysql -h {target} -u root -p',
                    'Test credentials: root:(blank), root:root'
                ]
            })

        # Display attack vectors
        if suggestions:
            for sug in suggestions:
                priority_color = Colors.NEON_PINK if sug['priority'] == 'CRITICAL' else Colors.NEON_ORANGE
                print(f"{priority_color}[{sug['priority']}]{Colors.END} {Colors.NEON_CYAN}{sug['service']}{Colors.END} {Colors.GRAY}(Port {sug['port']}){Colors.END}")
                for vector in sug['vectors']:
                    print(f"  {Colors.NEON_GREEN}►{Colors.END} {vector}")
                print()

        print(f"{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}")
