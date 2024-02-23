def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str_num1, str_num2 = str(num1), str(num2)
    freq_num1 = {}
    freq_num2 = {}
    
    for digit in str_num1:
        if digit in freq_num1:
            freq_num1[digit] += 1
        else:
            freq_num1[digit] = 1
    
    for digit in str_num2:
        if digit in freq_num2:
            freq_num2[digit] += 1
        else:
            freq_num2[digit] = 1
    
    return freq_num1 == freq_num2