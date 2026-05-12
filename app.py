from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    count = redis_client.incr('hits')
    return f"Hello! Visitor count: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
