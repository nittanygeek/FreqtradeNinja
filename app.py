from flask import Flask, render_template, jsonify
import sqlite3
import config

DATABASE = config.DATABASE

def get_open_trades():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trades WHERE is_open")
    open_trades = cursor.fetchall()
    conn.close()
    return open_trades


# Create an Instance of the Flask App:
app = Flask(__name__)

@app.route('/')
def index():
    open_trades = get_open_trades()
    return render_template('index.html', open_trades=open_trades, dark_mode_class='', dark_mode_nav_class='', dark_mode_button_class='btn-dark-mode', table_dark_class='')

@app.route('/orders/<trade_id>')
def get_order_details(trade_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE ft_trade_id=? AND order_filled_date", (trade_id,))
    order_details = cursor.fetchall()

    # Get the column names from the cursor description
    column_names = [description[0] for description in cursor.description]

    # Create a list of dictionaries with variable names as keys and order details as values
    orders = [dict(zip(column_names, order)) for order in order_details]

    conn.close()
    return jsonify(orders)

if __name__ == '__main__':
    app.run(debug=True)
