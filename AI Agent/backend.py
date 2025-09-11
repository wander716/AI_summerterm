from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from http import HTTPStatus
from dashscope import Application

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        api_key = "sk-82f8277bb1ba478eab793d5661b5df70"  # 内置API密钥
        app_id = "4b668f15d6bf4733b42125d4052e6473"  # 固定的应用ID
        prompt = data.get('prompt')
        
        if not prompt:
            return jsonify({
                'error': 'Missing required parameters',
                'message': 'Prompt is required'
            }), 400
        
        # 调用DashScope API
        response = Application.call(
            api_key=api_key,
            app_id=app_id,
            prompt=prompt
        )
        
        if response.status_code != HTTPStatus.OK:
            return jsonify({
                'error': 'API call failed',
                'status_code': response.status_code,
                'message': response.message,
                'request_id': response.request_id
            }), response.status_code
        else:
            return jsonify({
                'success': True,
                'response': response.output.text
            })
    
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
