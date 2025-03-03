from re import findall

def find_job(jobtitle: str = input("Enter jobtitle: ")):
    with open('sitemap.xml', 'r') as file:
        content = file.read()

        loc_tags = findall(r'<loc>(.*?)</loc>', content)
        lastmod_tags = findall(r'<lastmod>(.*?)</lastmod>', content)

        date = "2025-02-01"

        for loc, lastmod in zip(loc_tags, lastmod_tags):
            if jobtitle in loc and lastmod > date:
                print(loc)
                
find_job()
