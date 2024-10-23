def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    if marks:
        for mark in marks:
            text = text.replace(mark, '')
    remove_marks.count += 1
    return text



text = 'Application for drivers!'
marks = ''
print(remove_marks(text, marks))
print(remove_marks.count)