from pathlib import Path

import fitz


ROOT = Path(__file__).parent
IMG = ROOT / "gambar"
OUTPUT = ROOT / "Laporan_Eksperimen_Pertumbuhan_Salman_Fidinillah.pdf"
FONT_REGULAR = Path("C:/Windows/Fonts/arial.ttf")
FONT_BOLD = Path("C:/Windows/Fonts/arialbd.ttf")

NAVY = (0.08, 0.16, 0.29)
BLUE = (0.13, 0.34, 0.62)
PALE = (0.92, 0.95, 0.98)
INK = (0.13, 0.16, 0.20)
MUTED = (0.37, 0.42, 0.48)
WHITE = (1, 1, 1)
GREEN = (0.12, 0.42, 0.32)


def add_text(page, x, y, text, size=11, color=INK, font="helv"):
    bold = font == "hebo"
    page.insert_text(
        (x, y),
        text,
        fontsize=size,
        fontname="Arial-Bold" if bold else "Arial",
        fontfile=str(FONT_BOLD if bold else FONT_REGULAR),
        color=color,
    )


def add_box(page, rect, fill=PALE, stroke=None, radius=0.04):
    page.draw_rect(
        fitz.Rect(rect),
        color=stroke or fill,
        fill=fill,
        width=0.8,
        radius=radius,
    )


def add_paragraph(page, rect, text, size=11, color=INK, align=0):
    page.insert_textbox(
        fitz.Rect(rect),
        text,
        fontsize=size,
        fontname="Arial",
        fontfile=str(FONT_REGULAR),
        color=color,
        lineheight=1.3,
        align=align,
    )


def add_header(page, section, page_no, landscape=False):
    width = page.rect.width
    page.draw_rect(fitz.Rect(0, 0, width, 12), color=NAVY, fill=NAVY)
    add_text(page, 42, 34, "EKSPERIMEN PYTHON", 9, BLUE, "hebo")
    add_text(page, width - 82, 34, f"{page_no:02}", 9, MUTED)
    page.draw_line(fitz.Point(42, 43), fitz.Point(width - 42, 43), color=(0.82, 0.86, 0.90), width=0.7)


def add_footer(page, page_no):
    y = page.rect.height - 26
    page.draw_line(fitz.Point(42, y - 12), fitz.Point(page.rect.width - 42, y - 12), color=(0.82, 0.86, 0.90), width=0.7)
    add_text(page, 42, y, "Kompleksitas Algoritma | Salman Fidinillah", 8, MUTED)
    add_text(page, page.rect.width - 60, y, f"{page_no} / 7", 8, MUTED)


def add_title(page, title, subtitle=None):
    add_text(page, 42, 72, title, 22, NAVY, "hebo")
    if subtitle:
        add_text(page, 42, 92, subtitle, 10, MUTED)


def add_image(page, path, rect):
    image_path = IMG / path
    if not image_path.exists():
        raise FileNotFoundError(f"Screenshot tidak ditemukan: {image_path}")
    bounds = fitz.Rect(rect)
    page.draw_rect(bounds, color=(0.82, 0.86, 0.90), width=0.8)
    inner = fitz.Rect(bounds.x0 + 4, bounds.y0 + 4, bounds.x1 - 4, bounds.y1 - 4)
    page.insert_image(inner, filename=str(image_path), keep_proportion=True, overlay=True)


def add_table(page, x, y, widths, headers, rows, row_h=27, font_size=10):
    total_w = sum(widths)
    page.draw_rect(fitz.Rect(x, y, x + total_w, y + row_h), color=NAVY, fill=NAVY)
    cursor_x = x
    for width, header in zip(widths, headers):
        add_text(page, cursor_x + 8, y + 18, header, font_size, WHITE, "hebo")
        cursor_x += width
    for row_index, row in enumerate(rows):
        top = y + row_h * (row_index + 1)
        fill = WHITE if row_index % 2 else PALE
        page.draw_rect(fitz.Rect(x, top, x + total_w, top + row_h), color=(0.84, 0.88, 0.92), fill=fill, width=0.5)
        cursor_x = x
        for width, value in zip(widths, row):
            add_text(page, cursor_x + 8, top + 18, str(value), font_size, INK)
            cursor_x += width


