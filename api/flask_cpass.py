from flask import Flask, jsonify, request, send_file, redirect,has_request_context

app = Flask(__name__)

@app.route('/api/incall',methods=['GET','POST'])
def incall_api():
    #Play App Response
    #res = {"response":{"app":"play","url":"https://api.twilio.com/cowbell.mp3","refresh":"1"}}

    #Say App Response
    #res = {"response": {"app": "say","refresh": "1","text": "Welcome to my company, we are Voip solution provider, happy to help you"}}

    some_json = request.get_json()
    print(some_json)

    #Collect App Response
    res = {"response": {"app": "collect","refresh": "1","text": "Welcome to my company, press one for sales and press two for support","action":"http://localhost:5005/api/process_digits","timeout":"3","attempts":"3","numdigits":"1"}}

    #Dial Number App Response
    #res = {"response": {"app": "dial_number","refresh": "1","numbers": "9979272423,8000684001,9427914909","action":"http://localhost:5005/api/dial_number_action","timeout":"60"}}

    #Dial SIP App Response
    #res = {"response": {"app": "dial_sip","refresh": "1","agents": "102,103","action":"http://localhost:5005/api/dial_sip_action","timeout":"60"}}
    return jsonify(res)

@app.route('/api/process_digits',methods=['GET','POST'])
def process_digits_api():
    if(request.method=='POST'):
        some_json = request.get_json()
        digits = some_json['digits']
        if(digits=='1'):
            #res = {"response": {"app": "say","refresh": "1","text": "you have pressed one"}}
            #res = {"response": {"app": "dial_number","refresh": "1","numbers": "9979272423","action":"http://localhost:5005/api/dial_number_action","timeout":"60"}}
            res = {"response": {"app": "dial_sip","refresh": "1","agents": "102,103","action":"http://localhost:5005/api/dial_sip_action","timeout":"60"}}
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

@app.route('/api/dial_number_action',methods=['GET','POST'])
def dial_number_action_api():
    if(request.method=='POST'):
        some_json = request.get_json()
        print(some_json)
        dial_status = some_json['dial_status']
        if(dial_status=='CHANUNAVAIL'):
            res = {"response": {"app": "say","refresh": "1","text": "Channel is not available"}}
            return jsonify(res)
        elif(dial_status=='NOANSWER'):
            res = {"response": {"app": "say","refresh": "1","text": "no one is available to answer your call"}}
            return jsonify(res)
        elif(dial_status=='BUSY'):
            res = {"response": {"app": "say","refresh": "1","text": "Channel is busy now"}}
            return jsonify(res)
        else:
            res = {"response": {"app": "say","refresh": "1","text": "there is some technical issue in call dialing"}}
            return jsonify(res)

@app.route('/api/dial_sip_action',methods=['GET','POST'])
def dial_sip_action_api():
    if(request.method=='POST'):
        some_json = request.get_json()
        print(some_json)
        dial_status = some_json['dial_status']
        if(dial_status=='CHANUNAVAIL'):
            res = {"response": {"app": "say","refresh": "1","text": "Channel is not available"}}
            return jsonify(res)
        elif(dial_status=='NOANSWER'):
            res = {"response": {"app": "say","refresh": "1","text": "no one is available to answer your call"}}
            return jsonify(res)
        elif(dial_status=='BUSY'):
            res = {"response": {"app": "say","refresh": "1","text": "Channel is busy now"}}
            return jsonify(res)
        else:
            res = {"response": {"app": "say","refresh": "1","text": "there is some technical issue in call dialing"}}
            return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005,debug=True)

