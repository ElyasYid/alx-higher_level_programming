#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    titles = dir(hidden_4)
    for title in titles:
        if title[:2] != "__":
            print(title)
