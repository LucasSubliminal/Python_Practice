def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """ 
    # Remove spaces, convert to lowercase
    phrase = phrase.lower()
    phrase = ''.join(phrase.split())
    if phrase[::-1] == phrase:
        return True
    else:
        return False
    