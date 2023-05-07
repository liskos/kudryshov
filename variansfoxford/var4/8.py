k = 0
for s1 in "1234567":
    for s2 in "01234567":
        for s3 in "01234567":
            for s4 in "01234567":
                for s5 in "01234567":
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count("5") == 1 and ((int(s1) % 2 == 0 and int(s2) % 2 != 0) or (int(s1) % 2 != 0 and int(s2) % 2 == 0))
