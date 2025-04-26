# worker.py
from flask import Flask, request, jsonify
import time
import json
import random


app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

@app.route('/find_primes', methods=['POST'])
def find_primes():
    
    print("Connected to creampy")
    data = request.get_json()
    iterations = int(data['iterations'])
    t0 = time.time()
    primes = []
    for i in range(iterations):
        number = random.getrandbits(32)
        if is_prime(number):
            primes.append(number)
    t1 = time.time()
    
    #with open('primes_result.json', 'a') as f:
    #    f.write(json.dumps(primes) + '\n')
        
    return jsonify({
        "start": t0,
        "end" : t1,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)