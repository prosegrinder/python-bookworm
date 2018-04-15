# -*- coding: utf-8 -*-

import re
from collections import Counter

import pointofview


class Word:
    """A Word, the base unit for measuring fiction prose."""

    MIN_SYLLABLES_COMPLEX_WORD = 3
    MIN_CHARS_LONG_WORD = 7

    @staticmethod
    def get_word_frequency(word_list):
        """Returns a Counter of word / count pairs based on a list of non-unique words."""
        return Counter(word_list)

    def __init__(self, word_string, syllable_count, is_dictionary_word, is_numeric):
        self._initial_word = word_string
        self._syllable_count = syllable_count
        self._is_dictionary_word = is_dictionary_word
        self._is_numeric = is_numeric
        self._normalized_word = word_string.strip().lower()
        self._character_count = len(self._normalized_word)
        self._pov = pointofview.get_word_pov(self._normalized_word)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def initial_word(self):
        """Return the word string initially used to create the Word."""
        return self._initial_word

    @property
    def syllable_count(self):
        """Return the number of syllables in Word."""
        return self._syllable_count

    @property
    def is_dictionary_word(self):
        """Whether or not the Word was found in the Dictionary."""
        return self._is_dictionary_word

    @property
    def is_numeric(self):
        """Returns whether or not the Word is numeric per the Dictionary."""
        return self._is_numeric

    @property
    def normalized_word(self):
        """Returns the normalized string of the initial word."""
        return self._normalized_word

    @property
    def character_count(self):
        """Returns the number of characters in the Word."""
        return self._character_count

    @property
    def is_complex_word(self):
        """Returns whether or not the Word is considered complex."""
        return self.syllable_count >= Word.MIN_SYLLABLES_COMPLEX_WORD

    @property
    def is_long_word(self):
        """Returns whether or not the Word is considered long."""
        return self.character_count >= Word.MIN_CHARS_LONG_WORD

    @property
    def is_first_person_word(self):
        """Returns whether or not the Word inidicates first-peron point of view."""
        return self._pov == 'first'

    @property
    def is_second_person_word(self):
        """Returns whether or not the Word inidicates second-peron point of view."""
        return self._pov == 'second'

    @property
    def is_third_person_word(self):
        """Returns whether or not the Word inidicates third-peron point of view."""
        return self._pov == 'third'

    @property
    def is_pov_word(self):
        """Returns whether or not the Word inidicates any point of view."""
        return (self.is_first_person_word or
                self.is_second_person_word or
                self.is_third_person_word)

    @property
    def pov(self):
        return self._pov
