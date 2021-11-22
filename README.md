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
1. Change directory to project root folder.
> Notes: You can use 'tree' command line tools
> ```bash
> $ tree
> ```
> ```bash
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
