from wav2vec import text_gen
from sentiment import sentiment, emotion

txt1 = text_gen()
input("ASR from streamed recording")
print(txt1.text_from_recording())
input("ASR from file")
print(txt1.text_from_file('samples/sample1.wav'))
sent1 = sentiment()
input("Positive Sentiment")
print(sent1.from_audio())
input("Negative Sentiment")
print(sent1.from_audio())
emo1 = emotion()
input("Emotion 1")
print(emo1.from_audio())
input("Emotion 2")
print(emo1.from_audio())
input("Emotion 3")
print(emo1.from_audio())



