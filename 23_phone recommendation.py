#this is the program to suggest you the best phone in your budget
budget=int(input("enter your budget"))
if budget>=100000:
    print("ameer baap ki eklouti aulaad tumhare liye iphone best hai")
elif budget<100000 and budget>=50000:
    print("bhai iphone ke sapne mt hi dekho samsung aur one plus se kaam chalao")
elif budget<50000 and budget>=10000:
    print("motorola aur lava ya redmi se kaam chalao")
elif budget<10000 and budget>=5000:
    print("bete tumhari aukaat nokia ki hai")
else:
    print("tumhare liye voh barbie wala phone hi thik hai sunte rho dhoom machale dhoom machale dhoom")
