def scrambler(source,save_as, destination):
    import docx
    import random
    filename = source.split("\\")[-1]
    doc = docx.Document(filename)
    
    keys = []
    text = []
    fulltext = []
    
    for para in doc.paragraphs:
        fulltext.append(para.text)
    fulltext = list(filter(None,fulltext))
    
    for i, v in enumerate(fulltext):
        if v[0].isdigit():
            keys.append(i)
    keys.append(len(fulltext))
    
    for i,v in enumerate(keys):
        current_item = v
        next_item = keys[(i + 1) % len(keys)]
        joined = "\n".join(fulltext[current_item:next_item])
        text.append(joined)
    
    text = list(filter(None,text))
    random.shuffle(text)
    str1 = destination
    str2 = "{}.docx".format(save_as)
    
    destination =  str1 + '\\' + str2
    doc_out = docx.Document()
    for item in text:
        doc_out.add_paragraph(item)
        doc_out.save(destination)

    return "File written to directory"