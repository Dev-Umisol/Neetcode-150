# Neetcode practice problems

#! Contains Duplicate
    #? Given an inter array nums, return true if any value appears more than once in the array, otherwise return false
        #? Ex 1: Input: nums = [1, 2, 3, 3] Output: true
        #? Ex 2: Input: nums = [1, 2, 3, 4] Output: false

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set() # <-- set is unique only
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            
            seen.add(nums[i])
        return False
    
print(Solution().hasDuplicate([1, 2, 3, 3]))
print(Solution().hasDuplicate([1, 2, 3, 4]))

#* -------------------------------------------------------------------------

#! Valid Anagram
    #? Given two strings s and t, return true if the two strings are anagrams of each other otherwise return false
    #? An anagram is a string that contants the exact same characters as another string, but the order of the characters can be different
        #? Ex 1: Input: s = "racecar", t = "carrace" Output: true
        #? Ex 2: Input: s = "jar", t = "jam" Output: false
    #? Constraints: s and t consist of lowercase Enlgish letters

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        