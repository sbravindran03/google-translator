from googletrans import Translator
sen = str(input('Enter the sentence :'))
k = Translator()
lang=str(input('your language:'))
convert =str(input('which language:'))
output= k.translate(sen,src=lang,dest=convert)
print(output.text)