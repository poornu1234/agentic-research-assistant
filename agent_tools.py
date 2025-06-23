
# import wikipedia
# from transformers import pipeline

# # Initialize summarizer
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def search_wikipedia(topic):
#     try:
#         # Get a long enough summary
#         summary = wikipedia.summary(topic, sentences=10)
#         return summary
#     except Exception as e:
#         return f"No Wikipedia info found for '{topic}'. Error: {str(e)}"

# def generate_report(topic):
#     # Step 1: Search
#     source_info = search_wikipedia(topic)

#     # Step 2: Summarize (limit input size)
#     input_text = source_info[:1024]
#     summary = summarizer(input_text, max_length=200, min_length=60, do_sample=False)[0]['summary_text']

#     # Step 3: Format report
#     report = f"""
# 📌 Research Report: {topic}

# Introduction:
# {summary}

# Key Points:
# - {summary.split('.')[0]}.
# - {summary.split('.')[1]}.
# - {summary.split('.')[2]}.

# Conclusion:
# This report summarizes key aspects of {topic} based on available sources.
# """
#     return report
import wikipedia
from transformers import pipeline
from datetime import date

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def search_wikipedia(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        summary = page.summary
        url = page.url
        categories = page.categories
        return summary, url, categories
    except Exception as e:
        return f"No Wikipedia info found for '{topic}'. Error: {str(e)}", "", []

def generate_report(topic):
    source_info, url, categories = search_wikipedia(topic)

    input_text = source_info[:1024]
    summary = summarizer(input_text, max_length=200, min_length=60, do_sample=False)[0]['summary_text']

    key_points = summary.split('.')[:3]

    citation = f'Wikipedia contributors. "{topic}." Wikipedia, The Free Encyclopedia. Retrieved {date.today()} from {url}.'

    report = f"""
📌 Research Report: {topic}

Introduction:
{summary}

Key Points:
- {key_points[0]}.
- {key_points[1]}.
- {key_points[2]}.

Conclusion:
This report summarizes key aspects of {topic} based on available sources.

Source: {url}
"""

    return {
        "report": report,
        "source_url": url,
        "related_topics": categories[:5],  # First few categories
        "citation": citation,
        "summary_stats": {
            "word_count": len(summary.split()),
            "char_count": len(summary),
            "num_key_points": len(key_points),
            "retrieved_on": str(date.today())
        }
    }
