ques=["Fransanın başkenti.","Mesiz macunu ile ünlü ilimiz.","01 plaka kodlu ilimiz",
      "Python dilinin yazarı","bir dairenin çevresinin çapına bölümü ile elde edilen irrasyonel matematik sabiti",
      "Galatasaray hangi yıl UEFA kupasını almıştır?","İstiklal Marşı hangi yıl yazılmıştır?",
      "Dünya Sağlık Örgütünün Kısaltılmış İsmi","Türkiye’nin En Yüksek Dağı",
      "Alım Gücünün Azalması Olayına Ne Ad Verilir?"]

ans=["paris","manisa","adana","guido van rossum","pi sayısı","2000","1921","who","ağrı dağı","enflasyon"]
puan=0
print("-"*50)
print("10 soruluk bilgi yarışmamıza Hoşgeldiniz")
print("-"*50)
for n in range(len(ques)):
    print(f"{n+1}. soru \n",ques[n],end=":")
    cevap=input()
    cevap=cevap.lower()
    if(cevap==ans[n]):
        print("Cevap doğru")
        puan+=10
    else:
        print("Cevap yanlış","Doğrusu:",ans[n])
if(puan>50):
    print("TEBRİKLER")
    print(f"Bilgi yarışmamızı {puan} alarak başarı ile tamamladınız")
else:
    print(f"Bilgi yarışmamızda {puan} alarak başarısız oldunuz")
    
    
    
