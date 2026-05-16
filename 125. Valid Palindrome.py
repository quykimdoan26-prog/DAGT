class Solution:

    def isPalindrome(self, s: str) -> bool:
        # Lọc chuỗi: chỉ giữ lại chữ và số, đồng thời chuyển sang viết thường
        cleaned_s = "".join(ch.lower() for ch in s if ch.isalnum())

        # So sánh chuỗi đã lọc với chuỗi đảo ngược của nó
        return cleaned_s == cleaned_s[::-1]