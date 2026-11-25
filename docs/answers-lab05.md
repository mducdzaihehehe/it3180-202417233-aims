# Thảo luận Lab 05

1. Upstream first sửa master trước rồi chuyển bản vá xuống phiên bản bị ảnh hưởng: ít quên nhánh chính, nhưng phải kiểm tra tương thích bản cũ. Release first ưu tiên người dùng đang gặp lỗi, sau đó cần kiểm tra đã chuyển bản vá lên các dòng mới.

2. git log --all --grep với SHA của commit gốc cho thấy các commit cherry-pick -x. git cherry giúp tìm patch tương đương dù SHA khác. Cuối cùng phải chạy cùng ca tìm 'lion' trên v1.0.1, v1.1.0 và master.

3. Tách thay đổi phiên bản khỏi sửa lỗi để khi chuyển bản vá không vô tình hạ phiên bản 1.1.0 về 1.0.1.
