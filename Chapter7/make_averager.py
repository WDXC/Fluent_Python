def make_average():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager