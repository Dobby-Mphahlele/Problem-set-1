from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

def parse_timestamp(timestamp):
    """ Parse a timestamp string into a datetime object """
    return datetime.strptime(timestamp.strip(), "%a %d %b %Y %H:%M:%S %z")

def calculate_time_difference(t1, t2):
    """ Calculate the absolute difference in seconds between two datetime objects """
    return abs((t1 - t2).total_seconds())

def process_test_cases(data):
    """ Process multiple test cases and return a list of time differences in seconds """
    try:
        lines = data.splitlines()
        T = int(lines[0].strip())  # Number of test cases
        if T <= 0:
            return {"error": "Number of test cases must be greater than zero"}

        test_cases_data = lines[1:]  # Remaining lines are test case data
        if len(test_cases_data) != 2 * T:
            return {"error": "Mismatch in number of test cases and data"}

        results = []
        for i in range(0, len(test_cases_data), 2):
            t1_str = test_cases_data[i].strip()
            t2_str = test_cases_data[i + 1].strip()
            t1 = parse_timestamp(t1_str)
            t2 = parse_timestamp(t2_str)
            time_difference = calculate_time_difference(t1, t2)
            results.append(int(time_difference))

        return {"id": os.getenv("NODE_ID"), "result": results}
    except Exception as e:
        return {"error": str(e)}

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.data.decode('utf-8').strip()
        results = process_test_cases(data)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
