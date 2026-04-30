import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # CSV-dən gələn bütün məlumatlar mətndir, id və price-ı rəqəmə çeviririk
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Mənbə yoxlanışı
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Faylı oxu
    if source == 'json':
        products = read_json()
    else:
        products = read_csv()

    # 3. ID-yə görə filtrləmə
    if product_id:
        product_id = int(product_id)
        # Siyahıda həmin ID-li məhsulu axtarırıq
        products = [p for p in products if p['id'] == product_id]

        # Əgər siyahı boşdursa, deməli məhsul tapılmadı
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
