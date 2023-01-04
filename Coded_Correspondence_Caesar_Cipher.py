import string

def caesar(message, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = message.maketrans(alphabet, shifted_alphabet)
    return message.translate(table)

# Cipher 10
message_one = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
message_two = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
# Cipher 14
message_three = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'

decoded_message = caesar(message_three, 10)
