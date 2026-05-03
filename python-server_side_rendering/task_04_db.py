import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


# JSON və CSV oxuma funksiyaları (əvvəlki taskdan qalır)
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


# YENİ: SQL oxuma funksiyası
def read_sql(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Bu sətir məlumatları lüğət (dict) kimi götürməyə kömək edir
        cursor = conn.cursor()

        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
            product = cursor.fetchone()
            conn.close()
            return [dict(product)] if product else []
        else:
            cursor.execute('SELECT * FROM Products')
            products = cursor.fetchall()
            conn.close()
            return [dict(p) for p in products]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Mənbə yoxlanışı
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Məlumatın götürülməsi
    products = []
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
        if products is None:  # Verilənlər bazasında xəta baş veribsə
            return render_template('product_display.html', error="Database error")

    # 3. ID-yə görə filtrləmə (Əgər SQL-də edilməyibsə, Python tərəfində edilir)
    if product_id:
        product_id = int(product_id)
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)