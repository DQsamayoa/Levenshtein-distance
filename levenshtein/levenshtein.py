
class Levenshtein:

    def __init__(self, alphabet, symbols, weight_dict = {}, language = None):
        """ Initialize the levenshtein distance with a specific alphabet and
            set of symbols and an optional predefined set of weights.

        Parameters
        ----------
        alphabet: string
            A string with all the letters used in the language. It is not
            necessary to add the lower and upper letters, the class create
            both from the input
            Example: alphabet = 'abcdá'
        
        symbols: string
            A string with all the symbols used in the language.
            Example: symbols = '?! '

        weight_dict:
            dictionary of str: tuple(delete, insert, substitute), optional
            Keyword parameters setting the costs for characters  with the
            desired weights for the characters in the alphabet and symbols
            parameters.
            delete: int
                Cost for delete a specific character (default 1)
            insert: int
                Cost for insert a specific character (default 1)
            substitute: int
                Cost for substitute a specific character (default 1)
            (default {char: (1, 1, 1)} for all characters in the alphabet)
            Example: weight_dict = {'a': (1, 2, 3), 'á': (3, 1, 5)}

        language: string, optional
            A string description for the language intended to use the class.
            (default None)
        
        Raises
        ------
        NotImplementedError
        
        Returns
        -------
        None

        """

        self.lower_alphabet = alphabet.lower()
        self.upper_alphabet = alphabet.upper()
        self.symbols = symbols
        self.alphabet = self.lower_alphabet + self.upper_alphabet + self.symbols
        
        self.weight_dict = {}
        for item in self.alphabet:
            self.weight_dict[item] = (1, 1, 1)

        self.weight_dict.update(weight_dict)

        self.language = language

    def __update_alphabet(self, letter, weights):
        """ Add a new letter to the alphabet with the desired weights or
            update the existing weights values.

        Parameters
        ----------
        letter: string
            A leter to add or update in the weights dictionary and alphabet
        
        weights: tuple(int, int, int)
            The weights desired to used.
        
        Raises
        ------
        NotImplementedError
        
        Returns
        -------
        None

        """

        if letter.lower() not in self.lower_alphabet:
            self.lower_alphabet += letter.lower()
            self.upper_alphabet += letter.upper()

        updated_weights = {letter.lower(): weights, letter.upper(): weights}
        self.weight_dict.update(updated_weights)

        self.alphabet = self.lower_alphabet + self.upper_alphabet + self.symbols

        return None

    def __update_symbols(self, symbol, weights):
        """ Add a new symbol to the alphabet with the desired weights or
            update the existing weights values.

        Parameters
        ----------
        symbol: string
            A symbol to add or update in the weights dictionary and alphabet
        
        weights: tuple(int, int, int)
            The weights desired to used.
        
        Raises
        ------
        NotImplementedError
        
        Returns
        -------
        None

        """

        if symbol not in self.symbols:
            self.symbols += symbol

        self.weight_dict.update({symbol: weights})

        self.alphabet = self.lower_alphabet + self.upper_alphabet + self.symbols

        return None

    def __update_weights(self, item, weights = (1, 1, 1)):
        """ Add a new letter or symbol to the alphabet with the desired weights
            or update the existing weights values.

        Parameters
        ----------
        item: string
            A letter or symbol to add in the alphabet and to add or update the
            weights dictionary
        
        weights: tuple(int, int, int), optional
            The weights desired to used (default tuple(1, 1, 1)).
        
        Raises
        ------
        NotImplementedError
        
        Returns
        -------
        None

        """

        if item.isalpha():
            self.__update_alphabet(item, weights)
        else:
            self.__update_symbols(item, weights)

        return None

    def iterative_matrix(self, source_input, target_input):
        """ Create the iterative matrix to compute the Levenshtein distance
            between two strings.
            This code was taken from
            https://www.python-course.eu/levenshtein_distance.php
            It was modified but the core idea is from that website.

        Parameters
        ----------
        source_input: string
            A string to compare with the target_input
        
        target_input: string
            A string to compare with the source_input
        
        Raises
        ------
        NotImplementedError
        
        Returns
        -------
        tuple(dist, row, col)
            dist: list
                It will contain the Levenshtein distance between the first
                i characters of source_input and the first j characters of
                target_input
            row: int
                The number of characters for the source_input
            col: int
                The number of characters for the target_input
        """

        w = self.weight_dict
        
        rows = len(source_input) + 1
        cols = len(target_input) + 1

        dist = [ [0 for x in range(cols)] for x in range(rows) ]

        # source prefixes can be transformed into empty strings 
        # by deletions:
        for row in range(1, rows):
            # Validating if the item exist in the alphabet. In the case the
            # item does not exist, then update the alphabet with it.
            try:
                dist[row][0] = dist[row - 1][0] + w[source_input[row - 1]][0]
            except:
                new_item = source_input[row - 1]
                self.__update_weights(new_item)
                dist[row][0] = dist[row - 1][0] + w[source_input[row - 1]][0]

        # target prefixes can be created from an empty source string
        # by inserting the characters
        for col in range(1, cols):
            # Validating if the item exist in the alphabet. In the case the
            # item does not exist, then update the alphabet with it.
            try:
                dist[0][col] = dist[0][col - 1] + w[target_input[col - 1]][1]
            except:
                new_item = target_input[col - 1]
                self.__update_weights(new_item)
                dist[0][col] = dist[0][col - 1] + w[target_input[col - 1]][1]
            
        for col in range(1, cols):
            for row in range(1, rows):
                deletes = w[source_input[row - 1]][0]
                inserts = w[target_input[col - 1]][1]
                subs = max( (w[source_input[row - 1]][2], w[target_input[col - 1]][2]) )

                if source_input[row - 1] == target_input[col - 1]:
                    subs = 0
                else:
                    subs = subs

                dist[row][col] = min(dist[row - 1][col] + deletes, # delete
                                     dist[row][col-1] + inserts, # insert
                                     dist[row - 1][col - 1] + subs) # substitution

        # This step is to fix the error due to empty string
        if cols == 1:
            col = 0

        if rows == 1:
            row = 0
     
        return dist, row, col

    def distance(self,  source_input, target_input):
        """ Compute the Levenshtein distance between the strings provided.

        Parameters
        ----------
        source_input: string
            A string to compare with the target_input
        
        target_input: string
            A string to compare with the source_input
        
        Raises
        ------
        NotImplementedError
        
        Returns
        -------
        int
            The minimum number of insert, delete and substitutions to transform
            one string into other

        """

        dist, row, col = self.iterative_matrix(source_input, target_input)

        return dist[row][col]

    def similarity(self, source_input, target_input):
        """ Compute the Levenshtein similarity between the strings provided.

        Parameters
        ----------
        source_input: string
            A string to compare with the target_input
        
        target_input: string
            A string to compare with the source_input
        
        Raises
        ------
        NotImplementedError
        
        Returns
        -------
        int
            It will contain the Levenshtein distance between the first i
            characters of source_input and the first j characters of
            target_input

        """

        dist, row, col = self.iterative_matrix(source_input, target_input)

        sim = 1 - (dist[row][col] / max(row, col))
        
        return sim
