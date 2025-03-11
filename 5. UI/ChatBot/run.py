import requests
import json
from sentence_transformers import SentenceTransformer

# Endpoint configurations
COMPLETION_URL = "http://localhost:8080/completion"
VECTOR_SEARCH_URL = "http://127.0.0.1:6333/collections/sierra_db/points/search"
QA_URL_BASE = "http://127.0.0.1:6333/collections/sierra_db/points"

def search_similar_vectors(query, encoder, limit=2):
    """
    Encodes the query and searches for similar vectors.
    """
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({
        "vector": encoder.encode(query).tolist(), 
        "limit": limit
    })
    response = requests.post(VECTOR_SEARCH_URL, headers=headers, data=payload)
    response.raise_for_status()
    return response.json().get("result", [])

def get_question_answer(record_id):
    """
    Retrieves the question and answer of a given record.
    """
    url = f"{QA_URL_BASE}/{record_id}"
    response = requests.get(url, headers={"Content-Type": "application/json"})
    response.raise_for_status()
    result = response.json().get("result", {})
    payload = result.get("payload", {})
    question = payload.get("question", "")
    answer = payload.get("answer", "")
    return question, answer

def construct_prompt(context_data, user_query):
    """
    Constructs the prompt using the context and the user's question.
    """
    context_str = ""
    if context_data:
        context_str = "- ".join([f"Q: {q} - A: {a} |" for q, a in context_data])
        
    return f"""
    You are an educational assistant. Use the provided context and your reasoning to answer accurately and concisely.  
    If the context is incomplete, use only your reasoning.  

    ## Context:
    {context_str}

    ## User Question:
    {user_query}

    ## Instructions:
    1. Use the context and your knowledge to generate an accurate response.
    2. If context is insufficient, use only your knowledge.
    3. Provide a clear and simple answer.
    """

def generate_response(query, length=512):
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    
    try:
        points = search_similar_vectors(query, encoder, limit=2)
    except Exception as e:
        return f"Error during vector search: {e}", 0

    context_data = []
    for point in points:
        record_id = point.get("id")
        if record_id is not None:
            try:
                q, a = get_question_answer(record_id)
                context_data.append((q, a))
            except Exception:
                # Optionally log the error
                continue

    prompt = construct_prompt(context_data, query)
    message = {
        "prompt": prompt,
        "n_predict": length,
    }
    
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(COMPLETION_URL, headers=headers, json=message)
        response.raise_for_status()
        answer_data = response.json()
    except Exception as e:
        return f"Error during completion request: {e}", int(bool(context_data))
    
    content = answer_data.get("content")
    if content:
        return content, int(bool(context_data))
    else:
        return "No content found in the response.", int(bool(context_data))