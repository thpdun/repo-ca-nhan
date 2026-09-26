# SPEC - Lab 2: Ví và giao dịch đầu tiên

## 1. Mục đích

Thực hiện giao dịch Sepolia ETH và hiểu nguyên nhân một giao dịch có thể thất bại.

## 2. Đầu vào

- Ví MetaMask.
- Mạng thử nghiệm Sepolia.
- Sepolia ETH.
- Địa chỉ ví thứ 2.

## 3. Quy tắc nghiệp vụ

- R1: Chỉ sử dụng mạng Sepolia.
- R2: Giao dịch thành công chuyển 0.01 Sepolia ETH cho ví thứ 2.
- R3: Ghi lại mã băm của giao dịch.
- R4: Thực hiện một tình huống thất bại có chủ đích theo yêu cầu Lab 2.
- R5: Không sử dụng ETH thật trên Ethereum Mainnet.
- R6: Không chia sẻ Secret Recovery Phrase hoặc private key.

## 4. Đầu ra

- Một giao dịch thành công.
- Các tình huống giao dịch thất bại có chủ đích.
- Tệp lab02.md ghi nhận kết quả và bảng đối chiếu.

## 5. Trường hợp ngoại lệ

- Nếu không đủ Sepolia ETH thì chưa thực hiện giao dịch.
- Nếu địa chỉ người nhận không hợp lệ thì MetaMask có thể từ chối trước khi gửi.
- Nếu số dư không đủ trả cả số tiền chuyển và gas thì giao dịch không thể thực hiện.

## 6. Ngoài phạm vi

- Không sử dụng Ethereum Mainnet.
- Không chuyển tiền thật.
- Không sử dụng token khác ngoài Sepolia ETH.

