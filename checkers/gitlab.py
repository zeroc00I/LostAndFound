import requests, urllib

base_domains = ["gitlab.com"]
cache_domains = set()


def check(url):
	
	parsed_url = urllib.parse.urlparse(url)
	
	# get only user
	if parsed_url.path.count('/') >= 2 :
		url = '/'.join(url.split('/')[:4])
	
	if url not in cache_domains :
		cache_domains.add(url) 


		r = requests.get(url)

		if r.status_code == 302 and "You are being" in r.text :
			print("[!] Gitlab unregistred username:", url)