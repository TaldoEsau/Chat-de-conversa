from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# Armazenar mensagens em memória (não é persistente)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send_message():
    username = request.form['username']
    message = request.form['message']
    messages.append(f"{username}: {message}")
    return redirect('/')

@app.route('/fetch_messages', methods=['GET'])
def fetch_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
