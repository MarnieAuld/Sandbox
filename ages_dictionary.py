ages_dict = {"Bill": 17, "Jane": 34, "Jack": 56, "Sven": 13}

new_ones = {name: age for name, age in ages_dict.items() if age < 18}
print(new_ones)