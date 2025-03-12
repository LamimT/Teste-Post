from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    if 'login' in data and 'senha' in data:
        login = data['login']
        senha = data['senha']
        
        return jsonify({'login': login, 'senha': senha}), 200
    else:

        return jsonify({'error': 'Dados de login e senha são necessários'}), 400

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)

