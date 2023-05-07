import sys

KEYCODE_MAP = {
    0x04: ('a', 'A'), 0x05: ('b', 'B'), 0x06: ('c', 'C'), 0x07: ('d', 'D'), 0x08: ('e', 'E'), 0x09: ('f', 'F'),
    0x0A: ('g', 'G'), 0x0B: ('h', 'H'), 0x0C: ('i', 'I'), 0x0D: ('j', 'J'), 0x0E: ('k', 'K'), 0x0F: ('l', 'L'),
    0x10: ('m', 'M'), 0x11: ('n', 'N'), 0x12: ('o', 'O'), 0x13: ('p', 'P'), 0x14: ('q', 'Q'), 0x15: ('r', 'R'),
    0x16: ('s', 'S'), 0x17: ('t', 'T'), 0x18: ('u', 'U'), 0x19: ('v', 'V'), 0x1A: ('w', 'W'), 0x1B: ('x', 'X'),
    0x1C: ('y', 'Y'), 0x1D: ('z', 'Z'),
    0x1E: ('1', '!'), 0x1F: ('2', '@'), 0x20: ('3', '#'), 0x21: ('4', '$'), 0x22: ('5', '%'), 0x23: ('6', '^'),
    0x24: ('7', '&'), 0x25: ('8', '*'), 0x26: ('9', '('), 0x27: ('0', ')'),
    0x28: '\n', 0x2C: ' ', 0x2D: ('-', '_'), 0x2E: ('=', '+'), 0x2F: ('[', '{'), 0x30: (']', '}'),
    0x31: ('\\', '|'), 0x33: (';', ':'), 0x34: ('\'', '\"'), 0x36: (',', '<'), 0x37: ('.', '>'), 0x38: ('/', '?')
}

def convert_keycodes(hex_data):
    result = ""
    shift = False
    for line in hex_data.splitlines():
        keycode = int(line[4:6], 16)
        modifier = int(line[2:4], 16)
        shift = (modifier == 0x20 or modifier == 0x22)

        if keycode != 0 and keycode in KEYCODE_MAP:
            if isinstance(KEYCODE_MAP[keycode], tuple):
                result += KEYCODE_MAP[keycode][shift]
            else:
                result += KEYCODE_MAP[keycode]
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_hex_data_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
        hex_data = f.read()

    keystrokes = convert_keycodes(hex_data)
    print(keystrokes)