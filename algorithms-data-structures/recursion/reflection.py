def reflection_reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()

    if seq == emptySeq:
        return emptySeq

    restrev = reflection_reverse(seq[1:])
    first = seq[0:1]

    result = restrev + first

    return result

if __name__ == '__main__':
    print(reflection_reverse([1, 2, 3, 4, 5]))
    print(reflection_reverse('sekardayu'))