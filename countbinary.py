
class Binary():
    def __init__(self, s):

        if len(s)%2 == 0:
            string_counter = len(s)
        else:
            string_counter = len(s) -1

        divisibles = [i for i in range(1, string_counter+1) if i % 2 == 0]

        print(divisibles)

        sq_counter = 0
        sq_counter_list = []

        for d in divisibles:
            for k in range(len(s)):
                sequence = s[k:k+d]

                if len(sequence) == d:
                    if sequence.count('1') == sequence.count('0'):
                        for i in range(len(sequence)):
                            s1 = 0
                            s0 = 0
                            sq_track = []


                            b = i
                            while b != len(sequence) and sequence[b] == '1' :
                                s1 += 1
                                b += 1

                            c = b
                            while c != len(sequence) and sequence[c] == '0' :
                                s0 += 1
                                c += 1

                            # i = c

                            if s1 == s0:
                                sq_track.append(True)
                            else:
                                sq_track.append(False)

                            # print(sq_track)

                            if i == len(sequence) -1:
                                # print(sequence, d)
                                if not sq_track.__contains__(False):
                                    sq_counter_list.append(sequence)
                                    # print(sequence)
                                    sq_counter += 1


                            elif sequence[i] == '0':
                                c = i
                                while c != len(sequence)  and sequence[c] == '0':
                                    s0 += 1
                                    c += 1

                                b = c
                                while b != len(sequence) and sequence[b] == '1':
                                    s1 += 1
                                    b += 1

                                i = b

                                print(f"Sequence {sequence} and s1 {s1} and s0 {s0}")

                                if s1 == s0:
                                    sq_track.append(True)
                                else:
                                    sq_track.append(False)

                                print(sq_track)

                                if i == len(sequence) - 1:
                                    if not sq_track.__contains__(False):
                                        sq_counter_list.append(sequence)
                                        # print(sequence)
                                        sq_counter += 1



        print(sq_counter_list, sq_counter)


if __name__ == '__main__':
    b = Binary('110101000010101010')

