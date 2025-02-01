def hex_to_ascii(hex_string):
    try:
        # Remove spaces and non-hex characters
        hex_string = hex_string.replace(" ", "").replace("\n", "").replace("\r", "")
        # Convert hex to bytes
        bytes_object = bytes.fromhex(hex_string)
        # Convert bytes to ascii string
        ascii_string = bytes_object.decode("ascii")
        return ascii_string
    except Exception as e:
        return f"Error: {e}"

cipher_text = '''1 1977 8 0003689 0 240228022034BAZIRAMWABOGabrielBCCÒUq98ªªq)(á¥¥q␦ÄÄô©âVÄlÄ
ÿ÷.A¦¢lÿW¤

À
Ä
ÄÿÿaÊ111111j­9¡9%bE/¨C/F$>FBÆ,=+ÁnnE*ÄÉ£EJW´
8)Ê8ý
I·ÉC,ÊL ;I*ãJD(
%       f4If!/
+Å;@8ß¬E
©¥
I¢ÎY␦²EÑ\­ha¥+Ñ[-È␦FQN¦aÕ       ␦%ÝX¨^[$ëJ4gaK3bO¤Ã"R␦×f\§&ê
Fm¥ªUABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''

# Attempt hexadecimal decoding
ascii_result = hex_to_ascii(cipher_text)
print(f"Decoded Hexadecimal output: {ascii_result}")
