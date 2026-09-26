# LAB 2 — VÍ VÀ GIAO DỊCH ĐẦU TIÊN

## 1. Bảng đối chiếu giao dịch

| Trường | Giao dịch thành công | Giao dịch thất bại |
|---|---|---|
| Mã băm giao dịch | 0x2f7703ba057e0f16056921bb230c8d76bf5143c745d24a88bdf075cf3d217073 | Không có |
| Số tiền chuyển | 0.01 ETH | Không có |
| Phí giao dịch thực trả | 0.000052508204721 ETH | Không có |
| Trạng thái | Success | Bị chặn (Không hợp lệ) |
| Nguyên nhân (nếu thất bại) | | Nhập thiếu ký tự trong địa chỉ ví |


## 2. Các tình huống sai có chủ đích

### 2.1. Tình huống A — Nhập thiếu ký tự trong địa chỉ ví
- **Sinh viên đã làm gì:** Nhập thiếu 1 ký tự ở cuối địa chỉ nhận (`0x78567A377559F0cB30173f93869326a82320159`).
- **Kết quả thực tế:** MetaMask báo "Địa chỉ không hợp lệ" và không cho phép tiếp tục. Không phát sinh Transaction Hash do giao dịch chưa được gửi lên mạng.
- **Transaction Hash:** Không có
- **Trạng thái:** Bị MetaMask chặn
- **Phí thực trả:** Không có
- **Nguyên nhân:** Địa chỉ Ethereum phải có đủ 42 ký tự (bao gồm `0x`). Việc thiếu ký tự khiến địa chỉ sai định dạng nên ví từ chối ký giao dịch.
- **Bài học rút ra:** Luôn sử dụng chức năng sao chép/dán địa chỉ, không nên nhập tay để tránh sai sót định dạng.

### 2.2. Tình huống B — Không đủ phí gas
- **Sinh viên đã làm gì:** Chọn chuyển toàn bộ số dư Sepolia ETH trong ví.
- **Kết quả thực tế:** MetaMask phát cảnh báo liên quan đến phí mạng và không thể hoàn tất giao dịch theo số tiền đã chọn. Không tự tạo Transaction Hash.
- **Transaction Hash:** Không có
- **Trạng thái:** Bị MetaMask chặn
- **Phí thực trả:** Không có
- **Nguyên nhân:** Mọi giao dịch trên blockchain đều tốn phí mạng (Gas fee). Nếu gửi hết toàn bộ số dư (Max) mà không chừa lại một khoản ETH để làm phí, giao dịch sẽ không thể thực hiện được.
- **Bài học rút ra:** Luôn phải tính toán hoặc chừa lại một lượng nhỏ ETH trong ví làm phí gas khi muốn thực hiện giao dịch chuyển tiền.

### 2.3. Tình huống C — Nhập nhầm địa chỉ nhưng địa chỉ vẫn hợp lệ
- **Sinh viên đã làm gì:** Nhập nhầm địa chỉ người nhận thành `0xf5D971952dbDF69058a28D23110381d96B00cb50`.
- **Kết quả thực tế:** Giao dịch vẫn diễn ra bình thường, tiền bị trừ khỏi ví.
- **Transaction Hash:** 0x23a4b6ee19bc31e8ae102a132fd3c6eed745372d5efe9d999bc38f303b4676e3
- **Trạng thái:** Success
- **Phí thực trả:** 0.000053519639481 ETH
- **Nguyên nhân:** Địa chỉ nhập nhầm vẫn là một địa chỉ đúng chuẩn Ethereum (dù nó không phải là địa chỉ mong muốn). Blockchain chỉ kiểm tra tính hợp lệ của địa chỉ và số dư, nó không thể xác minh danh tính người nhận thực sự.
- **Bài học rút ra:** Cần kiểm tra kỹ địa chỉ người nhận (thường là vài ký tự đầu và cuối) trước khi xác nhận giao dịch.

**Nếu bạn chuyển nhầm cho người lạ, có lấy lại được không? Vì sao?**
Không thể lấy lại được. Khác với hệ thống ngân hàng truyền thống, blockchain có tính chất phi tập trung và bất biến. Khi một giao dịch đã được đưa lên mạng và chuyển sang trạng thái "Success", nó không thể bị đảo ngược hay hoàn tác bởi bất kỳ tổ chức hay cá nhân nào. Người duy nhất có quyền kiểm soát số tiền đó là người nắm giữ private key của địa chỉ nhận. Vì thế, nếu bạn không thể liên hệ và thuyết phục người đó chuyển trả lại tự nguyện, số tiền đó xem như mất vĩnh viễn.
