## Mean Reversion
### 1. Định nghĩa
Mean reversion (hồi quy về trung bình) là một thuộc tính của chuỗi thời gian (time series), cho thấy chuỗi này sẽ có một giá trị trung bình dài hạn mà xung quanh đó các giá trị có thể dao động theo thời gian, nhưng cuối cùng sẽ quay trở lại mức trung bình này (Chan, 2013; Ehrman, 2006; Vidyamurthy, 2004). Thuộc tính này đóng vai trò quan trọng trong giao dịch cặp, nơi mà chuỗi thời gian hồi quy về trung bình được tạo ra bằng cách kết hợp hai (hoặc nhiều) tài sản.

Hồi quy về trung bình cho phép nhà giao dịch mua ở mức giá thấp với kỳ vọng rằng giá sẽ quay trở lại mức trung bình dài hạn theo thời gian. Khi giá quay lại mức trung bình lịch sử, nhà giao dịch sẽ đóng vị thế để hiện thực hóa lợi nhuận.

Tất nhiên, điều này phụ thuộc vào giả định rằng mối quan hệ lịch sử giữa các tài sản sẽ tiếp tục trong tương lai, điều này tiềm ẩn rủi ro; do đó, việc theo dõi cẩn thận là rất quan trọng.

#### Giải thích:
-Mean reversion (hồi quy về trung bình): Đây là chiến lược trong đầu tư và giao dịch cặp tài sản. Nó giả định rằng các tài sản có mối quan hệ chặt chẽ về giá trị sẽ có xu hướng quay trở lại khoảng cách trung bình của chúng sau khi xảy ra biến động.
-Giao dịch cặp (Pairs trading): Đây là phương pháp kết hợp hai hoặc nhiều tài sản tương quan để tìm kiếm cơ hội thu lợi nhuận từ sự biến động tương đối giữa các tài sản này.
-Rủi ro: Nếu mối quan hệ lịch sử bị phá vỡ hoặc không còn đúng trong tương lai, chiến lược này có thể dẫn đến thua lỗ.

### 2. Các loại Mean Reversion
#### Longitudinal or Time Series Mean Reversion (Hồi quy về trung bình theo chuỗi thời gian):
>Xảy ra khi sự hồi quy diễn ra theo chiều thời gian.

Ví dụ: Giá tài sản dao động quanh mức trung bình và cuối cùng trở lại mức trung bình dài hạn sau khi lệch về một phía."
#### Cross-Sectional Mean Reversion (Hồi quy về trung bình theo chiều không gian):
>Xảy ra khi sự hồi quy diễn ra trên nhiều tài sản trong cùng một thời điểm. Một số tài sản có thể giảm giá trong khi những tài sản khác tăng, nhưng trung bình chung vẫn ổn định.
### 3. Stationarity (Tính dừng)
#### Định nghĩa:
>"Tính dừng **(stationary)** là thuộc tính của chuỗi thời gian mà trong đó trung bình **(Mean)**, phương sai **(Variance)**, và hiệp phương sai **(Covariance)** không thay đổi theo thời gian.
Một chuỗi dữ liệu stationary có thể được coi là mean-reverting vì các tham số của nó luôn cố định."
### 4. Unit-Root Stationarity (Tính dừng không có gốc đơn)
>Unit Root: Nếu một chuỗi có **"unit root"**, nó sẽ không có tính dừng **(stationary)** mà có xu hướng diverge (phân kỳ) thay vì hồi quy về trung bình. Chuỗi **random walk** là một ví dụ điển hình của chuỗi có unit root.

### 5. Mô hình Mô hình AR(1) (Autoregressive Order 1):
Phương trình mô hình AR(1):
>$y_t = \mu + \rho y_{t-1} + \epsilon_t\$

**Trong đó:**

- $$y_t: Giá trị tại thời điểm t.$$
- $$mu : Hằng số trôi dạt (drift).$$
- $$rho: Hệ số hồi quy (nếu |\rho| < 1, chuỗi hồi quy về trung bình).$$
- $$epsilon_t: Thành phần sai số ngẫu nhiên.$$
- $$Nếu |\rho| \geq 1, chuỗi không hồi quy về trung bình và có thể phân kỳ vô tận.$$



