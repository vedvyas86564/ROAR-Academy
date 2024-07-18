import PyPDF2 
file_handle = open('Sense-n-Sensibility-by-Jane-Austen.pdf', 'rb') 
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 
page_object = pdfReader.pages[0]    # We just get page 0 as example 
page_text = page_object.extract_text()   # this is the str type of full page
page_list = list(page_text.split('\n'))
words_list = list(page_text.split())
print(words_list)

frequency_table = dict()
for word in words_list:
    if(not word == ' ' and not word.isnumeric() and not word == "CHAPTER" and not word == "page"): 
        if(word in frequency_table):
            frequency_table[word] = frequency_table[word] + 1
        else:
            frequency_table[word] = 1

print(frequency_table)