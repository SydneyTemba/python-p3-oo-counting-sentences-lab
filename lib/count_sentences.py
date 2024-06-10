class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        value = self.value.replace('!!', '.').replace('?!', '.').replace('?', '.').replace('!', '.')
        sentences = value.split('.')
        sentences = [sentence.strip() for sentence in sentences if sentence]
        return len(sentences)