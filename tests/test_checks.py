from textkit.checks import is_anagram, is_palindrome


def test_palindrome_true():
    assert is_palindrome("level")


def test_palindrome_false():
    assert not is_palindrome("python")


def test_palindrome_with_spaces():
    assert is_palindrome("nurses run")


def test_is_anagram_true():
    assert is_anagram("listen", "silent")


def test_is_anagram_ignores_spaces_and_case():
    assert is_anagram("Dormitory", "Dirty room")


def test_is_anagram_false():
    assert not is_anagram("hello", "world")
