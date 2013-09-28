from steep.settings import SEARCH_SETTINGS

def parse_query(query):
    """
        Tokenize query into person, tag and literal tokens.
        Uses the special symbols as defined in the syntax setting.
    """
    # Get syntax
    syntax = SEARCH_SETTINGS['syntax']
    # Tokenize, get tags/users/queries
    tags = set([])
    persons = set([])
    literals = set([])

    # Initialize empty token
    token = None

    # Initialize symbol position
    i = 0

    # While query still contains symbols
    while i < len(query):
        # Eat symbol
        symbol = query[i]
        # If no token is being formed
        if token is None:
            # If symbol is the delimeter
            if symbol == syntax['DELIM']:
                # Ignore, means nothing in this context
                pass
            # If symbol is the escape character
            elif symbol == syntax['ESCAPE']:
                # If a special character is being escaped
                if i < len(query)-1 and query[i+1] in syntax.values():
                    # Add the escape character + the escaped character
                    #  as normal symbols. The escape character will be taken
                    #  out later.
                    token = query[i]+query[i+1]
                    # Jump over the escaped character
                    i += 1
                else:
                    # Ignore, means nothing in this context
                    pass
            # If symbol is literal character
            elif symbol == syntax['LITERAL']:
                # Start empty literal token
                token = ""
                # Jump to next character
                i += 1
                # Eat symbols until literal character or end of string
                while i < len(query):
                    # Eat symbol (inner loop)
                    symbol = query[i]
                    # If symbol is literal character
                    if symbol == syntax['LITERAL']:
                        # Add token to literals
                        literals.add(token)
                        # Clear token
                        token = None
                        # Stop eating symbols for literal
                        break
                    # If symbol is the escape character
                    elif symbol == syntax['ESCAPE']:
                        # If the literal character is being escaped
                        if i < len(query)-1 and \
                                query[i+1] == syntax['LITERAL']:
                            # Add literal character as normal symbol
                            token += syntax['LITERAL']
                            # Jump over literal character
                            i += 1
                        # If a different symbol follows the escape character
                        else:
                            # Add escape character to token
                            token += syntax['ESCAPE']
                    else:
                        # Add symbol to literal token
                        token += symbol
                    i += 1
                # If literal token was not ended
                if token is not None:
                    # Add token to literals
                    literals.add(token)
                    # Clear token
                    token = None
            # If symbol is something else
            else:
                # Start a new token with the symbol
                token = symbol
        # If a token is already being formed
        else:
            # If symbol is the delimeter
            if symbol == syntax['DELIM']:
                # If the token is a person
                if token[0] == syntax['PERSON']:
                    # Add the token (without syntax symbol) to persons
                    persons.add(token[1:])
                # If the token is a tag
                elif token[0] == syntax['TAG']:
                    # Add the token (without syntax symbol) to tags
                    tags.add(token[1:])
                # If the token is escaped
                elif token[0] == syntax['ESCAPE']:
                    # Treat the rest the token as literal
                    literals.add(token[1:])
                # If the token is a literal
                else:
                    # Add the token to the literals
                    literals.add(token)
                # Clear token
                token = None
            # If symbol is the escape character
            elif symbol == syntax['ESCAPE']:
                # If a special character is being escaped
                if i < len(query)-1 and query[i+1] in syntax.values():
                    # Add the character as normal symbol
                    token = query[i+1]
                    # Jump over the escaped character
                    i += 1
                else:
                    # Ignore, means nothing in this context
                    pass
            # If symbol is something else
            else:
                # Add symbol to token
                token += symbol
        # Jump to next symbol
        i += 1

    # If last token was not ended
    if token is not None:
        # If the token is a person
        if token[0] == syntax['PERSON']:
            # Add the token (without syntax symbol) to persons
            persons.add(token[1:])
        # If the token is a tag
        elif token[0] == syntax['TAG']:
            # Add the token (without syntax symbol) to tags
            tags.add(token[1:])
        # If the token is escaped
        elif token[0] == syntax['ESCAPE']:
            # Treat the rest the token as literal
            literals.add(token[1:])
        # If the token is a literal
        else:
            # Add the token to the literals
            literals.add(token)
        # Clear token
        token = None

    # Discard any empty tokens
    tags.discard('')
    persons.discard('')
    literals.discard('')

    # Return found tags, persons and literals
    return list(tags), list(persons), list(literals)
