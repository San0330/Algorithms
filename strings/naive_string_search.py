if __name__ == "__main__":
    text = input("Enter the text:\t")
    search = input("Enter the word to search in the text:\t")

    n = len(text)
    m = len(search)

    for i in range(n - m + 1):

        # Compare ith character of text string with first character of search string
        # if they doesn't match continue with the next character of text string
        if text[i] != search[0]:
            continue

        # if matched, check other characters for the match until there is no match or all character are compared
        j = 1
        while (j < m) and (text[i + j] == search[j]):
            j += 1

        # if the while loop ends with all character of search string compared, then the match is found
        if j == m:
            print(f"Found at index {i+1}" )

