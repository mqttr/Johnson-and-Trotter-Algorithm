def factorial(n: int) -> int:
    if n == 1: return 1
    return n * factorial(n-1)

def printPermutations(permutation: str, count: int) -> None:
    permutations = [char for char  in permutation]

    perm_dict = {perm:-1 for perm in permutations}

    for i in range(min(factorial(len(permutation)), count)):
        print(i+1, ''.join(permutations))
        
        # Find the character that we want to move
        char = ""
        for char in sorted(permutations, reverse=True):
            if ((perm_dict[char] == -1 and permutations[0] == char) or (perm_dict[char] == 1 and permutations[-1] == char) ):
                continue
            
            # Gets neighbor to make sure neighbor isn't smaller than value, if value is larger, it isn't mobile
            char_index = permutations.index(char)
            if char < permutations[char_index+perm_dict[char]]: 
                continue

            break
        
        # print(f"Largest mobile: {char}")

        char_index = permutations.index(char)

        # print(permutations[char_index], permutations[char_index-1])
        permutations[char_index], permutations[char_index+perm_dict[char]] = permutations[char_index+perm_dict[char]], permutations[char_index]

        for large_char in perm_dict.keys():
            if int(large_char) > int(char):
                perm_dict[large_char] = -perm_dict[large_char]

def main():
    printPermutations("1234", 24)

if __name__ == "__main__":
    main()