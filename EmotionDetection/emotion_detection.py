import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    # Task 3: Mengubah teks response menjadi dictionary
    formatted_response = json.loads(response.text)
    
    # Mengekstrak set emosi yang diminta
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Logika untuk mencari emosi dominan (skor tertinggi)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Menyusun output sesuai format yang diminta
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return result