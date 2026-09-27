# NHẬT KÝ LÀM VIỆC VỚI AI - Lab 6 
(Địa chỉ ví kiểm tra: 0xF977814e90dA44bFA03b6295A0616a897441aceC)

## Lần 1

**Prompt:** Đọc tệp `lab05/SPEC.md` và `AGENTS.md`.

Trước khi viết mã, hãy tóm tắt lại cách bạn hiểu yêu cầu của bài toán, gồm:
- đầu vào,
- cách xác định dòng tiền vào/ra,
- cách xử lý phí,
- giao dịch thất bại,
- đổi wei sang ETH,
- phân trang,
- đầu ra,
- ngoại lệ,
- ngoài phạm vi.

Chưa viết code.
Chỉ tóm tắt cách hiểu và chờ tôi xác nhận.


**AI trả về:** AI đã tóm tắt đúng hầu hết yêu cầu trong SPEC:
- Nhận địa chỉ ví, API key từ biến môi trường và số ngày phân tích.
- Xác định giao dịch vào/ra.
- Tính phí giao dịch.
- Xử lý giao dịch thất bại.
- Đổi wei sang ETH.
- Xử lý phân trang.
- Tạo bảng, biểu đồ và các chỉ tiêu tổng hợp.
- Xử lý các trường hợp ngoại lệ và giới hạn phạm vi.


**Đánh giá:** Dùng được

**Chỗ sai:** Không phát hiện lỗi. Tuy nhiên SPEC còn một điểm mơ hồ về cách khởi tạo số dư lũy kế.

**Cách sửa:** Tôi bổ sung quy ước:
- Số dư lũy kế trong bài này là dòng tiền ròng lũy kế trong kỳ.
- Bắt đầu từ 0.
- Tiền vào thành công: cộng giá trị ETH.
- Tiền ra thành công: trừ giá trị chuyển + phí.
- Tiền ra thất bại: chỉ trừ phí.
- Không coi đây là số dư blockchain thực tế của ví.

Sau đó yêu cầu AI xác nhận lại cách hiểu trước khi viết code.

**AI phát hiện:** Sinh viên phát hiện điểm mơ hồ trong SPEC và yêu cầu làm rõ trước khi AI sinh mã.

**Ai xác nhận lại:** AI xác nhận đã hiểu rằng số dư lũy kế là dòng tiền ròng phát sinh trong kỳ, bắt đầu từ 0; giao dịch vào được cộng giá trị, giao dịch ra thành công trừ giá trị và phí, giao dịch ra thất bại chỉ trừ phí.

AI đồng thời xác nhận đây không phải số dư blockchain thực tế của ví.

## Lần 2

**Prompt:** Tôi xác nhận cách hiểu của bạn là đúng.

Bây giờ hãy bắt đầu viết chương trình Python thực hiện đúng toàn bộ yêu cầu trong:

- lab05/SPEC.md
- AGENTS.md

và điểm bổ sung đã thống nhất về "số dư lũy kế dòng tiền trong kỳ".

YÊU CẦU:

1. Tạo chương trình:
   lab06/wallet_analyzer.py

2. Chương trình phải:
   - Nhận địa chỉ ví Ethereum.
   - Đọc khóa API từ biến môi trường ETHERSCAN_API_KEY.
   - Cho phép nhập số ngày phân tích, mặc định 90 ngày.
   - Lấy giao dịch ETH gốc từ Etherscan.
   - Không phân tích token ERC-20.
   - Xác định giao dịch vào/ra đúng theo SPEC.
   - Với giao dịch ra thành công:
     trừ giá trị chuyển + phí.
   - Với giao dịch ra thất bại:
     chỉ trừ phí.
   - Đổi wei sang ETH trước khi hiển thị.
   - Xử lý phân trang để không bỏ sót dữ liệu.
   - Sắp xếp giao dịch theo thời gian tăng dần.
   - Tính dòng tiền ròng lũy kế bắt đầu từ 0.
   - Hiển thị bảng giao dịch.
   - Hiển thị:
     + Tổng dòng tiền vào
     + Tổng dòng tiền ra
     + Số dư lũy kế cuối kỳ
   - Vẽ biểu đồ đường số dư lũy kế theo thời gian.
   - Xử lý các trường hợp ngoại lệ trong SPEC.

3. Không hardcode API key trong mã nguồn.

4. Không yêu cầu private key hoặc seed phrase.

5. Không sửa:
   - lab01/
   - lab02/
   - lab03/
   - lab04/
   - lab05/
   - SPEC.md gốc
   - AGENTS.md

6. Không git commit.
7. Không git push.

Sau khi viết xong:
- Hiển thị file nào đã được tạo.
- Giải thích ngắn gọn cấu trúc chương trình.
- KHÔNG tự sửa hoặc tự tối ưu thêm sau khi sinh phiên bản đầu tiên.
- Dừng lại để tôi tự chạy và kiểm tra.

**AI trả về:**  AI tạo chương trình Python `wallet_analyzer.py` để lấy giao dịch từ Etherscan,
phân loại dòng tiền vào/ra, tính phí, đổi wei sang ETH, tính số dư lũy kế
và vẽ biểu đồ.

**Đánh giá:** Phải sửa

