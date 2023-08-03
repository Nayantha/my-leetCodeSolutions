# https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150
def convert(s: str, num_rows: int) -> str:
    """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
    if num_rows == 1:
        return s
    zigzag_str = ""
    for row in range(num_rows):
        increment = 2 * (num_rows - 1)
        for i in range(row, len(s), increment):
            zigzag_str += s[i]
            if 0 < row < num_rows - 1 and i + increment - 2 * row < len(s):
                zigzag_str += s[i + increment - 2 * row]
    return zigzag_str
