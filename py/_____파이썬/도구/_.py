from urllib.request import urlopen, Request
import re
import sys

#너비우선탐색

user_agent='Mozilla/5.0\(compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0)like Gecko'
href_links = []


def runCrawler(home, urls, depth):
    global href_links
    tmp_urls = []

    if depth > 10:
        return
    
    print()
    print('\t\t\t+++++검색해볼 urls 개수 : ', len(urls))
    print('\t\t\t+++++depth : ', depth)
    #for url in urls:
    #    print(url)
    for url in urls:
        try:
            print('GETTING ALL LINKS in [%s]' %url)
            doc = readHtml(url)
            if doc is None:
                continue
            href_links.append(url)###########
            
            parent = home#처음
            if home != url:
                tmp = url.split('/')
                parent = '/'.join(tmp[0:-1])

            link_list = getLinks(doc, home, parent)####괜찮아보이는 urls 리턴
            for link in link_list:
                tmp_urls.append(link)
                
        except KeyboardInterrupt:
            print('Terminated by USER..Saving Crawled Links')
            finalize()
            sys.exit(0)
            
    unique_urls = unique(tmp_urls)
     
    runCrawler(home, unique_urls, depth+1)
    
    return  
            

def readHtml(url):
    #print('readhtml...[%s]' %url)
    try:
        req = Request(url)
        req.add_header('User-Agent', user_agent)
        
        h = urlopen(req)
        doc = h.read()
        h.close()
        doc = doc.decode()
        #print(doc)
    except Exception as e:
        print('ERROR: %s' %url)
        print(e)
        return None
    
    return doc
    

def getLinks(doc, home, parent):
    href_pattern = r'href="(.*?)"'
    #href_pattern = r'href="(\S*?)"'
    #href_pattern = r'href=(\S+)'
    p = re.compile(href_pattern)
    
    tmp_urls = p.findall(doc)
    tmp_urls = filter1(tmp_urls)#.css, 공백들어있는거, # 제거, 이미지제거
    tmp_urls = filter2(tmp_urls, home, parent)#http://붙임 https를 http로 맨끝/제거
    tmp_urls = filter3(tmp_urls)#href_links에 있으면 제거

    return tmp_urls


def filter1(urls):
    edit_urls = []
    for url in urls:
        url = url.strip('"')
        if len(url) <= 1 or'.css' in url or '.png' in url or '.jpg' in url or \
           ' ' in url or '#' == url[0]:
            #print('+++Removed this : [%s]+++' %url)
            continue
            
        edit_urls.append(url)

    return edit_urls


def filter2(urls, home, parent):
    edit_urls = []
    for url in urls:
        if len(url) <= 1:
            continue
        if url[-1] == '/':
            url = url[:-1]
        if url[:4] == 'http':
            pass
        else:
            if url[0:2] == './' or url[0:3] == '../':
                url = parent + '/' + url
            elif url[0:2] == '//':
                url = 'http:' + url
            elif url[0] == '/':
                url = home + url
            else :
                #print('+++What is this : [%s]+++' %url)
                continue
        edit_urls.append(url)

    return edit_urls


def filter3(urls):
    global href_links
    edit_urls = []
    for url in urls:
        if url in href_links:
            continue
        edit_urls.append(url)

    return edit_urls


def finalize():
    with open('mycrawled_links.txt', 'w+') as f:
        for href_link in href_links:
            f.write(href_link + '\n')
    print('+++ CRAWLED TOTAL href_links: [%s]' %len(href_links))
        

def unique(tmp_urls):
    urls = []
    for url in tmp_urls:
        if url in urls:
            continue
        urls.append(url)

    return urls


def main():
    targeturl = 'http://www.google.com'
    home = targeturl
    print('+++ WEB LINK CRAWLER START > [%s]' %targeturl)
    runCrawler(home, [targeturl], 0)
    finalize()


if __name__ == '__main__':
    main()
