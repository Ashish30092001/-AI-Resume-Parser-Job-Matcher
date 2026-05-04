import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from resume_parser.parser import get_profile

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

SAMPLE_JOBS = [
    {"title": "Data Scientist", "company": "Flipkart", "desc": "Python ML models A/B testing SQL pipelines statistics pandas numpy", "url": "https://naukri.com"},
    {"title": "Data Scientist", "company": "Zomato", "desc": "Statistical modeling Python experimentation product analytics machine learning", "url": "https://naukri.com"},
    {"title": "ML Engineer", "company": "Swiggy", "desc": "TensorFlow PyTorch recommendation systems deep learning Python scikit-learn", "url": "https://naukri.com"},
    {"title": "Data Scientist", "company": "Paytm", "desc": "Python SQL data analysis business intelligence dashboards visualization", "url": "https://naukri.com"},
    {"title": "Data Analyst", "company": "CRED", "desc": "SQL Python analytics dashboards Excel data visualization reporting", "url": "https://naukri.com"},
    {"title": "ML Scientist", "company": "Ola", "desc": "Machine learning Python real-time analytics predictive modeling SQL", "url": "https://naukri.com"},
    {"title": "Data Scientist", "company": "PhonePe", "desc": "LLMs Python MLOps model deployment FastAPI data science", "url": "https://naukri.com"},
    {"title": "AI Engineer", "company": "Razorpay", "desc": "LLM prompt engineering Python AI automation NLP generative AI", "url": "https://naukri.com"},
]

def score_fit(profile, job):
    """Resume aur job ke beech fit score calculate karo"""
    profile_text = " ".join(profile.get("skills", [])) + " " + \
                   " ".join(profile.get("job_titles", [])) + " " + \
                   profile.get("summary", "")
    
    job_text = job["title"] + " " + job["desc"]
    
    try:
        vectorizer = TfidfVectorizer()
        tfidf = vectorizer.fit_transform([profile_text, job_text])
        score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100
        return round(score, 1)
    except:
        return 0

def match_jobs(profile, jobs, min_score=60):
    """Jobs ko score karke filter karo"""
    scored = []
    for job in jobs:
        score = score_fit(profile, job)
        if score >= min_score:
            scored.append({**job, "fit_score": score})
    
    scored.sort(key=lambda x: x["fit_score"], reverse=True)
    return scored

def run_matcher():
    print("=" * 50)
    print("   🎯 AI Job Matcher — Ashish Singh")
    print("=" * 50)
    
    # Resume parse karo
    profile, _ = get_profile()
    
    print(f"\n🔍 {len(SAMPLE_JOBS)} jobs check kar raha hoon...")
    matched = match_jobs(profile, SAMPLE_JOBS, min_score=50)
    
    print(f"\n✅ {len(matched)} jobs match hui!\n")
    print("-" * 50)
    
    for job in matched:
        bar = "█" * int(job["fit_score"] / 5) + "░" * (20 - int(job["fit_score"] / 5))
        print(f"🏢 {job['company']:15} | {job['title']:20} | {bar} {job['fit_score']}%")
    
    print("-" * 50)
    print(f"\n🏆 Best match: {matched[0]['company']} — {matched[0]['title']} ({matched[0]['fit_score']}%)")

if __name__ == "__main__":
    run_matcher()
