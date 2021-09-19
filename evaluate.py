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
    for k, v in results.items():
        print(f"{k:10}: {v}")
    

def analyze_text_entities(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print("=" * 80)
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results.items():
            print(f"{k:15}: {v}")

with open('./api/clickbait_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for i in range(20000):
        next(csv_reader)
    for row in csv_reader:
        if line_count==0:
            print(f'Column names are {",".join(row)}')
            line_count+=1
        else:
            analyze_text_sentiment(row[0])
            analyze_text_entities(row[0])
            line_count+=1
        print("\n\n")






