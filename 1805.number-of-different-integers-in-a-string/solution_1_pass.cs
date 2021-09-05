public class Solution {
    public int NumDifferentIntegers(string word)
    {
        var startIndex = 0;
        var set = new HashSet<string>();

        for (var i = 0; i < word.Length; i++)
        {
            if (word[i] >= '0' && word[i] <= '9')
            {
                startIndex += startIndex < i && word[startIndex] == '0' ? 1 : 0;
            }
            else
            {
                if (startIndex < i)
                {
                    set.Add(word.Substring(startIndex, i - startIndex));
                }

                startIndex = i + 1;
            }
        }

        if (startIndex < word.Length)
        {
            set.Add(word.Substring(startIndex));
        }

        return set.Count;
    }
}