def is_valid_bracket_sequence(sequence):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for bracket in sequence:
        if bracket in bracket_map.values():
            stack.append(bracket)
        elif bracket in bracket_map.keys():
            if stack == [] or bracket_map[bracket] != stack.pop():
                return False
    return stack == []

# Example usage
print(is_valid_bracket_sequence("({[]})"))  # Output: True
print(is_valid_bracket_sequence("({[})"))  # Output: False