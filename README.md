# 🛍️ Etsy Digital Product Scraper & Analysis

This project is a **Web Scraping and Data Analysis pipeline** built with Python. It collects product data from Etsy based on specific keywords (e.g., "Digital Planner") and generates insights from the scraped dataset, including keyword frequency analysis and a professional PDF report.

## 📌 Features

- Automated data extraction using **Selenium + undetected-chromedriver**
- Manual CAPTCHA solving support
- Clean dataset saved as CSV
- Analysis of product titles and keywords
- Word frequency chart generation using matplotlib
- Automatic PDF report generation

## 📁 Project Structure

.
├── data/
│ └── etsy_data.csv # Raw data file
├── reports/
│ └── etsy_keywords_report.pdf # Generated PDF report
├── notebooks/
│ └── analysis.ipynb # Colab notebook for analysis and report generation
├── scraper.py # Web scraping script (Selenium)
├── requirements.txt # Python dependencies
└── README.md # This file


## 📊 Sample Output

![word-frequency](reports/sample_wordcloud.png)

## 🛠️ Technologies Used

- Python 3.x
- Selenium + undetected_chromedriver
- BeautifulSoup (optional)
- pandas
- matplotlib
- seaborn
- fpdf / reportlab

## 🧠 Insights

The generated report highlights the most frequent keywords used by top-selling digital products. This helps creators and sellers better understand trending phrases and optimize their product titles and SEO on Etsy.

## 🚀 How to Run

```bash
pip install -r requirements.txt
python scraper.py

