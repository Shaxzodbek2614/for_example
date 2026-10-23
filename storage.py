# rekordlar.json faylini o'qish va unga yozish. O'yin qoidalari bu yerda yo'q.
import json
from datetime import date
from pathlib import Path

# Rekordlar fayli shu papkada turadi (dastur qayerdan ishga tushirilishidan qat'i nazar)
REKORDLAR_FAYLI = Path(__file__).parent / "rekordlar.json"
JADVALDAGI_ORINLAR = 5  # Jadvalda saqlanadigan eng yaxshi natijalar soni


class RekordlarXatosi(Exception):
    """rekordlar.json faylini o'qib yoki yozib bo'lmaganda chiqadigan xato."""


def rekordlarni_oqi():
    """Rekordlar ro'yxatini qaytaradi. Fayl bo'lmasa, bo'sh ro'yxat bilan yaratadi."""
    if not REKORDLAR_FAYLI.exists():
        rekordlarni_yoz([])
        return []

    try:
        matn = REKORDLAR_FAYLI.read_text(encoding="utf-8")
        rekordlar = json.loads(matn)
    except json.JSONDecodeError as xato:
        # Buzilgan faylni indamasdan o'chirmaymiz, foydalanuvchiga aytamiz
        raise RekordlarXatosi(
            f"{REKORDLAR_FAYLI.name} fayli buzilgan ({xato.lineno}-qator): "
            "faylni tuzating yoki o'chirib yuboring."
        ) from xato
    except OSError as xato:
        raise RekordlarXatosi(f"{REKORDLAR_FAYLI.name} faylini o'qib bo'lmadi: {xato}") from xato

    if not isinstance(rekordlar, list):
        raise RekordlarXatosi(f"{REKORDLAR_FAYLI.name} ichida ro'yxat ([...]) bo'lishi kerak.")
    return rekordlar


def rekordlarni_yoz(rekordlar):
    """Rekordlar ro'yxatini faylga yozadi."""
    try:
        REKORDLAR_FAYLI.write_text(
            json.dumps(rekordlar, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except OSError as xato:
        raise RekordlarXatosi(f"{REKORDLAR_FAYLI.name} fayliga yozib bo'lmadi: {xato}") from xato


def rekord_qosh(ism, ketma_ket_galabalar):
    """Yangi natijani qo'shadi, eng yaxshi 5 tasini saqlaydi va jadvalni qaytaradi."""
    rekordlar = rekordlarni_oqi()
    rekordlar.append({
        "ism": ism,
        "ketma_ket_galabalar": ketma_ket_galabalar,
        "sana": date.today().isoformat(),
    })
    # Ko'p g'alabali natijalar yuqorida turadi
    rekordlar.sort(key=lambda rekord: rekord["ketma_ket_galabalar"], reverse=True)
    eng_yaxshilari = rekordlar[:JADVALDAGI_ORINLAR]
    rekordlarni_yoz(eng_yaxshilari)
    return eng_yaxshilari
