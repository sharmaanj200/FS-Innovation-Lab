from flask import Flask, jsonify
import yfinance as yf
from sec_edgar_downloader import Downloader
import os
from llama_index.core import download_loader

app = Flask(__name__)

@app.route('/download_10k')
def download_10k():
    ticker = "TSLA"  # Set the ticker directly in the code
    stock = yf.Ticker(ticker)
    try:
        company_name = stock.info['longName']
        company_email_address = f"xyz{company_name.replace(' ', '')}@example.com"

        # Set the download path (example: use your specific directory path)
        download_path = ""

        # Initialize the downloader with the specified path
        dl = Downloader(company_name, company_email_address)

        # Initialize the UnstructuredReader
        UnstructuredReader = download_loader("UnstructuredReader", refresh_cache=True, use_gpt_index_import=True)

        loader = UnstructuredReader()
        years = range(1995, 2024)
        all_docs = []
        doc_set = {}

        for year in years:
            # Download 10-K filings for the specific year
            dl.get("10-K", ticker, after=f"{year}-01-01", before=f"{year}-12-31")

            # Path where downloaded files are stored
            files_path = f"{download_path}/{ticker}/10-K/{year}"

            # Use Unstructured to load data
            year_docs = loader.load_data(filepath=f"{files_path}/*.html", split_documents=False)
            for d in year_docs:
                d.extra_info = {"year": year}
            doc_set[year] = year_docs
            all_docs.extend(year_docs)

        # save to a single text file
        with open(f"{download_path}/{ticker}_10-K_texts.txt", 'w', encoding='utf-8') as outfile:
            for doc in all_docs:
                outfile.write(f"Year {doc.extra_info['year']}:\n{doc.text}\n\n")

        response = {
            "Message": "Succeeded in downloading 10-K filings.",
            "CompanyName": company_name,
            "CompanyEmail": company_email_address
        }

    except Exception as e:
        response = {
        "Error": str(e)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
