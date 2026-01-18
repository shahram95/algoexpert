def semordnilap(words):
    buffer = set(words)
    out_lst = list()

    for word in words:
        reverse = word[::-1]

        if reverse in buffer and word in buffer and word != reverse:
            out_lst.append([word,reverse])
            buffer.remove(word)
            buffer.remove(reverse)
    return out_lst