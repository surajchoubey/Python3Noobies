def emoticoner(words):
    words = message.split(' ')    
    emojis = {
        ":)":"😀",
        ":(":"😟"
    }
    output = ""
    for word in words:
        output += emojis.get("word",word) + " " # word as it was before will be allotted by default if its not a smile from the given
    return output


message = input(">")
print(emoticoner(message))
