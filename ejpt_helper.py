#!/usr/bin/env python3
"""
eJPT NETRUNNER - Cyberpunk Penetration Testing Framework
Neural interface for security assessment operations
"""

import argparse
import sys
from pathlib import Path

# Import modules
from utils.colors import Colors
from utils.workspace import Workspace
from utils.logger import EJPTLogger
from core.scanner import Scanner
from core.web_hunter import WebHunter
from core.exploit_gen import ExploitGenerator
from core.report_gen import ReportGenerator

class NetRunner:
    def __init__(self):
        self.workspace = Workspace()
        self.logger = EJPTLogger(self.workspace.root / "logs")
        self.scanner = Scanner(self.workspace, self.logger)
        self.web_hunter = WebHunter(self.workspace, self.logger)
        self.exploit_gen = ExploitGenerator(self.workspace)
        self.report_gen = ReportGenerator(self.workspace, self.logger)

    def cyber_banner(self):
    """Display cyberpunk-themed banner - Night City Edition"""
    banner = f"""
{Colors.NEON_PINK}    ╔═══════════════════════════════════════════════════════════════════════╗{Colors.END}
{Colors.NEON_PINK}    ║ {Colors.NEON_CYAN}サイバーパンク  {Colors.NEON_PINK}◢◤◢◤◢◤  {Colors.NEON_GREEN}NEURAL INTERFACE  {Colors.NEON_PINK}◢◤◢◤◢◤  {Colors.NEON_YELLOW}2077{Colors.NEON_PINK}  ║{Colors.END}
{Colors.NEON_PINK}    ╚═══════════════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.NEON_CYAN}        ███╗   ██╗███████╗████████╗██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗███████╗██████╗ 
        ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗
        ██╔██╗ ██║█████╗     ██║   ██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
        ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
        ██║ ╚████║███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║  ██║
        ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{Colors.END}

{Colors.NEON_PINK}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}
{Colors.NEON_PURPLE}          eJPT SECURITY FRAMEWORK v2.0  {Colors.GRAY}|{Colors.END}  {Colors.NEON_GREEN}ネットランナー{Colors.END} {Colors.GRAY}|{Colors.END}  {Colors.NEON_YELLOW}侵入テスト{Colors.END}
{Colors.NEON_PINK}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}

{Colors.NEON_GREEN}    [√]{Colors.END} {Colors.NEON_CYAN}NEURAL LINK{Colors.END}      {Colors.NEON_GREEN}███████████████{Colors.GRAY}░░░{Colors.END} {Colors.NEON_GREEN}85%{Colors.END}
{Colors.NEON_GREEN}    [√]{Colors.END} {Colors.NEON_CYAN}WORKSPACE{Colors.END}        {Colors.NEON_PINK}{self.workspace.root}{Colors.END}
{Colors.NEON_GREEN}    [√]{Colors.END} {Colors.NEON_CYAN}EXPLOIT DB{Colors.END}       {Colors.NEON_GREEN}LOADED{Colors.END} {Colors.GRAY}[{Colors.NEON_YELLOW}4 MODULES{Colors.GRAY}]{Colors.END}
{Colors.NEON_GREEN}    [√]{Colors.END} {Colors.NEON_CYAN}LOGGING SYS{Colors.END}      {Colors.NEON_GREEN}ACTIVE{Colors.END} {Colors.GRAY}[{Colors.NEON_YELLOW}3 STREAMS{Colors.GRAY}]{Colors.END}

{Colors.NEON_PINK}    ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰{Colors.END}
{Colors.NEON_YELLOW}           WAKE UP SAMURAI...  WE HAVE A NETWORK TO BURN{Colors.END}
{Colors.NEON_PINK}    ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰{Colors.END}
"""
    print(banner)

    def cyber_footer(self):
        """Display footer message"""
        footer = f"""
{Colors.NEON_PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}
{Colors.NEON_CYAN}[{Colors.NEON_YELLOW}SYSTEM{Colors.NEON_CYAN}]{Colors.END} Neural link terminated
{Colors.NEON_CYAN}[{Colors.NEON_YELLOW}SYSTEM{Colors.NEON_CYAN}]{Colors.END} Data stream closed
{Colors.GRAY}Stay sharp, netrunner.{Colors.END}
"""
        print(footer)

