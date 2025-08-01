from string_swap import areAlmostEqual2

def test_areAlmostEqual():
    s2= areAlmostEqual2
    
    assert s2("bank", "bank") == True
    assert s2("abcd", "abcd") == True
    assert s2("bank", "knab") == False
    assert s2("listen", "silent") == False
    assert s2("abc", "xyz") == False
    assert s2("abcdef", "ghijkl") == False
    assert s2("ab", "cd") == False
    assert s2("hello", "holle") == True
    assert s2("", "") == True
    assert s2("a", "b") == False
    assert s2("ab", "ba") == True
    assert s2("abc", "acb") == True