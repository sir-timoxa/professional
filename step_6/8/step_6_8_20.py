from collections import Counter

def print_bar_chart(data, mark):
    max_len_data=len(max(data, key=len))
    for k,v in Counter(data).most_common():
        print(f"{k:{max_len_data}} |{v*mark}")

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart(languages, '#')