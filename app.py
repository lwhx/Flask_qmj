from flask import Flask, jsonify

app = Flask(__name__)

def read_numbers():
    try:
        with open('11.txt', 'r') as file:
            numbers = file.read().split(',')
            return [int(num) for num in numbers if num.strip()]
    except FileNotFoundError:
        return []

def write_numbers(numbers):
    with open('11.txt', 'w') as file:
        file.write(','.join(map(str, numbers)))

@app.route('/get_number', methods=['GET'])
def get_number():
    numbers = read_numbers()
    if numbers:
        number_to_send = numbers.pop(0)
        write_numbers(numbers)
        return jsonify(number=number_to_send)
    else:
        return jsonify(message="No more numbers available"), 404

if __name__ == '__main__':
    app.run(debug=True)
