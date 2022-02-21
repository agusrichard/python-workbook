from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""

    result = ""
    first_str = strs[0]
    for i in range(1, len(first_str) + 1):
        all_true = all([word.startswith(first_str[:i]) for word in strs])
        if all_true:
            result = first_str[:i]

    return result


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
