# NHẬT KÝ LÀM VIỆC VỚI AI - Lab03

## Lần 1

**Prompt:** Hãy tạo thư mục: lab03/
Trong thư mục lab03, tạo các tệp cần thiết sau:
1. SPEC.md
2. AI_JOURNAL.md
3. forensics.md
Yêu cầu:
- Sao chép nội dung mẫu của SPEC.md ở thư mục gốc vào:
  lab03/SPEC.md
- Sao chép nội dung mẫu của AI_JOURNAL.md ở thư mục gốc vào:
  lab03/AI_JOURNAL.md
- Tạo tệp:
  lab03/forensics.md
- Không tự viết nội dung Lab 3.
- Không sửa bất kỳ tệp nào của Lab 1 và Lab 2.
- Không sửa các tệp mẫu ở thư mục gốc.
- Không sửa AGENTS.md.

**AI trả về:** Đã tạo xong cấu trúc thư mục lab03

**Đánh giá:** Dùng được.

**Chỗ sai:** Không có.

**Cách sửa:** Không cần sửa.

** Ai phát hiện:** Sinh viên kiểm tra lại nội dung lab03

## Lần 2

**Prompt:** Bạn là trợ lý hỗ trợ hoàn thiện Lab 3
Tôi đang thực hiện phần:
"Đọc một hợp đồng thật trên Etherscan"

Thông tin hợp đồng:

Token: USDT
Network: Ethereum Mainnet

Contract Address:
0xdAC17F958D2ee523a2206206994597C13D831ec7

Địa chỉ dùng để kiểm tra balanceOf():
0xF977814e90dA44bFA03b6295A0616a897441aceC

Hãy truy cập trực tiếp hợp đồng USDT trên Ethereum Etherscan và đọc dữ liệu công khai.

Không thực hiện bất kỳ giao dịch nào.
Không kết nối ví để ký giao dịch.

Thực hiện các bước sau:

1. TAB CONTRACT

Kiểm tra và ghi nhận:

- Hợp đồng có Source Code (Verified) hay không.
- Bytecode là gì.
- Source Code (Verified) là gì.
- Giải thích ngắn gọn sự khác nhau giữa Bytecode và Source Code (Verified).
- Chỉ kết luận dựa trên nội dung thực tế hiển thị trên Etherscan.

2. TAB READ CONTRACT

Tìm và gọi hàm:

totalSupply()

Ghi lại:
- Giá trị gốc mà Etherscan trả về.
- Hàm được sử dụng để đọc tổng cung.

Sau đó gọi:

balanceOf(
0xF977814e90dA44bFA03b6295A0616a897441aceC
)

Ghi lại:
- Giá trị gốc Etherscan trả về.

Nếu cần quy đổi số lượng token:

- Trước tiên phải đọc giá trị decimals() từ hợp đồng.
- Ghi rõ giá trị decimals.
- Ghi cả giá trị gốc và giá trị sau khi quy đổi.
- Không tự giả định số chữ số thập phân.

3. TAB WRITE CONTRACT

Kiểm tra các hàm có liên quan đến:

- đóng băng tài khoản;
- blacklist;
- đưa địa chỉ vào danh sách hạn chế;
- gỡ địa chỉ khỏi danh sách hạn chế;
- xử lý tài sản của địa chỉ bị hạn chế.

Nếu tìm thấy:

- Ghi đúng tên hàm như trên Etherscan.
- Giải thích ngắn gọn chức năng của từng hàm dựa trên mã nguồn hoặc giao diện Etherscan.
- Xác định hàm nào trả lời trực tiếp câu hỏi:
  "Có hàm nào cho phép một địa chỉ đặc biệt đóng băng tài khoản người khác không?"

Nếu không tìm thấy thì ghi rõ:
"Không tìm thấy"

Không tự bịa tên hàm.

4. CẬP NHẬT FILE

Chỉ cập nhật:

lab03/forensics.md

Tạo phần:

2. Đọc một hợp đồng thật trên Etherscan

Trình bày theo cấu trúc:
2.1. Thông tin hợp đồng

- Token:
- Contract Address:
- Network:
- Source Code Verified:

2.2. Phân biệt Bytecode và Source Code

Giải thích ngắn gọn dựa trên hợp đồng đang xem.

2.3. Read Contract

Ghi kết quả:

- decimals()
- totalSupply()
- balanceOf(0xF977814e90dA44bFA03b6295A0616a897441aceC)

