## 1. Mổ xẻ giao dịch của chính mình

| Trường | Giá trị thực tế | Ý nghĩa | Vì sao người làm nghiệp vụ cần |
|---|---|---|---|
| Status | Success | Giao dịch đã được xác nhận thành công trên mạng lưới. | Dùng để xác định giao dịch thành công hay thất bại. |
| Block | 11788244 | Số thứ tự của khối trên mạng Sepolia chứa giao dịch này. | Dùng để xác định giao dịch đã được ghi vào khối nào. |
| Timestamp | Sep-26-2026 07:25:36 PM (UTC) | Thời điểm khối chứa giao dịch được đào thành công. | Dùng làm mốc thời gian ghi nhận. |
| From / To | 0x36Fd4887e9d1ecA4Ae5062A745cc2c6182B77060 <br> 0x78567A377559F0cB30173f93869326a82320159a | Địa chỉ ví thực hiện việc gửi và địa chỉ ví nhận tiền. | Dùng để xác định ví gửi và ví nhận. |
| Value | 0.01 ETH | Số ETH thực tế được chuyển đi trong giao dịch này. | Dùng để xác định giá trị tài sản được chuyển. |
| Transaction Fee | 0.000052508204721 ETH | Tổng chi phí thực tế mà người gửi phải trả cho mạng lưới (validator) để xử lý giao dịch. | Dùng để xác định chi phí giao dịch thực trả. |
| Gas Price | 2.500390701 Gwei | Mức giá phí gas tại thời điểm giao dịch được thực hiện. | Giúp giải thích đơn giá phí gas. |
| Gas Limit | 21,000 | Lượng gas tối đa giao dịch này được phép dùng (21,000 là mức chuẩn khi chuyển ETH). | Cho biết mức gas tối đa mà giao dịch cho phép sử dụng. |
| Gas Used | 21,000 | Lượng gas mà giao dịch thực sự đã tiêu thụ. | Cho biết lượng gas thực tế đã tiêu thụ. |
| Nonce | 54 | Lượt giao dịch thứ 54 phát ra từ địa chỉ ví của người gửi. | Cho biết số thứ tự giao dịch của ví gửi. |

### Kiểm tra phí giao dịch

- **Gas Used:** 21,000
- **Gas Price:** 2.500390701 Gwei = 0.000000002500390701 ETH
- **Phép tính:** Transaction Fee = Gas Used × Gas Price = 21,000 × 0.000000002500390701 ETH
- **Kết quả tính được:** 0.000052508204721 ETH
- **Transaction Fee trên Etherscan:** 0.000052508204721 ETH
- **Kết luận:** Kết quả tính toán khớp hoàn toàn với phí giao dịch hiển thị trên Etherscan.

## 2. Đọc một hợp đồng thật trên Etherscan

### 2.1. Thông tin hợp đồng

- Token: USDT
- Contract Address: 0xdAC17F958D2ee523a2206206994597C13D831ec7
- Network: Ethereum Mainnet
- Source Code Verified: Có (Dựa trên siêu dữ liệu HTML trả về: "Contract: Verified")

### 2.2. Phân biệt Bytecode và Source Code (Verified)

- **Bytecode:** Là mã máy của hợp đồng thông minh được lưu trên blockchain và được Ethereum Virtual Machine (EVM) thực thi. Bytecode thường được biểu diễn dưới dạng một chuỗi ký tự hexadecimal dài nên con người rất khó đọc trực tiếp.

- **Source Code:** Là mã nguồn do lập trình viên viết bằng ngôn ngữ như Solidity để mô tả logic của hợp đồng. Trong hợp đồng USDT đang xem, mã nguồn sử dụng Solidity `^0.4.17` và có thể đọc được các contract, biến và hàm như `balanceOf()`, `totalSupply()`, `addBlackList()`... :chatgpt-content-reference{index="0"}

