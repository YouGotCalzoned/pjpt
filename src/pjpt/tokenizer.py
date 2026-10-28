class CharacterTokenizer:

    def __init__(self, text: str):

        # Extract unique characters and sort them
        self.vocab = sorted(set(text))

        # Number of unique characters
        self.vocab_size = len(self.vocab)

        # Character -> Integer
        self.stoi = {
            ch: i for i, ch in enumerate(self.vocab)
        }

        # Integer -> Character
        self.itos = {
            i: ch for i, ch in enumerate(self.vocab)
        }

    def encode(self, text: str) -> list[int]:
        return [self.stoi[ch] for ch in text]

    def decode(self, tokens: list[int]) -> str:
        return "".join(self.itos[token] for token in tokens)