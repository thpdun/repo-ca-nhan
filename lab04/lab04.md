# LAB 4 — NHẬN DIỆN HỢP ĐỒNG CÓ RỦI RO

## 1. Kết quả đọc thủ công

### Hợp đồng A — ClubTokenA

- Phạm vi mã nguồn đã đọc: dòng 7–11.
- Có kế thừa `Ownable`: Không
- Có hàm `onlyOwner`: Không
- Quyền đặc biệt tôi tự phát hiện: Không
- Tên hàm: Không có
- Số dòng: Không có
- Rủi ro cho người nắm giữ token: Không thấy

### Hợp đồng B — ClubTokenB

- Phạm vi mã nguồn đã đọc: dòng 13-21
- Có kế thừa `Ownable`: Có
- Có hàm `onlyOwner`: Có
- Quyền đặc biệt tôi tự phát hiện: Có  
- Tên hàm: mint()
- Số dòng: 18-20
- Rủi ro cho người nắm giữ token: Không tìm thấy

### Hợp đồng C — ClubTokenC

- Phạm vi mã nguồn đã đọc: dòng 23-38
- Có kế thừa `Ownable`: Có
- Có hàm `onlyOwner`: Có
- Quyền đặc biệt tôi tự phát hiện: Có
- Tên hàm: setRestricted()
- Số dòng: 30-32
- Rủi ro cho người nắm giữ token: Chưa xác định được

## 2. Kết quả phân tích bằng AI

- **ClubTokenA**: Không tìm thấy quyền đặc biệt nào của chủ sở hữu có thể gây rủi ro cho người nắm giữ token.
- **ClubTokenB**: Phát hiện quyền đặc biệt cho phép chủ sở hữu đúc thêm token vô hạn cho bất kỳ địa chỉ nào.
- **ClubTokenC**: Phát hiện quyền đặc biệt cho phép chủ sở hữu đưa bất kỳ địa chỉ nào vào danh sách hạn chế, ngăn chặn giao dịch.

## 3. Bảng kết luận

| Hợp đồng | Kết luận | Tên hàm | Số dòng | Rủi ro cho người nắm giữ |
| :--- | :--- | :--- | :--- | :--- |
| ClubTokenA | Không tìm thấy | Không tìm thấy | Không tìm thấy | Không tìm thấy |
| ClubTokenB | Có quyền đặc biệt | mint() | 18-20 | Chủ sở hữu có thể tùy ý in thêm token vô hạn, làm pha loãng nguồn cung và giảm giá trị token của những người đang nắm giữ. |
| ClubTokenC | Có quyền đặc biệt | setRestricted() | 30-32 | Chủ sở hữu có quyền đưa một địa chỉ vào trạng thái `restricted`. Khi đó địa chỉ này không thể chuyển token đi, làm người nắm giữ có nguy cơ bị hạn chế quyền sử dụng tài sản của mình |