- **Source Code (Verified):** Trên Etherscan, hợp đồng USDT hiển thị mã nguồn ở trạng thái Verified. Điều này có nghĩa là mã nguồn Solidity được công bố đã được Etherscan đối chiếu với bytecode của hợp đồng đang triển khai trên blockchain.

**Khác nhau:**  
Source Code là dạng mã con người có thể đọc và dùng để hiểu logic của hợp đồng, còn Bytecode là dạng mã máy mà EVM thực thi. Trạng thái **Verified** giúp người dùng kiểm tra rằng mã nguồn được công bố tương ứng với hợp đồng đang chạy trên blockchain.

### 2.3. Read Contract

#### decimals()

- Giá trị đọc được: `6`
- Ý nghĩa: USDT sử dụng 6 chữ số thập phân.
- Vì vậy các giá trị số nguyên mà hợp đồng trả về cần chia cho `10^6` để chuyển sang số USDT thực tế.

#### totalSupply()

- Giá trị gốc: `88304342264551152`
- Decimals: `6`

Quy đổi:

`88304342264551152 / 10^6 = 88,304,342,264.551152 USDT`

Tại thời điểm kiểm tra, tổng cung đọc được từ hàm `totalSupply()` là:

**88,304,342,264.551152 USDT**

#### balanceOf()

Địa chỉ được kiểm tra:

`0xF977814e90dA44bFA03b6295A0616a897441aceC`

Kết quả Etherscan trả về:

`16000000001124208`

Quy đổi:

`16000000001124208 / 10^6 = 16,000,000,001.124208 USDT`

Như vậy, tại thời điểm kiểm tra, địa chỉ trên đang có:

**16,000,000,001.124208 USDT**

### 2.4. Write Contract

Qua phần Write Contract của hợp đồng USDT, phát hiện các hàm liên quan đến blacklist:

| Tên hàm | Chức năng | Liên quan đến đóng băng/blacklist |
|---|---|---|
| `addBlackList(address _evilUser)` | Đưa một địa chỉ vào danh sách đen | Có |
| `removeBlackList(address _clearedUser)` | Xóa một địa chỉ khỏi danh sách đen | Có |
| `destroyBlackFunds(address _blackListedUser)` | Xử lý số dư của một địa chỉ đã bị đưa vào danh sách đen | Có |

Ngoài ra còn có các hàm `pause()` và `unpause()`, nhưng đây là cơ chế tạm dừng/khôi phục hoạt động của hợp đồng nói chung, không phải chức năng blacklist riêng một địa chỉ.

Trong các hàm trên, `addBlackList()` là hàm trực tiếp cho phép đưa một địa chỉ cụ thể vào blacklist.

## 3. Trả lời câu hỏi

### Câu 1
**Hợp đồng bạn xem có công bố mã nguồn đã xác thực không?**
Có, hợp đồng có trạng thái "Verified" được ghi nhận trên Etherscan.

### Câu 2

**Tổng cung của đồng đó là bao nhiêu? Đọc ra từ hàm nào?**

Tổng cung được đọc từ hàm `totalSupply()`.

Giá trị gốc Etherscan trả về là:

`88304342264551152`

Hợp đồng có `decimals() = 6`, do đó:

`88304342264551152 / 10^6 = 88,304,342,264.551152 USDT`

Tại thời điểm kiểm tra, tổng cung là:

**88,304,342,264.551152 USDT**

### Câu 3

**Trong tab Write Contract có hàm nào cho phép một địa chỉ đặc biệt đóng băng tài khoản người khác không? Nếu có, tên hàm là gì?**

Có.

Hàm `addBlackList(address _evilUser)` cho phép đưa một địa chỉ cụ thể vào danh sách đen. Qua mã nguồn hợp đồng, hàm này có điều kiện `onlyOwner`, nghĩa là chỉ địa chỉ chủ sở hữu (owner) của hợp đồng mới có quyền thực hiện.

Ngoài ra, hợp đồng còn có:
- `removeBlackList()` để gỡ địa chỉ khỏi blacklist.
- `destroyBlackFunds()` để xử lý số dư của một địa chỉ đã bị blacklist.
