import argparse
import socket
from time import perf_counter


COMMON_SERVICES = {
    20: "ftp-data",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    143: "imap",
    443: "https",
    445: "smb",
    587: "smtp-tls",
    3306: "mysql",
    3389: "rdp",
}


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a TCP port range on a host.",
        epilog="Only scan systems you own or have explicit permission to test.",
    )
    parser.add_argument("target", help="Hostname or IP address to scan")
    parser.add_argument("--start-port", type=int, default=1)
    parser.add_argument("--end-port", type=int, default=1024)
    parser.add_argument("--timeout", type=float, default=0.1)
    return parser.parse_args()


def validate_port_range(start_port: int, end_port: int) -> None:
    if not 1 <= start_port <= 65535 or not 1 <= end_port <= 65535:
        raise ValueError("Ports must be between 1 and 65535.")
    if start_port > end_port:
        raise ValueError("The start port cannot be greater than the end port.")


def is_port_open(target: str, port: int, timeout: float) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.settimeout(timeout)
        return connection.connect_ex((target, port)) == 0


def main() -> None:
    args = parse_arguments()

    try:
        validate_port_range(args.start_port, args.end_port)
        target_ip = socket.gethostbyname(args.target)
    except (ValueError, socket.gaierror) as error:
        print(f"Error: {error}")
        return

    print(f"Scanning {args.target} ({target_ip})")
    started_at = perf_counter()

    try:
        for port in range(args.start_port, args.end_port + 1):
            if is_port_open(target_ip, port, args.timeout):
                service = COMMON_SERVICES.get(port, "unknown")
                print(f"{port:<6} open   tcp   {service}")
    except KeyboardInterrupt:
        print("\nScan cancelled.")
        return

    print(f"Scan completed in {perf_counter() - started_at:.2f} seconds.")


if __name__ == "__main__":
    main()
