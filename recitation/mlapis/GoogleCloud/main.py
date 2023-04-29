from google.cloud import language_v1
import argparse

def main(input_text):

    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=input_text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response_ents = client.analyze_entities(request={'document': document})
    response_sent = client.analyze_sentiment(request={'document': document})

    for entity in response_ents.entities:
        print('*' * 20)
        print('         name: {0}'.format(entity.name))
        print('         type: {0}'.format(entity.type_))
        print('     metadata: {0}'.format(entity.metadata))
        print('     salience: {0}'.format(entity.salience))

    print('*' * 20)
    print('Overall sentiment: {0}'.format(response_sent.document_sentiment.score))
    print('Sentiment magnitude: {0}'.format(response_sent.document_sentiment.magnitude))
    print('*' * 20)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='API calls to Google Cloud Natural Language API')
    parser.add_argument('arg1', type=str, help='input text')
    args = parser.parse_args()
    input_text = args.arg1
    main(input_text)