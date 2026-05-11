# WonderKids — Báo cáo đánh giá năng lực đầu kỳ

Báo cáo HTML tương tác cho hệ thống đánh giá năng lực toán học đầu kỳ của trẻ, thiết kế theo chuẩn CMS Edu, có thể nhập dữ liệu từ Excel/CSV và xuất PDF.

## 🚀 Demo trực tuyến

👉 **[Mở báo cáo trên GitHub Pages](https://hoangduong-dh.github.io/wonderkids-baocao/)**

## ✨ Tính năng

### Nhập liệu thông minh
- 📥 **Kéo-thả file** `.csv` hoặc `.xlsx` vào trang để tự fill toàn bộ form
- 🔄 **Template-aware parser**: nhận diện đúng các vùng dữ liệu trong template đánh giá CMS (đánh giá theo đơn vị, năng lực, cấp độ, bài toán có/không lời)
- 📋 **Paste tab-separated** từ Excel vào bảng để fill nhiều ô
- ⌨️ **Phím tắt**: `↑↓` di chuyển dòng, `Enter` xuống dòng, `3/5` ở ô Đạt = Chuẩn 5 / Đạt 3
- 💾 **Autosave** localStorage — gõ tới đâu lưu tới đó

### Visualization & Insight
- 🍩 **Donut chart** cho mỗi sumcard, màu thay đổi theo level (Khá / Tốt / Xuất sắc…)
- 🎯 **Radar chart** 6 lĩnh vực năng lực tư duy với auto-scale tránh "polygon lép kẹp" khi điểm thấp
- 📊 **Bar chart** tỷ lệ theo phân loại (Kiến thức cơ bản)
- 🧠 **Cluster bars** phân nhóm tư duy (Cơ bản / Nâng cao / Sáng tạo) — insight quan trọng nhất
- 📝 **Question Matrix** 20 câu với O/X tô màu xanh đỏ
- 🌳 **Stage caption** (Khởi đầu / Hình thành / Ổn định / Tiến bộ / Vượt trội) thay vì điểm số khô khan

### Xuất PDF
- 🖨️ **Print preview** xem trước in trên màn hình
- ✅ Print CSS tối ưu cho A4 portrait — không split section heading, không tràn trang
- ✅ Background graphics auto-preserve qua `print-color-adjust: exact`
- 📄 **Headless Edge/Chrome** sinh PDF mẫu chuyên nghiệp (xem `WonderKids-Bao-cao-mau.pdf`)

## 🛠 Cách dùng

### 1. Mở báo cáo
- Online: vào GitHub Pages link ở trên
- Offline: tải `index.html` về máy, mở bằng Chrome/Edge

### 2. Nhập dữ liệu
**Cách 1** — Tải file mẫu sẵn:
- Bấm **"Test CSV mẫu"** trên toolbar → tự fill data Đinh Mạnh Hùng (PDF gốc CMS)

**Cách 2** — Từ file của bạn:
- Lưu file đánh giá Excel → **File → Save As → CSV UTF-8**
- Kéo-thả file `.csv` (hoặc `.xlsx`) vào trang

**Cách 3** — Gõ tay:
- Điền trực tiếp vào các bảng. Form tự tính tỷ lệ và update chart realtime

### 3. Xuất PDF
- **Trong browser**: Bấm "In / Xuất PDF" → chọn "Save as PDF" (nhớ bật "Background graphics", tắt "Headers and footers")
- **Headless** (cho 1 batch nhiều học sinh):
  ```powershell
  msedge.exe --headless=new --disable-gpu `
    --print-to-pdf="output.pdf" --no-pdf-header-footer `
    --virtual-time-budget=10000 --run-all-compositor-stages-before-draw `
    "file:///path/to/index.html"
  ```

## 📁 Cấu trúc

```
├── index.html                          # File báo cáo chính
├── tweaks-panel.jsx                    # React tweaks panel (theme, font…)
├── assets/                             # Logo
├── uploads/                            # Sample CSV + XLSX
│   ├── IG-DGDK-THIENKHOI.xlsx
│   └── IG-DGDK-THIENKHOI.csv
└── WonderKids-Bao-cao-mau.pdf          # Output PDF mẫu
```

## 🎨 Thiết kế

- **Single-file HTML** — không build, không dependency local
- **CDN libs**: React + Babel (cho tweaks panel) + SheetJS XLSX (cho import Excel) — fallback 3 CDN
- **CSV parser thuần JS** — không cần thư viện cho `.csv`
- **SVG charts** — vector, in giấy nét sắc
- **Auto-grow textarea** — text dài tự xuống dòng
- **A11y**: keyboard navigation, ESC để thoát preview

## 📜 License

MIT
