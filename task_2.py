from collections import deque


def is_palindrome(input_string):
    normalized_string = input_string.replace(' ', '').lower()
    deque_string = deque(normalized_string)

    while len(deque_string) > 1:
        left_char = deque_string.popleft()
        right_char = deque_string.pop()

        if left_char != right_char:
            return False

    return True


palindrome_example = 'Do geese see God'
print(f"The string \"{palindrome_example}\" is_palindrome: {is_palindrome(palindrome_example)}")
