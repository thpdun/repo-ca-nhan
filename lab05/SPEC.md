# SPEC - Lab 5: Viết đặc tả cho công cụ phân tích dòng tiền

## 1. Mục đích

Xây dựng đặc tả cho một công cụ nhận vào một địa chỉ ví và tạo báo cáo dòng tiền vào, dòng tiền ra của ví đó trong 90 ngày gần nhất, đồng thời hiển thị số dư lũy kế theo thời gian.

Mục tiêu của SPEC là mô tả yêu cầu đủ rõ để người khác hoặc công cụ AI có thể xây dựng chương trình đúng yêu cầu mà không cần hỏi lại.

## 2. Đầu vào

- Một địa chỉ ví Ethereum.
- Địa chỉ ví phải là chuỗi gồm 42 ký tự và bắt đầu bằng `0x`.
- Khóa API của Etherscan.
- Khóa API phải được đọc từ biến môi trường: `ETHERSCAN_API_KEY`
- Số ngày cần phân tích.
- Giá trị mặc định là 90 ngày.


## 3. Quy tắc nghiệp vụ

- R1: Giao dịch có trường `to` trùng với địa chỉ ví đang được phân tích được tính là dòng tiền vào.

- R2: Giao dịch có trường `from` trùng với địa chỉ ví đang được phân tích được tính là dòng tiền ra.

- R3: Với giao dịch đi ra thành công, số tiền thực tế bị trừ khỏi ví bằng: `Giá trị chuyển + Phí giao dịch`

- R4: Giao dịch có trạng thái thất bại vẫn bị trừ phí giao dịch. Phí này phải được tính vào dòng tiền ra.

- R5: Mọi số tiền lấy từ API ở đơn vị wei phải được chia cho `10^18` trước khi hiển thị dưới đơn vị ETH.

- R6: Các giao dịch phải được sắp xếp theo thời gian tăng dần, từ giao dịch cũ nhất đến giao dịch mới nhất.

- R7: Chỉ phân tích các giao dịch ETH gốc của địa chỉ ví đang xét.

- R8: Kết quả phân tích chỉ bao gồm các giao dịch nằm trong khoảng thời gian được yêu cầu, mặc định là 90 ngày gần nhất.

## 4. Đầu ra

Công cụ phải tạo ra các kết quả sau:

4.1. Bảng dữ liệu giao dịch

Bảng phải gồm tối thiểu các trường:

- Thời gian giao dịch.
- Loại giao dịch: `Vào` hoặc `Ra`.
- Số tiền ETH.
- Phí giao dịch.
- Số dư lũy kế sau giao dịch.

4.2. Biểu đồ

Tạo một biểu đồ đường thể hiện số dư lũy kế theo thời gian.

- Trục ngang: thời gian.
- Trục dọc: số dư lũy kế của ví.

4.3. Các chỉ tiêu tổng hợp

Hiển thị tối thiểu ba chỉ tiêu:

- Tổng dòng tiền vào.
- Tổng dòng tiền ra.
- Số dư cuối kỳ.

## 5. Trường hợp ngoại lệ

- Nếu API trả về danh sách giao dịch rỗng thì hiển thị thông báo: `Vi khong co giao dich trong ky` và không báo lỗi.

- Nếu API trả về mã lỗi thì phải hiển thị mã lỗi và dừng xử lý.

- Nếu ví có hơn 10.000 giao dịch thì chương trình phải xử lý phân trang và lấy đủ tất cả các trang dữ liệu.

- Nếu địa chỉ ví không đúng định dạng yêu cầu thì không tiếp tục xử lý cho đến khi có địa chỉ hợp lệ.

- Nếu không có biến môi trường `ETHERSCAN_API_KEY` thì chương trình phải thông báo thiếu khóa API và dừng xử lý.

## 6. Ngoài phạm vi

- Không phân tích giao dịch token ERC-20 như USDT, USDC hoặc các token khác.

- Chỉ phân tích ETH gốc.

- Không quy đổi giá trị ETH sang VND.

- Không phân tích giá thị trường của ETH.

- Không thực hiện giao dịch blockchain.

- Không thay đổi dữ liệu của ví.

- Không yêu cầu người dùng cung cấp private key hoặc seed phrase.

