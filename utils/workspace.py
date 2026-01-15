#!/usr/bin/env python3
"""Workspace management"""

from pathlib import Path
from datetime import datetime

class Workspace:
    def __init__(self, base_dir=None):
        if base_dir:
            self.root = Path(base_dir)
        else:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.root = Path(f"ejpt_workspace_{timestamp}")

        self.scans = self.root / "scans"
        self.exploits = self.root / "exploits"
        self.screenshots = self.root / "screenshots"
        self.loot = self.root / "loot"
        self.reports = self.root / "reports"

        self._create_structure()

    def _create_structure(self):
        """Create workspace directory structure"""
        for directory in [self.root, self.scans, self.exploits,
                         self.screenshots, self.loot, self.reports]:
            directory.mkdir(exist_ok=True, parents=True)

    def get_scan_file(self, target, scan_type="nmap"):
        """Get path for scan output file"""
        filename = f"{scan_type}_{target.replace('.', '_')}.txt"
        return self.scans / filename

    def get_exploit_file(self, exploit_name):
        """Get path for exploit file"""
        return self.exploits / f"{exploit_name}.txt"
