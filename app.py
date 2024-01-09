from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        process_notification(data)
        return "OK", 200
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return "Internal Server Error", 500

def process_notification(data):
    print("Received Notification:")
    print(data)
    
if __name__ == '__main__':
    app.run(debug=True)

