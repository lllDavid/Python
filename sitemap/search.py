from re import findall

def find_loc(jobtitle:str = input("Enter jobtitle: "), date:str = (input("Enter date:"))):
    with open('sitemap.xml', 'r') as file:
        content = file.read()  

        loc_tags = findall(r'<loc>(.*?)</loc>', content)
        lastmod_tags = findall(r'<lastmod>(.*?)</lastmod>', content)

        for loc, lastmod in zip(loc_tags, lastmod_tags):
            if jobtitle in loc and date in lastmod:
                print(loc)

find_loc()
