# CLAUDE.md

Bu papkada terminalda o'ynaladigan **"Tosh-qaychi-qog'oz"** o'yini quriladi. Til: Python 3, faqat standart kutubxona (tashqi paketlar o'rnatilmaydi).

## O'yin nima qiladi

O'yinchi kompyuterga qarshi o'ynaydi. Bir o'yin **5 raunddan** iborat. Har raundda o'yinchi tanlov qiladi, kompyuter esa tasodifiy tanlaydi. Natija ekranga chiqadi va hisob yangilanadi.

O'yin boshida o'yinchi ismini kiritadi. O'yin oxirida g'olib e'lon qilinadi va rekordlar jadvali ko'rsatiladi.

## Qoidalar

- **Tosh** qaychini yengadi.
- **Qaychi** qog'ozni yengadi.
- **Qog'oz** toshni yengadi.
- Ikkala tomon bir xil narsani tanlasa, raund **durang** bo'ladi va hech kimga ochko berilmaydi.
- O'yinchi tanlovni raqam bilan kiritadi: `1` tosh, `2` qaychi, `3` qog'oz. `0` kiritilsa, o'yin to'xtaydi.
- Noto'g'ri kiritilgan javob raund hisoblanmaydi. Dastur xatoni aytadi va qayta so'raydi.
- 5 raunddan keyin ochkosi ko'p tomon yutadi. Ochkolar teng bo'lsa, o'yin durang tugaydi.

## Rekord

Rekord — **ketma-ket eng ko'p g'alaba** (bir o'yin ichida, raundlar bo'yicha). Durang yoki mag'lubiyat ketma-ketlikni nolga tushiradi.

Rekordlar `rekordlar.json` faylida saqlanadi. Jadvalda eng yaxshi 5 ta natija turadi: o'yinchi ismi, ketma-ket g'alabalar soni va sana.

## Fayl tuzilmasi

| Fayl | Vazifasi |
|---|---|
| `main.py` | Kirish nuqtasi. Ismni so'raydi, o'yinni boshlaydi, oxirida rekordlarni ko'rsatadi. Ishga tushirish: `python3 main.py` |
| `oyin.py` | O'yin mantig'i: tanlovlar, raund g'olibini aniqlash, hisob, ketma-ket g'alabalarni sanash. Fayl o'qish/yozish bu yerda **bo'lmaydi**. |
| `storage.py` | `rekordlar.json` faylini o'qish va unga yozish. O'yin qoidalari bu yerda **bo'lmaydi**. |
| `rekordlar.json` | Rekordlar ro'yxati (JSON). Fayl bo'lmasa, `storage.py` uni bo'sh ro'yxat bilan yaratadi. |

## Kod yozish qoidalari

- **Izohlar o'zbek tilida** (lotin yozuvida) yoziladi. Ekranga chiqadigan matnlar ham o'zbekcha bo'ladi.
- **Funksiya va o'zgaruvchi nomlari tushunarli bo'lsin.** Nomdan nima qilishi bilinib tursin: `raund_golibini_aniqla()`, `rekordlarni_oqi()`. `f1()`, `x`, `tmp` kabi nomlar ishlatilmaydi.
- **Xatolarni yashirma.** `except: pass` yoki xatoni jimgina yutib yuboradigan kod yozilmaydi. Xato bo'lsa, foydalanuvchiga tushunarli xabar chiqarilsin yoki xato yuqoriga uzatilsin. Masalan, `rekordlar.json` buzilgan bo'lsa, buni ochiq aytish kerak, faylni indamasdan o'chirib tashlash mumkin emas.
- **Har o'zgarishdan keyin nima qilganingni 3 gapda tushuntir:** nimani o'zgartirding, nima uchun, va qanday tekshirding.
