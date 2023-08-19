# https://leetcode.com/problems/simplify-path/
def simplify_path(path: str) -> str:
    path_stack = []
    folder_names = [folder_name for folder_name in path.removesuffix("/").replace("//", "/").split("/") if folder_name]
    for folder_name in folder_names:
        if folder_name == "..":
            if len(path_stack):
                path_stack.pop()
        elif folder_name == ".":
            continue
        else:
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
