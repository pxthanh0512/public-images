# Hướng dẫn up hình vào kho hình Platinum (dành cho team Marketing)

Kho hình này là nơi AI lấy banner cho email B2B. Bạn chỉ cần up hình đúng quy cách; danh sách hình tự cập nhật sau vài chục giây.

## Cách up hình (không cần biết git)
1. Vào https://github.com/pxthanh0512/public-images và đăng nhập tài khoản GitHub đã được mời.
2. Mở đúng thư mục: `nhahang` (nhà hàng, bar, khách sạn), `oem`, `privateparty`, hoặc `chung` (dùng lại cho mọi kênh; bán lẻ lon, chai và quà tặng cũng dùng `chung`).
3. Bấm **Add file → Upload files**, kéo hình vào.
4. Kéo xuống, bấm **Commit changes**.
5. Đợi khoảng 1 phút, mở `danh_sach_anh.txt` kiểm tra hình đã có dòng riêng. Vào tab **Actions** để xem kết quả và các lưu ý (nếu có).

## Quy cách hình
- Kích thước **1200 × 600 px** (tỷ lệ 2:1), dung lượng dưới **200 KB**. Hình sai tỷ lệ hoặc nhỏ hơn 1200 px sẽ tự bị đánh dấu `KHONG_DUNG` và AI không chọn.
- Chỉ ảnh thật của Platinum: không giá, không ưu đãi, không logo của bên thứ ba, không ảnh mờ; người trong ảnh rõ là từ 18 tuổi; bia đúng màu của dòng bia; chữ trên ảnh chỉ chung chung (tên dòng bia, câu cảm hứng).
- Không dùng từ "nấu bia" hay "bia hơi" trong chữ trên ảnh.

## Cách đặt tên file (quan trọng)
Chỉ dùng chữ thường không dấu, số, `_` và `-`; không khoảng trắng. Tên file nên có đủ **kiểu ảnh** và **màu bia** để danh sách tự điền đúng:

`[kenh]_[kieu]_[mau]_[so].jpg`

- Kiểu ảnh: `khongkhi` (không khí chung), `sanpham` (sản phẩm rõ nét), `nhanvat` (chân dung, người), `gianhang` (gian hàng, triển lãm).
- Màu bia: `vang`, `hophach` (nâu đỏ), `den`, `nhieumau` (nhiều ly khác màu), `khongapdung` (không thấy bia, ví dụ bao bì).
- Thêm `cochu` vào tên nếu trên ảnh có chữ hoặc logo chung (ví dụ `nhahang_khongkhi_vang_cochu_31.jpg`).

Ví dụ: `nhahang_khongkhi_vang_31.jpg`, `oem_sanpham_khongapdung_cochu_14.jpg`.

Tên file không theo quy ước vẫn được lưu nhưng ghi là `chua_phan_loai`, và AI sẽ **bỏ qua** hình đó cho đến khi bạn đổi tên (hoặc nhờ người quản lý kho sửa dòng trong danh sách).

## Ghi chú cho từng hình (tùy chọn)
Muốn thêm ghi chú (ví dụ "Có Michael Comerton", "Chỉ dùng cho thư giới thiệu năng lực"), thêm một dòng vào file `ghi_chu_anh.txt` ở thư mục gốc theo dạng:

`ten_file.jpg | nội dung ghi chú`

Hình có Michael Comerton: ghi rõ trong ghi chú để mọi người biết. Email dùng ảnh đó sẽ phải ghi tên ông dưới ảnh.

## Việc không nên làm
- Không xóa hay đổi tên hình đang dùng trong email đã gửi (link sẽ hỏng).
- Không sửa `danh_sach_anh.txt` bằng tay trừ khi là người quản lý kho. Muốn đổi thông tin một hình, dùng `ghi_chu_anh.txt` hoặc nhờ người quản lý.
- Không up hình nặng hơn 200 KB hoặc kích thước khác 1200×600.

## Dành cho người quản lý kho
- Danh sách tự cập nhật bởi `.github/workflows/cap-nhat-danh-sach.yml` và `tools/cap_nhat_danh_sach.py` (xem tab Actions, mục "Ket qua cap nhat danh sach anh" để biết hình nào có lưu ý).
- Dòng đã có trong danh sách được giữ nguyên, kể cả phần bạn sửa tay; chỉ cột kích thước tự cập nhật.
- Hình bị xóa khỏi kho thì dòng tương ứng tự bị bỏ.
- Chạy thử trên máy: `python3 tools/cap_nhat_danh_sach.py --kiem-tra`.
