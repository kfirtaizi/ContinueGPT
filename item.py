from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import openai

openai.api_key = ''

app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['POST'])
@cross_origin()
def my_api():
    data = request.get_json()
    prompt = data['prompt']

    messages = [
        {"role": "system",
         "content": "You're an helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1024,
    )

    print(response.choices[0]["message"]["content"])
    return jsonify(response.choices[0]["message"]["content"])


if __name__ == '__main__':
    app.run(port=5000)
