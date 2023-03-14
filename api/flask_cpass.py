from flask import Flask, jsonify, request, send_file, redirect,has_request_context

app = Flask(__name__)

@app.route('/api/incall',methods=['GET','POST'])
def incall_api():
    #res = {"response":{"app":"play","url":"https://api.twilio.com/cowbell.mp3","refresh":"1"}}
    #res = {"response": {"app": "say","refresh": "1","text": "Welcome to my company, we are Voip solution provider, happy to help you"}}
    some_json = request.get_json()
    print(some_json)
    res = {"response": {"app": "collect","refresh": "1","text": "Welcome to my company, press one for sales and press two for support","action":"http://localhost:5005/api/process_digits","timeout":"3","attempts":"3","numdigits":"1"}}
    return jsonify(res)

@app.route('/api/process_digits',methods=['GET','POST'])
def process_digits_api():
    if(request.method=='POST'):
        some_json = request.get_json()
        digits = some_json['digits']
        if(digits=='1'):
            res = {"response": {"app": "say","refresh": "1","text": "you have pressed one"}}
            return jsonify(res)
        elif(digits=='2'):
            res = {"response": {"app": "say","refresh": "1","text": "you have pressed two"}}
            return jsonify(res)
        elif(digits=='TIMEOUT'):
            res = {"response": {"app": "say","refresh": "1","text": "time out, please try again"}}
            return jsonify(res)
        else:
            res = {"response": {"app": "say","refresh": "1","text": "invalid input, please try again"}}
            return jsonify(res)
    else:
        api_result = {"response": {"app": "say","refresh": "1","text": "please use the post method in your request"}}
        return(jsonify(api_result))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005,debug=True)

