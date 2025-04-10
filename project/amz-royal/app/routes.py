from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    products = [
        {'name': 'Echo Dot', 'price': '$49.99', 'image': 'images/echo.jpg'},
        {'name': 'Fire Tablet', 'price': '$89.99', 'image': 'images/tablet.jpg'},
        {'name': 'Kindle Paperwhite', 'price': '$139.99', 'image': 'images/kindle.jpg'}
    ]
    return render_template('home.html', products=products)

@main.route('/gift-cards')
def gift_cards():
    gift_cards = [
        {'name': 'Amazon Gift Card $25', 'image': 'images/giftcard1.jpg'},
        {'name': 'Amazon Gift Card $50', 'image': 'images/giftcard2.jpg'},
        {'name': 'Amazon Gift Card $100', 'image': 'images/giftcard3.jpg'}
    ]
    return render_template('gift_cards.html', gift_cards=gift_cards)


@main.route('/product-search')
def product_search():
    return render_template('product_search.html')


