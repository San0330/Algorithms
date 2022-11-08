# computes Longest Proper Prefix which is also a Suffix (LPS) array of pattern
def computeLPS(pat):

    n = len(pat)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * n

    # first point to index 1 of pattern and second points to index 2 of pattern
    # first and second indexes are used to compare whether the string are equal or not
    first = 1
    second = 0

    while first < n:

        if pat[first] == pat[second]:
            # move second forward by 1
            second += 1
            # set lps[first] to second, i.e. upto index first we have same prefix/suffix
            lps[first] = second
            # move first forward by 1
            first += 1
        else:
            # if unmatched and second is at it's initial position
            if second == 0:
                # set 0 i.e. no common prefix/suffix
                lps[first] = 0
                # move first by 1
                first += 1
            else:
                # at this point we might have some common suffix and prefix
                # move second back to the index lps[second-1]
                # i.e. ignore the prefix which is also a suffix and continue from ahead of the prefix
                # this part uses the degeneration property of pattern
                second = lps[second - 1]
                # note: first is not incremented, we compare the new second index to the current
                # first index to find if a match is possible

    return lps


def kmp(text, pat):
    # Preprocess the pattern (calculate lps[] array)
    lps = computeLPS(pat)

    N = len(text)
    n = len(pat)

    second = 0  # index for text
    first = 0  # index of pat

    while first < N:

        if pat[second] == text[first]:
            first += 1
            second += 1

        # if every string of pattern is compared then patter in found.
        if second == n:
            print(f"Pattern found at {first-second}")
            second = lps[second - 1]
        # if pattern stops matching
        elif first < N and pat[second] != text[first]:
            # if second != 0, set second to lps[second-1] i.e. don't compare the common prefix
            if second != 0:
                second = lps[second - 1]
            else:
                first += 1


if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"

    kmp(text, pat)
