```markdown
# News Analysis Automation

A comprehensive project for automating news article analysis, integrating web scraping, entity extraction, sentiment analysis, and MongoDB for data storage. The project is containerized using Docker and provides an intuitive interface with Streamlit.


## Features
- 🌐 Web Scraping: Extracts article content using `news_scraper.py` with BeautifulSoup.
- 🧠 Named Entity Recognition (NER): Extracts entities using spaCy.
- 😊 Sentiment Analysis: Categorizes sentiments using VADER.
- 🗂️ Database Storage: Saves processed data in MongoDB with `dbstore.py`.
- 📊 Interactive Dashboard: User-friendly Streamlit interface.
- 🐳 Containerized Setup: Dockerized for easy deployment.


## Installation

### Prerequisites
- Python 3.9+
- Docker and Docker Compose

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Vinay45454/News_Analysis_Project
   cd News_Analysis_Project
   ```
2. Add a `.env` file with MongoDB credentials (if required).
3. Build and start Docker containers:
   ```bash
   docker-compose up --build
   ```
4. Access the Streamlit interface at:
   ```
   http://localhost:8501
   ```

---

## Directory Structure
```
📁 Project Root
├── .env                     # Environment variables
├── Data Science Project Assessment.pdf  # Project brief
├── dbstore.py               # MongoDB storage logic
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Dockerfile for app containerization
├── entity_extraction.py     # Entity extraction using spaCy
├── news_analysis_report.docx  # Detailed project report
├── news_scraper.py          # Scrapes articles from URLs
├── requirements.txt         # Python dependencies
├── sentiment_analysis.py    # Sentiment analysis with VADER
```

---

## Usage
1. Input: 
   - Enter a URL or paste article text into the Streamlit interface.
2. Processing:
   - `news_scraper.py`: Scrapes and cleans HTML content.
   - `entity_extraction.py`: Identifies entities (names, locations, etc.).
   - `sentiment_analysis.py`: Performs sentiment analysis.
   - `dbstore.py`: Saves processed data in MongoDB.
3. Output: 
   - Visualized results in the interface.
   - Data saved for future analysis.

---

## Technologies Used
- Python Libraries: 
  - `spaCy`, `vaderSentiment`, `BeautifulSoup`, `pymongo`, `streamlit`
- MongoDB: For persistent storage.
- Docker: For containerized deployment.
- Streamlit: For creating an interactive dashboard.

---

## Future Improvements
- 🔍 Advanced NLP Models: Use transformer models like BERT for improved accuracy.
- ⏳ Dynamic Content Handling: Integrate Selenium for JavaScript-heavy websites.
- 📈 Feedback Loop: Regularly refine NLP accuracy based on user feedback.

---


## Contact
- Name: Vinay Tiwari
- Email: tiwarivinay9310@gmail.com  
```  
