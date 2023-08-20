# https://leetcode.com/problems/simplify-path/
def simplify_path(path: str) -> str:
    """
    Simplify the path.
    Replace '//' with '/'.
    Ignore './'.
    Remove previous folder when encounter '../'.
    :param path: the string containing the complex path.
    :return: Simplified path.
    """
    path_stack = []
    folder_names = path.split("/")
    for folder_name in folder_names:
        if folder_name == "." or not folder_name:
            continue
        if folder_name == "..":
            if path_stack:
                path_stack.pop()
                continue
        path_stack.append(folder_name)
    return "/" + "/".join(path_stack)


def simplify_path_ii(path: str) -> str:
    stack = []
    cur = ""
    for c in path + "/":
        if c == "/":
            if cur == "..":
                if stack:
                    stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
        else:
            cur += c
    return "/" + "/".join(stack)
