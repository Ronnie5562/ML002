import argparse
dummy_text = """
    Lor29em ips3um do4lor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor5. 
    Aenean massa. Cum soc64iis natoque penatibus et magnis dis part4urient montes, nas9cetur ridiculus mus. 
    Done2c qua5m feli6s, ultri235cies nec, p6ellentesque e88u, pr7etium quis, sem. Nul2la 2consequat mas1sa quis enim. 
    Don3ec pede jdusto, fri1ngdilla vel, al55quet nec, vul4putate eget, arc6u. In en7im ju11sto, rhoncus ut, imperdiet a, venenatis vitae, jus5to. Nul8lam dict1um felis eu pede mollis preti443um. 
    Int2eger tinci4dunt. Cras dap3ibus. Viva3mus elem3entum s2empe24r nisi. Ae3nean vuldp3utate ele3iend tellus. 
    Aenean leo ligu3la, porttitor eu, CAST ME ÑOT vitae, eleif3end ac, enim. Aliq7uam 6lor3em a5n5te, dapibus in, viverra quis, feug56iat a, t6ell3us. Phasellus7 viverra8 n6ulla3 ut 3metus varius la2ore3et. 
    Qui56squ4e r2utr2u3m. Aen2ea2n imp7erdie2t. 3Etia2m 3ult4ric2ies ni52si vel augue. 
    Curabi5tur ullamcorp6er ultricie8s nisi.9 
    Nam eg9et du0i.
"""

words = dummy_text.split()

without_digit = [''.join('x' if letter.isdigit() else letter for letter in word) for word in words]

ascii_text = [word.encode('ascii', errors='replace').decode('ascii')
             for word in without_digit]


new_lines = [word + '\n' if word.endswith('.') else word for word in ascii_text]

LINE_SIZE = 80
lines = []
line = ''

for word in new_lines:
    if line.endswith('\n') or len(line) + len(word) + 1 > LINE_SIZE:
        lines.append(line)
        line = ''
    line = line + ' ' + word

#print('\n'.join(lines))

#_________________________________________________________________

import delorean

log = "[2023-05-5T11-09-56-235658] - SALE - PRODUCT: 1345 - PRICE: $09.99"
divide_it = log.split(' - ')
print(divide_it)


timestamp_string, _, product_string, price_string = divide_it
parsed = timestamp_string.strip('[]')
#timestamp = delorean.parse(parsed)
#print(parstimestamped)

#_________________________________________________________

from parse import parse

FORMAT = '[{date}] - SALE - PRODUCT: {product} - PRICE: ${price}'
result = parse(FORMAT, log)
print(result)


FORMAT2 = '{email}'
result2 = parse(FORMAT2, log)
print(result2)