#!/usr/bin/env python3
"""
Report generation module
Creates professional penetration test reports
"""

from datetime import datetime
from pathlib import Path
import json

class ReportGenerator:
    def __init__(self, workspace, logger):
        self.workspace = workspace
        self.logger = logger
        self.findings = []
        self.targets = []
        self.credentials = []
        self.screenshots = []

    def add_finding(self, title, severity, affected_systems, description,
                    impact, poc, remediation, cvss=None, cve=None):
        """Add a finding to the report"""
        finding = {
            'title': title,
            'severity': severity.upper(),
            'affected_systems': affected_systems if isinstance(affected_systems, list) else [affected_systems],
            'description': description,
            'impact': impact,
            'proof_of_concept': poc,
            'remediation': remediation,
            'cvss': cvss,
            'cve': cve,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.findings.append(finding)
        self.logger.log_finding(severity, affected_systems, title)

    def add_target(self, ip, hostname=None, os=None, services=None):
        """Add a target system"""
        target = {
            'ip': ip,
            'hostname': hostname or 'Unknown',
            'os': os or 'Unknown',
            'services': services or []
        }
        self.targets.append(target)

    def add_credential(self, system, username, password, service=None, notes=None):
        """Add discovered credentials"""
        cred = {
            'system': system,
            'username': username,
            'password': password,
            'service': service or 'Unknown',
            'notes': notes or ''
        }
        self.credentials.append(cred)

    def add_screenshot(self, filename, description):
        """Add screenshot reference"""
        screenshot = {
            'filename': filename,
            'description': description,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.screenshots.append(screenshot)

    def generate_executive_summary(self, custom_summary=None):
        """Generate executive summary"""
        if custom_summary:
            return custom_summary

        # Count findings by severity
        severity_counts = {
            'CRITICAL': 0,
            'HIGH': 0,
            'MEDIUM': 0,
            'LOW': 0
        }

        for finding in self.findings:
            severity = finding['severity'].upper()
            if severity in severity_counts:
                severity_counts[severity] += 1

        total = sum(severity_counts.values())

        summary = f"""## EXECUTIVE SUMMARY

A comprehensive penetration test was conducted against the target environment from {datetime.now().strftime('%B %d, %Y')}.

### Key Findings

**Total Vulnerabilities Identified: {total}**

- **Critical:** {severity_counts['CRITICAL']} findings
- **High:** {severity_counts['HIGH']} findings
- **Medium:** {severity_counts['MEDIUM']} findings
- **Low:** {severity_counts['LOW']} findings

### Risk Assessment

"""

        if severity_counts['CRITICAL'] > 0:
            summary += f"⚠️ **CRITICAL RISK**: {severity_counts['CRITICAL']} critical vulnerabilities require immediate attention. These vulnerabilities pose severe risk to the organization and could lead to complete system compromise, data breach, or significant operational impact.\n\n"

        if severity_counts['HIGH'] > 0:
            summary += f"⚠️ **HIGH RISK**: {severity_counts['HIGH']} high-severity vulnerabilities were identified. These should be addressed within 30 days to prevent potential exploitation.\n\n"

        summary += """### Recommendations

**Immediate Actions (0-7 days):**
- Address all critical vulnerabilities
- Change all default credentials
- Implement emergency patches

**Short-term Actions (7-30 days):**
- Remediate high-severity findings
- Implement Web Application Firewall (WAF)
- Deploy multi-factor authentication (MFA)

**Long-term Actions (30-90 days):**
- Establish vulnerability management program
- Conduct security awareness training
- Implement regular penetration testing schedule

"""
        return summary

    def generate_scope_section(self, in_scope, out_scope, start_date=None, end_date=None):
        """Generate scope section"""
        start = start_date or datetime.now().strftime('%Y-%m-%d')
        end = end_date or datetime.now().strftime('%Y-%m-%d')

        scope = f"""## SCOPE AND METHODOLOGY

### Testing Timeline

- **Start Date:** {start}
- **End Date:** {end}
- **Total Duration:** {len(self.targets)} systems tested

### In Scope

"""
        for item in in_scope:
            scope += f"- {item}\n"

        scope += "\n### Out of Scope\n\n"
        for item in out_scope:
            scope += f"- {item}\n"

        scope += """
### Methodology

The assessment followed industry-standard penetration testing methodologies including:

- **OWASP Testing Guide** - Web application security testing
- **PTES** (Penetration Testing Execution Standard)
- **NIST SP 800-115** - Technical Guide to Information Security Testing

#### Testing Phases

1. **Reconnaissance**
   - Network discovery and enumeration
   - Service identification and fingerprinting
   - Web application mapping

2. **Vulnerability Assessment**
   - Automated vulnerability scanning
   - Manual security testing
   - Configuration review

3. **Exploitation**
   - Proof-of-concept development
   - Controlled exploitation of vulnerabilities
   - Privilege escalation attempts

4. **Post-Exploitation**
   - Credential harvesting
   - Lateral movement testing
   - Impact assessment

5. **Reporting**
   - Comprehensive documentation
   - Risk analysis
   - Remediation recommendations

"""
        return scope

    def generate_findings_section(self):
        """Generate technical findings section"""
        if not self.findings:
            return "## TECHNICAL FINDINGS\n\nNo vulnerabilities were identified during testing.\n"

        # Sort findings by severity
        severity_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
        sorted_findings = sorted(self.findings, key=lambda x: severity_order.get(x['severity'], 4))

        findings_md = "## TECHNICAL FINDINGS\n\n"

        # Summary table
        findings_md += "### Findings Summary\n\n"
        findings_md += "| # | Severity | Vulnerability | Affected Systems |\n"
        findings_md += "|---|----------|---------------|------------------|\n"

        for i, finding in enumerate(sorted_findings, 1):
            systems = ', '.join(finding['affected_systems'][:2])
            if len(finding['affected_systems']) > 2:
                systems += f" (+{len(finding['affected_systems'])-2} more)"
            findings_md += f"| {i} | {finding['severity']} | {finding['title']} | {systems} |\n"

        findings_md += "\n---\n\n"

        # Detailed findings
        for i, finding in enumerate(sorted_findings, 1):
            findings_md += f"### Finding #{i}: {finding['title']}\n\n"
            findings_md += f"**Severity:** {finding['severity']}\n\n"

            if finding.get('cvss'):
                findings_md += f"**CVSS Score:** {finding['cvss']}\n\n"

            if finding.get('cve'):
                findings_md += f"**CVE:** {finding['cve']}\n\n"

            findings_md += f"**Affected Systems:**\n\n"
            for system in finding['affected_systems']:
                findings_md += f"- {system}\n"

            findings_md += f"\n**Description:**\n\n{finding['description']}\n\n"
            findings_md += f"**Impact:**\n\n{finding['impact']}\n\n"
            findings_md += f"**Proof of Concept:**\n\n```\n{finding['proof_of_concept']}\n```\n\n"
            findings_md += f"**Remediation:**\n\n{finding['remediation']}\n\n"
            findings_md += "---\n\n"

        return findings_md

    def generate_appendix(self, tools_used=None):
        """Generate appendix section"""
        appendix = "## APPENDICES\n\n"

        # Tools
        appendix += "### Appendix A: Tools Used\n\n"
        default_tools = [
            "Nmap 7.94 - Network scanning and service enumeration",
            "Metasploit Framework 6.3 - Exploitation framework",
            "Burp Suite Community - Web application testing",
            "Gobuster 3.6 - Directory/file enumeration",
            "Hydra 9.4 - Credential brute-forcing",
            "SQLMap 1.7 - SQL injection automation",
            "Nikto 2.5 - Web server scanning"
        ]

        tools = tools_used or default_tools
        for tool in tools:
            appendix += f"- {tool}\n"

        # Credentials
        if self.credentials:
            appendix += "\n### Appendix B: Discovered Credentials\n\n"
            appendix += "| System | Service | Username | Password | Notes |\n"
            appendix += "|--------|---------|----------|----------|-------|\n"
            for cred in self.credentials:
                appendix += f"| {cred['system']} | {cred['service']} | {cred['username']} | {cred['password']} | {cred['notes']} |\n"

        # Screenshots
        if self.screenshots:
            appendix += "\n### Appendix C: Screenshots\n\n"
            for screenshot in self.screenshots:
                appendix += f"**{screenshot['filename']}**\n"
                appendix += f"- Description: {screenshot['description']}\n"
                appendix += f"- Timestamp: {screenshot['timestamp']}\n\n"

        # References
        appendix += """
### Appendix D: References

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- CWE Top 25: https://cwe.mitre.org/top25/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- SANS Top 25 Software Errors: https://www.sans.org/top25-software-errors/
- CVE Database: https://cve.mitre.org/

"""
        return appendix

    def generate_full_report(self, client_name="Client", test_type="Penetration Test",
                           in_scope=None, out_scope=None, custom_summary=None,
                           tools_used=None):
        """Generate complete report"""

        in_scope = in_scope or ["Target network and systems as specified"]
        out_scope = out_scope or ["Physical security testing", "Social engineering", "Denial of Service attacks"]

        report = f"""# PENETRATION TEST REPORT

**Client:** {client_name}
**Assessment Type:** {test_type}
**Report Date:** {datetime.now().strftime('%B %d, %Y')}
**Prepared By:** eJPT Certified Tester

---

## TABLE OF CONTENTS

1. Executive Summary
2. Scope and Methodology
3. Technical Findings
4. Conclusion
5. Appendices

---

"""

        # Add sections
        report += self.generate_executive_summary(custom_summary) + "\n\n---\n\n"
        report += self.generate_scope_section(in_scope, out_scope) + "\n\n---\n\n"
        report += self.generate_findings_section() + "\n\n---\n\n"

        # Conclusion
        report += """## CONCLUSION

"""

        if self.findings:
            critical_count = sum(1 for f in self.findings if f['severity'] == 'CRITICAL')
            high_count = sum(1 for f in self.findings if f['severity'] == 'HIGH')

            if critical_count > 0 or high_count > 0:
                report += f"""The security assessment revealed {len(self.findings)} vulnerabilities requiring remediation.

**Priority Actions:**

The identified critical and high-severity vulnerabilities pose significant risk and should be addressed immediately. Implementing the recommended security controls will substantially improve the organization's security posture.

**Next Steps:**

1. Review and prioritize findings with stakeholders
2. Develop remediation plan with timelines
3. Implement security fixes
4. Request re-assessment to validate remediations
5. Establish ongoing vulnerability management program

"""
        else:
            report += "No significant vulnerabilities were identified during testing. The tested systems demonstrated adequate security controls.\n\n"

        report += "\n\n---\n\n"
        report += self.generate_appendix(tools_used)

        # Save report
        report_file = self.workspace.reports / f"pentest_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(report_file, 'w') as f:
            f.write(report)

        print(f"[+] Report generated: {report_file}")

        # Also save JSON version
        json_file = self.workspace.reports / f"findings_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(json_file, 'w') as f:
            json.dump({
                'findings': self.findings,
                'targets': self.targets,
                'credentials': self.credentials,
                'screenshots': self.screenshots
            }, f, indent=2)

        return report_file

    def quick_finding(self, title, severity, target, description, commands, result, fix):
        """Quick method to add finding with minimal input"""
        poc = f"""Steps to Reproduce:

{description}

Commands Executed:
{commands}

Result:
{result}
"""

        self.add_finding(
            title=title,
            severity=severity,
            affected_systems=target,
            description=description,
            impact=f"Successful exploitation of this {severity.lower()}-severity vulnerability could lead to unauthorized access and potential system compromise.",
            poc=poc,
            remediation=fix
        )
