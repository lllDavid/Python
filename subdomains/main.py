import socket

def load_wordlist(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

def subdomain_enumerate(domain, subdomains):
    found_subdomains = []
    for subdomain in subdomains:
        full_domain = f"{subdomain}.{domain}"
        try:
            ip = socket.gethostbyname(full_domain)
            print(f"Found: {full_domain} -> {ip}")
            found_subdomains.append((full_domain, ip))
        except socket.gaierror:
            pass
    return found_subdomains

if __name__ == "__main__":
    domain = input("Enter domain (e.g., github.com): ").strip()
    wordlist = load_wordlist("subdomains.txt")
    results = subdomain_enumerate(domain, wordlist)

    print("\nSummary:")
    for sub, ip in results:
        print(f"{sub} -> {ip}")
