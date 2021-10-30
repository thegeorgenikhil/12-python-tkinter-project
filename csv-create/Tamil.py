import csv
f=open("tamil.csv","w+",newline="")
mov_writer=csv.writer(f)
mov_writer.writerows([["No","Movie Name","Trailer"],
                      ["Ratsasan","https://www.youtube.com/watch?v=GsrN7rNch9Y"],
                      ["Peranbu","https://www.youtube.com/watch?v=1Nk7bEYIA7c"],
                      ["24","https://www.youtube.com/watch?v=wqXE_es_I3M"],
                      ["Sarkar","https://www.youtube.com/watch?v=VkkyaodksT4"],
                      ["Labaam","https://www.youtube.com/watch?v=e0gX_cFKEng"],
                      ["Vikramvedha","https://www.youtube.com/watch?v=1sVr-uWZPjE"],
                      ["I","https://www.youtube.com/watch?v=8uPK9Ov6Zd4"],
                      ["96","https://www.youtube.com/watch?v=r0synl-lI4I"],
                      ["Enthiran","https://www.youtube.com/watch?v=ODxHJasuCx4"],
                      ["Indian","https://www.youtube.com/watch?v=BbzKMT0MM7k"],
                      ["Nayakan","https://www.youtube.com/watch?v=XX25ea8PeFk"],
                      ["Super deluxe","https://www.youtube.com/watch?v=3-Xq_Zz3nPA"],
                      ["Ok kanmani","https://www.youtube.com/watch?v=2mBG4vlhcCc"],
                      ["Raavan","https://www.youtube.com/watch?v=7ZpY7_mpD4k"],
                      ["Bombay","https://www.youtube.com/watch?v=vIZmPQaDuI8"],
                      ["Thalapathy","https://www.youtube.com/watch?v=pC5yWXqb8Ys"],
                      ["Pithamagan","https://www.youtube.com/watch?v=rycv49ClLao"],
                      ["Anniyan","https://www.youtube.com/watch?v=bzAxJDtS7zE"],
                      ["Asuran","https://www.youtube.com/watch?v=vOCM9wztBYQ"],
                      ["Kaithi","https://www.youtube.com/watch?v=pC5yWXqb8Ys"],
                      ["Kannum kannum kolllaiyadithaal","https://www.youtube.com/watch?v=hPybzXeEWSI"],
                      ["Chekka chivantha vaanam","https://www.youtube.com/watch?v=x2q5w-ThJeE"],
                      ["Vaaranam aayiram","https://www.youtube.com/watch?v=QdM9L1FxFkY"],
                      ["Ghajini","https://www.youtube.com/watch?v=_I0xx8Oj3Ww"],
                      ["Naachiyaar","https://www.youtube.com/watch?v=DTtnh86GnTY"],
                      ["Anjaan","https://www.youtube.com/watch?v=MJxEQPMh_io"],
                      ["Kaththi","https://www.youtube.com/watch?v=bMf0IyzyKt4"],
                      ["Sethupathi","https://www.youtube.com/watch?v=dK5E8mzmD6w"],
                      ["Mankatha","https://www.youtube.com/watch?v=vHESM8iR1JE"],
                      ["Billa","https://www.youtube.com/watch?v=E2e6-Vi-VKs"],
                      ["Thambi","https://www.youtube.com/watch?v=y2vwIiLyt1Y"],
                      ["Madrasapattinam","https://www.youtube.com/watch?v=NrPKdhtovGw"],
                      ["Aarambam","https://www.youtube.com/watch?v=FltdImg7FPE"],
                      ["Vettaiyaadu Vilaiyaadu","https://www.youtube.com/watch?v=KSDAAqf6Img"],
                      ["Avvai Shanmughi","https://www.youtube.com/watch?v=D3ESUmGa9qY"],
                      ["Uttama Villain","https://www.youtube.com/watch?v=fD4F_dQgDUs"],
                      ["Aaranya Kaandam","https://www.youtube.com/watch?v=qBJ_UpyQw_s"],
                      ["Roja","https://www.youtube.com/watch?v=0GquoOZfkOc"],
                      ["Baasha","https://www.youtube.com/watch?v=1g-yZ3BDDK0"],
                      ["Oh Baby","https://www.youtube.com/watch?v=rinPndsJVrc"],
                      ["Oh my Kadavule","https://www.youtube.com/watch?v=5lUWBM2uYaQ"],
                      ["Anbe Sivam","https://www.youtube.com/watch?v=lPLN69KAukE"],
                      ["Mounaraagam","https://www.youtube.com/watch?v=zKN7LOs5Z5o"],
                      ["Alaipayuthe","https://www.youtube.com/watch?v=ez_XsttP9Es"],
                      ["papanaasam","https://www.youtube.com/watch?v=qTnYaTYl9RQ"],
                      ["Pariyerum perumal","https://www.youtube.com/watch?v=GMNsUxJe4R4"],
                      ["Visaaranai","https://www.youtube.com/watch?v=4mnzK2KIz9U"],
                      ["Joker","https://www.youtube.com/watch?v=4xr59w5r6Hw"],
                      ["Maanaragam","https://www.youtube.com/watch?v=R7MR12XOMGQ"],
                      ["Dhruvangal pathinaaru","https://www.youtube.com/watch?v=xpt2jfiL5GY"]])
                      
                      
f.close()

def Display():
    f=open("Tamil.csv","r")
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
    f=open("Tamil.csv","r")
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
    
