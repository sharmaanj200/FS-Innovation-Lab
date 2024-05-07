# FS-Innovation-Lab
This is the programming task for summer research position at the FS innovation Lab, Georgia Institute of Technology.

## Task 1.1
1. Utilized the sec-edgar-downloader package in python for extracting the 10-k filings.
2. Extracted the name of the company using the yfinance package in python and company ticker, for generating sample email address for the downloader. (for example: xyz@company_name.com)

## Task 1.2
1. Extracted the CIK numbers and file paths for the downloaded 10k filings
2. The data was in different formats due to which it had to be parsed before merging.
3. The HTML and XGBR format in the text file containing 10K filings was parsed using - BeautifulSoup.
4. Parsing XGBR was very challenging and required a lot of reading up and trial and errors. It is still not perfect but I am working on improving it.

For the LLM inference API, I utilized the merged document (according to years) and long text summarization model of transformers on hugging face to generate summaries. 

Due to lack of time, I wasnt able to analyze and devise strategies to generate visualization using the summarized data but,
### I have a potential approach in mind which I am sharing:
- The summarized data is passed through another LLM model trained on QA answering.
- Question based on inputs that a user might find insightful regarding a company's profile in the last 10 years can be collected and then fed into the pretrained model which is fed the summarized data.
- The answers to the questions contains tables and other metric that can be visualized using bar graphs, plots and charts which can then be fed into PowerBi to generate the visualizations.

## Task 2
For Task 2, I employed Flask, HTML, CSS and Javascript to create a web app which can take in input and generate visualization but I was not able to resolve certain errors due to time constraints. (Deployment app contains the code for this)

## References
1. https://www.sec.gov/developer
2. https://huggingface.co/docs/transformers/en/index
3. https://medium.com/@jan_5421/how-to-download-and-scrape-10-k-filings-from-sec-edgar-b0d245fc8d48
4. https://pypi.org/project/py-xbrl/
5. https://pypi.org/project/sec-edgar-downloader/
6. https://stackoverflow.com/questions/74225258/downloading-all-10-k-filings-for-sec-edgar-in-python
7. https://sec-api.io/resources/analyzing-sec-edgar-filing-trends-and-patterns-from-1994-to-2022
8. https://sec-api.io/resources/extract-textual-data-from-edgar-10-k-filings-using-python
9. https://financestime.com/understanding-secedgar-extracting-data-structure-explained/
10. https://www.investopedia.com/articles/fundamental-analysis/08/sec-forms.asp
and many more youtube channels, blogs, documentations I have gone through to make this project work

P.S.
I have learnt a lot working on this project. From understanding absolutely nothing about the project to working hard to put this together (even though it is not completed and last part of the task has some errors, I am grateful for this learning opportunity. 

