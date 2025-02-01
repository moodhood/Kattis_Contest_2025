desiigner_string = input()

def is_desiigner_string(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    
    # Check if the string starts with 'b'
    if not s.startswith('b'):
        return False
    
    # Find the index where the 'r's end and the vowel starts
    r_count = 0
    index = 1
    while index < len(s) and s[index] == 'r':
        r_count += 1
        index += 1
    
    # Check if there are at least two 'r's
    if r_count < 2:
        return False
    
    # Check if the remaining part is a single vowel
    if index >= len(s) or s[index] not in vowels or index != len(s) - 1:
        return False
    
    return True

if is_desiigner_string(desiigner_string):
    print("Jebb")
else:
    print("Neibb")