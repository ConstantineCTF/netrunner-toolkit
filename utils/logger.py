#!/usr/bin/env python3
"""Command and event logging"""

import logging
from datetime import datetime
from pathlib import Path

class EJPTLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        # Setup loggers
        self.command_log = self._setup_logger('commands', 'commands.log')
        self.event_log = self._setup_logger('events', 'events.log')
        self.finding_log = self._setup_logger('findings', 'findings.log')

    def _setup_logger(self, name, filename):
        """Setup individual logger"""
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        handler = logging.FileHandler(self.log_dir / filename)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

    def log_command(self, command, target=None):
        """Log executed command"""
        msg = f"TARGET: {target} | CMD: {command}" if target else command
        self.command_log.info(msg)

    def log_finding(self, finding_type, target, details):
        """Log security finding"""
        msg = f"{finding_type} on {target}: {details}"
        self.finding_log.info(msg)

    def log_event(self, event):
        """Log general event"""
        self.event_log.info(event)
