import csv
f=open("English.csv","w+",newline="")
wtrobj=csv.writer(f)
wtrobj.writerows([["Birds of prey","https://youtu.be/kGM4uYZzfu0"],
                  ["The Invisible Man","https://www.youtube.com/watch?v=WO_FJdiY9dA"],
                  ["Black Panther","https://www.youtube.com/watch?v=xjDjIWPwcPU"],
                  ["Mission:Impossible-Fallout","https://www.youtube.com/watch?v=wb49-oV0F78"],
                  ["Mulan","https://www.youtube.com/watch?v=KK8FHdFluOQ"],
                  ["UP","https://www.youtube.com/watch?v=pkqzFUhGPJg"],
                  ["Freaky Friday","https://www.youtube.com/watch?v=nZ8KJ4MzzOw"],
                  ["Apollo 13","https://www.youtube.com/watch?v=KtEIMC58sZo"],
                  ["Coco","https://www.youtube.com/watch?v=Rvr68u6k5sI"],
                  ["The Underwater","https://www.youtube.com/watch?v=jCFWEzIVILc"],
                  ["Black Widow","https://www.youtube.com/watch?v=ybji16u608U"],
                  ["2001: A Space Odyssey (1968)","https://youtu.be/Z2UWOeBcsJI"],
                  ["The Dark Knight","https://www.youtube.com/watch?v=EXeTwQWrcwY"],
                  ["Once Upon a Time in Hollywood","https://www.youtube.com/watch?v=ELeMaP8EPAA"],
                  ["Call Me By Your Name ","https://youtu.be/Z9AYPxH5NTM"],
                  ["The Hurt Locker","https://www.youtube.com/watch?v=AIbFvqFYRT4"],
                  ["Eden","https://www.youtube.com/watch?v=EXxQ52VaJPQ"],
                  ["Stories We Tell","https://www.youtube.com/watch?v=A_8BnZ471GY"],
                  ["Capernaum","https://www.youtube.com/watch?v=ULUo0048xZE"],
                  ["Love & Friendship","https://youtu.be/8MaSK3POHI0"],
                  ["The Conjuring 2","https://www.youtube.com/watch?v=VFsmuRPClr4"],
                  ["Joker","https://www.youtube.com/watch?v=-_DJEzZk2pc"],
                  ["Ghostbusters","https://www.youtube.com/watch?v=w3ugHP-yZXw"],
                  ["Annabelle Comes Home","https://www.youtube.com/watch?v=bCxm7cTpBAs"],
                  ["The Shallows","https://www.youtube.com/watch?v=EgdxIlSuB70"],
                  ["Bruce Almighty","https://www.youtube.com/watch?v=0XBxoKumlqQ"],
                  ["Get Out","https://www.youtube.com/watch?v=DzfpyUB60YY"],
                  ["Captain America: Civil War","https://www.youtube.com/watch?v=dKrVegVI0Us"],
                  ["Guardians Of The Galaxy","https://www.youtube.com/watch?v=d96cjJhvlMA"],
                  ["A Prophet","https://www.youtube.com/watch?v=l69ARbQt-Ko"],
                  ["Batman Begins","https://www.youtube.com/watch?v=neY2xVmOfUM"],
                  ["Avatar","https://www.youtube.com/watch?v=6ziBFh3V1aM"],
                  ["Toy Story 3","https://www.youtube.com/watch?v=JcpWXaA2qeg"],
                  ["Wall-E","https://www.youtube.com/watch?v=qGBZWbg_26A"],
                  ["Captain America: The Winter Soldier","https://www.youtube.com/watch?v=7SlILk2WMTI"],
                  ["Star Wars: The Force Awakens","https://www.youtube.com/watch?v=sGbxmsDFVnE"],
                  ["Avengers: Endgame","https://www.youtube.com/watch?v=TcMBFSGVi1c"],
                  ["Disney's Aladdin","https://www.youtube.com/watch?v=foyufD52aog"],
                  ["Wonder Woman","https://www.youtube.com/watch?v=1Q8fG0TtVAY"],
                  ["Inside Out","https://www.youtube.com/watch?v=WIDYqBMFzfg"],
                  ["Avengers: Infinity War","https://www.youtube.com/watch?v=6ZfuNTqbHE8"],
                  ["Incredibles 2","https://www.youtube.com/watch?v=i5qOzqD9Rms"],
                  ["Moana","https://www.youtube.com/watch?v=yfCOEGyHMwc"],
                  ["Finding Dory","https://www.youtube.com/watch?v=0tkLUap7oGQ"],
                  ["Ratatouille","https://www.youtube.com/watch?v=uVeNEbh3A4U"],
                  ["The Chronicles of Narnia: The Voyage of the Dawn Treader","https://www.youtube.com/watch?v=hrJQDPpIK6I"],
                  ["Margaret","https://www.youtube.com/watch?v=7YAiS-3EhMI"],
                  ["Lights Out","https://www.youtube.com/watch?v=6LiKKFZyhRU"],
                  ["Logan","https://www.youtube.com/watch?v=Div0iP65aZo"],
                  ["Assassin's Creed (film)","https://www.youtube.com/watch?v=gfJVoF5ko1Y"]])
f.close()     


def Display():
    f=open("English.csv","r")
    mov_reader=csv.reader(f)
    Var=0
    next(mov_reader)
    try:
        for rec in mov_reader:
            print(rec[0])
            Var+=1
        print("Total Number of Movies In the database:",Var,"movies")
    except IndexError:
        pass
    f.close()

def Search():
    f=open("English.csv","r")
    mov_reader=csv.reader(f)
    Movie_Name=input("Enter the Movie Name that you want to Search:")
    Var=False
    for rec in mov_reader:
        if rec[0].casefold()==Movie_Name.casefold():
            Var=True
    if Var==True:
        print("Movie Found")
    else:
        print("Movie Not Found!")
    

while True:
    var=input("1.Press D to display the movies in the database.\n2.Press S to search if a movie is in the database.\n3.Press E to Exit.\n")
    #if var in "Aa":
        #Add()
    if var in "Dd":
        Display()
    elif var in "Ss":
        Search()
    elif var in "Ee":
        break
    else:
        continue
    



