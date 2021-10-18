format_tuple = ('Liverpool', 845.15, 21, 134, 358.45, 'price')

format = "The initial lot {} of ${} at the {} auction exceeded the expected {} by {}%, but the lot with number {} was nevertheless sold for ${}."
print(format.format(format_tuple[5], round(format_tuple[4], 1), format_tuple[0], format_tuple[5], format_tuple[2], str(format_tuple[3]).zfill(4), int(format_tuple[1])))