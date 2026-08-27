class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Count characters in s1
        for ch in s1:
            count1[ord(ch) - ord('a')] += 1

        # Create the first window of s2
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        # Check the first window
        if count1 == count2:
            return True

        # Slide the window
        for right in range(len(s1), len(s2)):

            # Add the new character
            count2[ord(s2[right]) - ord('a')] += 1

            # Remove the leftmost character
            left = right - len(s1)
            count2[ord(s2[left]) - ord('a')] -= 1

            # Check if current window is a permutation of s1
            if count1 == count2:
                return True

        return False