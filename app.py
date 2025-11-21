from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/myproducts')
def getproducts():

    response = requests.get('https://fakestoreapi.com/products')
    return render_template('base.html', api = response.json())


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog_home')
def blog_home():
    return render_template('blog_home.html')

@app.route('/blog_post')
def blog_post():
    return render_template('blog_post.html')

@app.route('/portfolio_overview')
def portfolio_overview():
    return render_template('portfolio_overview.html')

@app.route('/portfolio_item')
def portfolio_item():
    return render_template('portfolio_item.html')

if __name__ == '__main__':
    app.run(debug=True)