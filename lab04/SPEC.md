# SPEC - Lab 4: Nhận diện hợp đồng có rủi ro

## 1. Mục đích

Phân tích mã nguồn các hợp đồng token để nhận diện những quyền đặc biệt của chủ sở hữu hợp đồng có thể gây bất lợi hoặc rủi ro cho người nắm giữ token, đồng thời đối chiếu kết quả đọc thủ công với kết quả phân tích của AI.

## 2. Đầu vào

- Mã nguồn các hợp đồng token A, B và C do giảng viên cung cấp.
- Số dòng tương ứng của từng đoạn mã nguồn.
- Kết quả đọc thủ công của sinh viên trước khi sử dụng AI.
- Công cụ AI dùng để phân tích mã nguồn sau bước đọc thủ công.
- Mẫu prompt thẩm định hợp đồng theo hướng dẫn của học phần.

## 3. Quy tắc nghiệp vụ

- R1: Sinh viên phải đọc mã nguồn thủ công trước khi sử dụng AI.

- R2: AI chỉ được sử dụng sau khi sinh viên đã hoàn thành bước đọc thủ công ban đầu.

- R3: Mỗi quyền đặc biệt được phát hiện phải gắn với tên hàm cụ thể.

- R4: Mỗi kết luận về rủi ro phải có số dòng của mã nguồn làm bằng chứng.

- R5: Với mỗi hàm có quyền đặc biệt, phải giải thích cụ thể người nắm giữ token có thể chịu rủi ro gì.

- R6: Không được kết luận một hợp đồng có rủi ro chỉ dựa trên câu trả lời của AI; phải kiểm tra lại trực tiếp trong mã nguồn.

- R7: AI chỉ được phép phân tích dựa trên mã nguồn được cung cấp, không được suy đoán các hàm hoặc quyền không tồn tại trong mã.

- R8: Nếu AI phát hiện thêm một quyền mà sinh viên chưa tìm thấy, sinh viên phải kiểm tra lại tên hàm và số dòng trước khi đưa vào kết luận.

- R9: Nếu AI đưa ra kết luận sai hoặc không có căn cứ trong mã nguồn, phải ghi nhận lỗi đó trong AI_JOURNAL.md.

- R10: Kết quả cuối cùng phải thể hiện rõ sự khác nhau giữa kết quả đọc thủ công và kết quả AI.


## 4. Đầu ra

- Kết quả đọc thủ công đối với hợp đồng A, B và C.
- Kết quả phân tích bằng AI đối với hợp đồng A, B và C.
- Bảng kết luận gồm các cột:
| Hợp đồng | Kết luận | Tên hàm | Số dòng | Rủi ro cho người nắm giữ |

## 5. Trường hợp ngoại lệ

- Nếu một hợp đồng không có quyền đặc biệt gây rủi ro thì phải ghi rõ "Không tìm thấy", không tự suy đoán thêm.

- Nếu AI nêu một hàm nhưng sinh viên không tìm thấy hàm đó trong mã nguồn thì không đưa vào kết luận cuối cùng và phải ghi nhận đây là lỗi của AI.

- Nếu có tên hàm nhưng không xác định được số dòng thì chưa được đưa vào bảng kết luận cho đến khi xác định được số dòng.

- Nếu mã nguồn bị thiếu hoặc không đầy đủ thì phải ghi rõ phần dữ liệu bị thiếu và không đưa ra kết luận vượt quá phần mã đã được cung cấp.

- Nếu AI và sinh viên đưa ra kết quả khác nhau thì phải đối chiếu lại trực tiếp mã nguồn trước khi chốt kết quả cuối cùng.

## 6. Ngoài phạm vi

- Không sửa mã nguồn của các hợp đồng A, B và C.
- Không triển khai các hợp đồng lên blockchain.
- Không thực hiện giao dịch thật.
- Không khai thác hoặc tấn công hợp đồng.
- Không đánh giá các lỗ hổng bảo mật ngoài phạm vi quyền đặc biệt của chủ sở hữu, trừ khi giảng viên yêu cầu.
- Không sử dụng thông tin ngoài mã nguồn được cung cấp để suy đoán rủi ro.

