# NHẬT KÝ LÀM VIỆC VỚI AI - Lab 2

## Lần 1

**Prompt:** Tạo thư mục lab02 trong thư mục gốc dự án.
Sao chép hai file mẫu SPEC.md và AI_JOURNAL.md vào lab02.
Giữ nguyên hai file gốc ở thư mục gốc, không sửa nội dung file gốc.
Không thực hiện thay đổi nào khác.

**AI trả về:** Đã tạo thư mục lab02 và sao chép hai file theo yêu cầu.

**Đánh giá:** Dùng được.

**Chỗ sai:** Không phát hiện.

**Cách sửa:** Không cần sửa.

**Ai phát hiện:** Sinh viên kiểm tra lại cấu trúc thư mục.

## Lần 2

**Prompt:** Trong thư mục lab02 tạo thêm file lab02.md.
Không thực hiện thay đổi nào khác.

**AI trả về:** Đã tạo file lab02.md.

**Đánh giá:** Dùng được.

**Chỗ sai:** Không phát hiện.

**Cách sửa:** Không cần sửa.

**Ai phát hiện:** Sinh viên kiểm tra lại cấu trúc thư mục.

## Lần 3

**Prompt:**  Bạn là trợ lý hỗ trợ thực hiện Lab 2. Transaction Hash giao dịch thành công của tôi trên mạng Sepolia là: 0x2f7703ba057e0f16056921bb230c8d76bf5143c745d24a88bdf075cf3d217073
Hãy thực hiện các bước sau:
1. Mở giao dịch này trên Sepolia Etherscan: https://sepolia.etherscan.io/tx/0x2f7703ba057e0f16056921bb230c8d76bf5143c745d24a88bdf075cf3d217073
2. Đọc trực tiếp dữ liệu giao dịch từ Etherscan.
3. Trích xuất chính xác các thông tin:
- Transaction Hash
- Status
- From
- To
- Value
- Transaction Fee
4. Kiểm tra rằng đây là giao dịch trên mạng Sepolia.
5. Cập nhật tệp:
lab02/lab02.md
6. Trong lab02.md, ghi thông tin giao dịch này vào mục
"Giao dịch thành công".
Yêu cầu:
- Chỉ sử dụng dữ liệu thực tế đọc được từ Sepolia Etherscan.
- Không tự suy đoán hoặc tự tạo dữ liệu.
- Không tự thay đổi đơn vị hoặc làm tròn số nếu chưa cần thiết.
- Nếu không truy cập được Etherscan hoặc không đọc được một trường nào, ghi rõ [KHÔNG ĐỌC ĐƯỢC] thay vì tự điền.
- Không sửa SPEC.md.
- Không sửa AI_JOURNAL.md.
- Không sửa bất kỳ tệp nào của Lab 1.
- Chỉ cập nhật lab02/lab02.md.
- Sau khi hoàn thành, cho tôi biết dữ liệu nào được lấy trực tiếp từ Etherscan. 

**AI trả về:** AI đã đọc giao dịch trên Sepolia Etherscan và lấy được Transaction Hash, Status, From, To, Value và Transaction Fee. Giao dịch có trạng thái Success, giá trị chuyển là 0.01 ETH và phí giao dịch là 0.000052508204721 ETH. Kết quả được ghi vào `lab02.md`.

**Đánh giá:** Dùng được.

**Chỗ sai:** Không phát hiện.

**Cách sửa:** Không cần sửa.

**Ai phát hiện:** Sinh viên kiểm tra lại nội dung tệp lab02/lab02.md.

## Lần 4

