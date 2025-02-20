from flask import Flask, render_template, request, jsonify, redirect, url_for
import openai

app = Flask(__name__)

# OpenAI API anahtarınızı buraya ekleyin
openai.api_key = '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'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    # Kullanıcıdan gelen sorguyu al
    destination_query = request.form.get('query')
    
    # OpenAI API'ye GPT-4 çağrısı yap
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful travel assistant."},
            {"role": "user", "content": f"Find budget-friendly travel deals for: {destination_query}"}
        ]
    )

    # Yanıtı al ve metin olarak işleyin
    result_text = response.choices[0].message['content'].strip()

    # Basit bir örnek liste oluşturun
    # Bu liste yerine OpenAI'den gelen yanıtı işleyerek dinamik içerik oluşturabilirsiniz
    deals = [{"hotel_name": "Sample Hotel", "location": "Sample Location", "price": "100 USD/night", "rating": "4.5"}]

    # result_text'i doğrudan göstermek isterseniz, `deals` yerine bir metin olarak render edebilirsiniz
    return render_template('result.html', deals=deals)

if __name__ == '__main__':
    app.run(debug=True)
