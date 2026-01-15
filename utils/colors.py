#!/usr/bin/env python3
"""
Cyberpunk color scheme for terminal output
Neon colors inspired by Night City
"""

class Colors:
    # Neon cyberpunk colors
    NEON_PINK = '\033[38;5;198m'
    NEON_CYAN = '\033[38;5;51m'
    NEON_GREEN = '\033[38;5;46m'
    NEON_PURPLE = '\033[38;5;165m'
    NEON_ORANGE = '\033[38;5;208m'
    NEON_BLUE = '\033[38;5;33m'
    NEON_YELLOW = '\033[38;5;226m'

    # Matrix/Terminal colors
    MATRIX_GREEN = '\033[38;5;40m'
    DEEP_PURPLE = '\033[38;5;93m'
    DARK_CYAN = '\033[38;5;30m'

    # Standard with cyberpunk twist
    RED = '\033[91m'
    ORANGE = '\033[38;5;202m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    DIM = '\033[2m'

    # Effects
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'

    # Glitch effect colors
    GLITCH_1 = '\033[38;5;196m'
    GLITCH_2 = '\033[38;5;21m'

    END = '\033[0m'

    @staticmethod
    def cyber_success(msg):
        """Success message in neon green"""
        return f"{Colors.NEON_GREEN}[+] {msg}{Colors.END}"

    @staticmethod
    def cyber_info(msg):
        """Info message in neon cyan"""
        return f"{Colors.NEON_CYAN}[*] {msg}{Colors.END}"

    @staticmethod
    def cyber_warning(msg):
        """Warning in neon orange"""
        return f"{Colors.NEON_ORANGE}[!] {msg}{Colors.END}"

    @staticmethod
    def cyber_error(msg):
        """Error in neon pink/red"""
        return f"{Colors.NEON_PINK}[X] {msg}{Colors.END}"

    @staticmethod
    def cyber_scan(msg):
        """Scan message in neon purple"""
        return f"{Colors.NEON_PURPLE}[>>] {msg}{Colors.END}"

    @staticmethod
    def cyber_exploit(msg):
        """Exploit message in neon yellow"""
        return f"{Colors.NEON_YELLOW}[>>>] {msg}{Colors.END}"

    @staticmethod
    def glitch_text(text):
        """Create glitch effect"""
        output = ""
        for i, char in enumerate(text):
            if i % 3 == 0:
                output += f"{Colors.GLITCH_1}{char}{Colors.END}"
            elif i % 3 == 1:
                output += f"{Colors.GLITCH_2}{char}{Colors.END}"
            else:
                output += f"{Colors.NEON_CYAN}{char}{Colors.END}"
        return output

    @staticmethod
    def neon_box(title, content, width=60):
        """Create neon-bordered box"""
        top = f"{Colors.NEON_CYAN}╔{'═' * (width - 2)}╗{Colors.END}"
        bottom = f"{Colors.NEON_CYAN}╚{'═' * (width - 2)}╝{Colors.END}"

        output = [top]

        # Title
        title_padded = title.center(width - 4)
        output.append(f"{Colors.NEON_CYAN}║{Colors.END} {Colors.NEON_PINK}{Colors.BOLD}{title_padded}{Colors.END} {Colors.NEON_CYAN}║{Colors.END}")
        output.append(f"{Colors.NEON_CYAN}╠{'═' * (width - 2)}╣{Colors.END}")

        # Content
        for line in content:
            line_padded = line.ljust(width - 4)
            output.append(f"{Colors.NEON_CYAN}║{Colors.END} {line_padded} {Colors.NEON_CYAN}║{Colors.END}")

        output.append(bottom)
        return '\n'.join(output)
