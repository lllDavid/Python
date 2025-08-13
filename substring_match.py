def substring(sentence1: str, sentence2: str) -> str:
    len1, len2 = len(sentence1), len(sentence2)
    max_len = 0
    max_substr = ""
    
    for i in range(len1):
        for j in range(len2):
            temp_substr = ""
            k = i
            l = j
            
            while k < len1 and l < len2 and sentence1[k] == sentence2[l]:
                temp_substr += sentence1[k]
                k += 1
                l += 1
            
            if len(temp_substr) > max_len:
                max_len = len(temp_substr)
                max_substr = temp_substr
    
    return max_substr

def check(sentence1, sentence2, threshold=0.5):
    lcs = substring(sentence1, sentence2)
    shortest_len = min(len(sentence1), len(sentence2))
    overlap_ratio = len(lcs) / shortest_len
    
    print(f"Substring: '{lcs}'")
    print(f"Overlap ratio: {overlap_ratio:.2f}")
    
    if overlap_ratio >= threshold:
        print("Potential plagiarism detected.")
    else:
        print("No significant plagiarism detected.")

sentence1 = "The research revealed that artificial intelligence is transforming industries rapidly."
sentence2 = "The research revealed that artificial intelligence is disrupting industries rapidly."

sentence3 = "He enjoys painting landscapes in the quiet countryside."
sentence4 = "Advanced algorithms process data in milliseconds."

check(sentence1, sentence2)

check(sentence3, sentence4)