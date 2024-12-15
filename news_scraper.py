import requests
from bs4 import BeautifulSoup
import streamlit as st
from entity_extraction import extract_entities
from sentiment_analysis import analyze_sentiment
from dbstore import store_article_data

def fetch_article_content(url: str) -> str:
    """
    Fetches and extracts the main text content of a news article from the given URL.
    """
    try:
        # 1.Data Scraping
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Data Presentation
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1')
        paragraphs = soup.find_all('p')

        # Extract article content
        content = " ".join(para.get_text(strip=True) for para in paragraphs)
        
        if not content:
            return "No content found in the article."

        # 2. Entity Extraction
        entities = extract_entities(content)

        # 3. Sentiment Analysis
        sentiment = analyze_sentiment(content)
        
        # 4. Storage via MongoDB
        store_article_data(url, content, entities, sentiment)

        return (
            f"Title:{title.get_text(strip=True) if title else 'No Title Found'}\n\n"
            f"Content: {content}\n\n"
            f"Extracted Entities: {entities}\n\n"
            f"Sentiment Analysis: {sentiment}"
        )

    except requests.exceptions.RequestException as e:
        return f"❌ **Network Error:** {e}"

    except Exception as e:
        return f"❌ **An Error Occurred:** {e}"


def main():
    st.title("📰 News Article Scraper")
    st.write("Enter the URL of a news article to extract its content, entities, and sentiment.")

    url = st.text_input("News Article URL", placeholder="https://example.com/news-article")

    if st.button("Scrape Article"):
        if url:
            with st.spinner("Scraping the article..."):
                content = fetch_article_content(url)

            st.text_area("Extracted Article Content", content, height=300)
        else:
            st.warning("Please enter a valid URL.")

if __name__ == "__main__":
    main()
