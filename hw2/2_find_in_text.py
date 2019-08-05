"""
    * Find and count top 10 words in text
Задание №2 (Посложнее)
Есть текст, который лежит в string.
Надо убрать из него все знаки препинания, и найти сколько раз встречается
каждое слово. Вывести TOP-10 самых встречающихся слов, с указанием,
какое это слово и сколько раз оно встретилось.
"""

text = """
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
 doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
  veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
   ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
    consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.
    Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet,
    consectetur, adipisci velit, sed quia non numquam eius modi tempora
    incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim
    ad minima veniam, quis nostrum exercitationem ullam corporis suscipit
    laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel
    eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae
     consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
"""


def find_count(text):
    new_text = text.replace('?', '').replace(',', '')
    new_text = text.replace('.', '').replace('\n', '')
    splitted = ''.join(new_text).split()

    temp = {}
    for word in splitted:
        if word not in temp:
            temp[word] = 1
        else:
            temp[word] += 1

    sorted_temp = sorted(temp.items(), key=lambda k: k[1], reverse=True)
    return sorted_temp[:10]


print(find_count(text))
