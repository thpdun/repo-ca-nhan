# SPEC - Lab 3: Đọc giao dịch và hợp đồng trên Etherscan

## 1. Mục đích

Đọc và phân tích dữ liệu của một giao dịch blockchain trên Etherscan, đồng thời đọc một hợp đồng thông minh thật để phân biệt bytecode với mã nguồn đã xác thực và phân biệt hàm đọc với hàm ghi.

## 2. Đầu vào

- Transaction Hash của giao dịch đã thực hiện ở Lab 2:
  `0x2f7703ba057e0f16056921bb230c8d76bf5143c745d24a88bdf075cf3d217073`
- Mạng thử nghiệm Sepolia.
- Trang Sepolia Etherscan để đọc dữ liệu giao dịch.
- Một hợp đồng token thật trên Ethereum Mainnet: USDT hoặc USDC.
- Trang Etherscan để đọc thông tin hợp đồng.


## 3. Quy tắc nghiệp vụ

- R1: Dữ liệu giao dịch phải được đọc trực tiếp từ đúng Transaction Hash trên Sepolia Etherscan, không tự suy đoán hoặc tự tạo số liệu.

- R2: Phân tích đầy đủ 10 trường của giao dịch gồm:
  Status, Block, Timestamp, From / To, Value, Transaction Fee, Gas Price, Gas Limit, Gas Used và Nonce.

- R3: Với mỗi trường giao dịch phải giải thích được giá trị thực tế, ý nghĩa của trường và vì sao thông tin đó cần thiết đối với người làm nghiệp vụ.

- R4: Kiểm tra mối quan hệ giữa Gas Used, Gas Price và Transaction Fee:
  `Transaction Fee = Gas Used × Gas Price`
  và phải xử lý đúng đơn vị trước khi đối chiếu.

- R5: Khi đọc hợp đồng, phải phân biệt:
  - Bytecode là mã máy được blockchain thực thi.
  - Source Code (Verified) là mã nguồn đã được công bố và xác thực khớp với bytecode.

- R6: Phải phân biệt:
  - Read Contract: chỉ đọc dữ liệu, không làm thay đổi trạng thái.
  - Write Contract: làm thay đổi dữ liệu và cần giao dịch ký bằng ví.

- R7: Khi đọc hợp đồng token, phải kiểm tra các hàm đọc như `totalSupply()` và `balanceOf()` theo yêu cầu của Lab 3.

- R8: Kiểm tra trong phần Write Contract xem có hàm liên quan đến việc đóng băng hoặc hạn chế tài khoản hay không và ghi đúng tên hàm nếu tìm thấy.

- R9: Chỉ đưa ra kết luận dựa trên thông tin quan sát được trên Etherscan; không suy đoán danh tính, động cơ hoặc mục đích của chủ ví.

## 4. Đầu ra


- Bảng phân tích 10 trường của giao dịch cá nhân.
- Giá trị thực tế của từng trường.
- Ý nghĩa của từng trường.
- Giải thích vì sao người làm nghiệp vụ cần trường đó.
- Phần kiểm tra Transaction Fee từ Gas Used và Gas Price.
- Phần đọc hợp đồng thật trên Etherscan.
- Phân biệt Bytecode và Source Code (Verified).
- Phân biệt Read Contract và Write Contract.
- Kết quả đọc `totalSupply()` và `balanceOf()`.
- Trả lời 3 câu hỏi cuối của Lab 3.

## 5. Trường hợp ngoại lệ

- Nếu không truy cập được Etherscan hoặc không đọc được một trường giao dịch thì ghi rõ `[KHÔNG ĐỌC ĐƯỢC]`, không tự tạo dữ liệu thay thế.

- Nếu hợp đồng không có Source Code đã xác thực thì phải ghi rõ hợp đồng chưa công bố mã nguồn xác thực, không tự suy đoán mã nguồn.

- Nếu hợp đồng là Proxy Contract thì phải tìm đúng phần `Read as Proxy` / `Write as Proxy` hoặc địa chỉ implementation trước khi kết luận về các hàm nghiệp vụ.

- Nếu một hàm hoặc thông tin không tồn tại trên hợp đồng đang xem thì ghi rõ không tìm thấy, không tự bịa tên hàm hoặc kết quả.

## 6. Ngoài phạm vi

- Không thực hiện giao dịch bằng tiền thật trên Ethereum Mainnet.
- Không gọi các hàm Write Contract để thay đổi trạng thái hợp đồng.
- Không triển khai smart contract mới.
- Không phân tích lỗ hổng bảo mật hoặc đánh giá rủi ro mã nguồn chuyên sâu; nội dung này thuộc các Lab sau.
- Không lưu hoặc cung cấp private key hay Secret Recovery Phrase.

