# O'yin mantig'i: tanlovlar, raund g'olibi, hisob va ketma-ket g'alabalar.
# Bu faylda fayl o'qish/yozish ham, input()/print() ham yo'q.
import random

RAUNDLAR_SONI = 5  # Bir o'yindagi raundlar soni

# Raqam -> tanlov nomi (o'yinchi shu raqamlarni kiritadi)
TANLOVLAR = {1: "tosh", 2: "qaychi", 3: "qog'oz"}

# Har bir tanlov qaysi tanlovni yengishi
NIMANI_YENGADI = {"tosh": "qaychi", "qaychi": "qog'oz", "qog'oz": "tosh"}


def kompyuter_tanlovi():
    """Kompyuter uchun tasodifiy tanlov qaytaradi."""
    return random.choice(list(TANLOVLAR.values()))


def raund_golibini_aniqla(oyinchi_tanlovi, kompyuter_tanlovi):
    """Raund natijasini qaytaradi: "oyinchi", "kompyuter" yoki "durang"."""
    if oyinchi_tanlovi not in NIMANI_YENGADI or kompyuter_tanlovi not in NIMANI_YENGADI:
        # Noma'lum tanlov kelsa, jim o'tib ketmaymiz, xatoni ochiq aytamiz
        raise ValueError(f"Noma'lum tanlov: {oyinchi_tanlovi!r} yoki {kompyuter_tanlovi!r}")
    if oyinchi_tanlovi == kompyuter_tanlovi:
        return "durang"
    if NIMANI_YENGADI[oyinchi_tanlovi] == kompyuter_tanlovi:
        return "oyinchi"
    return "kompyuter"


def yangi_hisob():
    """O'yin boshidagi bo'sh hisobni qaytaradi."""
    return {
        "oyinchi": 0,           # O'yinchi ochkolari
        "kompyuter": 0,         # Kompyuter ochkolari
        "joriy_seriya": 0,      # Hozirgi ketma-ket g'alabalar
        "eng_uzun_seriya": 0,   # O'yin davomidagi eng uzun ketma-ket g'alabalar
    }


def hisobni_yangila(hisob, natija):
    """Raund natijasiga qarab hisob va ketma-ket g'alabalarni yangilaydi."""
    if natija == "oyinchi":
        hisob["oyinchi"] += 1
        hisob["joriy_seriya"] += 1
        hisob["eng_uzun_seriya"] = max(hisob["eng_uzun_seriya"], hisob["joriy_seriya"])
    elif natija == "kompyuter":
        hisob["kompyuter"] += 1
        hisob["joriy_seriya"] = 0  # Mag'lubiyat seriyani nolga tushiradi
    elif natija == "durang":
        hisob["joriy_seriya"] = 0  # Durang ham seriyani nolga tushiradi
    else:
        raise ValueError(f"Noma'lum raund natijasi: {natija!r}")


def oyin_golibi(hisob):
    """O'yin oxiridagi g'olibni qaytaradi: "oyinchi", "kompyuter" yoki "durang"."""
    if hisob["oyinchi"] > hisob["kompyuter"]:
        return "oyinchi"
    if hisob["kompyuter"] > hisob["oyinchi"]:
        return "kompyuter"
    return "durang"
