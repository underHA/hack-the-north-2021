from google.cloud import language
import csv


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
    withholding = 0
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)
    qwordstrong = ["which"]
    qwordweak = ["if","how","what","what's","should"]

    for entity in response.entities:
        text = text.lower()

        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        counter=0
        for k, v in results.items():
            if counter==2:
                break
            salience = results["salience"]
            salscore=(0.5-float(salience))
            if salscore<0:
                salscore=0
            withholding+=salscore
            counter+=1

    if "NUMBER" in results.values():
        withholding +=0.3
    for wordstrong in qwordstrong:
        if wordstrong in text:
            withholding+=0.45
            break
    for wordweak in qwordweak:
        if wordweak in text:
            withholding+=0.15
            break

    if withholding<0:
        withholding=0
    elif withholding>1:
        withholding=1    
    return withholding
        



with open('./api/clickbait_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count ==10:
            break
        elif line_count==0:
            print(f'Column names are {",".join(row)}')
            line_count+=1
        else:
            print("Article "+str(line_count))
            print(analyze_text_sentiment(row[0]),analyze_text_entities(row[0]))
            line_count+=1
        print("\n\n")