**Prompt:** Bạn là trợ lý hỗ trợ hoàn thiện Lab 2.
Hãy chỉnh lại tệp: lab02/lab02.md
Dữ liệu giao dịch thành công đã có sẵn trong file hiện tại. 
Không được thay đổi các giá trị đã đọc từ Sepolia Etherscan.
Yêu cầu trình bày lại đúng theo mẫu:
Bảng đối chiếu giao dịch
Tạo bảng Markdown gồm 3 cột:
| Trường | Giao dịch thành công | Giao dịch thất bại |
Các dòng bắt buộc:
- Mã băm giao dịch
- Số tiền chuyển
- Phí giao dịch thực trả
- Trạng thái
- Nguyên nhân (nếu thất bại)
Đối với cột "Giao dịch thành công":
- Điền đúng dữ liệu hiện có trong file.
- Giữ nguyên chính xác Transaction Hash, Value, Transaction Fee và Status đã đọc được từ Sepolia Etherscan.
Đối với cột "Giao dịch thất bại":
- Hiện tại chưa có dữ liệu nên điền [CHƯA THỰC HIỆN].
Yêu cầu:
- Không tự bịa dữ liệu.
- Không thay đổi số liệu giao dịch thành công đã có.
- Không sửa SPEC.md.
- Không sửa AI_JOURNAL.md.
- Không sửa file Lab 1.
- Chỉ cập nhật lab02/lab02.md.
- Sau khi hoàn thành, hiển thị toàn bộ nội dung file để tôi kiểm tra.

**AI trả về:** AI đã chỉnh lại tệp `lab02/lab02.md` từ dạng liệt kê sang bảng đối chiếu theo mẫu của sổ tay.


**Đánh giá:** Dùng được.

**Chỗ sai:** Không phát hiện.

**Cách sửa:** Không cần sửa.

**Ai phát hiện:** Sinh viên kiểm tra lại nội dung `lab02.md`.

## Lần 5

**Prompt:** Bạn là trợ lý hỗ trợ hoàn thiện Lab 2. Hãy cập nhật tệp: lab02/lab02.md
Giữ nguyên toàn bộ dữ liệu giao dịch thành công hiện có.
Tôi đã thực hiện thêm 3 tình huống sau:
TÌNH HUỐNG A — NHẬP THIẾU KÝ TỰ TRONG ĐỊA CHỈ
Địa chỉ đúng:
0x78567A377559F0cB30173f93869326a82320159a
Địa chỉ nhập sai:
0x78567A377559F0cB30173f93869326a82320159
Kết quả thực tế:
MetaMask báo "Địa chỉ không hợp lệ" và không cho phép tiếp tục.
Không phát sinh Transaction Hash.

TÌNH HUỐNG B — KHÔNG ĐỦ PHÍ GAS
Tôi thử chọn chuyển toàn bộ số dư Sepolia ETH.
MetaMask phát cảnh báo liên quan đến phí mạng và không thể hoàn tất giao dịch theo số tiền đã chọn.
Không tự tạo Transaction Hash nếu giao dịch chưa được phát lên blockchain.

