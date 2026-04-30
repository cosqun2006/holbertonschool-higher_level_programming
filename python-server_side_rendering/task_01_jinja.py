from flask import Flask, render_template

app = Flask(__name__)

# Əsas səhifə
@app.route('/')
def home():
    return render_template('index.html')

# Haqqımızda səhifəsi
@app.route('/about')
def about():
    return render_template('about.html')

# Əlaqə səhifəsi
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Tapşırıq xüsusi olaraq 5000-ci portu tələb edir
    app.run(debug=True, port=5000)
