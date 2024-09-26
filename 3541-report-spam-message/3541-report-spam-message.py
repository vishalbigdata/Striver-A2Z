class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned_set = set(bannedWords)
        
        # Initialize a counter for words in message that are in bannedWords
        count = 0
        
        # Iterate through the message array
        for word in message:
            if word in banned_set:
                count += 1
                if count >= 2:  # If we found two matches, it's spam
                    return True
        
        return False  # Return false if fewer than 2 matches found
