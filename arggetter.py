def arggetter(*positions):
    def getter(*args, **kwargs):
        if len(positions) == 1:
            return args[positions[0]]
        return tuple(args[pos] for pos in positions)
    return getter

get_first = arggetter(0)
get_first_and_third = arggetter(0, 2)

print(get_first('a', 'b', 'c'))         
print(get_first_and_third('a', 'b', 'c'))  