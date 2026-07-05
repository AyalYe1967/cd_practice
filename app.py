from flask import Flask

# יצירת האובייקט של האפליקציה
app = Flask(__name__)

# הגדרת נתיב ברירת המחדל (דף הבית)
@app.route('/')
def home():
    return "Hello, DevOps World! Flask is running."

# הגדרת נתיב דינמי שמקבל שם ומברך את המשתמש
@app.route('/hello/<name>')
def greet(name):
    return f"Hello {name}, welcome to my Flask server!"

# הרצת השרת במצב דיבאג (מתעדכן אוטומטית כשמשנים את הקוד)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
