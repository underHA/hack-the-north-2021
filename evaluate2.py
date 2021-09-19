from google.cloud import language
import csv
from flask import Flask
app = Flask('Clickfait')










def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1}",
        magnitude=f"{sentiment.magnitude:.1}",
    )
    return results['score']  

def analyze_text_entities(text):
    withholding = 1.95
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)
    qwordstrong = ["which","based"]
    qwordweak = ["if","how","what","what's","should"]
    counter=0
    for entity in response.entities:
        if counter>=3:
            withholding-=0.3

        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        
        if counter<3:
            salience = results["salience"]
            salscore=(float(salience)*1.5)
            if salscore<0:
                salscore=0
            withholding-=salscore
                 
        if results["type"]=="NUMBER" and counter==0:
            withholding +=0.45
        counter+=1
        


    text = text.lower()
    for wordstrong in qwordstrong:
        if wordstrong in text:
            withholding+=0.55
            
    for wordweak in qwordweak:
        if wordweak in text:
            withholding+=0.35
            

    if withholding<0:
        withholding=0
    elif withholding>1:
        withholding=1    
    return withholding
        

f=open('/Users/rickzhang/Documents/code/htn/google/hack-the-north-2021/trainingSet3.csv','w')
writer = csv.writer(f)
writer.writerow(["Title","Sentiment","Withhold"])

with open('./api/clickbait_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:

        if line_count==0:
            print(f'Column names are {",".join(row)}')
            line_count+=1
        else:
            print("Article "+str(line_count))
            sentiment = float(analyze_text_sentiment(row[0]))
            withhold = float(analyze_text_entities(row[0]))
            print("{:0.2f}, {:0.2f}".format(sentiment,withhold))

            writer.writerow([row[0],sentiment,withhold])
            line_count+=1
        print("\n\n")

f.close()



def main(text):
    sentiment = round(analyze_text_sentiment(text),2) #sentiment rating from -1 to 1, with -1 being extremely negative, 0 being neutral, and 1 being extremely positive sentiment.
    withhold = round(analyze_text_entities(text),2) #withhold information rating from 0 to 1, with 0 withholding little to no information, and 1 withholding very much information.

    return sentiment, withhold




@app.route('/clickbaitPlots')
def returnData(text):
    return main(text)




