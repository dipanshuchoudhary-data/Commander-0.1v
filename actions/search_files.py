from pathlib import Path

def search_files(query:str,root="C:/"):
    matches = []

    for path in path(root).rglob("*"):
        if query.lower() in path.name.lower():
            matches.append(str(path))

        if len(matches) >= 20:
            break
    
    return matches if matches else "No files found."