# News-Analyzer-and-Bias-Sentiment app
An interactive web application built with Streamlit and powered by the Google Gemini API to analyze news articles. This tool can generate summaries in different tones and analyze the sentiment of an article from either a URL or pasted text.
# 📰 AI News Summarizer & Bias Detector

An interactive web application built with Streamlit and powered by the Google Gemini API to analyze news articles. This tool can generate summaries in different tones and analyze the sentiment of an article from either a URL or pasted text.

---

## ✨ Features

- **Dual Input:** Analyze articles by providing a direct URL or by pasting the article's full text.
- **Intelligent Scraping:** Automatically extracts the main content from news URLs using the `newspaper3k` library.
- **Customizable Summaries:** Choose from three distinct summary tones:
    - Neutral Summary
    - Fact-Only Summary
    - Explain to a 10-Year-Old
- **Bias & Tone Analysis:** Leverages the Google Gemini API for sentiment analysis, classifying the tone as POSITIVE, NEGATIVE, or NEUTRAL.

---

## 🛠️ Technologies Used

- **Framework:** Streamlit
- **AI Model:** Google Gemini API (`gemini-1.5-flash`)
- **Web Scraping:** Newspaper3k
- **Language:** Python 3

---

## 🚀 How to Run Locally

Follow these steps to run the project on your own machine.

**1. Set Up the Project:**
Clone or download this repository to your local machine.

**2. Install Dependencies:**
Open your terminal in the project folder and run the following command to install the required libraries:
```bash
pip install -r requirements.txt
