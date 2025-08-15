import streamlit as st
import google.generativeai as genai
from newspaper import Article
import json

# --- Page Configuration ---
st.set_page_config(page_title="News Analyzer", page_icon="📰", layout="centered")

# --- API Configuration and Model Loading ---
@st.cache_resource
def load_model():
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
        return model
    except Exception as e:
        st.error(f"Error configuring Gemini API: {e}")
        return None

model = load_model()

# --- Functions ---
def get_article_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception:
        return None

def analyze_text_with_gemini(text_to_analyze, tone_choice):
    if not model:
        return {"error": "Gemini model not loaded."}
    
    prompt = f"""
    Analyze the following text: "{text_to_analyze}"
    Perform two tasks:
    1.  Summarization: Create a summary based on this tone: '{tone_choice}'.
    2.  Sentiment Analysis: Analyze the overall tone (POSITIVE, NEGATIVE, or NEUTRAL).
    Return a single JSON object with "summary" and "sentiment" keys. 
    The sentiment value must be an object with "label" and "score" keys.
    """
    try:
        response = model.generate_content(prompt)
        cleaned_response = response.text.strip().replace("```json", "").replace("```", "")
        return json.loads(cleaned_response)
    except Exception as e:
        return {"error": f"Error from API: {e}"}

# --- App Layout ---
st.title("📰 News Summarizer & Bias Detector")

tab1, tab2 = st.tabs(["Analyze by URL", "Analyze by Pasted Text"])
with tab1:
    url_input = st.text_input("Enter a news article URL:")
with tab2:
    text_input = st.text_area("Paste the full article text here:", height=250)

summary_choice = st.selectbox(
    "Choose a summary tone:",
    ("Neutral Summary", "Fact-Only Summary", "Explain to a 10-Year-Old")
)

if st.button("Analyze Article"):
    article_to_process = ""
    if url_input:
        with st.spinner("Fetching article..."):
            article_to_process = get_article_from_url(url_input)
            if not article_to_process:
                st.error("Failed to fetch article from URL.")
    elif text_input:
        article_to_process = text_input
    else:
        st.warning("Please provide a URL or text to analyze.")

    if article_to_process:
        with st.spinner("Gemini is analyzing..."):
            result = analyze_text_with_gemini(article_to_process, summary_choice)

            if "error" in result:
                st.error(result["error"])
            else:
                st.subheader("Summary")
                st.write(result.get("summary", "No summary provided."))

                st.subheader("Bias & Tone Analysis")
                sentiment = result.get("sentiment", {})
                label = sentiment.get('label', 'UNKNOWN')
                score = sentiment.get('score', 0.0)
                
                if label == 'NEUTRAL' and score == 0.0:
                    score = 1.0
                
                st.write(f"Detected Tone: **{label}** (Confidence: {score*100:.2f}%)")