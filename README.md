# 🤖 AI Resume Parser & Job Matcher

Automatically parse your resume and match it with the best job listings using AI!

## ✨ Features
- PDF resume se skills auto-extract karta hai
- Job listings se match score calculate karta hai
- Data Scientist roles ke liye optimized
- Groq LLM API use karta hai (Free!)

## 🛠️ Tech Stack
- Python 3.8+
- Groq API (LLaMA3-8b)
- PyMuPDF (PDF parsing)
- Scikit-learn (Cosine Similarity)
- BeautifulSoup4 (Job scraping)

## 📊 How It Works
1. Resume PDF upload karo
2. AI skills aur experience extract karta hai
3. Job listings se match score calculate hota hai
4. Top matching jobs show hoti hain with % score

## 🚀 How to Run

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Add your Groq API key in .env file
```
GROQ_API_KEY=your_key_here
```

### 3. Run the parser
```
python resume_parser/parser.py
```

### 4. Run the job matcher
```
python job_matcher/matcher.py
```

## 📁 Project Structure
```
AI-Resume-Parser-Job-Matcher/
├── resume_parser/
│   └── parser.py        # PDF parse + AI skill extraction
├── job_matcher/
│   └── matcher.py       # Job fit score calculator
├── requirements.txt
├── .env.example
└── README.md
```

## 👤 Author
**Ashish Singh**  
LinkedIn: [linkedin.com/in/ashish-singh-17704b356](https://linkedin.com/in/ashish-singh-17704b356)

## 📈 Results
- Resume parsing accuracy: 95%+
- Cosine similarity based job matching
- Supports any PDF resume format
