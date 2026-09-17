# Maximum Average Subarray I

**LeetCode 643** – Najlepší sliding-window prístup (O(n) časová zložitosť)

## Problém

Nájdi kontinuálny podpole dĺžky **k**, ktoré má **najvyššiu priemernú hodnotu** a vráť túto priemernú hodnotu.

### Príklad

## Riešenie – Sliding Window (Fixed Size)

```python
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k
