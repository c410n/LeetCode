public class Solution
{
    public int UniquePaths(int _rows, int _cols)
    {
        if (_rows <= 1 || _cols <= 1)
            return 1;

        BigInteger C = 1;
        int pascal_column = _cols - 1;
        BigInteger pascal_row = _cols + _rows - 2;

        foreach (int index in Enumerable.Range(0, pascal_column))
        {
            Func<BigInteger, BigInteger, BigInteger> binomial_cfs = (BigInteger n, BigInteger k) =>
            {
                return (C * BigInteger.Subtract(n, k) / (k + 1));
            };


            C = binomial_cfs(pascal_row, index);
        }

        return (int)C;
    }
}