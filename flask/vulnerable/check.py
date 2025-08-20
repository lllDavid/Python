import requests, sys, re, logging
from datetime import datetime

def setup_logger():
    f=f"pentest_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                        handlers=[logging.FileHandler(f), logging.StreamHandler()])
    l=logging.getLogger()
    l.info(f"Logging initialized. Results will be saved to {f}")
    return l

def test_accessibility(u,l):
    try:
        r=requests.get(u,timeout=5); l.info(f"Status Code: {r.status_code}")
        return r
    except: l.error("Endpoint not reachable"); return None

def test_http_methods(u,l):
    try:
        r=requests.options(u,timeout=5)
        m=r.headers.get("Allow","Not provided"); l.info(f"Allowed HTTP methods: {m}")
        if any(x in m.upper() for x in ["PUT","DELETE","TRACE"]): l.warning("Insecure HTTP methods detected")
        pr=requests.put(u,data={"test":"data"},timeout=5)
        if pr.status_code in [200,201]: l.warning("PUT method allowed")
    except: l.error("HTTP methods test failed")

def test_sql_injection(u,l):
    try:
        r=requests.get(u+"?id=' OR 1=1 --",timeout=5)
        if any(e in r.text.lower() for e in ["sql syntax","mysql","sqlite","database error"]): l.warning("Potential SQL Injection")
    except: l.error("SQL Injection test failed")

def test_xss(u,l):
    try:
        p="<script>alert('xss')</script>"
        r=requests.get(u+"?q="+p,timeout=5)
        if p in r.text: l.warning("Potential XSS vulnerability")
    except: l.error("XSS test failed")

def test_cors(u,l):
    try:
        r=requests.get(u,headers={"Origin":"http://malicious.example.com"},timeout=5)
        c=r.headers.get("Access-Control-Allow-Origin","Not set"); l.info(f"CORS header: {c}")
        if c=="*" or c=="http://malicious.example.com": l.warning("CORS misconfiguration detected")
    except: l.error("CORS test failed")

def test_verbose_errors(u,l):
    try:
        r=requests.get(u+"?invalid_param=malformed",timeout=5)
        if any(k in r.text.lower() for k in ["stack trace","exception","error at line"]): l.warning("Verbose errors detected")
    except: l.error("Verbose error test failed")

def test_sensitive_data(u,l):
    try:
        r=requests.get(u,timeout=5)
        emails=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',r.text)
        if emails: l.warning(f"Potential info leak: {emails}")
    except: l.error("Sensitive data test failed")

def main():
    if len(sys.argv)!=2: print("Usage: python script.py <endpoint>"); sys.exit(1)
    t=sys.argv[1]; t="http://"+t if not t.startswith(("http://","https://")) else t
    l=setup_logger()
    test_accessibility(t,l)
    test_http_methods(t,l)
    test_sql_injection(t,l)
    test_xss(t,l)
    test_cors(t,l)
    test_verbose_errors(t,l)
    test_sensitive_data(t,l)
    l.info("Security testing completed.")

if __name__=="__main__": main()