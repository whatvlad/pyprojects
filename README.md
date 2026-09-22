# Python Mini Projects

A small collection of command-line projects created while learning Python fundamentals, networking, input validation, and program structure.

## Projects

| Project | Description | Concepts |
| --- | --- | --- |
| Password Generator | Generates a cryptographically secure password of a chosen length | Functions, validation, `secrets` |
| Port Scanner | Checks a configurable TCP port range on a host | Sockets, CLI arguments, error handling |
| WHOIS Lookup | Queries WHOIS servers and follows an available referral | TCP communication, parsing, timeouts |

## Requirements

- Python 3.10 or newer
- No third-party packages

## Usage

Clone the repository and run a project from its directory:

```bash
python3 PasswordGenerator/scr.py
python3 PortScanner/src.py example.com --start-port 1 --end-port 1024
python3 WhoIS/src.py example.com
```

Run the syntax checks locally:

```bash
python3 -m compileall PasswordGenerator PortScanner WhoIS
```

## Responsible use

The port scanner is an educational tool. Only scan systems you own or have explicit permission to test.

## Status

This repository documents early Python learning projects. The code has been reorganised and documented while keeping each project intentionally small and readable.
