def filter2(urls):
    edit_urls = []
    for url in urls:
        if '.css' in url:
            continue
        if ' ' in url:
            continue
        if '#' in url:
            continue
        edit_urls.append(url)

    return edit_urls




urls = ['asdfasfd .css', 'www.naver.com', 'asfd# ', 'www naver']

edit_urls = filter2(urls)

print(edit_urls)
