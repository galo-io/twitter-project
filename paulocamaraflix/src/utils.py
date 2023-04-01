class stringUtils():
    def remove_first_non_alphabetic_chars(self, text):
        """
        Definition: removes in-place first non alphabetic characters from string `text`
        Inputs:
            `text`, string
        Outputs:
            `text`, string without first non alphabetic characters
        Author:
            @joaoreboucas1
        Since:
            03-2023
        """
        while True:
            if not text[0].isalpha():
                text = text[1:]
            else:
                return text
    
    def turn_long_text_into_subtexts(self, text, subtext_length):
        """
        Separates a long string into a list of strings whose length is less than `subtext_length`.

        Inputs:
            long_text = string text

        Outputs:
            List of strings of lenght less than 280.
        Authors:
            @joaoreboucas1
        
        Since:
            02-2023.
        """
        phrases = text.split('.')
        split_text = ['']
        i = 0
        for phrase in phrases:
            if len(phrase) == 0:
                continue
            if phrase[0] == '\n':
                phrase = phrase[1:]
            phrase = phrase + '.'
            if len(split_text[i]) < subtext_length - len(phrase):
                split_text[i] += phrase
            else:
                i += 1
                split_text.append(phrase)
        return split_text