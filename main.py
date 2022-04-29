####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant', '-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
    if (S == ""):
        return (len(T))
    elif (T == ""):
        return (len(S))
    else:
        if (S[0] == T[0]):
            return (MED(S[1:], T[1:]))
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
    for i in range(len(S)):
        for j in range(len(T)):
            if j == 0:
                MED[i, j] = len(S[:i])
            elif i == 0:
                MED[i, j] = len(T[:j])
            else:
                if S[i] == T[j]:
                    MED[i, j] = MED[i - 1, j - 1]
                else:
                    MED[i, j] = 1 + min(MED[i, j - 1], MED[i - 1, j], MED[i - 1, j - 1])
    return MED[len(S) - 1, len(T) - 1], MED


def fast_align_MED(S, T, MED={}):
    edits, MED_prime = fast_MED(S, T)
    S_prime = ""
    T_prime = ""
    i = len(S) - 1
    j = len(T) - 1
    while i >= 0:
        while j >= 0:
            if i == 0 and j == 0:
                S_prime = S[i] + S_prime
                T_prime = T[j] + T_prime
                return S_prime, T_prime
            elif j == 0:
                left = MED_prime[i - 1, j]
                up = MED_prime[i, j]
                diagonal = MED_prime[i - 1, j]
            elif i == 0:
                left = MED_prime[i, j]
                up = MED_prime[i, j - 1]
                diagonal = MED_prime[i, j - 1]
            else:
                left = MED_prime[i - 1, j]
                up = MED_prime[i, j - 1]
                diagonal = MED_prime[i - 1, j - 1]
            if left <= up and left <= diagonal:
                S_prime = S[i] + S_prime
                T_prime = '-' + T_prime
                i -= 1
            elif up <= left and up <= diagonal:
                S_prime = '-' + S_prime
                T_prime = T[j] + T_prime
                j -= 1
            else:
                S_prime = S[i] + S_prime
                T_prime = T[j] + T_prime
                i -= 1
                j -= 1
    return S_prime, T_prime


def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)


def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
