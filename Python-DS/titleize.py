def titleize(phrase):
    return ' '.join(word.capitalize() for word in phrase.split())

print(titleize('this is awesome'))
print(titleize('oNLY capITALize fIRSt'))