Với mỗi hàm ghi:
- Giá trị gốc
- Giá trị sau quy đổi nếu có
- Ý nghĩa của kết quả

2.4. Write Contract

Lập bảng:

| Tên hàm | Chức năng | Liên quan đến đóng băng/blacklist hay không |


Chỉ đưa vào các hàm thực sự tìm thấy trên Etherscan.

5. TRẢ LỜI 3 CÂU HỎI CỦA LAB 3

Tạo phần:

3. Trả lời câu hỏi

Câu 1
Hợp đồng bạn xem có công bố mã nguồn đã xác thực không?

Trả lời dựa trên kết quả tab Contract.

Câu 2
Tổng cung của đồng đó là bao nhiêu? Đọc ra từ hàm nào?

Trả lời dựa trên kết quả totalSupply() và decimals().

Câu 3
Trong tab Write Contract có hàm nào cho phép một địa chỉ đặc biệt đóng băng tài khoản người khác không? Nếu có, tên hàm là gì?

Trả lời dựa trên hàm thực tế tìm được trong Write Contract.

YÊU CẦU BẮT BUỘC:

- Chỉ sử dụng dữ liệu thực tế đọc từ Ethereum Etherscan.
- Không tự bịa số liệu.
- Không tự bịa tên hàm.
- Không suy đoán khi chưa có bằng chứng.
- Nếu không đọc được trường nào, ghi [KHÔNG ĐỌC ĐƯỢC].
- Không thực hiện Write Contract.
- Không ký giao dịch.
- Không sửa lab03/SPEC.md.
- Không sửa lab03/AI_JOURNAL.md.
- Không sửa Lab 1 hoặc Lab 2.
- Không sửa AGENTS.md.
- Chỉ cập nhật phần đọc hợp đồng trong lab03/forensics.md.

Sau khi hoàn thành:

1. Hiển thị toàn bộ phần vừa thêm vào forensics.md.
2. Nêu rõ dữ liệu nào được lấy trực tiếp từ Etherscan.
3. Nêu rõ hàm nào được dùng để trả lời câu hỏi về đóng băng tài khoản.
4. Nếu có bất kỳ thông tin nào không chắc chắn, phải chỉ rõ thay vì tự kết luận.

**AI trả về:** AI đã đọc Transaction Hash của giao dịch cá nhân trên Sepolia Etherscan và tạo bảng phân tích 10 trường gồm: Status, Block, Timestamp, From/To, Value, Transaction Fee, Gas Price, Gas Limit, Gas Used và Nonce.

AI cũng kiểm tra lại phí giao dịch theo công thức:

Transaction Fee = Gas Used × Gas Price

Kết quả tính được là `0.000052508204721 ETH`, khớp với Transaction Fee hiển thị trên Etherscan.

Ở phần đọc hợp đồng USDT trên Ethereum Mainnet, AI xác định hợp đồng có trạng thái Source Code Verified. Tuy nhiên, AI không đọc được Bytecode, Source Code, `decimals()`, `totalSupply()`, `balanceOf()` và danh sách các hàm trong Write Contract nên các trường này được ghi `[KHÔNG ĐỌC ĐƯỢC]`.

**Đánh giá:** Phải sửa.

**Chỗ sai:** Phần phân tích giao dịch cá nhân thực hiện được và các số liệu phí giao dịch khớp nhau Tuy nhiên, phần đọc hợp đồng USDT chưa hoàn thành. AI không truy xuất được các hàm trong Read Contract và Write Contract.

Ngoài ra, AI ghi: "Không tìm thấy" ở phần Write Contract và câu hỏi về hàm đóng băng tài khoản. Kết luận này chưa chính xác vì AI chưa đọc được dữ liệu của Write Contract, do đó không thể kết luận rằng hợp đồng không có hàm đó.

**Cách sửa:** Giữ lại phần phân tích giao dịch đã kiểm tra đúng.

Phần hợp đồng USDT, sinh viên sẽ kiểm tra trực tiếp trên Etherscan để bổ sung:

- Source Code (Verified)
- Bytecode
- `decimals()`
- `totalSupply()`
- `balanceOf()`
- các hàm liên quan đến blacklist/đóng băng trong Write Contract.

Sau khi có dữ liệu thực tế, cập nhật lại `forensics.md` và không sử dụng kết luận "Không tìm thấy" khi dữ liệu chưa được đọc đầy đủ.

**Ai phát hiện:** Sinh viên kiểm tra.

