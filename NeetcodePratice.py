# Neetcode practice problems

#! Contains Duplicate
    #? Given an inter array nums, return true if any value appears more than once in the array, otherwise return false
        #? Ex 1: Input: nums = [1, 2, 3, 3] Output: true
        #? Ex 2: Input: nums = [1, 2, 3, 4] Output: false

print('hasDuplicate')

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

print("\n")
#* -------------------------------------------------------------------------
print("----------------------Separator----------------------------\n")

#! Valid Anagram
    #? Given two strings s and t, return true if the two strings are anagrams of each other otherwise return false
    #? An anagram is a string that contants the exact same characters as another string, but the order of the characters can be different
        #? Ex 1: Input: s = "racecar", t = "carrace" Output: true
        #? Ex 2: Input: s = "jar", t = "jam" Output: false
    #? Constraints: s and t consist of lowercase Enlgish letters
    
print('isAnagram')

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # <-- return false if words arent same length
        
        hashS, hashT = {}, {}
        
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        
        return hashS == hashT
print(Solution().isAnagram("racecar", "carrace"))
print(Solution().isAnagram("jar", "jam"))

print("\n")
#* -------------------------------------------------------------------------
print("----------------------Separator----------------------------\n")

#! Two Sum
    #? Given an array of intergers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j
    #? You may assume that every input has exactly one pair of indices i and j that satisfy the conditions
    #? Return the answer with the smaller index first
        #? Ex 1: Input: nums = [3, 4, 5, 6], target = 7 Output: [0, 1]
        #? Ex 2: Input: nums = [4, 5, 6], target = 10 Ouput: [0, 2]
        #? Ex 3: Input: nums = [5, 5], target = 10 Output: [0, 1]
    #? Constraints: 2 <= nums.length <= 1000
    #? -10,000,000 <= nums[i] <= 10,000,000
    #? -10,000,000 <= target <= 10,000,000
    #? Only one valid answer exists

print('twoSum')

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[nums[i]] = i
            
print(Solution().twoSum([3, 4, 5, 6], 7))
print(Solution().twoSum([4, 5, 6], 10))
print(Solution().twoSum([5, 5], 10))

print("\n")
#* -------------------------------------------------------------------------
print("----------------------Separator----------------------------\n")

#! Remove Duplicates from Sorted Array
    #? Given an integer array nums sorted in non-decreasing order, remove the duplicates in
    #? place such that each unique element appears only once. The relative order of the elements should be kept the same.
    #? Then return the number of unique elements in nums.
    #? Consider the number of unique elements of nums to be k, to get accepted,
    
print('removeDuplicates')

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 1
        # left is writer variable, i is reader variable
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[left] = nums[i]
                left += 1
        return left

print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

print("\n")
#* -------------------------------------------------------------------------
print("----------------------Separator----------------------------\n")