def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value

    return averager