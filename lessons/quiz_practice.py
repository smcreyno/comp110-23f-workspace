WORD: str = "happy"
l1_idx: int = 0
l2_idx: int = 0
t1: str = ""
t2: str = ""
n_appearances: int = 0

while l1_idx < len(WORD):
    t1 = WORD[l1_idx]
    n_appearances = 1
    l2_idx = 0

    while l2_idx < len(WORD):
        t2 = WORD[l2_idx]

        if (t1 == t2) and (l1_idx != l2_idx):
            n_appearances = n_appearances + 1
        l2_idx = l2_idx + 1
    print(f"{WORD[l1_idx]} appears {n_appearances} times. ")
    l1_idx = l1_idx + 1
