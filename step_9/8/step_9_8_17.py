import functools
def make_html(tag):
            def decorator(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    value = func(*args, **kwargs)
                    return f"<{tag}>{value}</{tag}>"
                return wrapper
            return decorator


# INPUT DATA:

# TEST_1:
@make_html('del')
def get_text(text):
    return text


print(get_text('Python'))


# TEST_2:
@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text(text='decorators are so cool!'))


# TEST_3:
@make_html('small')
@make_html('mark')
@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text('ANRIANRIANRI'))

