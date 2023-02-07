for codec in ['latin_1', 'utf_8', 'utf-16']:
    print(codec, 'E1 Niño'.encode(codec), sep='\t')
    