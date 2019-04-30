import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ProcessPoolExecutor() as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    print(future_to_url)
# =============================================================================
#     try:
#         data = future.result()
#     except Exception as exc:
#         print('%r generated an exception: %s' % (url, exc))
#     else:
#         print('%r page is %d bytes' % (url, len(data)))
# =============================================================================