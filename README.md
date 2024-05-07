# FS-Innovation-Lab
This is the programming task for summer research position at the FS innovation Lab, Georgia Institute of Technology

## Task 1.1
1. Utilized the sec-edgar-downloader package in python for extracting the 10-k filings.
2. Extracted the name of the company using the yfinance package in python and company ticker, for generating sample email address for the downloader. (for example: xyz@company_name.com)

## Task 1.2
1. Extracted the CIK numbers and file paths for the downloaded 10k filings
2. The data was in different formats due to which it had to be parsed before merging.
3. The HTML and XGBR format in the text file containing 10K filings was parsed using - BeautifulSoup.
4. Parsing XGBR was very challenging and required a lot of reading up and trial and errors. It is still not perfect but I am working on improving it.

