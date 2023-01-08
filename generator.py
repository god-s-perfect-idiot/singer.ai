import openai
import os

openai.api_key = "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"

def gen_song(keyword):
    response = openai.Completion.create(model="text-davinci-003", prompt="Write a song about "+keyword, temperature=0.7, max_tokens=4000)
    return (response.get("choices")[0].get("text"))

def gen_title(song):
    response = openai.Completion.create(model="text-davinci-003", prompt="Write a title for the song "+song, temperature=0.7, max_tokens=20)
    return (response.get("choices")[0].get("text"))

