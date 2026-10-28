from pjpt.tokenizer import CharacterTokenizer


def test_vocabulary():
    tokenizer = CharacterTokenizer("abaac")

    assert tokenizer.vocab == ['a', 'b', 'c']
    assert tokenizer.vocab_size == 3


def test_encoding():
    tokenizer = CharacterTokenizer("abaac")

    assert tokenizer.encode("abc") == [0, 1, 2]


def test_decoding():
    tokenizer = CharacterTokenizer("abaac")

    assert tokenizer.decode([0, 1, 2]) == "abc"


def test_round_trip():
    tokenizer = CharacterTokenizer("abaac")

    original = "abaac"

    encoded = tokenizer.encode(original)
    decoded = tokenizer.decode(encoded)

    assert decoded == original