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

For the LLM inference API, I utilized the merged document according to years and long text summarization model of transformers on hugging face to generate summaries. 

Due to lack of time, I wasnt able to analyze and devise strategies to generate visualization using the summarized data but,
### I have a potential approach in mind which I am sharing:
- The summarized data is passed through another LLM model trained on QA answering.
- Question based on inputs that a user might find insightful regarding a company's profile in the last 10 years can be collected and then fed into the pretrained model which is fed the summarized data.
- The answers to the questions contains tables and other metric that can be visualized using bar graphs, plots and charts which can then be fed into PowerBi to generate the visualizations.

## Task 2
For Task 2, I employed Flask, HTML, CSS and Javascript to create a web app which can take in input and generate visualization but I was not able to resolve certain errors due to time constraints. 

