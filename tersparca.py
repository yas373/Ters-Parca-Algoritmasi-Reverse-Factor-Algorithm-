# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
from suffix_trees import STree                  #suffix tree oluşturmak için kütüphane

def bul(aranacak,cumle):
    
    st = STree.STree(aranacak)                  #aradığımız kelimenin suffix treesini oluşturuyoruz

    index=len(aranacak)-1                       #diziler 0. elemandan başladığı için dizide aranacak kelimenin boyutunun 1 eksiğine konumlanıyoruz 
    ilerlenecek=0                               #her işlemin sonunda kaç eleman ilerleyeceğimizi belirleyen değişken
    ara_deger=""                                #arama esnasında oluşturulan kelime grupları

    while len(cumle)>index:    
        for i in range(len(aranacak)):
            ara_deger=cumle[index-i]+ara_deger
            ara_deger=ara_deger.lower()        #gelen veri büyük küçük harf karışık da olsa hepsini küçülterek işleme alıyoruz
            sonuc=st.find(ara_deger)           #oluşturulan ara değerin suffix ağacımızda olup olmadığına bakıyoruz
            if sonuc==-1:                      #sonuc -1 ise eşleşmeyen bir cümle bulundu demektir bu durumda aramayı en son eşleşen bölüme kadar kaydırıyoruz
                ilerlenecek=len(aranacak)-i    
                #print(ilerlenecek)
                break
            elif(ara_deger==aranacak):
                print(index-(len(aranacak)-1))
                break
        
        if ara_deger==aranacak:
            index=index+1
        index=index+ilerlenecek
        ilerlenecek=0
        ara_deger=""

bul("yasin","sosxoxmyastklyasindir")
bul("deli","deldeldeldeldeldeldeldeldeldelideldeldeldel")