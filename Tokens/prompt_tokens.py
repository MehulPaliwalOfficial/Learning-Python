# prompt_tokens.py   -- GIVEN TO YOU. DO NOT MODIFY THIS FILE.
#
# A PromptTokens object holds a list of tokens and hands them out one at a
# time, from left to right. A token is one piece of text, such as a word or
# a punctuation mark.


class PromptTokens:

    def __init__(self, tokens):
        self._tokens = tokens
        self._i = 0

    def has_next(self):
        # True if another token is still waiting, False if they are finished.
        return self._i < len(self._tokens)

    def next_token(self):
        # Hands you the next token, then moves forward by one.
        token = self._tokens[self._i]
        self._i = self._i + 1
        return token
