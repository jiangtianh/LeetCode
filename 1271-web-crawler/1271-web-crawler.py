# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        s = set()
        i = 8
        while i < len(startUrl) and startUrl[i] != "/":
            i += 1
        hostname = startUrl[:i]
        
        def f(url, hostname):
            if not url.startswith(hostname):
                return
            s.add(url)
            for other in htmlParser.getUrls(url):
                if other not in s:
                    f(other, hostname)
        
        f(startUrl, hostname)
        return s