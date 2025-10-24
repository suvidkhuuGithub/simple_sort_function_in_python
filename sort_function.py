def sort(w, h, l, m):
    if (max(w, h, l) >= 150 or w * h * l >= 1_000_000) and m >= 20:
        return "REJECTED"
    if max(w, h, l) >= 150 or w * h * l >= 1_000_000 or m >= 20:
        return "SPECIAL"
    return "STANDARD"
