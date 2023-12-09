with open("input.txt", "r") as f:
    lines = f.read().splitlines()

def get_differences(nums: list[int]) -> list[int]:
    return [*map(lambda x, y: y - x, nums, nums[1:])]

def repeat(nums: list[int]) -> list[list[int]]:
    diffs = get_differences(nums)
    if all(d == 0 for d in diffs):
        return [diffs]
    return repeat(diffs) + [diffs]

def interpolate(nums: list[list[int]], idx: int):
    if idx == len(nums): return nums
    nxt = nums[idx-1][-1] + nums[idx][-1]
    nums[idx].append(nxt)
    return interpolate(nums, idx + 1)

def sol(lines: list[str]):
    for l in lines:
        nums = [*map(int, l.split())]
        diffs = repeat(nums) + [nums]
        yield interpolate(diffs, 1)[-1][-1]
        
print(sum(sol(lines)))