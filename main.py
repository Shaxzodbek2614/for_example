# Kirish nuqtasi: ismni so'raydi, o'yinni o'ynatadi, oxirida rekordlarni ko'rsatadi.
# Ishga tushirish: python3 main.py
import sys

import oyin
import storage


def ismni_sora():
    """O'yinchi ismini so'raydi, bo'sh ism qabul qilinmaydi."""
    while True:
        ism = input("Ismingiz nima? ").strip()
        if ism:
            return ism
        print("Ism bo'sh bo'lmasin, qaytadan yozing.")


def oyinchi_tanlovini_sora():
    """O'yinchi tanlovini qaytaradi yoki o'yindan chiqmoqchi bo'lsa None qaytaradi."""
    while True:
        javob = input("Tanlang (1 tosh, 2 qaychi, 3 qog'oz, 0 chiqish): ").strip()
        if javob == "0":
            return None
        if javob.isdigit() and int(javob) in oyin.TANLOVLAR:
            return oyin.TANLOVLAR[int(javob)]
        # Noto'g'ri javob raund hisoblanmaydi, qayta so'raymiz
        print(f"\"{javob}\" noto'g'ri. Faqat 0, 1, 2 yoki 3 kiriting.")


def rekordlar_jadvalini_chiqar(rekordlar):
    """Rekordlar jadvalini ekranga chiqaradi."""
    print("\n=== Rekordlar (ketma-ket g'alabalar) ===")
    if not rekordlar:
        print("Hali rekord yo'q.")
        return
    for orin, rekord in enumerate(rekordlar, start=1):
        print(f"{orin}. {rekord['ism']} — {rekord['ketma_ket_galabalar']} ta ({rekord['sana']})")


def oyinni_oyna(ism):
    """5 raundlik o'yinni o'ynatadi. Oxirigacha o'ynalsa hisobni, to'xtatilsa None qaytaradi."""
    hisob = oyin.yangi_hisob()
    natija_matnlari = {
        "oyinchi": "Siz yutdingiz!",
        "kompyuter": "Kompyuter yutdi.",
        "durang": "Durang.",
    }

    for raund in range(1, oyin.RAUNDLAR_SONI + 1):
        print(f"\n--- {raund}-raund ---")
        oyinchi_tanlovi = oyinchi_tanlovini_sora()
        if oyinchi_tanlovi is None:
            print("O'yin to'xtatildi. Natija saqlanmadi.")
            return None

        kompyuter_tanlovi = oyin.kompyuter_tanlovi()
        natija = oyin.raund_golibini_aniqla(oyinchi_tanlovi, kompyuter_tanlovi)
        oyin.hisobni_yangila(hisob, natija)

        print(f"Siz: {oyinchi_tanlovi}  |  Kompyuter: {kompyuter_tanlovi}")
        print(f"{natija_matnlari[natija]}  Hisob: {ism} {hisob['oyinchi']} : {hisob['kompyuter']} Kompyuter")

    golib = oyin.oyin_golibi(hisob)
    yakuniy_matnlar = {
        "oyinchi": f"Tabriklaymiz, {ism}! O'yinda siz g'olib bo'ldingiz.",
        "kompyuter": "Bu safar kompyuter g'olib. Yana urinib ko'ring!",
        "durang": "O'yin durang bilan tugadi.",
    }
    print(f"\n{yakuniy_matnlar[golib]}")
    print(f"Ketma-ket eng ko'p g'alabangiz: {hisob['eng_uzun_seriya']}")
    return hisob


def main():
    print("=== Tosh-qaychi-qog'oz ===")
    ism = ismni_sora()
    hisob = oyinni_oyna(ism)
    if hisob is None:
        return 0

    try:
        if hisob["eng_uzun_seriya"] > 0:
            # Faqat kamida bitta g'alaba bo'lsa, rekord sifatida saqlaymiz
            rekordlar = storage.rekord_qosh(ism, hisob["eng_uzun_seriya"])
        else:
            rekordlar = storage.rekordlarni_oqi()
    except storage.RekordlarXatosi as xato:
        print(f"\nXato: {xato}", file=sys.stderr)
        return 1

    rekordlar_jadvalini_chiqar(rekordlar)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        # Ctrl+C bosilganda uzun xato matni o'rniga qisqa xabar chiqaramiz
        print("\nO'yin to'xtatildi.")
        sys.exit(130)
