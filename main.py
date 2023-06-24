

# kitoblar haqidagi funksiyalar

   
book = {
    "Garri Poter":{
        "muallif":"bitta odam",
        "sotilgan":150,
        "yili":1230
    },
        "Hobbit":{
        "muallif":"tolkin",
        "sotilgan":2000,
        "yili":1700
    },
        "Aloviddin":{
        "muallif":"kimdur",
        "sotilgan":120,
        "yili":1900
    },

}
k = input("kitob nomini yozing:").title()


def myfunc():
 
    if k in book:
        print(f"{k} muallifi: {book[k]['muallif']} \n sotilgan: {book[k]['sotilgan']}  \n yili: {book[k]['yili']}")
    else:
        print("bu kitob mavjud emas")
        surash = input('xa yoki yuq : kiriting>>> ').lower()
        if surash == 'xa' or 'ha' or 'yes' or 'sa':
            
            mual = input("muallifi>>> ")
            sotilgan = int(input("sotilgan soni>>> "))
            yili = int(input("yilini kiriting>>> "))
            book[k] = {'muallif':mual , "sotilgan":sotilgan , "yili":yili }
            
            print(book)

        else:
            print("ok") 
