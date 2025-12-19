from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# サンプルのユーザー情報
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # ユーザー認証
    if username in users and users[username] == password:
        return render_template('index.html', username=username)
    else:
        return render_template('result.html', message="Login failed. Please check your username and password.")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return render_template('result.html', message="Username already exists.")

        users[username] = password
        return render_template('result.html', message="Registration successful!")

    return render_template('register.html')

# --- WebSocket（リアルタイム共有） ---
@socketio.on('send_location')
def handle_location(data):
    # 全クライアントにブロードキャスト
    emit('new_marker', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
