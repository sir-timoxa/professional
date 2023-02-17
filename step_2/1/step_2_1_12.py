def spell(*words):

    result = {word[0].lower(): max(map(len, filter(lambda x: x.startswith(word[0]), words))) for word in words}
    return result