# Scrapy Tokopedia Python
This project demonstrates how to build web crawler or scrapper using [Scrapy](https://scrapy.org/) framework. 

## Contents
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Run](#run)

## Getting Started
### Prerequisites
1.  Please make sure you have [pip](https://pip.pypa.io/en/stable/cli/pip_install/) installed on your system.
2.  Please make sure you have [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html#installing-scrapy) installed on your system.

### Installation
1. Clone this repository to your local machine using terminal.
```bash
git clone https://github.com/mushoffa/scrapy-tokopedia-python.git
```
2. Change the current working directory to the location of cloned directory.
```bash
cd scrapy-tokopedia-python
```

## Run
1. Change directory to project root folder and ensure you have Makefile in the same directory.
> Notes: You can use 'tree' command line tools to check
> ```bash
> $ tree
> ```
```bash
.                                                                            
├── Makefile                                                  
├── README.md                 
├── output                                   
├── scrapy.cfg                                                   
└── tokopedia                                                    
    ├── __init__.py                                             
    ├── __pycache__                         
    │   ├── __init__.cpython-39.pyc       
    │   └── settings.cpython-39.pyc      
    ├── items.py                                 
    ├── middlewares.py                                                   
    ├── pipelines.py                                                             
    ├── settings.py                                                
    └── spiders                                                        
        ├── __init__.py                                  
        ├── __pycache__
        │   ├── __init__.cpython-39.pyc
        │   └── handphone_spider.cpython-39.pyc
        └── handphone_spider.py     
```
2. Execute the following command to run the spider.
```bash
$ make run
```
3. The spider will do initialization before scraping.
```bash
$ make run
scrapy crawl tokopedia-handphone -o output/result.csv  
2021-11-23 00:21:37 [scrapy.utils.log] INFO: Scrapy 2.5.1 started (bot: tokopedia)
2021-11-23 00:21:37 [scrapy.utils.log] INFO: Versions: lxml 4.6.4.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 21.7.0, Python 3.9.5 (default, May 11 2021, 08:20:37) - [GCC 10.3.0], pyOpenSSL 21.0.0 (OpenSSL 1.1.1j  16 Feb 2021), cryptography 3.3.2, Platform Linux-5.11.0-40-generic-x86_64-with-glibc2.33                                            
2021-11-23 00:21:37 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.epollreactor.EPollReactor
2021-11-23 00:21:37 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'tokopedia',      
 'NEWSPIDER_MODULE': 'tokopedia.spiders',                        
 'ROBOTSTXT_OBEY': True,                                                                                                                                                                                                                                                                                     
 'SPIDER_MODULES': ['tokopedia.spiders'],                                                                                                
 'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 '
               'Safari/537.36'}                                                                               
2021-11-23 00:21:37 [scrapy.extensions.telnet] INFO: Telnet Password: d97f9f524843455e
2021-11-23 00:21:37 [scrapy.middleware] INFO: Enabled extensions:                                             
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2021-11-23 00:21:37 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2021-11-23 00:21:37 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2021-11-23 00:21:37 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2021-11-23 00:21:37 [scrapy.core.engine] INFO: Spider opened
2021-11-23 00:21:37 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2021-11-23 00:21:37 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2021-11-23 00:21:37 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.tokopedia.com/robots.txt> (referer: None)
2021-11-23 00:21:41 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1> (referer: None)
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
```
4. Check the log to see the scraping process.
```bash
{'product_name': 'Xiaomi - Redmi Note 10s Varian Kapasitas 6GB/64GB dan 8GB/128GB -Resmi', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp2.672.500', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Milano Cell ITC Kuningan'}
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
{'product_name': 'hp samsung e1272 termurah original jadul samsung lipat dual sim', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp152.100', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Little Master.shop'}
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
{'product_name': 'HP Nokia 105 DS 4MB/4MB Handphone Dual SIM', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp123.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'sodo shop'}
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
{'product_name': 'hp nokia 1280 fullset murah garansi tam jadul nokia single sim', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp92.100', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Mike Net'}
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
{'product_name': 'Hp 981y Extra high Balack', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp1.450.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/6d3a4c5b.svg', 'merchant_name': 'mlatifjaya'}
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
{'product_name': 'Xiaomi Official Redmi 9A 2/32GB 6.53" HD Mi Smartphone AI Face Unlock', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp1.299.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Xiaomi Official Store'}
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
{'product_name': 'Xiaomi Redmi Note 9 6/128 GB Garansi Resmi', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp2.443.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Gudang-HP'}
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
{'product_name': 'NOKIA 105 KING 2019 GARANSI RESMI TAM', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp230.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Garden Cell Official'}
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
{'product_name': 'Xiaomi Redmi Note 10 Pro 8/128GB NFC 6.67" 108MP 5020mAh Smart HP', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp3.899.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Xiaomi Official Store'}
2021-11-23 00:21:41 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1>
{'product_name': 'Nokia 105 King (2019) Garansi Resmi TAM', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp226.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'LJS OFFICIAL'}
2021-11-23 00:21:43 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2> (referer: https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=1)
2021-11-23 00:21:43 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2>
{'product_name': 'Infinix Hot 10 Play 4GB/64GB Garansi Resmi', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp1.533.900', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Vhe Shop jkt'}
2021-11-23 00:21:43 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2>
{'product_name': 'Vivo V21 4G 8/128GB / 8/256GB Garansi Resmi Vivo Indonesia', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp3.750.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Blossom Phone'}
2021-11-23 00:21:43 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2>
{'product_name': 'iPhone 11 64Gb Second Original Mulus No Minus', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp6.950.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Matahari Store Online'}
2021-11-23 00:21:43 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2>
{'product_name': 'Iphone 7 Second / Bekas 32 - 128 Original 100%', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp1.930.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'NET Store168'}
2021-11-23 00:21:43 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2>
{'product_name': 'Handphone Samsung S20 FE 8/128 8/256 GB RAM 8 ROM 128 256GB HP Garansi', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp7.500.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'artic'}
2021-11-23 00:21:43 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2>
{'product_name': 'Nokia 105 – Blue', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp260.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Nokia Mobile Official'}
2021-11-23 00:21:43 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2>
{'product_name': 'OPPO A3S RAM 2/16 GARANSI RESMI OPPO INDONESIA 1TH', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp1.449.900', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': '189 CELL'}
2021-11-23 00:21:43 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2>
{'product_name': 'Iphone XR 64gb Bekas Fullset', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp5.050.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Boboy Store'}
2021-11-23 00:21:43 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.tokopedia.com/p/handphone-tablet/handphone?ob=5&page=2>
{'product_name': '(IBOX) iPhone XR 64GB 128GB 256GB Garansi Resmi TAM 1 Tahun 64 128 256', 'product_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAQAAACTbf5ZAAAAiklEQVR42u3PMQEAAAwCoNm/9Cr4Cw3IjYmwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsHDrASUpAHnJhbktAAAAAElFTkSuQmCC', 'product_price': 'Rp8.999.000', 'product_rating': 'https://assets.tokopedia.net/assets-tokopedia-lite/v2/zeus/kratos/4fede911.svg', 'merchant_name': 'Putra Group'}
```
