def counterfeit_dollar(results):
    
    balanced = set()
    candidates = {}
    for input in results:
        words = input.split()
        if words[-1] == 'even':
            for w in words[:2]:
                for letter in w:
                    balanced.add(letter)
                    if letter in candidates:
                        candidates.pop(letter)
        else:
            for i, w in enumerate(words[:2]):
                for letter in w:
                    if letter not in balanced:
                        if (i == 0 and words[-1] == 'up') or (i == 1 and words[-1] == 'down'):
                            candidates[letter] = 'heavy'
                        else:
                            candidates[letter] = 'light'
                    else:
                        if letter in candidates:
                            candidates.pop(letter)
                    
    if len(candidates) == 1:       
        clave, valor = next(iter(candidates.items()))
        return f'{clave} is the counterfeit coin and it is {valor}.'
    else:
        return '???'