
#Part 1
def sumIncrease(nums):
    count = 0
    last = nums[0] if nums else 0
    for i in nums[1:]:
        if last < i:
            count += 1
        last = i
    
    return count


nums1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
assert sumIncrease(nums1) == 7, "should be 7"

nums2 = [199, 200, 200, 210]
assert sumIncrease(nums2) == 2, "should be 2"

nums3 = []
assert sumIncrease(nums3) == 0, "should be 0"

nums4 = [1]
assert sumIncrease(nums4) == 0, "should be 0"

#I store the input in a txt
with open('input_q1.txt', "r") as f:
    array = [int(line) for line in f]

print(sumIncrease(array))

#part 2
def sumIncreaseWindow(nums):
    count = 0
    l = 0
    for r in range(len(nums)):
        if r - l < 3:
            continue
        else:
            if nums[l] < nums[r]:
                count += 1
            l += 1
    
    return count

assert sumIncreaseWindow(nums1) == 5, "should be 5"

assert sumIncreaseWindow(nums2) == 1, "should be 1"

assert sumIncreaseWindow(nums3) == 0, "should be 0"

assert sumIncreaseWindow(nums4) == 0, "should be 0"

print(sumIncreaseWindow(array))




