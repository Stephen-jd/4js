from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import TaylorFitSubmission, ContactInquiry
import json
import urllib.parse
import urllib.request
import os

def home(request):
    return render(request, 'website/home.html')

def primary(request):
    return render(request, 'website/primary.html')

def secondary(request):
    return render(request, 'website/secondary.html')

def gcse(request):
    return render(request, 'website/gcse.html')

def alevel(request):
    return render(request, 'website/alevel.html')

def entrance_exams(request):
    return render(request, 'website/entrance_exams.html')

def why_us(request):
    return render(request, 'website/why_us.html')

def submit_taylorfit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        exams = ",".join(request.POST.getlist('exams'))
        target_grade = request.POST.get('target_grade')
        guidance = request.POST.get('guidance', '')

        if name and year:
            TaylorFitSubmission.objects.create(
                student_name=name,
                year_group=year,
                target_exams=exams,
                target_grade=target_grade,
                guidance=guidance
            )
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactInquiry.objects.create(
                name=name,
                email=email,
                message=message
            )
            # Redirect to WhatsApp
            wa_text = f"Hello, I have an inquiry from the website.\nName: {name}\nEmail: {email}\nMessage: {message}"
            wa_url = f"https://wa.me/447854885030?text={urllib.parse.quote(wa_text)}"
            return redirect(wa_url)
    return JsonResponse({'status': 'error'}, status=400)

import re
import math
from collections import Counter

def get_cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator: return 0.0
    return float(numerator) / denominator

def text_to_vector(text):
    words = re.compile(r'\w+').findall(text.lower())
    return Counter(words)

def chatbot_query(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            # 1. True RAG Retrieval
            try:
                kb_path = os.path.join(os.path.dirname(__file__), 'knowledge_base.json')
                with open(kb_path, 'r', encoding='utf-8') as f:
                    kb_data = json.load(f)
                
                # Simple Vector Space search (TF)
                user_vec = text_to_vector(user_message.lower())
                scored_kb = []
                for item in kb_data:
                    q_vec = text_to_vector(item['question'].lower())
                    a_vec = text_to_vector(item['answer'].lower())
                    # Match against both question and answer
                    score_q = get_cosine_similarity(user_vec, q_vec)
                    score_a = get_cosine_similarity(user_vec, a_vec)
                    scored_kb.append((max(score_q, score_a), item))
                
                # Sort by score desc and take top 3
                scored_kb.sort(key=lambda x: x[0], reverse=True)
                top_matches = [item for score, item in scored_kb[:3] if score > 0.01]
                
                if top_matches:
                    retrieved_context = "\n".join([f"Q: {m['question']}\nA: {m['answer']}" for m in top_matches])
                else:
                    retrieved_context = "No highly relevant specific information found. Use general knowledge about 4J's Educational Academy (located in Peterborough, PE1 5DD. Phone: +44 7854 885030. Email: 4jseducationalacademy@gmail.com)."
            except Exception as e:
                retrieved_context = "Error loading knowledge base."

            # 2. Call Local Qwen Model via Ollama
            ollama_url = "http://localhost:11434/api/generate"
            prompt = f"You are a helpful, professional assistant for 4J's Educational Academy. Use the following retrieved knowledge to answer the user.\n\nRetrieved Knowledge:\n{retrieved_context}\n\nUser: {user_message}\nAssistant:"
            
            payload = {
                "model": "qwen",
                "prompt": prompt,
                "stream": False
            }
            
            req = urllib.request.Request(ollama_url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
            
            try:
                with urllib.request.urlopen(req, timeout=10) as response:
                    result = json.loads(response.read().decode())
                    bot_reply = result.get('response', "I am currently having trouble connecting to my knowledge base. Please contact us on WhatsApp!")
            except Exception as e:
                bot_reply = "It seems I'm offline at the moment. Please reach out to our team at 4jseducationalacademy@gmail.com or WhatsApp us!"

            return JsonResponse({'reply': bot_reply})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
