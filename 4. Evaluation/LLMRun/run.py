import json
import requests
from sentence_transformers import SentenceTransformer
from transformers import pipeline

COMPLETION_URL = "http://localhost:8080/completion"

def fetch_context(query, encoder, points_url, qa_url, limit, score_threshold=0.0):
    payload = json.dumps({
        "vector": encoder.encode(query).tolist(),
        "limit": limit
    })
    headers = {"Content-Type": "application/json"}
    response = requests.post(points_url, headers=headers, data=payload)
    results = response.json().get("result", [])
    questions, answers = [], []
    for item in results:
        if score_threshold and item.get("score", 0) <= score_threshold:
            continue
        qa_response = requests.get(f"{qa_url}/{item['id']}")
        payload_data = qa_response.json().get("result", {}).get("payload", {})
        questions.append(payload_data.get("question", ""))
        answers.append(payload_data.get("answer", ""))
    return questions, answers

def build_prompt(query, questions=None, answers=None):
    if questions and answers:
        context = "- ".join([f"Q: {q} - A: {a} |" for q, a in zip(questions, answers)])
        prompt = f"""
        You are a highly optimized assistant, designed to answer questions precisely and concisely. 
        Use the provided context to craft accurate responses. 
        If the context does not contain enough information, politely indicate that more data is needed.

        ## Input Context:
        {context}

        ## User Question:
        {query}

        ## Your Task:
        1. Combine the input context with your general knowledge to generate an accurate and relevant answer.
        2. If the context is incomplete or insufficient, explain what additional information is required to provide a precise response.
        3. Respond in clear, simple language, focusing on brevity and accuracy.
        """
    else:
        prompt = f"""
        You are a highly optimized assistant, designed to answer questions precisely and concisely.

        ## User Question:
        {query}
        
        ## Your Task:
        1. Use your general knowledge to generate an accurate and relevant answer.
        2. Respond in clear, simple language, focusing on brevity and accuracy.
        """
    return prompt

def call_completion(prompt, n_predict=128, extra_params=None):
    headers = {"Content-Type": "application/json"}
    message = {"prompt": prompt, "n_predict": n_predict}
    if extra_params:
        message.update(extra_params)
    return requests.post(COMPLETION_URL, headers=headers, json=message).json()

def clear_input(prompt):
    prompt = " ".join(prompt.split())
    # Standardize quotes and apostrophes
    prompt = prompt.replace("“", '"').replace("”", '"')
    prompt = prompt.replace("‘", "'").replace("’", "'")
    
    pipe = pipeline("summarization", model="google/pegasus-xsum")
    input_tokens = len(pipe.tokenizer.tokenize(prompt))
    if input_tokens > 512:
        summary = pipe(prompt, min_length=5, max_length=512, do_sample=False)[0]['summary_text']
    else:
        summary = prompt
    return summary

def generate_response(query, run_function, rag_ip):
    points_url = f"http://{rag_ip}:6333/collections/sierra_db_4o_mini/points/search"
    qa_url = f"http://{rag_ip}:6333/collections/sierra_db_4o_mini/points"
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    
    if run_function in ["classic", "classic_stream"]:
        extra_params = {"stream": True} if run_function == "classic_stream" else {}
        result = call_completion(query, n_predict=128, extra_params=extra_params)
        return result.get("content", "No content found in the response.")
    
    elif run_function in ["rag_sierra_5", "rag_sierra_2"]:
        limit = 5 if run_function == "rag_sierra_5" else 2
        questions, answers = fetch_context(query, encoder, points_url, qa_url, limit)
        prompt = build_prompt(query, questions, answers)
        result = call_completion(prompt, n_predict=128)
        content = result.get("content", "No content found in the response.")
        return content, questions, answers
    
    elif run_function == "custom":
        questions, answers = fetch_context(query, encoder, points_url, qa_url, limit=3, score_threshold=0.65)
        prompt = build_prompt(query, questions, answers) if questions else build_prompt(query)
        prompt = clear_input(prompt)
        result = call_completion(prompt, n_predict=512)
        content = result.get("content", "No content found in the response.")
        return content, questions, answers
    
    else:
        raise ValueError(f"Unknown run_function: {run_function}")
