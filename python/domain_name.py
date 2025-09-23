"""
Write a function that when given a URL as a string,
parses out just the domain name and returns it as a string.
For example:
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url: str) -> str:
    return url.split("/")[2].split(".")[::-1][1]

url =["http://www.zombie-bites.com", "http://github.com/carbonfive/raygun", "https://www.cnet.com"]
for u in url:
    print(domain_name(u))
