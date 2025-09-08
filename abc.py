# String metodlari:
# • capitalize: Stringning birinchi harfini katta qiladi.
# • count: Berilgan substringning nechta marta uchraganini hisoblaydi.
# • join: Elementlarni birlashtirib, yangi string hosil qiladi.
# • lower: Stringni kichik harflarga o'zgartiradi.
# • replace: Berilgan substringni boshqa substring bilan almashtiradi.
# • split: Stringni berilgan ajratgich bo'yicha bo'ladi.
# • upper: Stringni katta harflarga o'zgartiradi.
# List metodlari:
# • append: Liste yangi element qo'shadi.
# • clear: Liste ichidagi barcha elementlarni o'chiradi.
# • extend: Boshqa bir liste elementlarini qo'shadi.
# • insert: Berilgan indeksga yangi element qo'shadi.
# • remove: Berilgan elementni listdan o'chiradi.
# • sort: Listni tartiblaydi.
# Dictionary metodlari:
# • clear: Dictionaryni tozalaydi.
# • get: Berilgan kalitga mos qiymatni yoki standart qiymatni qaytaradi.
# • items: Dictionaryning kalit-qiymat juftlarini qaytaradi.
# • keys: Dictionaryning barcha kalitlarini qaytaradi.
# • values: Dictionaryning barcha qiymatlarini qaytaradi.
# Funktsiyalar:
# • abs: Sonning mutlaq qiymatini qaytaradi.
# • len: Ob'ektning uzunligini qaytaradi.
# • max, min: Berilgan argumentlardan eng katta yoki eng kichik qiymatni qaytaradi.
# • sum: Berilgan iterativ ob'ektning yig'indisini hisoblaydi.
# • sorted: Ob'ektni tartiblaydi va yangi list qaytaradi.
# Boshqa muhim kalit so'zlar:
# • def: Funktsiya e'lon qiladi.
# • class: Sinf e'lon qiladi.
# • if, else, elif: Shartli operatorlar.
# • for: Takrorlash (loop) operatori.
# • while: Takroriy shartli sikl operatori.


# 1. class - yangi klass (sinf) yaratish.
# 2. def - klass ichida metodlar (funksiyalar) yaratish.
# 3. self - klassning o'zini ko'rsatish, bu barcha instansiyalarda foydalaniladi.
# 4. init - bajarilish vaqtida yangi obyekt yaratishda chaqiriladigan konstruktor metodi.
# 5. str - obyektning matnli ifodasini berish uchun, print yoki str() bilan chaqiriladi.
# 6. repr - obyektni tavsiflovchi formatda qaytarish, asosan debugg qilish uchun.
# 7. inheritance (meros olish) - boshqa klassdan o'z xususiyatlarini va metodlarini olish.
# 8. super() - ota klassdagi metodlarga yoki xususiyatlarga murojaat qilish.
# 9. @property - klass atributini metod sifatida boshqarish.
# 10. del - obyekt bartaraf etilganda chaqiriladigan destructor metodi.


# 1. open() - faylni ochish uchun ishlatiladi. Bu funksiya faylga kirish va uni o'qish yoki yozish uchun kerak.
#    • Sintaksis: open('fayl_nomi', 'mod'), bu yerda mod - ochilish rejimi (masalan, 'r', 'w', 'a').
# 2. read() - fayldagi barcha ma'lumotlarni o'qish uchun ishlatiladi.
#    • Sintaksis: fayl.read()
# 3. readline() - fayldan bir qatorda ma'lumot o'qish uchun ishlatiladi.
#    • Sintaksis: fayl.readline()
# 4. readlines() - fayldagi barcha qatorlarni ro'yxat sifatida o'qish uchun ishlatiladi.
#    • Sintaksis: fayl.readlines()
# 5. write() - faylga ma'lumot yozish uchun ishlatiladi.
#    • Sintaksis: fayl.write('matn')
# 6. writelines() - ro'yxatdagi har bir elementni faylga yozish uchun ishlatiladi.
#    • Sintaksis: fayl.writelines(['qator1', 'qator2'])
# 7. close() - faylni yopish uchun ishlatiladi. Faylni yopmaslik resurslarni isrof qilishiga olib kelishi mumkin.
#    • Sintaksis: fayl.close()
# 8. with open - faylni avtomatik ravishda yopish uchun foydalidir. Bu kontekst menejeri yordamida fayl bilan ishlashni soddalashtiradi.
#    • Sintaksis: 
#           with open('fayl_nomi', 'mod') as fayl:
#          # fayl bilan ishlash
# 9. seek() - fayldagi kursorning joylashuvini o'zgartirish uchun ishlatiladi.
#    • Sintaksis: fayl.seek(offset, whence)
# 10. tell() - fayl ichidagi joriy kursor pozitsiyasini olish uchun ishlatiladi.
#     • Sintaksis: fayl.tell()

