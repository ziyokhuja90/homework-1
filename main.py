
# bu yangi funksiya
def hisobla(*ism):
    """
        bu hisoblash uchun funksiya. sizdan hozir 2 ta son va amalni so'raymiz
    """
    
    umumiy = sum(ism)
    return umumiy


hisobla = hisobla(*range(1,20))

print(hisobla)