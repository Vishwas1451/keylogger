from flask import *
app = Flask(__name__)

users = {'alice':'alicepass','bob':'bobpass','daniel':'danpass','admin':'adminpass'}
logged_in = False
user = None

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    global user, logged_in
    error = ''
    if request.method == 'POST':
        if request.form['username'] not in users.keys():
            error = 'Invalid User'
        elif request.form['password'] != users[request.form['username']]:
            error = 'Invalid Password'
        else:
            logged_in = True
            user = request.form['username']
            return redirect(url_for('success'))
    return render_template('login.html',error=error)

@app.route('/success', methods=['GET'])
def success():
    global user
    if logged_in:
        return render_template('success.html',user=user)
    else:
        return redirect(url_for('login'))

@app.route('/admin', methods=['GET'])
def admin():
    return 'You found the ADMIN page!'

@app.route('/robots.txt', methods=['GET'])
def robots():
    return render_template('robots.txt')

@app.route('/js/',methods=['GET'])
def js():
    return render_template('js.js')
