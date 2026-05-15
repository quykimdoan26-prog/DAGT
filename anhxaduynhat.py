class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.lower().split()
        if len(pattern) != len(words):
            return False
        
        char_to_word = {} # dic lưu ánh xạ
        word_to_char = {}
        
        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:# nếu c đã có trong dict char->word thì kiểm tra nếu gặp một từ khác nữa 
                return False # trả về sai 
            if w in word_to_char and word_to_char[w] != c: # tương tự ví dụ c[abb],w=[dog,dog,dog] khi gặp b và dog nó sẽ vào lệnh hai
                # và trả về trùng ánh xạ
                return False
            char_to_word[c] = w # ánh xạ chữ cái tới từ
            word_to_char[w] = c # từ ánh xạ của chũ cái

        return True