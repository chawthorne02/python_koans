#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):


    #https://docs.python.org/3/library/functions.html?highlight=format#format
    # Format method formats the specified values and puts them in the string placeholder

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual('The values are one and 2', string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual('The values are DOH, doh, doh and DOH!', string)

    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual("The square root of 5 is 2.2361", string)

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual('let', string[7:10])

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual('a', string[1])

        #https://docs.python.org/3/library/functions.html?highlight=format#ord
        # Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97

    def test_single_characters_can_be_represented_by_integers(self):
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(["Sausage", "Egg", "Cheese"], words)

    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library

        #https://docs.python.org/3/library/functions.html?highlight=format#compile
        # re.compile method is used to compile a regular expression pattern provided as a string into a regex pattern object 


        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        self.assertListEqual(['the', 'rain', 'in', 'spain'], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual('\\n', string)
        self.assertEqual(2, len(string))

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual('Now is the time', ' '.join(words))

    def test_strings_can_change_case(self):
        self.assertEqual('Guido', 'guido'.capitalize()) #capitalizes the first index of the string
        self.assertEqual("GUIDO", 'guido'.upper()) # makes the entire string uppercase
        self.assertEqual('timbot', 'TimBot'.lower()) # makes the entire string lowercase
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title()) # Make the first index of a string uppercase
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase()) # returns a string where all the uppercase letters are lowercase and vice versa
