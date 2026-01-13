from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        return render_template('index.html', message=f"Welcome, {username}!")
    else:
        return render_template('result.html', message="ログインに失敗しました。ユーザー名とパスワードをご確認ください。")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ユーザーが既に存在しないかチェック
        if username in users:
            return render_template('result.html', message="ユーザー名は既に存在します。別のユーザー名をお選びください。")

        # 新しいユーザーを登録
        users[username] = password
        return render_template('result.html', message="登録が完了しました！ログインできます。")

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)




