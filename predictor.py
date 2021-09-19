import evaluate2
import tfevaluate2
import json



from flask import Flask, request
app = Flask('Clickfait')

global answer

@app.route('/api/handleData', methods=["GET", "POST"])
def returnData(text):
    if (request.method == "POST"): 
        global title
        title = request.json().title

    answer = {
        "coordinates": evaluate2.main(title),            
        "clickbait": tfevaluate2.main(title)
            }

    if (request.method == "GET"): 
        return answer
    
