class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []

        for i, w in enumerate(words, 1):
            if w[0] in vowels:
                goat_word = w + "ma"
            else:
                goat_word = w[1:] + w[0] + "ma"
            goat_word += "a" * i
            result.append(goat_word)

        return " ".join(result)




        """
        :type sentence: str
        :rtype: str
        """