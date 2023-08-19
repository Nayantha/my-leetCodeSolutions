# https://leetcode.com/problems/simplify-path/
def simplify_path(path: str) -> str:
    return path.replace("//", "/").removesuffix("/").replace("..", "").replace("/.", "/")