def build_pdf():
    doc = fitz.open()
    a4 = (595, 842)
    wide = (842, 595)

    # 1. Sampul dan ringkasan hasil.
    page = doc.new_page(width=a4[0], height=a4[1])
    page.draw_rect(fitz.Rect(0, 0, a4[0], 290), color=NAVY, fill=NAVY)
    add_text(page, 48, 70, "LAPORAN PRAKTIKUM", 10, (0.72, 0.82, 0.94), "hebo")
    add_paragraph(page, (48, 103, 535, 193), "Eksperimen Python:\nMemahami Pertumbuhan Operasi", 29, WHITE)
    add_text(page, 48, 223, "Kompleksitas Algoritma | Tugas Pengantar", 12, (0.82, 0.88, 0.96))
    add_box(page, (42, 315, 553, 447), WHITE, (0.84, 0.88, 0.92))
    add_text(page, 60, 342, "IDENTITAS MAHASISWA", 10, BLUE, "hebo")
    add_text(page, 60, 373, "Nama", 10, MUTED)
    add_text(page, 170, 373, "Salman Fidinillah", 12, INK, "hebo")
    add_text(page, 60, 404, "NIM", 10, MUTED)
    add_text(page, 170, 404, "2025061007", 12, INK, "hebo")
    add_text(page, 60, 435, "Kelas", 10, MUTED)
    add_text(page, 170, 435, "Semester 3", 12, INK, "hebo")
    add_text(page, 42, 492, "RINGKASAN HASIL EKSPERIMEN", 10, BLUE, "hebo")
    add_table(page, 42, 507, [90, 190, 190], ["n", "Satu perulangan", "Dua perulangan"], [[5, 5, 25], [10, 10, 100], [20, 20, 400]], 30, 10)
    add_paragraph(page, (48, 638, 535, 703), "Satu perulangan menghasilkan n operasi (O(n)). Dua perulangan bersarang yang masing-masing berjalan n kali menghasilkan n² operasi (O(n²)).", 12, NAVY)
    add_paragraph(page, (48, 752, 535, 790), "Tujuan laporan: menjalankan program, menghitung operasi, membandingkan pertumbuhan, dan membaca grafik hasil percobaan.", 9, MUTED)
    add_footer(page, 1)

    # 2. Prediksi awal dan percobaan linear.
    page = doc.new_page(width=a4[0], height=a4[1])
    add_header(page, "Prediksi dan Percobaan 1", 2)
    add_title(page, "Satu Perulangan", "Prediksi awal dan hasil hitung operasi linear")
    add_box(page, (42, 110, 553, 201))
    add_text(page, 58, 135, "C. SEBELUM MULAI: TEBAK DULU", 10, BLUE, "hebo")
    add_paragraph(page, (58, 148, 530, 190), "Satu baris berisi 5 balok. Grid 5 × 5 berisi 25 balok.\nJumlah balok pada grid dihitung dengan 5 × 5 = 25.", 11)
    add_text(page, 42, 233, "D. PERCOBAAN 1 — SATU PERULANGAN", 12, NAVY, "hebo")
    add_paragraph(page, (42, 246, 550, 282), "Perulangan berjalan n kali, sehingga jumlah operasi bertambah mengikuti n.", 10, MUTED)
    add_table(page, 42, 292, [160, 170, 180], ["Jumlah data (n)", "Jumlah operasi", "Pengamatan"], [[5, 5, "ikut bertambah"], [10, 10, "ikut bertambah"], [20, 20, "ikut bertambah"]], 28, 9)
    add_text(page, 42, 420, "Screenshot kode Percobaan 1", 9, MUTED)
    add_image(page, "percobaaan linier.png", (42, 432, 553, 715))
    add_footer(page, 2)

    # 3. Grid dua perulangan dan pertanyaan grid.
    page = doc.new_page(width=a4[0], height=a4[1])
    add_header(page, "Percobaan 2", 3)
    add_title(page, "Dua Perulangan", "Perulangan bersarang membentuk jumlah operasi kuadrat")
    add_text(page, 42, 121, "E. HASIL PERCOBAAN", 12, NAVY, "hebo")
    add_paragraph(page, (42, 135, 550, 181), "hitung_grid(3) menghasilkan 9, bukan 3, karena untuk setiap putaran perulangan luar, perulangan dalam berjalan 3 kali.", 10)
    add_table(page, 42, 191, [160, 190, 160], ["Jumlah data (n)", "Jumlah operasi", "Perhitungan"], [[3, 9, "3 × 3"], [5, 25, "5 × 5"], [10, 100, "10 × 10"]], 28, 9)
    add_text(page, 42, 313, "Screenshot kode Percobaan 2", 9, MUTED)
    add_image(page, "percobaan grid.png", (42, 324, 553, 570))
    add_box(page, (42, 590, 553, 714))
    add_text(page, 58, 615, "F. MENGGAMBAR GRID DI PIKIRAN", 10, BLUE, "hebo")
    add_paragraph(page, (58, 630, 532, 695), "Jika n = 10, jumlah operasi = 10 × 10 = 100. Perulangan pertama berjalan 10 kali; untuk setiap putaran, perulangan kedua berjalan 10 kali. Jadi jumlah operasi = n × n = n².", 10)
    add_footer(page, 3)

    # 4. Percobaan grafik, orientasi landscape agar kode dan grafik terbaca.
    page = doc.new_page(width=wide[0], height=wide[1])
    add_header(page, "Grafik Pertumbuhan", 4, landscape=True)
    add_title(page, "Pertumbuhan Jumlah Operasi", "G. Kode percobaan dan grafik hitung_grid(n)")
    add_text(page, 42, 115, "KODE", 9, BLUE, "hebo")
    add_text(page, 440, 115, "HASIL RUNNING", 9, BLUE, "hebo")
    add_image(page, "grafik pertumbuhan.png", (42, 126, 410, 526))
    add_image(page, "pertumbuhann.png", (426, 126, 800, 455))
    add_box(page, (426, 470, 800, 526))
    add_paragraph(page, (438, 481, 787, 518), "Grafik naik semakin cepat. Nilai n = 20 menunjukkan pertumbuhan terbesar; jumlah operasi bertambah semakin cepat mengikuti n².", 9, NAVY)
    add_footer(page, 4)

    # 5. Pembacaan grafik dan tabel perbandingan.
    page = doc.new_page(width=a4[0], height=a4[1])
    add_header(page, "Analisis Perbandingan", 5)
    add_title(page, "Membaca dan Membandingkan Grafik", "H. Pengamatan grafik dan I. perbandingan jumlah operasi")
    add_box(page, (42, 111, 553, 292))
    add_text(page, 58, 137, "H. MEMBACA GRAFIK", 11, BLUE, "hebo")
    add_paragraph(page, (58, 153, 530, 273), "1. Ketika n bertambah, grafik naik.\n2. Ya, grafik naik semakin cepat ketika n semakin besar.\n3. Pertumbuhan terbesar terjadi pada n = 20.\n4. Jumlah operasi bertambah semakin cepat karena jumlahnya mengikuti n².", 11)
    add_text(page, 42, 332, "I. PERBANDINGAN OPERASI", 12, NAVY, "hebo")
    add_table(page, 42, 348, [90, 190, 190], ["n", "Satu perulangan", "Dua perulangan"], [[5, 5, 25], [10, 10, 100], [20, 20, 400]], 30, 10)
    add_box(page, (42, 493, 553, 687))
    add_text(page, 58, 519, "JAWABAN PENGAMATAN", 10, BLUE, "hebo")
    add_paragraph(page, (58, 536, 530, 672), "Pada n = 5 dan n = 20, dua perulangan menghasilkan lebih banyak operasi. Selisihnya semakin besar ketika n meningkat. Ini terjadi karena perulangan dalam berjalan n kali untuk setiap putaran perulangan luar, sehingga total operasi menjadi n × n.", 11)
    add_footer(page, 5)

    # 6. Bukti kode dan grafik perbandingan.
    page = doc.new_page(width=wide[0], height=wide[1])
    add_header(page, "Grafik Perbandingan", 6, landscape=True)
    add_title(page, "Perbandingan Pertumbuhan Operasi", "I. Kode dan hasil running satu perulangan vs dua perulangan")
    add_text(page, 42, 115, "KODE", 9, BLUE, "hebo")
    add_text(page, 440, 115, "HASIL RUNNING", 9, BLUE, "hebo")
    add_image(page, "grafik perbandingan.png", (42, 126, 410, 526))
    add_image(page, "perbandingan.png", (426, 126, 800, 440))
    add_box(page, (426, 456, 800, 526))
    add_paragraph(page, (438, 467, 787, 518), "Garis biru menunjukkan n operasi (O(n)); garis oranye menunjukkan n² operasi (O(n²)). Pada n = 20, hasilnya 20 dan 400 operasi.", 9, NAVY)
    add_footer(page, 6)

    # 7. Pola, pertanyaan pemahaman, dan notasi.
    page = doc.new_page(width=a4[0], height=a4[1])
    add_header(page, "Kesimpulan", 7)
    add_title(page, "Pola Pertumbuhan dan Kesimpulan", "J. Menemukan pola | K. Pemahaman | L. Notasi kompleksitas")
    add_box(page, (42, 112, 553, 251))
    add_text(page, 58, 138, "J. POLA YANG DITEMUKAN", 11, BLUE, "hebo")
    add_paragraph(page, (58, 154, 530, 233), "Satu perulangan: 5 → 10 → 20 operasi, mengikuti n.\nDua perulangan: 25 → 100 → 400 operasi, mengikuti n².\nNotasi pertumbuhannya masing-masing O(n) dan O(n²).", 11)
    add_box(page, (42, 271, 553, 490))
    add_text(page, 58, 297, "K. PERTANYAAN PEMAHAMAN", 11, BLUE, "hebo")
    add_paragraph(page, (58, 313, 530, 474), "1. Satu perulangan: hitung_linear().\n2. Perulangan di dalam perulangan: hitung_grid().\n3. Satu perulangan sebanyak n kali mengikuti n, yaitu O(n).\n4. Dua perulangan yang masing-masing berjalan n kali mengikuti n², yaitu O(n²).", 11)
    add_box(page, (42, 510, 553, 665))
    add_text(page, 58, 536, "L. HUBUNGAN DENGAN NOTASI", 11, BLUE, "hebo")
    add_table(page, 58, 551, [210, 225], ["Pola jumlah operasi", "Notasi"], [["Konstan", "O(1)"], ["n", "O(n)"], ["n²", "O(n²)"]], 26, 10)
    add_paragraph(page, (48, 697, 540, 751), "Kesimpulan: memahami perubahan jumlah operasi saat n bertambah membantu mengenali pola kompleksitas, bukan sekadar menghafal notasinya.", 11, GREEN)
    add_footer(page, 7)

    doc.set_metadata({
        "title": "Eksperimen Python: Memahami Pertumbuhan Operasi",
        "author": "Salman Fidinillah",
        "subject": "Tugas Kompleksitas Algoritma",
        "keywords": "Python, O(n), O(n^2), algoritma",
    })
    doc.save(OUTPUT, garbage=4, deflate=True)
    doc.close()
    print(f"PDF dibuat: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
