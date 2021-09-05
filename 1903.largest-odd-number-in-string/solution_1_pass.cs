public class Solution {
    public string LargestOddNumber(string num)
    {
        var endIndex = num.Length;

        while (endIndex > 0 && num[endIndex - 1] % 2 == 0)
        {
            endIndex--;
        }

        return num.Substring(0, endIndex);
    }
}