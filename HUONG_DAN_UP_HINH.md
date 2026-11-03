# Hướng dẫn up hình vào kho hình Platinum (dành cho team Marketing)

Kho hình này là nơi AI lấy banner cho email B2B. Bạn chỉ cần up hình vào **một thư mục duy nhất: `_moi_up`**. Việc phân loại, cắt về đúng cỡ, đặt tên, chuyển vào đúng thư mục kênh và cập nhật danh sách hình sẽ được xử lý sau.

## Cách up hình (không cần biết git)
1. Vào https://github.com/pxthanh0512/public-images và đăng nhập tài khoản GitHub đã được mời.
2. Mở thư mục **`_moi_up`**. Không up vào `nhahang`, `oem`, `privateparty`, `chung`.
3. Bấm **Add file → Upload files**, kéo hình vào (có thể up nhiều hình một lần, khoảng 20 hình mỗi lần là hợp lý).
4. Kéo xuống, bấm **Commit changes**.
5. Xong. Hình sẽ nằm trong `_moi_up` cho đến khi được xử lý; hình đã xử lý sẽ biến mất khỏi đây và xuất hiện trong thư mục kênh tương ứng.

Tên file đặt thế nào cũng được, không cần theo quy ước, không cần cắt hay đổi cỡ trước.

## Hình nào nên up
- Ảnh thật của Platinum, rõ nét, chụp đủ lớn (từ khoảng 1200 px chiều ngang trở lên; ảnh càng lớn càng dễ cắt đẹp).
- Không giá, không ưu đãi, không logo của bên thứ ba, không ảnh mờ.
- Người trong ảnh rõ là từ 18 tuổi trở lên; ảnh có bia phải đúng màu của dòng bia.
- Chữ trên ảnh chỉ chung chung (tên dòng bia, câu cảm hứng). Không có chữ "nấu bia" hoặc "bia hơi".
- Hình đã được phép dùng cho quảng bá.

## Muốn hình vào đúng chỗ nhanh hơn (tùy chọn)
Thêm gợi ý vào **tên file**, máy sẽ ưu tiên dùng:
- Kênh: `nhahang`, `oem`, `privateparty`, `chung` (hình dùng chung; bán lẻ lon, chai và quà tặng cũng dùng `chung`).
- Kiểu ảnh: `khongkhi` (không khí chung), `sanpham` (sản phẩm rõ nét), `nhanvat` (chân dung, người), `gianhang` (gian hàng, triển lãm).
- Màu bia: `vang`, `hophach`, `den`, `nhieumau`, `khongapdung` (không thấy bia).
- Hình có Michael Comerton: thêm `michael` vào tên file (ví dụ `oem_nhanvat_michael_05.jpg`).

Ví dụ: `nhahang_khongkhi_vang_buoi_toi.jpg`. Chỉ dùng chữ thường không dấu, số, `_` và `-`.

## Sau khi up, điều gì xảy ra
- Hình được xem và phân loại theo kênh, kiểu ảnh, màu bia.
- Cắt về **1200 × 600 px** (tỷ lệ 2:1), dung lượng dưới 200 KB; cắt theo nội dung ảnh để không mất người hoặc sản phẩm chính.
- Đặt tên theo quy ước, chuyển vào thư mục kênh và cập nhật `danh_sach_anh.txt`.
- Hình không dùng được (có giá, logo bên thứ ba, ảnh mờ, quá nhỏ, cần xác nhận về người trong ảnh) sẽ **ở lại `_moi_up`** kèm lý do trong báo cáo gửi người quản lý kho.

## Việc không nên làm
- Không up hình vào thư mục kênh trực tiếp, và không sửa `danh_sach_anh.txt`.
- Không xóa hoặc đổi tên hình đang nằm trong thư mục kênh (link trong email đã gửi sẽ hỏng).
- Không up hình chưa chắc được phép dùng.

## Dành cho người quản lý kho
- Quy trình xử lý hình trong `_moi_up` do Claude thực hiện (chạy theo lệnh hoặc theo lịch); script `tools/cap_nhat_danh_sach.py` và workflow `.github/workflows/cap-nhat-danh-sach.yml` tự cập nhật `danh_sach_anh.txt` mỗi khi có hình mới trong thư mục kênh.
- Workflow chỉ theo dõi 4 thư mục kênh, không theo dõi `_moi_up`.
- Dòng đã có trong danh sách được giữ nguyên, kể cả phần sửa tay. Ghi chú riêng cho từng hình: file `ghi_chu_anh.txt`.
- Chạy thử trên máy: `python3 tools/cap_nhat_danh_sach.py --kiem-tra`.
