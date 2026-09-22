import argparse
import re
import socket


DEFAULT_SERVER = "whois.iana.org"
WHOIS_PORT = 43


def query_whois(domain: str, server: str, timeout: float = 5.0) -> str:
    """Query a WHOIS server and return its complete text response."""
    chunks: list[bytes] = []

    with socket.create_connection((server, WHOIS_PORT), timeout=timeout) as connection:
        connection.sendall(f"{domain}\r\n".encode("utf-8"))

        while chunk := connection.recv(4096):
            chunks.append(chunk)

    return b"".join(chunks).decode("utf-8", errors="replace")


def find_referral_server(response: str) -> str | None:
    match = re.search(r"^refer:\s*(\S+)", response, flags=re.IGNORECASE | re.MULTILINE)
    return match.group(1) if match else None


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Look up WHOIS information for a domain.")
    parser.add_argument("domain", help="Domain to look up, for example: example.com")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    domain = args.domain.strip().lower()

    try:
        initial_response = query_whois(domain, DEFAULT_SERVER)
        referral_server = find_referral_server(initial_response)
        response = (
            query_whois(domain, referral_server)
            if referral_server
            else initial_response
        )
    except (OSError, socket.timeout) as error:
        print(f"WHOIS lookup failed: {error}")
        return

    print(response)


if __name__ == "__main__":
    main()
