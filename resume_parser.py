import PyPDF2

def extract_resume_text(file):
    """
    Extracts text from a PDF file.
    """
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(resume_text):
    """
    Provides feedback on the resume.
    """
    # Basic analysis (expandable with LLM)
    feedback = {
        "word_count": len(resume_text.split()),
        "suggestions": [
            "Add more quantifiable achievements.",
            "Use action verbs for job descriptions.",
            "Ensure consistent formatting."
        ],
    }
    return feedback
