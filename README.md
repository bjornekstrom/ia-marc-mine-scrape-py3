# ia-marc-mine-scrape

Python scripts for mining bibliographic data in MARC format from the [Internet Archive](https://archive.org/) and scraping a chosen field and indicator.

As presented in the lecture at [Programming Historian](https://programminghistorian.org/lessons/data-mining-the-internet-archive), modified to work with Python 3.

## Prerequisites

Install the following prerequisites using the terminal or command prompt.

### pip

`curl -O https://bootstrap.pypa.io/get-pip.py`

`python3 get-pip.py`

### internetarchive

`pip3 install internetarchive`

### pymarc

`pip3 install pymarc`

## Usage

### Authentication

1. After installing `internetarchive` and `pymarc`, run `ia-configure` in a Terminal window to login with your Internet Archive credentials.

### Mining

2. In mine.py, add the collection name after `collection:` at line 8.
3. Run program: `python3 mine.py`. This will download all MARC files within the collection.

### Scraping

4. In scrape.py, add the MARC field in the first [] and MARC indicator in the second [] at line 10.
5. Run program: `python3 scrape.py`. This will scrape the chosen MARC fields and indicators, presenting them in the file `out.txt`

Happy mining and scraping! 👌
