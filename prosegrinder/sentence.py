# -*- coding: utf-8 -*-

import re
from collections import Counter

import pointofview

from prosegrinder.fragment import Fragment


class Sentence(Fragment):

    RE_SENTENCE = re.compile("""
            # Match a sentence ending in punctuation or EOS.
            [^.!?…\\s]        # First char is non-punct, non-ws
            [^.!?…]*          # Greedily consume up to punctuation.
            (?:               # Group for unrolling the loop.
            [.!?…]            # (special) inner punctuation ok if
            (?!['\")]?\\s|$)  # not followed by ws or EOS.
            [^.!?…]*          # Greedily consume up to punctuation.
            )*                # Zero or more (special normal*)
            [.!?…]            # Ending punctuation.
            ['\")]?           # Optional closing quote.
            (?=\\s|$)
            """,
                             flags=re.MULTILINE | re.VERBOSE)

    RE_SMART_QUOTES = re.compile("[“”]")

    @property
    def sentence_string(self):
        return self.fragment_string
