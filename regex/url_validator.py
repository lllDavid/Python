import re

url_pattern = re.compile(r"""
\b
https?://                     # http or https protocol
(?:[a-zA-Z0-9-]+\.)+          # subdomain(s) and domain
[a-zA-Z]{2,6}                 # TLD
(?::\d{1,5})?                 # optional port
(?:/[^\s?#]*)?                # optional path
(?:\?[^\s#]*)?                # optional query
(?:\#[^\s]*)?                 # optional fragment
\b
""", re.VERBOSE)

urls = [
    "http://example.com",
    "https://sub.domain.co.uk:8080/path/to/page?query=1&sort=asc#section",
    "ftp://wrong.protocol.com",
    "https://example.com/noquery"
]
for u in urls:
    print(u, "=>", bool(url_pattern.match(u)))