TÌNH HUỐNG C — NHẬP NHẦM ĐỊA CHỈ NHƯNG ĐỊA CHỈ VẪN HỢP LỆ
Địa chỉ tôi dự định chuyển:
0x78567A377559F0cB30173f93869326a82320159a
Địa chỉ tôi nhập nhầm:
0xf5D971952dbDF69058a28D23110381d96B00cb50
Giao dịch thực tế:
Transaction Hash:
0x23a4b6ee19bc31e8ae102a132fd3c6eed745372d5efe9d999bc38f303b4676e3
Transaction Hash giao dịch thành công của tôi trên mạng Sepolia là: 0x2f7703ba057e0f16056921bb230c8d76bf5143c745d24a88bdf075cf3d217073
Hãy thực hiện các bước sau:
1. Mở giao dịch này trên Sepolia Etherscan: https://sepolia.etherscan.io/tx/0x2f7703ba057e0f16056921bb230c8d76bf5143c745d24a88bdf075cf3d217073
2. Đọc trực tiếp dữ liệu giao dịch từ Etherscan.
3. Trích xuất chính xác các thông tin:
- Transaction Hash
- Status
- From
- To
- Value
- Transaction Fee
Yêu cầu trình bày với các bước sau:
1. Giữ bảng đối chiếu chính theo đúng mẫu sổ tay:
| Trường | Giao dịch thành công | Giao dịch thất bại |
Dùng tình huống A làm giao dịch thất bại trong bảng chính.
2. Sau bảng, tạo mục: 2. Các tình huống sai có chủ đích
Gồm các trường hợp: 
2.1. Tình huống A — Nhập thiếu ký tự trong địa chỉ ví
2.2. Tình huống B — Không đủ phí gas
2.3. Tình huống C — Nhập nhầm địa chỉ nhưng địa chỉ vẫn hợp lệ
3. Với mỗi tình huống ghi:
- Sinh viên đã làm gì
- Kết quả thực tế
- Transaction Hash nếu có
- Trạng thái
- Phí thực trả nếu có
- Nguyên nhân
- Bài học rút ra
4. Phải phân biệt rõ:
- Tình huống A và B bị MetaMask chặn/cảnh báo trước khi giao dịch hoàn tất nên không tự tạo Transaction Hash.
- Tình huống C không phải giao dịch thất bại về mặt blockchain. Đây là giao dịch Success nhưng sai người nhận.
5. Trả lời câu hỏi:
"Nếu bạn chuyển nhầm cho người lạ, có lấy lại được không? Vì sao?"
6. Không tự bịa dữ liệu.
7. Không sửa SPEC.md.
8. Không sửa AI_JOURNAL.md.
9. Không sửa Lab 1.
10. Chỉ cập nhật lab02/lab02.md.
11. Sau khi hoàn thành, hiển thị toàn bộ nội dung tệp để tôi kiểm tra.

**AI trả về:** AI đã cập nhật tệp `lab02/lab02.md` và tổng hợp kết quả gồm:

- Giao dịch thành công:
  - Transaction Hash:
    `0x2f7703ba057e0f16056921bb230c8d76bf5143c745d24a88bdf075cf3d217073`
  - Số tiền chuyển: `0.01 ETH`
  - Phí giao dịch: `0.000052508204721 ETH`
  - Trạng thái: `Success`

- Tình huống A — nhập thiếu ký tự trong địa chỉ ví:
  - MetaMask báo địa chỉ không hợp lệ.
  - Giao dịch bị chặn trước khi phát lên blockchain.
  - Không phát sinh Transaction Hash.
  - Không mất phí giao dịch.

- Tình huống B — chuyển toàn bộ số dư, không đủ phí gas:
  - MetaMask phát cảnh báo liên quan đến phí mạng.
  - Giao dịch không được hoàn tất.
  - Không phát sinh Transaction Hash.
  - Không mất phí giao dịch.

- Tình huống C — nhập nhầm địa chỉ nhưng địa chỉ vẫn hợp lệ:
  - Blockchain vẫn xử lý giao dịch thành công.
  - Transaction Hash:
    `0x23a4b6ee19bc31e8ae102a132fd3c6eed745372d5efe9d999bc38f303b4676e3`
  - Phí giao dịch:
    `0.000053519639481 ETH`
  - Trạng thái: `Success`

AI cũng bổ sung nguyên nhân, bài học rút ra cho từng tình huống và trả lời câu hỏi cuối của Lab 2.

**Đánh giá:** Phải sửa. 

**Chỗ sai:** AI mở đầu câu trả lời bằng câu:
"Không thể lấy lại được."
Cách diễn đạt này hơi tuyệt đối, vì người gửi không thể tự hoàn tác giao dịch nhưng vẫn có khả năng nhận lại tài sản nếu xác định được người nhận và người nhận tự nguyện chuyển trả.

**Cách sửa:** Sửa thành: "Người gửi không thể tự lấy lại được sau khi giao dịch đã được xác nhận."
Các nội dung còn lại được giữ nguyên vì phù hợp với kết quả thực nghiệm..

**Ai phát hiện:** Sinh viên kiểm tra lại nội dung `lab02.md`.


