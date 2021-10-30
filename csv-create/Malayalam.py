import csv
f=open("Malayalam.csv","w+",newline="")
mov_writer=csv.writer(f)
mov_writer.writerows([["Movie Name","Trailer"],
                      ["Shylock","https://www.youtube.com/watch?v=yuroURGFllQ"],
                      ["Trance","https://www.youtube.com/watch?v=uSudz8zb2I8"],
                      ["Driving license","https://www.youtube.com/watch?v=8pXjSuTdV7o"],
                      ["Oppam","https://www.youtube.com/watch?v=YKXq5jTuQSc"],
                      ["Odiyan","https://www.youtube.com/watch?v=e1BHZ4Jtg-A"],
                      ["Kumbalangi nights","https://www.youtube.com/watch?v=3P4BFBSafF0"],
                      ["Forensic","https://www.youtube.com/watch?v=zTBzGaiAzwY"],
                      ["Mamangam","https://www.youtube.com/watch?v=hCU_B_QKVR4"],
                      ["Madhura raja","https://www.youtube.com/watch?v=qhOtGVRGfSg"],
                      ["Masterpiece","https://www.youtube.com/watch?v=1vOck2Nguso"],
                      ["Puthan panam","https://www.youtube.com/watch?v=IyJAhnrAmUE"],
                      ["Pokkiri raja","https://www.youtube.com/watch?v=om8Ce6oLclk"],
                      ["Lucifer","https://www.youtube.com/watch?v=x1-Ya0NZQso"],
                      ["Love action drama","https://www.youtube.com/watch?v=nmd2M-3k-Ds"],
                      ["Christian brothers","https://www.youtube.com/watch?v=m0PmnALzVD4"],
                      ["Premam","https://www.youtube.com/watch?v=pbgvTikmIMk"],
                      ["Kayamkulam kochunni","https://www.youtube.com/watch?v=0XO03BdZi2Y"],
                      ["Pathinettan padi","https://www.youtube.com/watch?v=22rLzgXTC8g"],
                      ["Abrahaminte santhathikal","https://www.youtube.com/watch?v=1jhbgD4BGvM"],
                      ["Ramaleela","https://www.youtube.com/watch?v=j3UN0nF_KbE"],
                      ["Bangalore days","https://www.youtube.com/watch?v=uVpHL5g4buY"],
                      ["Jomonte suvisheshangal","https://www.youtube.com/watch?v=dmYUI536bZI&list=PL07fTLkdmLo7W94SiqFgxxHcTSRJAS2bR&index=2&t=0s"],
                      ["Maheshinte prathikaram","https://www.youtube.com/watch?v=Fdz7NUf9G5w&list=PLIU90_mrhapP1acGNZpoHehUEyVTPUntl&index=63"],
                      ["Iyobinte Pusthakam","https://www.youtube.com/watch?v=IbD5Baz0kOI"],
                      ["CIA","https://www.youtube.com/watch?v=f5nvCp0QFdA"],
                      ["Kammara Sambhavam","https://www.youtube.com/watch?v=UKkNcfTvVjI"],
                      ["Drishyam","https://www.youtube.com/watch?v=AuuX2j14NBg"],
                      ["Munthirivallikal Thalirkkumbol","https://m.youtube.com/watch?v=8qHITluVfX8&list=PLkXZ7hMQPTvCdKwgOWHjel2Minn8DFVKu&index=5&t=0s"],
                      ["Puthiya Niyamam","https://www.youtube.com/watch?v=dX8snwD0MEA"],
                      ["Charlie","https://www.youtube.com/watch?v=oYxtLNJJ54Y"],
                      ["Puthiya Mugham","https://www.youtube.com/watch?v=TwgNaNXsOMY"],
                      ["Action hero biju","https://www.youtube.com/watch?v=bJgV9eC0GJE"],
                      ["Ohm shanthi Oshaana","https://www.youtube.com/watch?v=M5-mzpNvnrY"],
                      ["Varathan","https://www.youtube.com/watch?v=STHwR_ZzEGU"],
                      ["Amar Akbar Anthony","https://www.youtube.com/watch?v=s3Q6AM4MDs4"],
                      ["Pretham","https://www.youtube.com/watch?v=EjIYhkH3ztw&list=PLw94rwVRhBKV0IbcFfS7BynYsp-x30VuC&index=21"],
                      ["Vikramadithyan","https://www.youtube.com/watch?v=mUCWhRnBb7s"],
                      ["Take off","https://www.youtube.com/watch?v=vzYSKjxtKNg"],
                      ["Solo","https://www.youtube.com/watch?v=BXCUqa9cboI&list=PLaENq2b0ZqjWb0oJj1VBXnfRHYu9L2Or9&index=10&t=0s"],
                      ["Moothon","https://www.youtube.com/watch?v=XqHGkcvDAEE&list=PLhiVAW-D5_GC8DJX9X7l-6FTndxV2TBwV&index=46"],
                      ["Sakhavu","https://www.youtube.com/watch?v=VRqEXJ-bpZI&list=PLTihxqJD1mfAc4y9nCWLgWskn0UGmzsPh"],
                      ["Mr. Fraud","https://www.youtube.com/watch?v=URZkb9AxkQI"],
                      ["Anjaam Pathiraa","https://www.youtube.com/watch?v=dn5KZD1E67Y"],
                      ["Virus","https://www.youtube.com/watch?v=38MijVTyP7s"],
                      ["Kettyolaanu Ente Malakha","https://www.youtube.com/watch?v=wxyi6zkC1G4"],
                      ["Helen","https://www.youtube.com/watch?v=Z12zJCpj95w"],
                      ["Pretham 2","https://www.youtube.com/watch?v=j3uaKtT7PtE"],
                      ["Jamna Pyari","https://www.youtube.com/watch?v=ScyhCXI9VzE"],
                      ["Big Brother","https://www.youtube.com/watch?v=GAY3jdx1PoA"],
                      ["Thoppil Joppan","https://www.youtube.com/watch?v=B7RBtZGbj2Q"],
                      ["Unda","https://www.youtube.com/watch?v=KxeMmKULuZk"],
                      ["Velipadinte Pusthakam","https://www.youtube.com/watch?v=wch_ORhMU5g"],
                      ["Pulimurugan","https://www.youtube.com/watch?v=blQUlD8g4Pk"],
                      ["Pullikkaran Staraa","https://www.youtube.com/watch?v=hez3gYfnra4"],
                      ["Pathemari","https://www.youtube.com/watch?v=a95a2qy_fl4"],
                      ["Thrissur pooram","https://www.youtube.com/watch?v=X-lcmMNli_w"],
                      ["Jacobinte Swargarajyam","https://www.youtube.com/watch?v=ydHzDHz12fw"],
                      ["Rajamanikam","https://www.youtube.com/watch?v=hez3gYfnra4"],
                      ["Varane Avashyamund","https://www.youtube.com/watch?v=M3i-VGCY69c"],
                      ["Sudani from Nigeria","https://www.youtube.com/watch?v=EHyaTJGmN4k"],
                      ["Angamaly Diaries","https://www.youtube.com/watch?v=4yRBJCrjabU"],
                      ["Thondimuthalum Driksakshiyum","https://www.youtube.com/watch?v=f2zG7g4AVoQ"],
                      ["Njan Prakashan","https://www.youtube.com/watch?v=8EVi5VByNNg"],
                      ["Ustad hotel","https://www.youtube.com/watch?v=rhfVeDnd7-M"],
                      ["Oru vadakkan selfie ","https://www.youtube.com/watch?v=7s0uX2u6b5w"],
                      ["Aadu","https://www.youtube.com/watch?v=4fiZ52yj4b4"],
                      ["Aadu 2","https://www.youtube.com/watch?v=_jlVhEs75Fo"],
                      ["Kuttanadan Marpappa","https://www.youtube.com/watch?v=0rUe8b6EL90"],
                      ["Parole","https://www.youtube.com/watch?v=jnhHC8xKznE"],
                      ["Aravindante Athidhikal","https://www.youtube.com/watch?v=5YIThlVcjbU"],
                      ["Kunjiramayanam","https://www.youtube.com/watch?v=iSxYYphno1s"],
                      ["The Great Father","https://www.youtube.com/watch?v=eqE4L87RI7E"],
                      ["Honey Bee 2","https://www.youtube.com/watch?v=ynKvrmsBQmY"],
                      ["Honey Bee 2.5","https://www.youtube.com/watch?v=elYLAAlr320"],
                      ["Darvinte Parinamam","https://www.youtube.com/watch?v=jGuBc-AvNxk"]])

f.close()

def Display():
    f=open("Malayalam.csv","r")
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
    f=open("Malayalam.csv","r")
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
    
