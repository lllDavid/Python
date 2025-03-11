from collections import deque

def word_ladder(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    wordSet = set(wordList)
    queue = deque([(beginWord, 1)])

    while queue:
        current_word, length = queue.popleft()

        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + char + current_word[i+1:]

                if next_word == endWord:
                    return length + 1

                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, length + 1))

    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(word_ladder(beginWord, endWord, wordList))
