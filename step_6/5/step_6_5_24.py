from collections import defaultdict


def best_sender(messages, senders):
    count = defaultdict(int)
    for key, value in zip(senders, messages):
        count[key] += (len(value.split()))
    return max(sorted(count,reverse=True), key=count.get)

