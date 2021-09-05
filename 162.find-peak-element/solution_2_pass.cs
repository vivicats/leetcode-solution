public class Solution {
    public int FindPeakElement(int[] nums)
    {
        return BinarySearch(nums, 0, nums.Length - 1);
    }

    private int BinarySearch(int[] nums, int left, int right)
    {
        if (left == right)
            return left;

        var mid = left + (right - left) / 2;

        if (nums[mid] < nums[mid + 1])
            return BinarySearch(nums, mid + 1, right);

        return BinarySearch(nums, left, mid);
    }
}