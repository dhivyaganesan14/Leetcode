class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # best solution using hash set O(1) time for lookup
        # O(n) by default because we need to lookup at every element atleast once.
        elementSeen = set()
        for duplicateValue in nums:
            if duplicateValue in elementSeen:
                return True 
            elementSeen.add(duplicateValue)
        return False