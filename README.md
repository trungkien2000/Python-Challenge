# Python-Challenge

Thực hiện: Trung Kiên

Ngày thực hiện: 4/4/2022, 7/4/2022

Link challenge: http://www.pythonchallenge.com/pc/def/equality.html

### Ý tưởng thực hiện:
- Inspect để xem trang web có gì lạ không -> kiểm tra thì thấy có một đoạn text dài được comment ở cuối.
- Trang web chính có câu "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides." -> 1 chữ cái dược bao bởi CHÍNH XÁC 3 vệ sĩ lớn ở bên -> có thể mỗi ký tự của bức thư nằm giữa 3 ký tự hoa mỗi bên. Trong hình ảnh xuất hiện trên trang web là 7 ngọn nến, mỗi bên có 3 ngọn nến lớn (tượng trưng cho 3 vệ sĩ lớn), ở giữa là ngọn nến nhỏ -> chữ cái được lấy ra phải là chữ cái thường. Ví dụ: ABCoDEF -> chữ cái cần lấy là o 
-> sử dụng Regular Expression

