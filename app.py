from flask import Flask, request, jsonify, send_from_directory
import os


app = Flask(__name__)

documents = {}

@app.route('/document/<doc_id>', methods=['GET'])
def get_document(doc_id):
    return jsonify({'doc_id': doc_id, 'content': documents.get(doc_id, '')})

@app.route('/document/<doc_id>', methods=['POST'])
def update_document(doc_id):
    data = request.get_json()
    content = data.get('content', '')
    documents[doc_id] = content
    return jsonify({'doc_id': doc_id, 'status': 'updated', 'content': content})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

