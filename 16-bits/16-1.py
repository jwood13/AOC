test_strings = {'8A004A801A8002F478': 16,
                '620080001611562C8802118E34': 12,
                'C0015000016115A2E0802F182340': 23,
                'A0016C880162017C3686B18A3D4780': 31}
test_strings = ['D2FE28', '38006F45291200', 'EE00D40C823060', '8A004A801A8002F478',
                '620080001611562C8802118E34', 'C0015000016115A2E0802F182340', 'A0016C880162017C3686B18A3D4780']

test_answers = [6, 9, 14, 16, 12, 23, 31]


class string_queue():
    def __init__(self, string):
        self.position = 0
        self.string = string

    def __repr__(self) -> str:
        return self.string[self.position:]

    def get_char(self, num_characters):
        output = self.string[self.position:self.position + num_characters]
        self.position += num_characters
        return output

    def is_done(self):
        if len(self.string)-self.position < 10 and sum([int(x) for x in self.string[self.position:]]) == 0:
            return True
        else:
            return False


def hex_to_bin(char):
    '''convert hexadecimal character to a binary character'''
    return bin(int(char, 16))[2:].zfill(4*len(char))


def bin_to_dec(number):
    '''Convert a binary string to a decimal'''
    return int(number, 2)


def pop_string(string, length):
    value = string[:length]
    string.pop(0)
    return value


def process_packet(bitcode):
    # print('--------\n', bitcode)
    version_number = bin_to_dec(bitcode.get_char(3))
    # print(bitcode)
    type_id = bitcode.get_char(3)
    # print(f'v:{version_number}, t:{type_id}')
    if type_id == '100':
        continue_bit = '1'
        literal_binary = ''
        while continue_bit == '1':
            continue_bit = bitcode.get_char(1)
            literal_binary += bitcode.get_char(4)
        # print(f'value:{bin_to_dec(literal_binary)}')
    else:
        mode = bitcode.get_char(1)
        if mode == '0':
            package_length = bin_to_dec(bitcode.get_char(15))
            version_number += process_packet(
                string_queue(bitcode.get_char(package_length)))
        else:
            num_subpackets = bin_to_dec(bitcode.get_char(11))
            # print('looping', num_subpackets)
            # for i in range(num_subpackets):
            #     print('loop', i)
            version_number += process_packet(bitcode)
    if bitcode.is_done():
        return version_number
    else:
        return version_number + process_packet(bitcode)


def decode_message(message):
    val = process_packet(string_queue(hex_to_bin(message)))
    return val


for i in range(len(test_strings)):
    known = test_answers[i]
    trial = decode_message(test_strings[i])
    assert(trial == known)

message = open('input.txt').readline().strip()
print(decode_message(message))
