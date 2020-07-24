a = ['<span class="mobilesv icon-dc"></span>',
 '<span class="mobilesv icon-fe"></span>',
 '<span class="mobilesv icon-ji"></span>',
 '<span class="mobilesv icon-yz"></span>',
 '<span class="mobilesv icon-hg"></span>',
 '<span class="mobilesv icon-ba"></span>',
 '<span class="mobilesv icon-ji"></span>',
 '<span class="mobilesv icon-yz"></span>',
 '<span class="mobilesv icon-vu"></span>',
 '<span class="mobilesv icon-po"></span>',
 '<span class="mobilesv icon-ji"></span>',
 '<span class="mobilesv icon-po"></span>',
 '<span class="mobilesv icon-rq"></span>',
 '<span class="mobilesv icon-rq"></span>',
 '<spanclass="mobilesv icon-ji"></span>',
 '<span class="mobilesv icon-yz"></span>']





l = ['ji', 'yz', 'vu', 'po', 'ji', 'po', 'rq', 'rq', 'ji', 'yz']

#   {'NAME': 'Shree S S Properties and De..', 'Contact': '+(91)-9136965591'}














def extract_number(s):
    p = s.split("-")
    number_list = []
    number_string = "+(91)-"
    for i in range(len(p)):
        p1 = p[i].split('''"''')
        if i != 0:
            number_list.append(p1[0])

    for i in number_list[6:]:
        if i == "ji":
            number_string += "9"
        elif i == "lk":
            number_string += "8"
        elif i == "nm":
            number_string += "7"
        if i == "po":
            number_string += "6"
        elif i == "rq":
            number_string += "5"
        elif i == "ts":
            number_string += "4"
        if i == "vu":
            number_string += "3"
        elif i == "wx":
            number_string += "2"
        elif i == "yz":
            number_string += "1"
        elif i == "acb":
            number_string += "0"

    return number_string