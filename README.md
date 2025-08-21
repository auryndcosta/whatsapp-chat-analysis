WhatsApp Chat Analyzer

A Streamlit-based web application that analyzes WhatsApp chat exports and provides insights like:

-> Chat activity by time, day, and month

-> Most active users

-> Media, links, and emoji usage

-> Most common words & wordcloud


Features

-> Upload your WhatsApp chat .txt file
-> Clean preprocessing (removes system/media messages)
-> User-level and group-level analysis
-> Sentiment Analysis (Positive / Negative / Neutral)
-> WordCloud & Top Words Visualization
-> Emoji usage analysis
-> Activity heatmaps

Installation
1. Clone the Repository
git clone https://github.com/auryndcosta/whatsapp-chat-analysis.git
cd whatsapp-chat-analysis

2. Create Virtual Environment 
python -m venv venv
venv\Scripts\activate   

3. Install Requirements
pip install -r requirements.txt

Run the App
streamlit run app.py


Then open the link in your browser (usually http://localhost:8501/).

📂 Project Structure
whatsapp-chat-analysis/
│── app.py                # Main Streamlit app
│── helper.py             # Functions for stats & visualizations
│── preprocessor.py       # Chat preprocessing & cleaning
│── stop_hinglish.txt     # Custom stopwords for wordcloud
│── sentiment_model.pkl   # Trained ML model for sentiment
│── requirements.txt      # Project dependencies
│── README.md             # Project documentation

Example Insights

Most Active Users → Who texts the most

Sentiment Trends → How positive/negative the chat is

WordCloud → Commonly used words

Emoji Analysis → Favorite emojis per user

Activity Heatmap → Chat frequency by hour/day

Future Improvements

Deep Learning sentiment model (BERT)

Support for multiple languages

Export insights as PDF report
