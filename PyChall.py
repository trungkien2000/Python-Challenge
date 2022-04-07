import requests  # thư viện requests của python dùng để gửi các yêu cầu HTTP đến dịch vụ web
import re  # thư viện re, dùng để xử lý Regular expression

if __name__ == "__main__":

    # câu lệnh dùng để requests đến trang web, với yêu cầu get
    # response trả về sẽ được dùng lệnh text để lấy toàn bộ text
    html = requests.get(
        "http://www.pythonchallenge.com/pc/def/equality.html").text

    # findall dùng để tìm toàn bộ chuỗi có thể có theo điều kiện bên trong
    # với điều kiện là đoạn comment HTML với bất kì nội dung nào bên trong
    # re.DOTALL để ký tự đặc biệt '.' có thể khớp với bất kì ký tự nào, kể cả dòng mới (newline)
    # [-1] ở cuối câu lệnh dùng để lấy đoạn comment cuối cùng của toàn bộ text, do khi check source web thì đoạn text cần lấy ở cuối
    data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

    # vì các ký tự tìm được là từng ký tự riêng lẻ, nên dùng hàm join để nối chúng lại
    # [A-Z]{3}: khớp với 3 ký tự hoa liên tiếp
    # [a-z]: khớp với bất kì ký tự thường nào
    # ([a-z]): chỉ lấy các kết quả có ký tự thường tại vị trí này (vị trí bên trong 6 ký tự hoa)
    # vì yêu cầu là CHÍNH XÁC 3 ký tự hoa mỗi bên, nên bên ngoài 3 ký tự hoa phải là ký tự thường
    _str = "".join(re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", data))

    print(_str)  # linkedlist
