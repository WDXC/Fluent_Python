import unicodedata

from shave_marks_latin import shave_marks_latin
single_map = str.maketrans(""",ƒ,,†ˆ‹‘’“”•––˜›""",
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({
    '€': '<euro>',
    '…': '...',
    'OE': 'OE',
    '™': '(TM)',
    'oe': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)

def dewinize(txt):
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)