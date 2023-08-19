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
