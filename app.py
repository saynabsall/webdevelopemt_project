from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database connection
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="train_booking_db"
    )

# Home page route (search available routes)
@app.route('/')
def index():
    return render_template('index.html')

# Route to display booking form
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        departure = request.form['departure']
        arrival = request.form['arrival']
        seats = int(request.form['seats'])

        # Calculate fare (basic example with a flat fare per seat)
        fare_per_seat = 50  # flat fare per seat
        total_price = seats * fare_per_seat

        # Save booking information in database
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO bookings (departure, arrival, seats, total_price)
            VALUES (%s, %s, %s, %s)
        """, (departure, arrival, seats, total_price))
        db.commit()
        booking_id = cursor.lastrowid
        db.close()

        # Redirect to receipt page with booking information
        return redirect(url_for('receipt', booking_id=booking_id))

    return render_template('booking.html')

# Route to display receipt for a booking
@app.route('/receipt/<int:booking_id>')
def receipt(booking_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM bookings WHERE id = %s", (booking_id,))
    booking = cursor.fetchone()
    db.close()
    return render_template('receipt.html', booking=booking)

if __name__ == '__main__':
    app.run(debug=True)
