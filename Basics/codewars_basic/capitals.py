# Complete the method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings.

# The method should return an array of sentences declaring the state or country and its capital.

# Examples

# [{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
# [{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
# [{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}] --> ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]


def capital(capitals): 
    sentences = []
    for object in capitals:
        capital = object.get('capital')
        governingBody = object.get('country') or object.get('state')
        sentences.append(f'The capital of {governingBody} is {capital}.')
    return sentences

