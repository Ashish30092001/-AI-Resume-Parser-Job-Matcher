import fitz  # PyMuPDF
import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(path):
    """PDF se raw text nikalo"""
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_resume_with_ai(resume_text):
    """Groq AI se resume parse karo"""
    prompt = f"""
    Extract information from this resume and return ONLY valid JSON.
    No markdown, no explanation, just JSON.
    
    Keys required:
    - name (string)
    - email (string)
    - phone (string)
    - skills (array of strings, max 15)
    - experience_years (number)
    - education (string)
    - job_titles (array of past roles)
    - summary (2 sentence professional summary)
    
    Resume:
    {resume_text[:3000]}
    """
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a resume parser. Return only valid JSON."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800
    )
    
    raw = response.choices[0].message.content
    clean = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(clean)

def get_profile(resume_path=None):
    """Main function — resume parse karo"""
    path = resume_path or os.getenv("RESUME_PATH", "resume.pdf")
    
    print(f"📄 Resume padh raha hoon: {path}")
    text = extract_text_from_pdf(path)
    
    print("🤖 AI profile extract kar raha hai...")
    profile = parse_resume_with_ai(text)
    
    print(f"\n✅ Profile ready!")
    print(f"   Name     : {profile.get('name', 'N/A')}")
    print(f"   Skills   : {', '.join(profile.get('skills', [])[:5])}...")
    print(f"   Exp      : {profile.get('experience_years', 0)} years")
    
    return profile, text

if __name__ == "__main__":
    profile, text = get_profile()
    print("\n📊 Full Profile:")
    print(json.dumps(profile, indent=2))