**Chỗ sai:** 
Chương trình sử dụng endpoint Etherscan V1:

`https://api.etherscan.io/api`

Khi chạy thực tế, Etherscan trả về thông báo:

`You are using a deprecated V1 endpoint, switch to Etherscan API V2`

nên chương trình không lấy được dữ liệu giao dịch.

**Cách sửa:** Tôi yêu cầu AI chỉ sửa lỗi phiên bản API. AI đã:
- đổi endpoint thành `https://api.etherscan.io/v2/api`;
- thêm tham số `chainid = 1` cho Ethereum Mainnet.

**AI phát hiện:** Sinh viên phát hiện lỗi phiên bản API và yêu cầu AI sửa lại.

## Lần 3

**Prompt:** Sau khi sửa Etherscan API V1 sang V2, tôi chạy lại chương trình và nhận được lỗi:

`Missing chainid parameter (required for v2 api)`

Hãy kiểm tra nguyên nhân trong `lab06/wallet_analyzer.py`.

Chỉ sửa nguyên nhân làm cho tham số `chainid` không được gửi đến Etherscan.
Không sửa hoặc tối ưu các phần khác.
Không git commit.
Không git push.

Sau khi sửa, hãy cho biết dòng nào đã thay đổi và vì sao, sau đó dừng lại để tôi tự chạy lại.

**AI trả về:**  AI xác định chương trình đang sử dụng Etherscan API V1 đã ngừng hỗ trợ.  
AI sửa endpoint từ `https://api.etherscan.io/api` sang
`https://api.etherscan.io/v2/api` và bổ sung tham số `chainid = 1`
để xác định mạng Ethereum Mainnet.

**Đánh giá:** Phải sửa

**Chỗ sai:**

Mặc dù chương trình đã khai báo `chainid = 1` trong `params`,
lệnh gọi API chỉ sử dụng:

`requests.get(url)`

nên toàn bộ `params`, bao gồm `chainid`, không được gửi đến Etherscan.

Khi chạy thực tế, API trả về:

`Missing chainid parameter (required for v2 api)`

**Cách sửa:**

Tôi yêu cầu AI kiểm tra nguyên nhân API vẫn báo thiếu `chainid`.
AI xác định biến `params` đã được tạo nhưng chưa được truyền vào request
và sửa:

`requests.get(url)`

thành:

`requests.get(url, params=params)`

Sau khi sửa, tôi chạy lại chương trình và chương trình đã lấy được dữ liệu,
hiển thị bảng kết quả và vẽ được biểu đồ.

**Ai phát hiện:** Sinh viên phát hiện

## Kiểm tra 6 điểm:
## 1. Kiểm tra đơn vị tiền:

Sau khi chương trình chạy được, tôi kiểm tra đơn vị tiền bằng cách
đối chiếu một giao dịch với Etherscan:

- Transaction Hash:
  `0x2be62ae5fd796749add7e4fe685e3e09e6a4ce220be87d095b2c45525c783731`
- Chương trình hiển thị: `100000.000000 ETH`
- Etherscan hiển thị: `100,000 ETH`
- Chương trình hiển thị phí: `0.000044 ETH`
- Etherscan hiển thị phí: `0.000043693326306 ETH`

Phần phí chênh lệch ở số chữ số hiển thị do chương trình làm tròn đến
6 chữ số thập phân. Kết quả đối chiếu cho thấy việc chuyển đổi wei sang
ETH là đúng.

Bằng chứng: `lab06/Kiem tra don vi ETH.png`

## 2. Kiểm tra khóa API

Chương trình không ghi khóa API trực tiếp trong mã nguồn mà đọc từ biến môi trường
`ETHERSCAN_API_KEY` bằng `os.environ.get()`.

Kết luận: đạt yêu cầu bảo mật API key.

## 3. Kiểm tra phân trang:
Tạm đặt `offset = 100` để kiểm thử. Chương trình lần lượt gọi nhiều trang
và tăng `page` sau mỗi lần lấy đủ dữ liệu.

Sau kiểm thử, tôi trả `offset` về `10000` theo SPEC.

Kết luận: cơ chế phân trang hoạt động.

## 4. Kiểm tra giao dịch thất bại

Tôi tiếp tục kiểm tra quy tắc xử lý giao dịch thất bại bằng cách đếm các
giao dịch đi ra có `isError = 1`.

Kết quả với dữ liệu ví kiểm tra trong 90 ngày:
`Số giao dịch đi ra thất bại tìm thấy: 0`.

Do dữ liệu thực tế không có giao dịch đi ra thất bại trong khoảng kiểm tra,
tôi chưa có giao dịch thật để đối chiếu quy tắc này trên Etherscan.

## 5. Kiểm tra xử lý lỗi:

Tôi tiếp tục kiểm tra khả năng xử lý lỗi bằng cách cố tình thay
`ETHERSCAN_API_KEY` bằng một API key không hợp lệ rồi chạy lại chương trình.

Kết quả chương trình trả về:

`Lỗi từ Etherscan API: Invalid API Key (#err2)`

và dừng xử lý bình thường, không xuất hiện Traceback.

Kết luận: chương trình xử lý trường hợp API key sai đúng yêu cầu.