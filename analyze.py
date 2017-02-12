from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key="c6bd936f453f87a013d95cbe0bfe6b85d2d5874b")
colors = {"anger": "ff0000", "joy": "6600ff", "fear": "000000", "sadness": "0000ff", "disgust": "00cc00"}

def get_emotions(text):
    return alchemy_language.emotion(text)["docEmotions"]


def main_emotion(emotions):
    max = 0
    main = ""
    color = ""
    for emotion in emotions:
        if emotions[emotion] > max:
            max = emotions[emotion]
            main = emotion
            color = colors[emotion]
    return color

main_emotion(get_emotions("I like pie a lot"))