def main():
    parser = argparse.ArgumentParser(
        description='NETRUNNER - Cyberpunk Penetration Testing Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f'''{Colors.NEON_CYAN}
NEURAL INTERFACE COMMANDS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  -t, --target          Designate target node for scanning
  --quick               Execute rapid reconnaissance protocol
  --full                Deploy comprehensive scan matrix
  --web                 Initialize web application analysis
  --shell               Generate reverse neural link payload
  --sqli                Load SQL injection exploit database
  --xss                 Access XSS payload archives
  --lfi                 Retrieve file inclusion vectors
  --creds               Query default credential matrix
  --report              Compile security assessment dossier
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.END}'''
    )

    parser.add_argument('-t', '--target', help='Target IP or network designation')
    parser.add_argument('--quick', action='store_true', help='Rapid scan protocol')
    parser.add_argument('--full', action='store_true', help='Deep scan protocol')
    parser.add_argument('--web', help='Web application analysis target')
    parser.add_argument('--shell', help='Reverse shell generator (LHOST:LPORT:TYPE)')
    parser.add_argument('--sqli', action='store_true', help='SQL injection payloads')
    parser.add_argument('--xss', action='store_true', help='XSS payload database')
    parser.add_argument('--lfi', action='store_true', help='File inclusion vectors')
    parser.add_argument('--creds', help='Default credentials lookup')
    parser.add_argument('--report', action='store_true', help='Generate assessment report')

    args = parser.parse_args()

    netrunner = NetRunner()
    netrunner.cyber_banner()

    try:
        if args.quick and args.target:
            print(f"\n{Colors.NEON_PURPLE}[SCANNING]{Colors.END} Initiating rapid reconnaissance protocol...")
            netrunner.scanner.quick_scan(args.target)

        elif args.full and args.target:
            print(f"\n{Colors.NEON_PURPLE}[SCANNING]{Colors.END} Deploying comprehensive scan matrix...")
            netrunner.scanner.full_scan(args.target)

        elif args.web:
            print(f"\n{Colors.NEON_PURPLE}[WEB ANALYSIS]{Colors.END} Probing web application infrastructure...")
            netrunner.web_hunter.quick_check(args.web)

        elif args.shell:
            parts = args.shell.split(':')
            lhost = parts[0]
            lport = int(parts[1]) if len(parts) > 1 else 4444
            shell_type = parts[2] if len(parts) > 2 else 'all'
            print(f"\n{Colors.NEON_PURPLE}[PAYLOAD GEN]{Colors.END} Compiling reverse neural link...")
            netrunner.exploit_gen.reverse_shell(lhost, lport, shell_type)

        elif args.sqli:
            print(f"\n{Colors.NEON_PURPLE}[DATABASE]{Colors.END} Loading SQL injection exploit vectors...")
            netrunner.exploit_gen.sqli_payloads()

        elif args.xss:
            print(f"\n{Colors.NEON_PURPLE}[DATABASE]{Colors.END} Accessing XSS payload archives...")
            import json
            with open('data/payloads.json') as f:
                payloads = json.load(f)
            for category, payload_list in payloads['xss'].items():
                print(f"\n{Colors.NEON_CYAN}[{category.upper()}]{Colors.END}")
                for p in payload_list:
                    print(f"  {Colors.NEON_GREEN}>{Colors.END} {p}")

        elif args.lfi:
            print(f"\n{Colors.NEON_PURPLE}[DATABASE]{Colors.END} Retrieving file inclusion vectors...")
            import json
            with open('data/payloads.json') as f:
                payloads = json.load(f)
            for category, payload_list in payloads['lfi'].items():
                print(f"\n{Colors.NEON_CYAN}[{category.upper()}]{Colors.END}")
                for p in payload_list:
                    print(f"  {Colors.NEON_GREEN}>{Colors.END} {p}")

        elif args.creds:
            print(f"\n{Colors.NEON_PURPLE}[CREDENTIAL DB]{Colors.END} Querying authentication matrix...")
            import json
            with open('data/default_creds.json') as f:
                all_creds = json.load(f)

            service = args.creds.lower()
            if service in all_creds:
                print(f"\n{Colors.NEON_CYAN}[{service.upper()} CREDENTIALS]{Colors.END}\n")
                for cred in all_creds[service]:
                    print(f"  {Colors.NEON_GREEN}>{Colors.END} {Colors.NEON_YELLOW}{cred['username']: <15}{Colors.END} :  {Colors.NEON_PINK}{cred['password']}{Colors.END}")
            else:
                print(f"{Colors.cyber_error('Unknown service protocol')}")
                print(f"  Available: {Colors.NEON_CYAN}{', '.join(all_creds.keys())}{Colors.END}")

        elif args.report:
            print(f"\n{Colors.NEON_PURPLE}[REPORT GEN]{Colors.END} Compiling security assessment dossier...")
            netrunner.report_gen.generate_full_report()

        else:
            parser.print_help()

    except KeyboardInterrupt:
        print(f"\n\n{Colors.NEON_PINK}[INTERRUPT]{Colors.END} Neural link severed by operator")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.cyber_error(f'System malfunction: {str(e)}')}")
        sys.exit(1)
    finally:
        netrunner.cyber_footer()

if __name__ == "__main__":
    main()
