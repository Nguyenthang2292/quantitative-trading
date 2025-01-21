***Bản quyền dịch thuật và diễn giải thuộc về justinnguyen92&copy; - [telegram](https://t.me/justinnguyen92)***

# Mean Reversion
## 1. Định nghĩa
Hồi quy về trung bình *(mean reversion)* là một thuộc tính của chuỗi thời gian *(time series)*, cho thấy chuỗi này sẽ có một giá trị trung bình dài hạn mà xung quanh đó các giá trị có thể dao động theo thời gian, nhưng cuối cùng sẽ quay trở lại mức trung bình này *(Chan, 2013; Ehrman, 2006; Vidyamurthy, 2004)*. Thuộc tính này đóng vai trò quan trọng trong giao dịch cặp *(pair trading)*, nơi mà chuỗi thời gian hồi quy về trung bình được tạo ra bằng cách kết hợp hai (hoặc nhiều) tài sản. Hồi quy về trung bình cho phép nhà giao dịch mua ở mức giá thấp với kỳ vọng rằng giá sẽ quay trở lại mức trung bình dài hạn theo thời gian. Khi giá quay lại mức trung bình lịch sử, nhà giao dịch sẽ đóng vị thế để hiện thực hóa lợi nhuận. Tất nhiên, điều này phụ thuộc vào giả định rằng mối quan hệ lịch sử giữa các tài sản sẽ tiếp tục trong tương lai, điều này tiềm ẩn rủi ro; do đó, việc theo dõi cẩn thận là rất quan trọng.

#### Giải thích:
- Hồi quy về trung bình *(mean reversion)*: Đây là chiến lược trong đầu tư và giao dịch cặp tài sản. Nó giả định rằng các tài sản có mối quan hệ chặt chẽ về giá trị sẽ có xu hướng quay trở lại khoảng cách trung bình của chúng sau khi xảy ra biến động.
- Giao dịch cặp *(pairs trading)*: Đây là phương pháp kết hợp hai hoặc nhiều tài sản tương quan để tìm kiếm cơ hội thu lợi nhuận từ sự biến động tương đối giữa các tài sản này.
- Rủi ro: Nếu mối quan hệ lịch sử bị phá vỡ hoặc không còn đúng trong tương lai, chiến lược này có thể dẫn đến thua lỗ.

## 2. Các loại Mean Reversion
#### Longitudinal or Time Series Mean Reversion (Hồi quy về trung bình theo chuỗi thời gian):
>Xảy ra khi sự hồi quy diễn ra theo trục thời gian và có một giá trị trung bình dài hạn *(long-term average value)*. Độ lệch *(deviation)* xảy ra tại một thời điểm theo một hướng và tại một thời điểm khác theo hướng ngược lại.

#### Cross-Sectional Mean Reversion (Hồi quy về trung bình theo chiều không gian):
>Xảy ra khi sự hồi quy diễn ra trên trục thời gian và có giá trị trung bình trên các tài sản. Một số tài sản có thể giảm giá trong khi những tài sản khác tăng, nhưng trung bình chung vẫn ổn định *(Fabozzi et al., 2010)*.

## 3. Stationarity (Tính dừng)
#### Định nghĩa:
>Tính dừng *(stationary)* là thuộc tính của chuỗi thời gian mà trong đó đề cập đến tính chất mà các số liệu thống kê (như trung bình *(mean)*, phương sai *(variance)*, và hiệp phương sai *(covariance)*) của một chuỗi thời gian vẫn cố định theo thời gian. Một chuỗi dữ liệu stationary có thể được coi là mean-reverting *(Vidyamurthy, 2004)* vì các tham số của nó luôn cố định.
>
><span style="color:red">Tính dừng là một tính chất liên quan đến *mean reversion*, nhưng đó là hai khái niệm khác nhau</span>.

## 4. Unit-Root Stationarity
>"Unit-Root Stationarity" là một loại tính dừng cụ thể *(Tsay, 2010, 2013)*

Nó đề cập đến việc mô hình hóa chuỗi thời gian - *time series* với mô hình *autoregressive (AR)* không có gốc đơn vị - *no unit roots* (điều này liên quan đến tiến trình *Ornstein–Uhlenbeck process* trong thời gian liên tục). Chuỗi thời gian có một gốc đơn vị *(A time series with a unit root)* thì không dừng và có xu hướng phân kỳ theo thời gian. Một ví dụ đáng chú ý về *unit-root nonstationarity* là mô hình *random walk* thường được sử dụng cho *log-prices* (xem Chương 3):

$$y_t = \mu + y_{t-1} + \epsilon_t\tag{1}$$

**Trong đó:**
- $y_t$ biểu thị *log-price*  tại thời điểm $t$, 
- $\mu$ là độ trôi *(drift)*,  
- $\epsilon_t$ là phần dư *residual*.

Hình 15.1 cho thấy một ví dụ về Chuỗi thời gian có một gốc đơn vị *(A time series with a unit root)* không quay trở lại giá trị trung bình theo cách được kiểm soát.(61) 

![image](https://github.com/user-attachments/assets/5c2faea7-d674-4f16-bef1-4fa0135ed4da)
Figure 15.1: Example of a random walk (nonstationary time series with unit root).

Mặt khác, nếu không có gốc đơn vị, chuỗi thời gian sẽ không phân kỳ và cuối cùng sẽ quay trở lại giá trị trung bình; một ví dụ là mô hình AR bậc 1 (AR(1)):

```math
y_t = \mu + \rho y_{t-1} + \epsilon_t\
```

Với $|\rho| < 1$. Hình 15.2 minh họa chuỗi thời gian AR(1) với *no unit root* ($rho = 0.2$ và \$mu = 0$), chuỗi này hồi về giá trị trung bình một cách có kiểm soát.

![image](https://github.com/user-attachments/assets/9f8fcf2f-ee1f-4fab-8152-c66d4472f64d)
Figure 15.2: Example of a unit-root stationary AR(1) sequence.

**Trong đó:**
- $y_t$: Biểu thị *log-price*  tại thời điểm $t$.
- $\mu$: Hằng số trôi dạt (drift).
- $\rho$: Hệ số hồi quy (nếu $|\rho| < 1$, chuỗi hồi quy về trung bình).
- $\epsilon_t$: là phần dư *residual*.
- Nếu $|\rho| \geq 1$, chuỗi không hồi quy về trung bình và có thể phân kỳ vô tận. (chuyển về công thức [1])

#### Ví dụ code:
Mô hình AR(1)

```python
# Reimport necessary libraries after the environment reset
import numpy as np
import matplotlib.pyplot as plt

# Thiết lập tham số cho mô hình AR(1)
np.random.seed(42)  # Đảm bảo tính tái lập kết quả
T = 100  # Số điểm dữ liệu
mu = 0  # Drift (hằng số trôi dạt)
rho = 0.8  # Hệ số hồi quy (phải nhỏ hơn 1 để có tính dừng)
sigma = 1  # Độ lệch chuẩn của nhiễu ngẫu nhiên
epsilon = np.random.normal(0, sigma, T)  # Thành phần phần dư

# Khởi tạo chuỗi thời gian AR(1)
y = np.zeros(T)
y[0] = mu  # Giá trị ban đầu

# Tính chuỗi AR(1)
for t in range(1, T):
    y[t] = mu + rho * y[t - 1] + epsilon[t]

# Vẽ biểu đồ chuỗi AR(1)
plt.figure(figsize=(10, 6))
plt.plot(y, label=f'AR(1) Model: $\mu={mu}$, $\\rho={rho}$')
plt.axhline(mu, color='r', linestyle='--', label='Mean (μ)')
plt.title('Autoregressive Model AR(1)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
```

![output (11)](https://github.com/user-attachments/assets/134084af-9b57-49ba-bfab-12d16e9fc7ef)

### Giải thích Mô hình AR(1) (Autoregressive Order 1)

#### Mô tả biểu đồ:
- Đây là chuỗi thời gian được tạo từ mô hình AR(1) với:
  - **$\mu$ (Mean)**: Hằng số trung bình bằng 0.
  - **$\rho$ (Rho)**: Hệ số hồi quy bằng 0.8, cho thấy giá trị ở thời điểm $t$ phụ thuộc 80% vào giá trị ở thời điểm trước đó ($t - 1$).
  - **$\epsilon$ (Phần dư)**: Thành phần ngẫu nhiên phân phối chuẩn có độ lệch chuẩn bằng 1.

#### Diễn giải:
- Đường màu vàng biểu diễn chuỗi thời gian theo mô hình AR(1).
- Đường đỏ là đường trung bình (mean) bằng 0.
- Chuỗi dao động quanh mức trung bình và không có xu hướng phân kỳ (vì |ρ| < 1).

#### Kết luận:
Mô hình AR(1) thể hiện sự hồi quy, trong đó giá trị hiện tại phụ thuộc vào giá trị trước đó cùng với một mức phần dư. Với hệ số hồi quy ρ < 1, chuỗi sẽ hội tụ về trung bình theo thời gian. Nếu ρ ≥ 1, chuỗi sẽ trở thành "random walk" hoặc phân kỳ thay vì hồi quy.

---

Mặc dù Hồi quy về trung bình *(mean reversion)* và *unit-root stationarity* không phải là các khái niệm tương đương nhau, nhưng trong thực tế, unit-root stationarity* là một đại diện *(proxy)* thuận tiện cho Hồi quy về trung bình *(mean reversion)* *(Tsay, 2010, 2013)*. Trên thực tế, việc kiểm tra *unit-root stationarity* là phương pháp tiêu chuẩn để xác định tính hồi quy về trung bình trong thực tế.

Lấy sai phân *(Differencing)* là một thao tác thường được sử dụng để đạt được tính dừng *(Tsay, 2010, 2013)*. Nó đề cập đến việc lấy sự chênh lệch giữa các mẫu liên tiếp của chuỗi thời gian $y_1, y_2, y_3, \ldots$ để tạo ra:

$$\Delta y_t = y_t - y_{t-1}$$

Ý nghĩa của thao tác này là một chuỗi thời gian không có tính dừng, chẳng hạn như một chuỗi bước ngẫu nhiên *(random walk)*, có thể trở thành chuỗi dừng sau khi lấy sai phân *(differencing)*. 

Đây chính là trường hợp khi lấy sai phân *log-price* của một tài sản để tính toán *log-return* (Xem thêm Chương 3). Khi đó, chúng ta nói rằng chuỗi *log-price* được tích hợp ở bậc 1 *(integrated of order 1)*. Ngoài ra, cũng có thể xem xét sai phân ở bậc cao hơn *(higher-order differencing)*.

#### Ví dụ code: 
Lấy sai phân `log-price` của một tài sản để tính toán `log-return` (ví dụ: chuỗi *time-series* của `EURUSD` với giá đóng cửa `close`) - kiểm tra tính dừng của ví dụ `EURUSD` trên.

```python
# ========================================================================================================
# VÍ DỤ STATIONARY CỦA MỘT CHUỖI TIME SERIES
# ví dụ code Lấy sai phân log-price của một tài sản để tính toán log-return (log lợi nhuận) 
# (ví dụ: chuỗi time series của EURUSD với giá đóng cửa close) - kiểm tra tính dừng của ví dụ EURUSD
# ========================================================================================================
# Import các thư viện cần thiết
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Tạo chuỗi thời gian giả lập giá đóng cửa của cặp EUR/USD
np.random.seed(42)
T = 200  # số lượng điểm dữ liệu
initial_price = 1.1  # giá ban đầu
returns = np.random.normal(0, 0.001, T)  # lợi nhuận ngẫu nhiên nhỏ
prices = initial_price * np.exp(np.cumsum(returns))  # chuỗi giá giả lập

# Tạo DataFrame chứa giá đóng cửa EUR/USD
df = pd.DataFrame({'Close': prices}, index=pd.date_range(start='2022-01-01', periods=T))

# Tính toán log-price và log-return (lấy sai phân)
df['Log_Close'] = np.log(df['Close'])  # log-price
df['Log_Return'] = df['Log_Close'].diff()  # log-return (sai phân)

# Kiểm tra tính dừng bằng Augmented Dickey-Fuller (ADF) Test cho log-return
adf_result = adfuller(df['Log_Return'].dropna())
p_value = adf_result[1]

# Vẽ biểu đồ log-price và log-return
plt.figure(figsize=(14, 6))

plt.subplot(2, 1, 1)
plt.plot(df['Log_Close'], label='Log-Price (EUR/USD)', color='blue')
plt.title('Log-Price of EUR/USD')
plt.xlabel('Time')
plt.ylabel('Log-Price')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(df['Log_Return'], label='Log-Return (Differencing)', color='orange')
plt.title('Log-Return (First Differencing)')
plt.xlabel('Time')
plt.ylabel('Log-Return')
plt.legend()

plt.tight_layout()
plt.show()

p_value
```
#### Result
>3.0415339027305817e-27

![output (2)](https://github.com/user-attachments/assets/017517f9-f1fb-43bd-84e1-8cce27ae277f)

#### Phân tích kết quả kiểm tra tính dừng cho log-return của EUR/USD
##### 1. Biểu đồ Log-Price và Log-Return:
- **Log-Price (trên)**: Chuỗi `log-price` biến động dần theo thời gian, có xu hướng tăng hoặc giảm, không cố định quanh mức trung bình → Có thể là chuỗi không dừng.
- **Log-Return (dưới)**: Chuỗi `log-return` là sai phân bậc 1 của `log-price`. Biểu đồ cho thấy chuỗi này dao động quanh mức 0 mà không có xu hướng tăng hoặc giảm dài hạn rõ ràng.
##### 2. Kết quả kiểm tra ADF Test (Augmented Dickey-Fuller):
- **P-value**: $\approx 3.04 \times 10^{-27}$, nhỏ hơn 0.05 $\Rightarrow$ Bác bỏ giả thuyết $H_0$.
- **Kết luận**: Chuỗi `log-return` có tính dừng $\Rightarrow$ Đây là một chuỗi *stationary* sau khi lấy sai phân bậc 1.

#### Tóm lại:
- Chuỗi giá `log-price` ban đầu không có tính dừng.
- Sau khi lấy sai phân `log-price (log-return)`, chuỗi trở thành dừng, phù hợp với lý thuyết *mean reversion* trong chuỗi *time-series*.

---

# 1. Mean Reversion (Hồi quy về trung bình)
#### Định nghĩa: 
*Mean reversion* là xu hướng của chuỗi thời gian quay về mức trung bình dài hạn theo thời gian.

#### Ứng dụng:
- Chiến lược giao dịch *mean reversion* dựa vào việc mua khi giá thấp hơn mức trung bình và bán khi giá cao hơn mức trung bình.

#### Thách thức:
- Việc tìm một tài sản riêng lẻ có tính hồi quy về trung bình với hành vi có thể dự đoán được rất khó.
- Tuy nhiên, dễ dàng hơn khi tìm cặp tài sản có chung tính hồi quy về trung bình.

# 2. Cointegration (Đồng tích hợp)
>Định nghĩa: *Cointegration* là tính chất trong đó hai hoặc nhiều tài sản, dù không hồi quy về trung bình riêng lẻ, lại có mối quan hệ hồi quy về trung bình đối với nhau *(Chan, 2013; Ehrman, 2006; Vidyamurthy, 2004)*.
>
>Điều này thường xảy ra khi bản thân các chuỗi chứa các xu hướng ngẫu nhiên (tức là chúng không dừng) nhưng tuy nhiên chúng vẫn di chuyển gần nhau theo thời gian theo cách mà sự khác biệt *(difference)* của chúng vẫn ổn định (tức là dừng). Do đó, khái niệm Đồng tích hợp mô phỏng sự tồn tại của trạng thái cân bằng dài hạn mà một hệ thống kinh tế hội tụ theo thời gian.

Ý tưởng trực quan là, trong khi có thể khó hoặc không thể dự đoán các tài sản riêng lẻ, thì có thể dễ dàng hơn để dự đoán hành vi tương đối của chúng. Một ví dụ phổ biến:"Một người đàn ông say rượu *(random walk)* đi lang thang với một con chó *(another random walk)*.
- Tuy cả hai đi theo những hướng không thể đoán trước *(non-stationary)*, nhưng khoảng cách giữa người và chó vẫn ổn định trong dài hạn ***(distance between them is mean reverting and stationary) → Cointegration."***

<center>
<img src="https://github.com/user-attachments/assets/565c559e-cb20-468b-91bf-6a0f486d1c11" width="300" align="center">
</center>

### Ý nghĩa thực tế:
Mặc dù rất khó để dự đoán chuyển động của từng tài sản một cách độc lập (vì chúng có thể là chuỗi không dừng *(non-stationary series)*), nhưng có thể dự đoán mối quan hệ tương đối giữa chúng (như *spread* giữa hai tài sản) nếu có đồng tích hợp.
- Trong các hệ thống kinh tế, *cointegration* phản ánh sự tồn tại của trạng thái cân bằng dài hạn giữa các thành phần, nơi hệ thống có xu hướng hội tụ theo thời gian.

### Về mặt toán học:
Một chuỗi thời gian đa biến $y_1, y_2, y_3, \ldots$ được gọi là đồng tích hợp *(cointegration)* nếu có một tổ hợp tuyến tính nào đó của các chuỗi có thể trở thành chuỗi dừng *(stationary)*. Ví dụ, nếu $y_t$ là chuỗi không dừng, nhưng tổ hợp tuyến tính $w^T y_t$ trở thành chuỗi dừng với một trọng số $w$, thì ta nói rằng chuỗi này có tính đồng tích hợp.

- *Cointegration* có thể được hiểu là một phiên bản nâng cao của việc lấy sai phân *(differencing)* chuỗi để đạt được tính dừng.
- Thay vì phải lấy sai phân, ta tìm một tổ hợp tuyến tính phù hợp giữa các chuỗi dữ liệu để tạo thành một chuỗi dừng. <span style="color:red">Tính chất này có hệ quả đáng chú ý về mặt giao dịch và nó hình thành nên những điều cơ bản của *pairs trading*</span>.

Một cách phổ biến để mô hình hóa đồng tích hợp của hai chuỗi thời gian là:

$$y_{1t} = \gamma x_t + w_{1t}$$

$$y_{2t} = x_t + w_{2t}$$
[15.1]

**Trong đó:**
- $x_t$ là một chuỗi bước ngẫu nhiên *stochastic common trend "random walk"* với phương trình:

$$x_t = x_{t-1} + w_t$$

- $w_{1t}, w_{2t}, w_t$  là các phần dư residual độc lập, có phương sai *variances* $\sigma^2_1, \sigma^2_2, \sigma^2$ .
- Hệ số $\gamma$ quyết định mối quan hệ đồng tích hợp giữa hai chuỗi dữ liệu.

Tuy mỗi chuỗi riêng *time series* riêng lẻ $y_{1t}$ và $y_{2t}$ là 1 *random walk* với *noise* thêm vào, do đó đều không dừng, nhưng do cả hai chia sẻ một xu hướng chung - *common stochastic trend* $x_t$, sự kết hợp tuyến tính giữa chúng có thể loại bỏ xu hướng này. Chuỗi **"spread"** kết hợp tuyến tính giữa chúng mà không có xu hướng - *This linear combination without the trend* $y_{1t}$ và $y_{2t}$  được biểu diễn là:

$$z_t = y_{1t} - \gamma y_{2t} = w_{1t} - \gamma w_{2t},$$

Chuỗi $z_t$ là một chuỗi dừng và có tính hồi quy về trung bình *(mean-reverting)*.

### Giải thích chi tiết
#### 1. Đồng tích hợp *(Cointegration)* là gì?

- Mặc dù từng chuỗi thời gian riêng lẻ $y_{1t}$ và $y_{2t}$ có thể không dừng *(random walk)*, sự kết hợp tuyến tính giữa chúng có thể trở thành một chuỗi có tính dừng.
- Trong bối cảnh *pairs trading*, *cointegration* được sử dụng để tìm kiếm cặp tài sản có sự liên kết dài hạn nhưng tạm thời phân kỳ, cho phép khai thác lợi nhuận khi chúng quay trở lại trạng thái cân bằng.

#### 2. Ví dụ minh họa:
- Giả sử chuỗi $x_t$ đại diện cho "xu hướng chung" của hai tài sản.

- Chuỗi $y_{1t}$ và $y_{2t}$  là giá của hai tài sản có mối quan hệ với xu hướng chung $x_t$, cộng thêm thành phần nhiễu $w_{1t}$ và $w_{2t}$ .

- Spread $z_t = y_{1t} - \gamma y_{2t}$ loại bỏ xu hướng $x_t$ và chỉ còn lại phần nhiễu $w_{1t}$ và $w_{2t}$.

#### 3. Ý nghĩa trong giao dịch:
- Nếu chuỗi *spread* $z_t$ là chuỗi dừng, điều này cho thấy sự chênh lệch giữa hai tài sản có xu hướng hồi quy về mức trung bình.
- Khi spread lớn hơn mức trung bình, có thể thực hiện chiến lược **SHORT** tài sản tăng giá và **LONG** tài sản giảm giá, kỳ vọng rằng giá sẽ hồi tụ về mức cân bằng.

#### 4. Tóm tắt:
*Cointegration* là công cụ quan trọng trong việc tìm kiếm cặp tài sản có quan hệ dài hạn. Dù từng chuỗi dữ liệu riêng lẻ có thể là *random walk* (không dự đoán được), nhưng sự kết hợp giữa chúng có thể tạo ra một chuỗi dừng, mang lại cơ hội thực hiện chiến lược *pairs trading* dựa trên tính hồi quy về trung bình của *spread*.

---

#### Ví dụ code:
Tính `spread` chuỗi *time-series* của `EURUSD` với giá đóng cửa `close` và đoạn chuỗi *time-series* của `GBPUSD` với giá đóng cửa `close`, kiểm tra tính dừng của chuỗi `spread` - kết luận *Cointegration* giữa 2 chuỗi 

```python
# ======================================================================================================================================
# VÍ DỤ COINTEGRATION GIỮA HAI CHUỖI TIME SERIES
# cho tôi ví dụ đoạn code tính spread chuỗi time series của EURUSD với giá đóng cửa [close] và đoạn chuỗi time series của GBPUSD 
# với giá đóng cửa [close],kiểm tra tính dừng của chuỗi spread - kết luận Cointegration giữa 2 chuỗi 
​# ======================================================================================================================================
# Import các thư viện cần thiết
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint, adfuller

# Tạo chuỗi thời gian giả lập giá đóng cửa của EUR/USD và GBP/USD
np.random.seed(42)
T = 200  # số lượng điểm dữ liệu
initial_price_eur = 1.1  # Giá ban đầu EUR/USD
initial_price_gbp = 1.3  # Giá ban đầu GBP/USD

returns_eur = np.random.normal(0, 0.001, T)  # Lợi nhuận ngẫu nhiên EUR/USD
returns_gbp = np.random.normal(0, 0.001, T)  # Lợi nhuận ngẫu nhiên GBP/USD

prices_eur = initial_price_eur * np.exp(np.cumsum(returns_eur))  # Chuỗi giá EUR/USD
prices_gbp = initial_price_gbp * np.exp(np.cumsum(returns_gbp))  # Chuỗi giá GBP/USD

# Tạo DataFrame chứa giá đóng cửa
df = pd.DataFrame({
    'EURUSD_Close': prices_eur,
    'GBPUSD_Close': prices_gbp
}, index=pd.date_range(start='2022-01-01', periods=T))

# Vẽ biểu đồ giá EUR/USD và GBP/USD
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['EURUSD_Close'], label='EUR/USD Close', color='blue')
plt.plot(df.index, df['GBPUSD_Close'], label='GBP/USD Close', color='orange')
plt.title('Giá đóng cửa EUR/USD và GBP/USD')
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.legend()
plt.show()

# Tính toán chuỗi spread: spread = EUR/USD - gamma * GBP/USD
gamma = np.polyfit(df['GBPUSD_Close'], df['EURUSD_Close'], 1)[0]  # Tìm gamma qua hồi quy tuyến tính
df['Spread'] = df['EURUSD_Close'] - gamma * df['GBPUSD_Close']

# Kiểm tra tính dừng của chuỗi spread bằng Augmented Dickey-Fuller (ADF) Test
adf_result = adfuller(df['Spread'].dropna())
p_value = adf_result[1]

# Vẽ biểu đồ chuỗi spread
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['Spread'], label='Spread (EUR/USD - gamma * GBP/USD)', color='purple')
plt.axhline(df['Spread'].mean(), color='red', linestyle='--', label='Mean (Spread)')
plt.title('Spread giữa EUR/USD và GBP/USD')
plt.xlabel('Time')
plt.ylabel('Spread')
plt.legend()
plt.show()

# Kiểm tra Cointegration bằng kiểm định Engle-Granger
coint_score, coint_p_value, _ = coint(df['EURUSD_Close'], df['GBPUSD_Close'])

# Kết luận
conclusion = "Có Cointegration" if coint_p_value < 0.05 else "Không có Cointegration"

p_value, coint_p_value, conclusion
```
#### Result
>(0.21767844943807863, 0.43847298625304515, 'Không có Cointegration')

![output (3)](https://github.com/user-attachments/assets/e8cf6778-1a70-49b6-badb-99d84aa0e8d5)
![output (4)](https://github.com/user-attachments/assets/0203841b-ef6f-419b-87cf-709524e6c1f7)

### Kết quả kiểm tra Cointegration giữa EUR/USD và GBP/USD
#### 1. Biểu đồ:
- **Biểu đồ 1 (giá đóng cửa)**: Hiển thị diễn biến giá đóng cửa của `EUR/USD` <span style="color:blue">(xanh dương)</span> và `GBP/USD` <span style="color:orange">(cam).</span>
- **Biểu đồ 2 (spread)**: Hiển thị chuỗi `spread` giữa `EUR/USD` và `GBP/USD`. Đường màu đỏ là mức trung bình của `spread`.

#### 2. Kết quả kiểm tra:
- **ADF Test cho chuỗi spread**:
  - **P-value**: 0.2177 (lớn hơn 0.05) → Không bác bỏ giả thuyết $H_0$ → Chuỗi `spread` không có tính dừng.
  
- **Kiểm định Engle-Granger Cointegration**:
  - **P-value**: 0.4385 (lớn hơn 0.05) → Không có bằng chứng cho thấy có mối quan hệ đồng tích hợp giữa hai chuỗi.

#### 3. Kết luận:
Với dữ liệu giả lập này, **không có Cointegration** giữa `EUR/USD` và `GBP/USD`, cho thấy rằng không tồn tại mối liên hệ dài hạn ổn định giữa hai chuỗi dữ liệu. Vì vậy, chiến lược *pairs trading* có thể không hiệu quả trong trường hợp này.

# Correlation (tương quan) và Cointegration (đồng tích hợp)
Tại thời điểm này, các khái niệm về tương quan *(correlation)* và đồng tích hợp *(cointegration)* đã được giới thiệu, nhưng sự khác biệt giữa chúng có thể gây nhầm lẫn. Cả hai khái niệm đều nhằm mục đích đo lường mức độ giống nhau trong chuyển động của hai chuỗi thời gian, vì chúng có vẻ giống nhau về mặt bề ngoài. Tuy nhiên, về định nghĩa, chúng hoàn toàn khác nhau.

Thực tế, hệ số tương quan *(correlation)* của các sai phân *(differences)* trong hai chuỗi thời gian đồng tích hợp *(cointegrated time serires)* được mô hình hóa theo phương trình [15.1] có thể được biểu diễn như sau:

$$\rho = \frac{1}{\sqrt{1 + 2\sigma_{1}^2 / \sigma^2} \cdot \sqrt{1 + 2\sigma_{2}^2 / \sigma^2}}$$

- Biểu thức này cho thấy hệ số tương quan *(correlation)* có thể giảm xuống rất thấp nếu phương sai *(variance)* của các thành phần phần dư *(residual)* *(- variances of the residual terms)* $\sigma_{1}^2, \sigma_{2}^2$ được chọn thích hợp so với $\sigma^2$.

- Điều này chứng minh rằng có thể tồn tại hai chuỗi thời gian hoàn toàn đồng tích hợp *(cointegration)*, nhưng có hệ số tương quan *(correlation)* rất thấp, điều này có vẻ đáng ngạc nhiên.

### Ví dụ 15.1 (Hai chuỗi thời gian đồng tích hợp *(cointegration)* nhưng có tương quan *(correlation)* thấp):

Mô hình xu hướng chung [15.1] được sử dụng với:
>- $\gamma = 1$, độ lệch chuẩn *std* $\sigma = 0.1$, và $\sigma_1 = \sigma_2 = 0.2$.

#### Kết quả:
- Tương quan *(correlation)* lý thuyết: $\rho = 0.111$.
- Tương quan *(correlation)* thực nghiệm (200 quan sát): $\rho = 0.034$.
- Tương quan *(correlation)* thực nghiệm (2,000 quan sát): $\rho = -0.108$.

Biểu đồ bên trái cho thấy hai chuỗi không dừng $y_{1t}$ và $y_{2t}$, chuỗi *spread* $z_t$ có tính dừng. Biểu đồ bên phải cho thấy độ phân tán của các sai phân *(differences)* $\Delta y_{1t}$ và $\Delta y_{2t}$ không có sự liên kết rõ ràng → Thể hiện tương quan *(correlation)* thấp.

Figure 15.4: Example of cointegrated time series with low correlation.
![image](https://github.com/user-attachments/assets/c541853c-5179-4303-817c-78c35a17beac)

### Giải nghĩa:
#### 1. Tương quan *(correlation)* và đồng tích hợp *(cointegration)* khác nhau ở đâu?
- **Tương quan *(correlation)***: Đo lường mức độ giống nhau giữa biến động tức thời (*log-return* hoặc *differences*) của hai chuỗi thời gian.
- **Đồng tích hợp *(cointegration)***: Đo lường mối quan hệ dài hạn giữa hai chuỗi thời gian.

Dù hai chuỗi có thể đồng tích hợp *(cointegration)* mạnh (có xu hướng hội tụ về một trạng thái cân bằng dài hạn), nhưng tương quan *(correlation)* tức thời giữa các thay đổi ngắn hạn của chúng có thể rất thấp hoặc thậm chí không liên quan.

#### 2. Ví dụ thực tế:
- Hai tài sản có thể di chuyển theo cùng xu hướng dài hạn nhưng biến động ngắn hạn có thể hoàn toàn khác nhau.
- Trong mô hình minh họa, dù chuỗi $y_{1t}$ và $y_{2t}$ đồng tích hợp *(cointegration)* và có chuỗi *spread* $z_t$ ổn định, hệ số tương quan *(correlation)* giữa các sai phân của chúng vẫn rất thấp hoặc gần 0.

### Kết luận:
Tương quan *(correlation)* và đồng tích hợp *(cointegration)* đo lường hai khía cạnh khác nhau của chuỗi thời gian. Trong khi tương quan *(correlation)* tập trung vào các thay đổi ngắn hạn, đồng tích hợp *(cointegration)* tập trung vào mối quan hệ dài hạn. Một cặp chuỗi thời gian có thể đồng tích hợp *(cointegration)* nhưng không có tương quan *(correlation)* mạnh giữa các biến động ngắn hạn.

---

### Ví dụ 15.2 (Hai chuỗi thời gian không đồng tích hợp *(cointegration)* nhưng có tương quan *(correlation)* cao):
Xét mô hình xu hướng chung trong phương trình [15.1] với:

$\gamma = 1$, độ lệch chuẩn *std* $\sigma = 0.3$, và $\sigma_1 = \sigma_2 = 0.05$.

Ngoài ra, thêm một xu hướng tuyến tính - *linear trend* là $0.01\times t$ vào chuỗi thời gian đầu tiên $y_{1t}$, điều này phá hủy tính đồng tích hợp *(cointegration)* giữa hai chuỗi nhưng không ảnh hưởng đến hệ số tương quan *(correlation)*.

#### Kết quả:
- Hệ số tương quan *(correlation)* lý thuyết: $\rho = 0.947$.
- Tương quan *(correlation)* thực nghiệm với 200 quan sát: $\rho = 0.952$.
- Tương quan *(correlation)* thực nghiệm với 2,000 quan sát: $\rho = 0.941$.

#### Biểu đồ minh họa:
- Biểu đồ bên trái hiển thị hai chuỗi thời gian không dừng $y_{1t}$ và $y_{2t}$ với chuỗi *spread* $z_t$ cũng không dừng tương đương.
- Biểu đồ phần tán bên phải của sai phân $\Delta y_{1t}$ và $\Delta y_{2t}$ cho thấy sự liên kết mạnh mẽ theo một hướng cụ thể, đúng như kỳ vọng với hệ số tương quan *(correlation)* cao.

Figure 15.5: Example of non-cointegrated time series with high correlation.
![image](https://github.com/user-attachments/assets/6c90ecac-fb2e-45d8-ad73-65f787022558)

### Giải nghĩa:
#### 1. Không đồng tích hợp *(cointegration)* nhưng có tương quan *(correlation)* cao:
- Mặc dù hai chuỗi có hệ số tương quan *(correlation)* cao (đồng biến), nhưng chuỗi *spread* giữa chúng lại không ổn định và không hồi quy về trung bình → Không có đồng tích hợp *(cointegration)*.
- Điều này cho thấy rằng **tương quan *(correlation)* cao không đồng nghĩa** với việc có mối quan hệ dài hạn ổn định (*cointegration*).

#### 2. Hiệu ứng xu hướng tuyến tính:
- Việc thêm xu hướng tuyến tính $0.01 \times t$ vào chuỗi $y_{1t}$ khiến chuỗi này phân kỳ dần so với $y_{2t}$, phá hủy trạng thái cân bằng dài hạn.
- Tuy nhiên, hệ số tương quan *(correlation)* giữa các biến động ngắn hạn (sai phân) vẫn rất cao, dẫn đến đồ thị phân tán hiển thị một đường nghiêng rõ ràng.

### Kết luận:
Ví dụ này minh họa rằng mặc dù hai chuỗi thời gian có thể có tương quan *(correlation)* cao trong biến động ngắn hạn, nhưng chúng có thể không có mối quan hệ đồng tích hợp *(cointegration)* trong dài hạn. Sự xuất hiện của xu hướng ngầm trong dữ liệu có thể làm phá hủy tính đồng tích hợp *(cointegration)* mà không ảnh hưởng đến hệ số tương quan *(correlation)*.

---

Cả tương quan *(correlation)* và đồng tích hợp *(cointegration)* đều cố gắng đo lường khái niệm về sự đồng biến động (*co-movement*) của chuỗi thời gian, nhưng chúng thực hiện theo những cách rất khác nhau:
- **Correlation** cao khi hai chuỗi thời gian biến động đồng thời theo cùng một hướng và sẽ gần bằng 0 khi chúng biến động độc lập.
- **Cointegration** cao khi hai chuỗi thời gian di chuyển cùng nhau và giữ khoảng cách ổn định trong dài hạn, và sẽ không tồn tại nếu chúng không giữ được mối liên hệ này.

### Sự khác biệt giữa ngắn hạn và dài hạn:
Một cách để hiểu sự khác biệt đó là xem xét khía cạnh ngắn hạn và dài hạn:
- **Correlation** tập trung vào biến động ngắn hạn — tức là sự thay đổi hướng từ khoảng thời gian này sang khoảng thời gian tiếp theo, bỏ qua các xu hướng dài hạn.
- **Cointegration** lại tập trung vào mối quan hệ dài hạn, tức là kiểm tra xem hai chuỗi thời gian có phục hồi như nhau sau nhiều thời kỳ hay không, mà không quan tâm đến các biến động nhỏ trong ngắn hạn.

Có thể diễn giải chính xác hơn về sự khác biệt giữa ngắn hạn và dài hạn như sau.
- Định nghĩa sự sai khác của chuỗi thời gian $y_t$ trong khoảng $k$ thời kỳ là: 

$$r_t(k) = y_t - y_{t-k}$$

Mục tiêu là đo lường mức độ giống nhau của hai chuỗi thời gian $y_{1t}$ và $y_{2t}$ trong khoảng $t = 0, \ldots, T$.

#### 1. Tương quan (*correlation*):
- Được tính toán thông qua sự khác biệt ở    1 thời kỳ:

$$r_{1t}(1) = \Delta y_{1t}, \quad r_{2t}(1) = \Delta y_{2t} \quad \text{với} \quad t = 1, \ldots, T$$

Điều này đo lường sự biến động ngắn hạn giữa hai chuỗi.

#### 2. Đồng tích hợp (*cointegration*):
- Được tính toán thông qua sự khác biệt giữa hai chuỗi thời gian $y_{1t} - y_{2t}$ (giả sử $\gamma = 1$ để đơn giản). Tương đương, mỗi chuỗi thời gian có thể được dịch chuyển với giá trị ban đầu của nó và sau đó được so sánh về độ phân kỳ. Điều thú vị là, các chuỗi thời gian đã dịch chuyển này chính là sự khác biệt tại thời điểm $t$: $r_{1t}(t) = y_{1t} - y_{10}$ và $r_{2t}(t) = y_{2t} - y_{20}$ trong khoảng $t = 1, \dots, T$.

Điều này kiểm tra xem liệu sự chênh lệch giữa chúng có ổn định trong dài hạn hay không.

### Kết luận:
>Trong chiến lược *pairs trading*, <span style="color:red">điều quan trọng là *cointegration* chứ không phải *correlation*</span>, vì trọng tâm là tính hồi quy về trung bình dài hạn chứ không phải sự đồng biến ngắn hạn.

### Chú ý: 
>Từ chương 5 trở đi từ "đồng tích hợp" sẽ không được dịch và chỉ viết là *cointegration*, từ "tương quan" sẽ không được dịch và chỉ viết là *correlation*

***Bản quyền dịch thuật và diễn giải thuộc về justinnguyen92&copy; - [telegram](https://t.me/justinnguyen92)***

# Pairs Trading
Giao dịch một tài sản có tính hồi quy về trung bình *(mean reversion)* khá đơn giản: mua khi giá trị của nó thấp hơn giá trị trung bình và đóng vị thế khi nó quay về mức trung bình để kiếm lợi nhuận; tương tự, bán khống khi giá vượt quá giá trị trung bình và đóng vị thế khi nó giảm trở lại mức trung bình. Tuy nhiên, việc tìm một tài sản hồi quy về trung bình trên thị trường tài chính là điều hiếm khi xảy ra. Nếu có tài sản như vậy, nhiều nhà đầu tư sẽ nhanh chóng phát hiện và giao dịch nó, điều này sẽ khiến khả năng sinh lợi biến mất.

Trong thực tế, có thể tìm một cặp tài sản *cointegration* và tạo ra một tài sản hồi quy về trung bình giả định *(spread)*. Với tính chất hồi quy về trung bình của *spread* được tạo ra, xu hướng chung của thị trường có trong hai tài sản gốc sẽ không tồn tại trong *spread* này, điều này có nghĩa là *spread* không theo xu hướng thị trường và có tính trung lập thị trường *(market neutral)*.

### *Pairs Trading*
*Pairs Trading* là một chiến lược trung lập thị trường *(market-neutral)* mà mục tiêu là giao dịch *spread* hồi quy về trung bình *(mean-reverting spread)*. Điều này có nghĩa là xác định hai công cụ tài chính *cointegration*, chẳng hạn như cổ phiếu, và thực hiện vị thế mua hoặc bán khống khi giá của chúng phân kỳ khỏi mối quan hệ lịch sử, với hy vọng rằng giá sẽ hội tụ trở lại mức cân bằng lịch sử, cho phép nhà giao dịch kiếm lợi nhuận từ sự hội tụ đó.

> :memo: **Note:** Một số cuốn sách chuyên khảo về *pairs trading* bao gồm Vidyamurthy (2004), Ehrman (2006), và Chan (2013); cũng như Feng và Palomar (2016).

*Pairs Trading* được phát triển vào giữa những năm 1980 bởi nhóm giao dịch định lượng dẫn đầu bởi Nunzio Tartaglia tại Morgan Stanley và đạt được thành công lớn. Tuy nhiên, nhóm đã giải thể vào năm 1989 và thành viên gia nhập các công ty giao dịch khác nhau. Kết quả là tính bảo mật ban đầu của chiến lược *pairs trading* bị mất đi và kỹ thuật này lan rộng trong cộng đồng định lượng.

### Phân loại các chiến lược giao dịch theo triết lý cơ bản như sau:
#### 1. Chiến lược dựa trên đà (*Momentum-based strategies* hoặc *Directional trading*):
- Mục tiêu là nắm bắt xu hướng của thị trường trong khi coi sự biến động không mong muốn như một dạng rủi ro.

#### 2. Pairs Trading (*Statistical-arbitrage*):
- Đây là các chiến lược trung lập thị trường và cố gắng giao dịch các biến động hồi quy về trung bình của chênh lệch giá tương đối giữa hai tài sản.

Hình 15.6 hiển thị sự phân chia giá của một tài sản thành thành phần xu hướng - *trend component* (được nắm bắt bởi các chiến lược dựa trên động lượng *momentum-based*) và thành phần quay trở lại giá trung bình - *mean-reverting component* (được nắm bắt bởi giao dịch theo *pairs trading*).

Figure 15.6: Decomposition of asset price into trend component and mean-reverting component.
![image](https://github.com/user-attachments/assets/bb03b9e4-2e26-4b32-851a-4b19f4e3dc15)

# Spread
Cách triển khai đơn giản nhất của *pairs trading* dựa vào việc so sánh *spread* giữa hai chuỗi thời gian $y_{1t}$ và $y_{2t}$ với một ngưỡng. Giá trị *spread* được định nghĩa là:

$$z_t = y_{1t} - \gamma y_{2t}$$

Chuỗi $z_t$ có tính hồi quy về trung bình với trung bình là $\mu$.

### Ý tưởng giao dịch như sau:
- **Mua (LONG)** khi *spread* thấp, $z_t < \mu - s_0$.
- **Bán khống (SHORT-SELL)** khi *spread* cao, $z_t > \mu + s_0$.

- Sau đó đóng vị thế khi *spread* quay trở lại mức trung bình $\mu$, khi nó trở lại mức trung bình sau $k$ chu kỳ, dẫn đến sự khác biệt ít nhất là: $|z_t - \mu| \geq s_0$

Hình 15.7 minh họa quá trình thực hiện chiến lược *pairs trading* bằng cách mua và bán khống *spread* dựa trên các ngưỡng $s_0 = 1.5$.

![image](https://github.com/user-attachments/assets/22354aa0-58dc-43e9-a1aa-3696546d26dd)

### Giải thích chi tiết:
#### 1. *Spread* trong *Pairs Trading*:
- *Spread* ($z_t$) là sự chênh lệch giữa giá trị của hai tài sản có liên kết *cointegration*.
- Nếu *spread* dao động quanh một mức trung bình $\mu$, ta có thể kỳ vọng rằng *spread* sẽ quay về mức trung bình này khi nó vượt quá hoặc giảm xuống một ngưỡng nhất định.

#### 2. Ngưỡng $s_0$ trong giao dịch:
$s_0$ là một ngưỡng được thiết lập để xác định các điểm **quá mua** ***(OVER-BOUGHT)*** hoặc **quá bán** ***(OVER-SOLD)***:
  - Khi ($z_t$) vượt quá $\mu + s_0$ → Dự đoán rằng *spread* sẽ giảm xuống → **Bán khống** ***(SHORT-SELL)***.
  - Khi ($z_t$ ) giảm dưới $\mu - s_0$ → Dự đoán rằng *spread* sẽ tăng trở lại → **Mua** ***(BUY)***. 

#### 3. Minh họa trong biểu đồ:
Trong biểu đồ:
  - **Buy**: Điểm mà *spread* giảm dưới ngưỡng $\mu - s_0$ .
  - **Sell to unwind**: Đóng vị thế khi *spread* quay trở về gần mức trung bình.
  - **Short-sell**: Điểm mà *spread* tăng vượt quá $\mu + s_0$.
  - **Buy to unwind**: Đóng vị thế bán khống khi *spread* giảm trở lại mức trung bình.
    
#### 4. Ý nghĩa thực tế của chiến lược:
Chiến lược này dựa trên giả định rằng sự chênh lệch giữa hai tài sản sẽ quay về mức cân bằng sau khi phân kỳ. Nếu *spread* tiếp tục phân kỳ mà không quay về mức trung bình, chiến lược sẽ gặp rủi ro lớn. Do đó, cần kiểm tra *cointegration* giữa hai chuỗi trước khi áp dụng chiến lược này.

### Kết luận:
*Pairs trading* sử dụng *spread* để tìm kiếm cơ hội mua hoặc bán khống dựa trên mức phân kỳ so với trung bình. Ngưỡng $s_0$ giúp xác định các điểm vào và thoát vị thế một cách có kiểm soát nhằm tối ưu hóa lợi nhuận từ sự hồi quy về trung bình của *spread*.

---

## 1. Tổng quan:
*Pairs trading* có thể được triển khai dựa trên giá gốc *(prices)* hoặc giá log *(log-prices)*. Việc lựa chọn phụ thuộc vào việc chuỗi dữ liệu *cointegration* được thể hiện trên chuỗi *time series* liên quan đến giá - *price* hoặc *log-prices*. Cách diễn giải trong hai trường hợp này có đôi chút khác biệt.

## 2. Trường hợp sử dụng giá (*prices*):
Giả sử $y_{1t}$ và $y_{2t}$ đại diện cho giá của hai tài sản. *Spread* được tính như sau: $z_t = y_{1t} - \gamma y_{2t}$

- 1 và $\gamma$ là hệ số thể hiện **số lượng cổ phiếu** mua và bán khống.

- **Ý nghĩa**: *Spread* thể hiện sự chênh lệch giá trong một khoảng thời gian $k$ (bỏ qua chi phí giao dịch): 

$$z_{t+k} - z_t = s_0$$

- Đây là phần lợi nhuận từ sự thay đổi về giá.

## 3. Trường hợp sử dụng *log-prices*:
Giả sử $y_{1t}$ và $y_{2t}$ đại diện cho *log-prices* của hai tài sản. Lúc này, thuận tiện hơn nếu dùng ký hiệu danh mục đầu tư *portfolio notation* (xem Chương 6):

$$\mathbf{w} = \begin{bmatrix} 1 \\ -\gamma \end{bmatrix}$$

trong đó bây giờ các hệ số $1$ và $-\gamma$ biểu thị các giá trị dollar được chuẩn hóa - *normalized dollar values* thay vì cổ phiếu, công thức *spread* có thể được viết một cách ngắn gọn như sau:

$$z_t = \mathbf{w}^T \mathbf{y}_t$$

với $
\mathbf{y}_t = 
\begin{bmatrix} 
y_{1t} \\ 
y_{2t} 
\end{bmatrix}
$

**Ý nghĩa**: *Spread* lúc này gần tương đương với lợi nhuận trong khoảng thời gian $k$ (bỏ qua chi phí giao dịch): 

$$\mathbf{w}^T (\mathbf{y}_{t+k} - \mathbf{y}_t) = z_{t+k} - z_t = s_0$$

Lưu ý rằng đây là một phép tính gần đúng vì lợi nhuận của danh mục đầu tư phải được tính toán bằng cách sử dụng lợi nhuận tuyến tính *(linear returns)*, $\mathbf{w} \left( \exp(\mathbf{y}_{t+k} - \mathbf{y}_t) - 1 \right)$ thay vì *log-returns*. Tuy nhiên, với $x$ nhỏ, ta có thể xấp xỉ $\exp(x) - 1 \approx x$ (xem Chương 6), nên *log-returs* xấp xỉ với *linear returns*.

Ngoài ra, lưu ý rằng danh mục đầu tư này có đòn bẩy $1+\gamma$, do đó trên thực tế, chúng ta có thể muốn chuẩn hóa nó thành đòn bẩy đơn vị - *unit leverage*.

## 4. Tóm tắt:
Tóm lại, tùy thuộc vào việc chuỗi thời gian *cointegration* ban đầu tương ứng với giá - *prices* hoặc *log-price*, ngưỡng $s_0$ sẽ xác định lợi nhuận tuyệt đối - *absolute profit* hoặc tỷ suất lợi nhuận của giao dịch trong khoảng $k$ thời kỳ. Lựa chọn này được quyết định bởi bản chất của *cointegration* trong chuỗi thời gian. 

Điều quan trọng cần lưu ý là, trong trường hợp *log-price* *cointegration*, danh mục đầu tư $w$ mang ý nghĩa của giá trị *dollars* được chuẩn hóa, điều này có thể yêu cầu <span style="color:red">cân bằng lại - *rebalancing* qua thời gian (tăng chi phí giao dịch)</span>; 

Đối với prices *cointegration*, số lượng cổ phiếu tự nhiên duy trì không đổi theo thời gian và không cần phải cân bằng lại. Điều này làm cho chuỗi giá *cointegration* trở nên hấp dẫn hơn; tuy nhiên, trong thực tế, việc tìm chuỗi giá *cointegration* khó khăn hơn vì nhiễu trong giá ít đối xứng hơn so với *log-price*, khiến các *spread* tiềm năng ít có tính dừng hơn.

---

#### Ví dụ code: 
Tính `spread_1` theo các sử dụng giá, `spread_2` theo cách sử dụng `log-prices` với công thức tính đầy đủ $w(exp(y t+k −y t)−1)$, kiểm tra *stationary* của `spread_1` và `spread_2`

```python
# ============================================================================================================================================
# TÍNH SPREAD THEO PRICE VÀ LOG_PRICE
# cho tôi đoạn code tính spread_1 theo các sử dụng giá, spread_2 theo cách sử dụng log-prices với công thức tính đầy đủ w(exp(y t+k −y t)−1), 
# kiểm tra stationary của spread_1 và spread_2
# ============================================================================================================================================
# Reimport necessary libraries after the environment reset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Tạo chuỗi thời gian giả lập giá đóng cửa của hai tài sản (giá thực tế)
np.random.seed(42)
T = 200  # Số lượng điểm dữ liệu
initial_price_1 = 100  # Giá ban đầu tài sản 1
initial_price_2 = 150  # Giá ban đầu tài sản 2

returns_1 = np.random.normal(0, 0.01, T)  # Lợi nhuận ngẫu nhiên tài sản 1
returns_2 = np.random.normal(0, 0.01, T)  # Lợi nhuận ngẫu nhiên tài sản 2

prices_1 = initial_price_1 * np.exp(np.cumsum(returns_1))  # Chuỗi giá tài sản 1
prices_2 = initial_price_2 * np.exp(np.cumsum(returns_2))  # Chuỗi giá tài sản 2

# Tính log-prices
log_prices_1 = np.log(prices_1)
log_prices_2 = np.log(prices_2)

# Tạo DataFrame chứa dữ liệu
df = pd.DataFrame({
    'Prices_1': prices_1,
    'Prices_2': prices_2,
    'Log_Prices_1': log_prices_1,
    'Log_Prices_2': log_prices_2
})

# Hệ số gamma (tìm qua hồi quy tuyến tính đơn giản)
gamma = np.polyfit(df['Prices_2'], df['Prices_1'], 1)[0]

# Tính Spread_1 (dùng giá)
df['Spread_1'] = df['Prices_1'] - gamma * df['Prices_2']

# Tính Spread_2 (dùng log-prices với công thức đầy đủ)
df['Spread_2'] = log_prices_1 - gamma * log_prices_2  # log-return xấp xỉ
df['Spread_2_full'] = (1 + gamma) * (np.exp(df['Log_Prices_1'] - df['Log_Prices_2']) - 1)  # công thức đầy đủ

# Kiểm tra tính dừng (ADF Test) cho Spread_1 và Spread_2
adf_result_spread_1 = adfuller(df['Spread_1'].dropna())
adf_result_spread_2 = adfuller(df['Spread_2_full'].dropna())

# Lấy p-value để kiểm tra tính dừng
p_value_spread_1 = adf_result_spread_1[1]
p_value_spread_2 = adf_result_spread_2[1]

# Vẽ biểu đồ Spread_1 và Spread_2
plt.figure(figsize=(12, 5))
plt.subplot(2, 1, 1)
plt.plot(df.index, df['Spread_1'], label='Spread_1 (Price)', color='blue')
plt.axhline(df['Spread_1'].mean(), color='red', linestyle='--', label='Mean (Spread_1)')
plt.title('Spread_1 (Price-based)')
plt.xlabel('Time')
plt.ylabel('Spread')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(df.index, df['Spread_2_full'], label='Spread_2 (Log-Prices)', color='orange')
plt.axhline(df['Spread_2_full'].mean(), color='red', linestyle='--', label='Mean (Spread_2)')
plt.title('Spread_2 (Log-Price-based)')
plt.xlabel('Time')
plt.ylabel('Spread')
plt.legend()

plt.tight_layout()
plt.show()

# Trả về p-value để kiểm tra tính dừng
p_value_spread_1, p_value_spread_2
```
#### Result
>(0.22339005729108286, 0.09315577123485508)

![output (6)](https://github.com/user-attachments/assets/d7aa1f2b-4d28-41f4-83fa-cb9ec07c5978)

### Kết quả kiểm tra tính dừng của `Spread_1` và `Spread_2`
#### Biểu đồ:
- **Biểu đồ 1 (*Spread_1 - Price-based*)**: Biểu diễn `spread` tính từ giá gốc của hai tài sản.
- **Biểu đồ 2 (*Spread_2 - Log-Price-based*)**: Biểu diễn `spread` tính từ `log-prices` của hai tài sản theo công thức đầy đủ $\mathbf{w} \left( \exp(\mathbf{y}_{t+k} - \mathbf{y}_t) - 1 \right)$.

#### Kết quả kiểm định ADF Test:
- **P-value của *Spread_1***: 0.223 (lớn hơn 0.05) → Không bác bỏ giả thuyết $H_0$ → `spread` không có tính dừng.
- **P-value của *Spread_2***: 0.093 (lớn hơn 0.05) → Không có bằng chứng rõ ràng cho tính dừng của `spread`.

#### Giải thích:
- **Spread_1 (giá thực tế)**: `spread` từ giá gốc có xu hướng phân kỳ thay vì hội tụ quanh mức trung bình.
- **Spread_2 (log-prices)**: `spread` từ `log-prices` có xu hướng dao động quanh mức trung bình hơn, nhưng vẫn không đủ bằng chứng để kết luận tính dừng.

### Kết luận:
- Trong dữ liệu giả lập này, cả hai chuỗi `spread` chưa thể hiện tính dừng rõ ràng. Điều này cho thấy rằng sự kết hợp giữa hai chuỗi giá có thể không có tính chất *cointegration* hoặc cần tinh chỉnh thêm các tham số như $\gamma$ hoặc cách lựa chọn dữ liệu.

---

# 1. Pairs Trading có lợi nhuận không?
*Pairs trading* dựa trên giả định rằng mối quan hệ lịch sử giữa hai công cụ tài chính sẽ được duy trì trong tương lai. Tuy nhiên, điều này không phải lúc nào cũng đúng vì mối quan hệ *cointegration* có thể thay đổi theo thời gian do nhiều yếu tố như:

- Điều kiện thị trường.
- Xu hướng ngành.
- Sự kiện cụ thể liên quan đến công ty.

Do đó, *pairs trading* tiềm ẩn rủi ro và yêu cầu nhà giao dịch phải giám sát chặt chẽ mối quan hệ giữa các công cụ, cũng như sử dụng các kỹ thuật quản lý rủi ro để bảo vệ vị thế giao dịch của mình.

Một số nghiên cứu cho thấy *pairs trading* có thể tạo ra lợi nhuận *(Avellaneda & Lee, 2010; Elliott et al., 2005; Gatev et al., 2006)*, trong khi những nghiên cứu khác cho rằng mối quan hệ cointegration không được duy trì ổn định theo thời gian *(Chan, 2013; Clegg, 2014)*.

### Những cảnh báo khi sử dụng *Pairs Trading*:
**1. Chi phí giao dịch:**
  - Phí giao dịch có thể lớn hơn cả lợi nhuận kiếm được từ *spread*. *(Chan, 2008)*

**2. Hiệu quả giảm dần:**
  - Một chiến lược từng hiệu quả trong quá khứ có thể không còn hiệu quả trong thời gian gần đây.*(Chan, 2013)*

**3. Khó khăn kỹ thuật:**
  - Thanh khoản thấp khi bán khống.
  - Nguy cơ *margin call* (bị yêu cầu bổ sung ký quỹ khi giá biến động bất lợi).
  - Cạnh tranh giữa các nhà giao dịch tần suất cao. *(Chan, 2013)*

### Giải pháp:
- Sử dụng lọc Kalman *(Kalman Filter)* để ước tính một mối quan hệ *cointegration* thay đổi theo thời gian. (Mục 15.6)
- Sử dụng mô hình **VECM** *(Vector Error Correction Model)* để khắc phục các hạn chế về *cointegration*. (Mục 15.7)

# 2. Thiết kế Pairs Trading
Phần này giới thiệu chi tiết về thiết kế chiến lược *pairs trading*. Mục tiêu của chiến lược là giao dịch một *spread* hồi quy về trung bình có lợi nhuận, bao gồm các bước chính như:
1. Xác định cặp tài sản có quan hệ *cointegration*:
    - Từ các bước sàng lọc cơ bản đến các kiểm tra thống kê phức tạp.
2. Thiết kế chiến lược giao dịch:
    - Dựa trên việc lựa chọn ngưỡng $𝑠_0$ hoặc sử dụng các phương pháp phức tạp hơn.

**Các phương pháp nâng cao:**
- Lọc *Kalman*: Dùng để ước tính một mối quan hệ *cointegration* thay đổi theo thời gian.
- Mở rộng *pairs trading*: Áp dụng chiến lược này cho hơn hai tài sản.

---

Chìa khóa trong *pairs trading* nằm ở khả năng khám phá ra các cặp *cointegration*. Các phương pháp khả dụng bao gồm từ phương pháp tìm kiếm đơn giản đến mô hình đa biến phức tạp *(Krauss, 2017)*.

# Pre-screening (Sàng lọc sơ bộ)
Sàng lọc sơ bộ (*pre-screening*) là một quá trình đơn giản và tiết kiệm chi phí, trong đó nhiều cặp tài sản có thể được loại bỏ một cách nhanh chóng, chỉ giữ lại một số cặp tiềm năng để phân tích sâu hơn.
- Một thước đo phổ biến để đánh giá *cointegration* là khoảng cách giá chuẩn hóa ***(Normalized Price Distance - NPD)*** *(Gatev et al., 2006)*.

### Công thức NPD:

```math
\text{NPD} \triangleq \sum_{t=1}^{T} \left( \bar{p}_{1t} - \bar{p}_{2t} \right)^2,
```

**Trong đó:**
- $\tilde{p}_ {1t}$ và $\tilde{p}_{2t}$ là giá chuẩn hóa - *normalized prices*:

$$\tilde{p}_{1t} = \frac{p_{1t}}{p_{10}}, \quad \tilde{p}_{2t} = \frac{p_{2t}}{p_{20}}$$

- $p_{1t}, p_{2t}$ là giá gốc của hai tài sản - *original prices*.

**Ý nghĩa:**
- NPD đo lường sự khác biệt giữa các giá chuẩn hóa theo thời gian. Nếu NPD nhỏ, nghĩa là sự khác biệt giữa các giá chuẩn hóa ổn định trong dài hạn → cặp tài sản có tiềm năng *cointegration*.


Một thước đo tương tự cũng có thể được định nghĩa theo *log-prices* $y_{1t}$ và $y_{2t}$ bằng cách trừ đi giá trị tại thời điểm ban đầu:

$$\tilde{y}_{1t} = y_{1t} - y_{10}$$

$$\quad \tilde{y}_{2t} = y_{2t} - y_{20}$$

- Lưu ý rằng *shifted log-price* này tương ứng với chuỗi chênh lệch dài hạn - *long-term difference series*, tức là *log-return* trong các khoảng thời gian dài được mô tả trước đó và được biểu thị bằng $\tilde{y}_ {1t}$ và $\tilde{y}_{2t}$

### 4. Ý nghĩa thực tế:
- *Pre-screening* giúp nhanh chóng loại bỏ những cặp tài sản không có tiềm năng *cointegration* để tập trung phân tích kỹ hơn vào các cặp có giá trị NPD nhỏ.
- Điều này làm giảm thời gian và chi phí tính toán khi thực hiện chiến lược *pairs trading* trên nhiều cặp tài sản.

### Tóm tắt:
- *Prescreening* là bước đầu tiên trong quy trình tìm kiếm cặp tài sản *cointegration* tiềm năng.
- NPD đo lường sự khác biệt giữa các giá chuẩn hóa theo thời gian. Nếu NPD thấp, hai chuỗi thời gian có thể có mối quan hệ *cointegration* mạnh.
- Phương pháp này cũng có thể áp dụng cho *log-prices* để đo lường các biến động dài hạn của chuỗi thời gian.

#### Ví dụ code:
Ví dụ phương pháp `NPD` và `log-prices` với 1 list các pair ví dụ: `pairs = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", "NZDUSD"]` (sử dụng giá `close` cho mỗi *pair*)

```python
# Reimport necessary libraries after the environment reset
import pandas as pd
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt

# Tạo chuỗi dữ liệu giả lập cho các cặp tiền tệ
np.random.seed(42)
T = 200  # Số lượng điểm dữ liệu
pairs = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", "NZDUSD"]
prices_data = {}

# Giả lập dữ liệu giá đóng cửa cho mỗi cặp tiền tệ
for pair in pairs:
    initial_price = np.random.uniform(1.0, 2.0)  # Giá ban đầu ngẫu nhiên
    returns = np.random.normal(0, 0.01, T)  # Lợi nhuận ngẫu nhiên
    prices_data[pair] = initial_price * np.exp(np.cumsum(returns))  # Giá đóng cửa giả lập

# Tạo DataFrame chứa giá đóng cửa của tất cả các cặp tiền tệ
df_prices = pd.DataFrame(prices_data, index=pd.date_range(start='2022-01-01', periods=T))

# Tính toán khoảng cách giá chuẩn hóa (NPD) cho từng cặp
npd_results = {}
for pair1, pair2 in combinations(pairs, 2):
    # Giá chuẩn hóa
    norm_prices_1 = df_prices[pair1] / df_prices[pair1].iloc[0]
    norm_prices_2 = df_prices[pair2] / df_prices[pair2].iloc[0]
    # Tính NPD
    npd = np.sum((norm_prices_1 - norm_prices_2) ** 2)
    npd_results[(pair1, pair2)] = npd

# Tính toán log-prices
log_prices = np.log(df_prices)

# Tính toán khoảng cách log-prices cho từng cặp
log_distance_results = {}
for pair1, pair2 in combinations(pairs, 2):
    shifted_log_1 = log_prices[pair1] - log_prices[pair1].iloc[0]
    shifted_log_2 = log_prices[pair2] - log_prices[pair2].iloc[0]
    log_distance = np.sum((shifted_log_1 - shifted_log_2) ** 2)
    log_distance_results[(pair1, pair2)] = log_distance

# Chuyển kết quả thành DataFrame để dễ quan sát
npd_df = pd.DataFrame.from_dict(npd_results, orient='index', columns=['NPD'])
log_distance_df = pd.DataFrame.from_dict(log_distance_results, orient='index', columns=['Log-Price Distance'])

# Sắp xếp theo thứ tự tăng dần
npd_df_sorted = npd_df.sort_values(by='NPD')
log_distance_df_sorted = log_distance_df.sort_values(by='Log-Price Distance')

# Hiển thị kết quả
print(npd_df_sorted,log_distance_df_sorted)
```

### Result
>![image](https://github.com/user-attachments/assets/c2912084-a6ca-4678-8d01-9826c0ecb66f)

Tôi đã tính toán khoảng cách giá chuẩn hóa `NPD` và khoảng cách `log-prices` cho tất cả các cặp tiền tệ trong danh sách. Bạn có thể xem bảng kết quả để tìm ra các cặp có khoảng cách thấp nhất, tiềm năng có *cointegration* mạnh mẽ. Các cặp có giá trị `NPD` và `log-price distance` thấp hơn thường được ưu tiên để phân tích chi tiết hơn trong chiến lược *pairs trading*.

[Sau khi *Pre-screening* chúng ta đến bước tiếp theo là Kiểm định đồng tích hợp - "Cointegration Test"](https://github.com/Nguyenthang2292/quantitative-trading/blob/main/statistical_arbitrage/08.%20Cointegration%20Tests.md)

---

***Bản quyền dịch thuật và diễn giải thuộc về justinnguyen92&copy; - [telegram](https://t.me/justinnguyen92)***

Sau khi hoàn tất quá trình *pre-screening* các cặp tài sản có tiềm năng quan hệ *cointegration*, cần thực hiện một phân tích kỹ lưỡng hơn. Đây là vai trò của các **kiểm định đồng tích hợp (*cointegration tests*)** được phát triển trong lĩnh vực thống kê từ nhiều thập kỷ trước *(Harris, 1995; Tsay, 2010, 2013)*.

## 1. Ý nghĩa của *Cointegration Tests*:
Các kiểm định này nhằm kiểm tra xem liệu có một tổ hợp tuyến tính nào đó của hai chuỗi thời gian tạo thành một mô hình tự hồi quy dừng *(stationary autoregressive model)* hay không.

- Nếu chuỗi *time series* có gốc đơn *unit-root*, chuỗi sẽ hành xử như một *random walk* và không hồi quy về trung bình.

- Nếu chuỗi không có gốc đơn, chuỗi thời gian sẽ có xu hướng quay trở lại mức trung bình dài hạn.

Do đó, các bài kiểm tra *cointegration* thường được triển khai thông qua các bài kiểm tra *unit-root stationarity tests*.

#### Công thức toán học:
Mục tiêu là kiểm tra xem có tồn tại một giá trị $\gamma$ sao cho chuỗi *spread*:

$$z_t = y_{1t} - \gamma y_{2t}$$

là một chuỗi dừng.

- Trong thực tế, mức trung bình của *spread* $\mu$ (giá trị cân bằng - *equilibrium value*) không nhất thiết phải bằng 0 và $\gamma$ không phải lúc nào cũng bằng $1$.
- Nhiều nghiên cứu đặt $\gamma = 1$ để đơn giản hóa trong các chiến lược giao dịch *dollar-neutral* *(Elliott et al., 2005; Gatev et al., 2006; Triantafyllopoulos and Montana, 2011)*; tuy nhiên điều này làm giảm số lượng cặp tài sản có tính chất *cointegration*.

## 2. Phương pháp kiểm định phổ biến: Engle-Granger Test
Một trong những phương pháp đơn giản và phổ biến nhất để kiểm tra *cointegration* là **kiểm định Engle-Granger**(62) *(Engle và Granger, 1987)*. Nó dựa trên hai bước:

- **Bước 1**: Ước lượng giá trị $\gamma$ thông qua Hồi quy tuyến tính bình phương tối thiểu -  *least squares regression* (*OLS*).
- **Bước 2**: Kiểm tra tính dừng của phần dư (*residual*)(63)
Chính xác hơn, hai chuỗi $y_{1t}$ và $y_{2t}$ được hồi quy với nhau (xem Chương 3 để biết chi tiết về hồi quy bình phương nhỏ nhất),

$$y_{1t} - \gamma y_{2t} = \mu + r_t$$

với $r_t$ là phần dư - *residual* sau khi hồi quy được kiểm tra tính dừng của *unit-root* hoặc một số dạng đảo ngược giá trị trung bình - *some form of mean reversion*.

### Giải thích chi tiết:
#### Kiểm định Engle-Granger: 
Kiểm định này dựa trên việc kiểm tra xem phần dư $r_t$ có tính dừng hay không. Nếu phần dư là chuỗi dừng, điều này chứng tỏ rằng hai chuỗi thời gian $y_{1t}$ và $y_{2t}$ có mối quan hệ *cointegration*.

#### Ý nghĩa của $\gamma$:
- Giá trị $\gamma$ là hệ số xác định mối quan hệ giữa hai chuỗi thời gian.
- Nếu $\gamma$ quá khác biệt so với 1 hoặc không cho thấy tính dừng, cặp tài sản có thể không *cointegration*.

Có nhiều cách thức *heuristic* để đo lường sức mạnh của sự trở lại giá trị trung bình của phần dư. Ví dụ, người ta có thể sử dụng tỷ lệ giao cắt trung bình, tức là số lần phần dư giao cắt giá trị trung bình của nó trong một khoảng thời gian *(Vidyamurthy, 2004)*: tỷ lệ giao cắt trung bình càng cao thì sự trở lại giá trị trung bình càng mạnh. Một biện pháp khác là chu kỳ *half-life* của sự trở lại giá trị trung bình (Chan, 2013), định lượng thời gian cần thiết để một chuỗi thời gian quay trở lại trong phạm vi một nửa khoảng cách từ giá trị trung bình sau khi lệch một lượng nhất định so với giá trị trung bình.

---

### Phần dư: $r_t$ - *"residual"*.
- **Giải thích:**
  - *Residual* là phần chênh lệch giữa giá trị thực tế và giá trị dự đoán từ mô hình hồi quy.
  - Trong kiểm định Engle-Granger, $r_t$ đại diện cho chênh lệch giữa chuỗi thời gian $y_{1t}$ và chuỗi $y_{2t}$ đã được hiệu chỉnh bởi hệ số $\gamma$.
  - Mục tiêu là kiểm tra xem chuỗi $r_t$ có đặc tính dừng *(stationary)* không. Nếu $r_t$ là chuỗi dừng, điều đó cho thấy hai chuỗi ban đầu có mối quan hệ *cointegration*.

- **Ví dụ:** Nếu hồi quy $y_{1t} = \gamma y_{2t} + \mu + r_t$ thì:
  - **Giá trị thực tế:** $y_{1t}$
  - **Giá trị dự đoán:** $\gamma y_{2t} + \mu$
  - **Residual $r_t$:** $r_t = y_{1t} - (\gamma y_{2t} + \mu)$

#### Phần dư $r_t$ và Spread $z_t$ có phải là một không?
  - **Phần dư $r_t$ (Residual):** Là sự chênh lệch giữa giá trị thực tế và giá trị ước lượng từ mô hình hồi quy. Trong kiểm định Engle-Granger, phần dư là sự khác biệt giữa chuỗi thời gian thứ nhất và chuỗi thời gian thứ hai đã được điều chỉnh bởi hệ số $\gamma$:

$$r_t = y_{1t} - \gamma y_{2t} - \mu$$

  - **Spread $z_t$:** Là sự chênh lệch giữa hai chuỗi thời gian trong chiến lược *pairs trading*: $z_t = y_{1t} - \gamma y_{2t}$

**SO SÁNH RESIDUAL VÀ SPREAD:**

| **Yếu tố**       | **Residual $r_t$**                                            | **Spread $z_t$**                                         |
|-------------------|-----------------------------------------------------------------|-------------------------------------------------------------|
| **Định nghĩa**    | Chênh lệch giữa giá trị thực tế và giá trị dự đoán từ mô hình hồi quy. | Chênh lệch giữa hai chuỗi giá tài sản $y_{1t}$ và $y_{2t}$ với hệ số $\gamma$. |
| **Vai trò**       | Dùng để kiểm tra tính dừng và xác nhận mối quan hệ *cointegration*. | Dùng trong chiến lược giao dịch *pairs trading* để xác định điểm mua/bán. |
| **Công thức**     | $$r_t = y_{1t} - \gamma y_{2t} - \mu$$                        | $$z_t = y_{1t} - \gamma y_{2t}$$                         |
| **Ý nghĩa**       | Đo lường mức sai lệch trong mô hình hồi quy.                   | Đo lường mức phân kỳ giữa hai chuỗi tài sản.               |

**Kết luận:**
- *Residual* $r_t$ và *Spread* $z_t$ có sự khác biệt nhỏ về khái niệm:
  - *Spread* là chênh lệch thô giữa hai chuỗi tài sản.
  - *Residual* là kết quả điều chỉnh của hai chuỗi, loại bỏ ảnh hưởng của mức trung bình $\mu$.
- Trong một số trường hợp, nếu $\mu = 0$, *residual* và *spread* có thể giống nhau về mặt giá trị. Tuy nhiên, về bản chất, *residual* dùng trong kiểm định tính dừng, còn *spread* dùng trong chiến lược giao dịch.

### Tóm tắt:
- Sau khi sàng lọc sơ bộ các cặp tài sản tiềm năng, cần kiểm tra chính xác bằng các kiểm định *cointegration*.
- Phương pháp *Engle-Granger* là một trong những phương pháp kiểm tra đơn giản và phổ biến nhất, dựa trên việc xác định *residual* từ Hồi quy bình phương tối thiểu *(least squares regression)* giữa hai chuỗi tài sản.
- Nếu *residual* là chuỗi dừng, hai chuỗi có tính chất *cointegration* và có thể được sử dụng trong chiến lược *pairs trading*.

> :memo: **Note:** Hồi quy bình phương tối thiểu *(least squares regression)* là một kỹ thuật cụ thể (và phổ biến nhất) để thực hiện *Linear Regression* (*Linear Regression* là mô hình tổng quát).

#### Ví dụ code:
Kiểm định mẫu Engle-Granger với 2 time-series `EURUSD` và `GBPUSD` (2 cặp lấy giá `close`).

```python
# Reimport libraries after environment reset
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller

# Giả lập dữ liệu giá đóng cửa cho EUR/USD và GBP/USD
np.random.seed(42)
T = 200  # Số lượng điểm dữ liệu
initial_price_eur = 1.1  # Giá ban đầu EUR/USD
initial_price_gbp = 1.3  # Giá ban đầu GBP/USD

# Lợi nhuận ngẫu nhiên và giá giả lập
returns_eur = np.random.normal(0, 0.01, T)
returns_gbp = np.random.normal(0, 0.01, T)

prices_eur = initial_price_eur * np.exp(np.cumsum(returns_eur))
prices_gbp = initial_price_gbp * np.exp(np.cumsum(returns_gbp))

# Tạo DataFrame chứa giá đóng cửa
df = pd.DataFrame({
    'EURUSD_Close': prices_eur,
    'GBPUSD_Close': prices_gbp
})

# 1. Hồi quy OLS để ước lượng gamma
X = sm.add_constant(df['GBPUSD_Close'])  # Thêm hằng số để hồi quy
model = sm.OLS(df['EURUSD_Close'], X).fit()
gamma = model.params['GBPUSD_Close']  # Hệ số gamma

# 2. Tính phần dư (residuals)
df['Spread'] = df['EURUSD_Close'] - gamma * df['GBPUSD_Close']

# 3. Kiểm tra tính dừng của phần dư bằng ADF Test
adf_result = adfuller(df['Spread'].dropna())
p_value = adf_result[1]

# Kết quả kiểm định Engle-Granger
conclusion = "Có đồng tích hợp" if p_value < 0.05 else "Không có đồng tích hợp"

# Hiển thị kết quả
gamma, p_value, conclusion
```

#### Result
>(-0.09752042728106353, 0.22339005729108385, 'Không có đồng tích hợp')

### Kết quả Kiểm định Engle-Granger cho EUR/USD và GBP/USD
- **Hệ số gamma ($\gamma$)**: -0.0975
- **P-value của kiểm định ADF**: 0.2234 (> 0.05)
- **Kết luận**: "Không có *cointegration*" → Phần dư *(residuals)* không phải là chuỗi dừng, cho thấy hai chuỗi giá giả lập EUR/USD và GBP/USD không có mối quan hệ *cointegration* trong dài hạn.

### Giải thích:
Mặc dù hồi quy cho thấy có một mối quan hệ giữa hai chuỗi - giá trị **($\gamma$)** âm cho thấy giá GBP/USD có xu hướng ngược chiều với EUR/USD trong mối quan hệ này. Tuy nhiên, nếu giá trị **($\gamma$)** không đáng kể (như trong ví dụ xấp xỉ = 0), điều đó ám chỉ rằng mối quan hệ giữa hai chuỗi không ổn định, nhưng kiểm định Engle-Granger cho thấy sự khác biệt giữa chúng không ổn định trong dài hạn, vì vậy cặp này không thích hợp cho chiến lược *pairs trading*.

---

## 3. Các kiểm định thống kê phổ biến
Bên cạnh phương pháp Engle-Granger, có nhiều kiểm định được phát triển nhằm xác định tính dừng và hồi quy về trung bình của chuỗi thời gian *(A. Banerjee et al., 1993; Harris, 1995; Pfaff, 2008; Tsay, 2010, 2013)*, bao gồm:
- Dickey–Fuller (DF)
- Augmented Dickey–Fuller (ADF)
- Phillips–Perron (PP)
- Pantula, Gonzales-Farias, and Fuller (PGFF)
- Elliott, Rothenberg, and Stock DF-GLS (ERSD)
- Johansen’s trace test (JOT)
- Schmidt and Phillips rho (SPR)

#### Ý nghĩa thực tế của các kiểm định:
- ***ADF (Augmented Dickey-Fuller) Test***: Là phương pháp kiểm tra tính dừng phổ biến nhất trong thực tế.
- ***Johansen’s Test***: Thích hợp khi kiểm tra *cointegration* trên nhiều hơn hai chuỗi thời gian.
- Sử dụng kết hợp nhiều phương pháp kiểm định có thể giúp đảm bảo kết luận chính xác hơn khi đánh giá mối quan hệ dài hạn giữa các chuỗi thời gian.

Kiểm định *Engle-Granger* và các phương pháp thống kê khác giúp xác định liệu hai chuỗi thời gian có mối quan hệ *cointegration* và hồi quy về mức trung bình hay không. Điều này rất quan trọng trong việc xây dựng chiến lược *pairs trading*, vì mối quan hệ dài hạn giữa hai tài sản giúp khai thác lợi nhuận từ sự phân kỳ và hội tụ giá trong ngắn hạn.

---

Ví dụ, mô hình đơn giản nhất cho *residual* $r_t$ là:

$$r_t = \rho r_{t-1} + \epsilon_t$$

Trong đó:
- $\epsilon_t$ là thành phần nhiễu (*innovation term*).
- Tính dừng yêu cầu *no unit root* $\rho$ phải thỏa mãn $|\rho| < 1$ (không có gốc đơn trong thành phần tự hồi quy).

**Kiểm định Dickey-Fuller (DF Test)** *(Dickey and Fuller, 1979)* định nghĩa bài toán kiểm định giả thuyết như sau:
  - **Giả thuyết không ($H_0$)**: Chuỗi có gốc đơn ($\rho = 1$).
  - **Giả thuyết thay thế ($H_1$)**: Chuỗi là chuỗi dừng ($|\rho| < 1$).

  Với hai giả thuyết này, một **p-value nhỏ**(64) cho thấy chuỗi có tính dừng mạnh (bác bỏ giả thuyết $H_0$). Mô hình của *residual* có thể mở rộng để kết hợp một hằng số và một xu hướng tuyến tính:

$$r_t = \phi_0 + c t + \rho r_{t-1} + \epsilon_t$$

Trong đó:
- $\phi_0$: Hằng số.
- $ct$: Xu hướng tuyến tính theo thời gian.

**Kiểm định ADF (Augmented Dickey-Fuller Test)**: Kiểm định ADF phổ biến hơn vì bổ sung các bậc trễ cao hơn trong mô hình tự hồi quy.

---

#### Giải thích chi tiết:
  **1. Mô hình cơ bản của *residual*:**
  - Mô hình $r_t = \rho r_{t-1} + \epsilon_t$ là mô hình tự hồi quy bậc 1 (*AR(1)*).
  - Tính dừng yêu cầu $|\rho| < 1$, tức là giá trị hiện tại của $r_t$ sẽ không lệch xa so với trung bình mà có xu hướng quay lại sau khi bị nhiễu $\epsilon_t$.

  **2. Kiểm định Dickey-Fuller (DF Test):**
  - **Mục đích:** Kiểm tra liệu chuỗi có phải là chuỗi dừng hay không.
    - Nếu $\rho = 1$, chuỗi là chuỗi không dừng (*random walk*).
    - Nếu $|\rho| < 1$, chuỗi có tính hồi quy về trung bình.

  - **Ý nghĩa p-value:**
    - Nếu p-value **nhỏ hơn 0.05**, bác bỏ giả thuyết $H_0$ → chuỗi là chuỗi dừng.
    - Nếu p-value **lớn hơn 0.05**, không thể bác bỏ $H_0$ → chuỗi có thể không dừng.

  **3. Mô hình mở rộng:**
    - Mô hình mở rộng thêm hằng số $\phi_0$ và xu hướng $ct$ cho phép mô hình hóa chuỗi thời gian với các điều kiện hướng hoặc mức trung bình khác nhau.

  **4. Kiểm định ADF (Augmented Dickey-Fuller):**
    - Là phiên bản mở rộng của DF Test, trong đó bổ sung thêm các bậc trễ cao hơn của $r_t$ để loại bỏ ảnh hưởng của nhiễu ngẫu nhiên trong chuỗi dữ liệu.

---

#### Kết luận:
- *DF Test* và *ADF Test* kiểm tra xem chuỗi thời gian có tính dừng hay không, dựa vào mô hình tự hồi quy.
- Một chuỗi có tính dừng nếu giá trị của chuỗi có xu hướng quay về mức trung bình thay vì phân kỳ.
- Trong chiến lược *pairs trading*, *ADF Test* giúp xác định tính *cointegration* bằng cách kiểm tra xem *residual* từ mô hình hồi quy có tính hồi quy về trung bình hay không.

---

## 4. Ý nghĩa của các giá trị tới hạn (Critical Values) ở mức ý nghĩa 10%, 5%, 1%
Giá trị tới hạn *(Critical Values)* là các ngưỡng giúp so sánh với giá trị thống kê kiểm định để quyết định có bác bỏ giả thuyết không *(null hypothesis)* hay không.

#### Ý nghĩa của các mức giá trị tới hạn:
1. Mức ý nghĩa 10% (0.1):
    - Có 10% xác suất kết luận sai khi bác bỏ giả thuyết không (nghĩa là có 90% xác suất đúng).
    - Đây là mức ý nghĩa thoải mái, chấp nhận nhiều khả năng sai hơn để tăng cơ hội phát hiện đồng tích hợp.

2. Mức ý nghĩa 5% (0.05):
    - Có 5% xác suất kết luận sai khi bác bỏ giả thuyết không (95% xác suất đúng).
    - Đây là mức ý nghĩa thường được sử dụng trong thống kê và tài chính vì cân bằng giữa độ chính xác và mức độ tin cậy.

3. Mức ý nghĩa 1% (0.01):
    - Có 1% xác suất kết luận sai khi bác bỏ giả thuyết không (99% xác suất đúng).
    - Đây là mức ý nghĩa nghiêm ngặt nhất, đòi hỏi bằng chứng rất mạnh mẽ để bác bỏ giả thuyết không. Phù hợp với các phân tích cần độ tin cậy cao.

#### Trong kiểm định Johansen:
- Giả thuyết không (H₀): Không có đồng tích hợp.
- Giả thuyết thay thế (H₁): Có mối quan hệ đồng tích hợp.
→ Nếu giá trị thống kê kiểm định *(Eigenvalue Test Statistic)* lớn hơn giá trị tới hạn tại một mức ý nghĩa nhất định (ví dụ, mức 5%), ta bác bỏ giả thuyết không và kết luận rằng các chuỗi thời gian có mối quan hệ cointegration.

#### Ví dụ trong kết quả kiểm định Johansen:
Nếu giá trị thống kê là 85.04 và các giá trị tới hạn là:
- Mức 10%: 91.10 → Không đủ lớn để bác bỏ giả thuyết không.
- Mức 5%: 95.75 → Không đủ lớn để bác bỏ giả thuyết không.
- Mức 1%: 104.96 → Không đủ lớn để bác bỏ giả thuyết không.
Do vậy, kết luận rằng không có đồng tích hợp giữa các chuỗi thời gian.

**Tóm lại:**
- Mức ý nghĩa càng nhỏ (1%), yêu cầu bằng chứng mạnh hơn để bác bỏ giả thuyết không.
- Nếu giá trị thống kê lớn hơn giá trị tới hạn tại mức ý nghĩa 5% hoặc 1%, điều đó cho thấy bằng chứng mạnh mẽ cho sự đồng tích hợp giữa các chuỗi thời gian.

---

#### Ví dụ code:
Ví dụ lần lượt về các kiểm định: `Dickey–Fuller (DF)` | `Augmented Dickey–Fuller (ADF)` | `Phillips–Perron (PP)` | `Pantula, Gonzales-Farias, and Fuller (PGFF)` |
`Elliott, Rothenberg, and Stock DF-GLS (ERSD)` | `Johansen’s trace test (JOT)` | `Schmidt and Phillips rho (SPR)`

```python
# ===============================================
# VÍ DỤ CÁC KIỂM ĐỊNH THÔNG DỤNG 
# ===============================================

# 1. Dickey-Fuller (DF) Test
from statsmodels.tsa.stattools import adfuller

# Giả lập dữ liệu
np.random.seed(42)
residuals = np.random.normal(0, 1, 200).cumsum()  # Chuỗi không dừng giả lập

# Dickey-Fuller Test
df_test_result = adfuller(residuals, regression='nc')  # Không có constant
print(f"Dickey-Fuller Test p-value: {df_test_result[1]}")

# ===============================================
# 2. Augmented Dickey-Fuller (ADF) Test
# ADF Test (có các bậc trễ bổ sung)
adf_test_result = adfuller(residuals, regression='c')  # Có constant
print(f"Augmented Dickey-Fuller Test p-value: {adf_test_result[1]}")

# ===============================================
# 3. Phillips-Perron (PP) Test
from arch.unitroot import PhillipsPerron

# Phillips-Perron Test
pp_test = PhillipsPerron(residuals)
print(f"Phillips-Perron Test p-value: {pp_test.pvalue}")

# ===============================================
# 4. Pantula, Gonzales-Farias, and Fuller (PGFF) Test
# Hiện tại không có thư viện Python trực tiếp cho kiểm định PGFF. 
# Tuy nhiên, PGFF là một phương pháp kết hợp giữa ADF Test và các giả thuyết thay thế với nhiều xu hướng. 
# Có thể sử dụng adfuller với các tham số regression='ct' (constant + trend).

# PGFF-style Test (Approximation)
pgff_test_result = adfuller(residuals, regression='ct')  # Constant + Trend
print(f"Pantula, Gonzales-Farias, and Fuller (Approximate) p-value: {pgff_test_result[1]}")

# ===============================================
# 5. Elliott, Rothenberg, and Stock DF-GLS (ERSD) Test
from arch.unitroot import DFGLS

# DF-GLS Test (Elliott, Rothenberg, and Stock)
dfgls_test = DFGLS(residuals)
print(f"DF-GLS Test p-value: {dfgls_test.pvalue}")

# ===============================================
# 6. Johansen’s Trace Test (JOT)
from statsmodels.tsa.vector_ar.vecm import coint_johansen

# Johansen’s Test
johansen_test = coint_johansen(df[['EURUSD_Close', 'GBPUSD_Close']], det_order=0, k_ar_diff=1)
print(f"Johansen’s Trace Statistic: {johansen_test.lr1}")
print(f"Critical Values: {johansen_test.cvt}")

# ===============================================
# 7. Schmidt and Phillips rho (SPR) Test
# Hiện chưa có thư viện phổ biến hỗ trợ trực tiếp kiểm định SPR trong Python. 
# Tuy nhiên, có thể thực hiện phương pháp tương tự như PP Test:
from arch.unitroot import PhillipsPerron

# Schmidt and Phillips rho (SPR) (Approximation using PP)
spr_test = PhillipsPerron(residuals, test_type='rho')  # rho-type PP test
print(f"Schmidt-Phillips rho Test p-value: {spr_test.pvalue}")
```

## 5. *Mean-Crossing Rate* và *Half-Life* của *Residual*

Có nhiều phương pháp kinh nghiệm để đo cường độ hồi quy về trung bình của phần dư.

#### Ví dụ:
1. Tần suất vượt qua mức trung bình *(Mean-crossing rate)*:
    - Là số lần *residual* cắt qua mức trung bình trong một khoảng thời gian.
    - Số lần vượt qua càng cao, mức độ hồi quy về trung bình càng mạnh.

2. *Half-life* (thời gian bán rã của hồi quy về trung bình):
    - Là thời gian cần thiết để chuỗi quay trở lại một nửa khoảng cách so với mức trung bình sau khi lệch khỏi mức này.

#### Ý nghĩa:
- Nếu *mean-crossing rate* cao, chuỗi có xu hướng hồi quy nhanh và mạnh về mức trung bình. 
- *Half-life* nhỏ thể hiện tốc độ hồi quy về mức cân bằng nhanh hơn, giúp đánh giá tiềm năng sinh lợi từ chiến lược *pairs trading* dựa trên hồi quy về trung bình. 

#### Ví dụ code:
```python
# Import thư viện cần thiết
import numpy as np
import pandas as pd

# Giả lập dữ liệu residuals (phần dư) từ mô hình hồi quy
np.random.seed(42)
T = 200  # Số lượng điểm dữ liệu
residuals = np.random.normal(0, 1, T).cumsum() - 50  # Chuỗi phần dư giả lập có xu hướng hồi quy về trung bình

# Tính mean-crossing rate
def mean_crossing_rate(residuals):
    mean_value = np.mean(residuals)
    crossings = np.sum((residuals[:-1] - mean_value) * (residuals[1:] - mean_value) < 0)
    rate = crossings / len(residuals)
    return rate

# Tính half-life
def half_life_of_mean_reversion(residuals):
    lagged_residual = residuals[:-1]
    diff_residual = residuals[1:] - residuals[:-1]
    X = np.vstack([lagged_residual, np.ones(len(lagged_residual))]).T
    beta = np.linalg.lstsq(X, diff_residual, rcond=None)[0][0]
    half_life = -np.log(2) / beta if beta != 0 else np.nan  # Tránh chia cho 0
    return half_life

# Tính toán kết quả
mean_crossing_rate_result = mean_crossing_rate(residuals)
half_life_result = half_life_of_mean_reversion(residuals)

# Trả về kết quả
mean_crossing_rate_result, half_life_result
```
#### Result
>(0.075, 18.608891994379192)

**Kết quả Tính *Mean-Crossing Rate* và *Half-Life* của *Residual*:**
Tần suất vượt qua mức trung bình `Mean-Crossing Rate`: 0.075
→ Chuỗi *residual* cắt qua mức trung bình khoảng 7.5% số lần so với tổng số điểm dữ liệu.
→ Đây là dấu hiệu về mức độ hồi quy về trung bình của chuỗi.

Thời gian bán rã `Half-Life`: 18.61 kỳ
→ Sau khi lệch khỏi mức trung bình, chuỗi *residual* mất trung bình 18.61 kỳ để quay lại một nửa khoảng cách đến mức trung bình.

## 6. Kiểm định Cointegrated Augmented Dickey-Fuller (CADF)
CADF Test là kiểm định được sử dụng trong mô hình *cointegration* để kiểm tra tính dừng của *residual* từ mô hình hồi quy giữa hai hoặc nhiều chuỗi thời gian. CADF test tương tự như ADF test nhưng áp dụng với *residual* để xác nhận tính *cointegration* giữa các chuỗi.

Dưới đây là đoạn mã minh họa cách thực hiện kiểm định CADF trong Python:
#### Ví dụ code:
```python
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import numpy as np
import pandas as pd

# Giả lập dữ liệu chuỗi thời gian cho EURUSD và GBPUSD
np.random.seed(42)
T = 200
returns_eur = np.random.normal(0, 0.01, T)
returns_gbp = np.random.normal(0, 0.01, T)

prices_eur = 1.1 * np.exp(np.cumsum(returns_eur))
prices_gbp = 1.3 * np.exp(np.cumsum(returns_gbp))

# DataFrame chứa giá đóng cửa
df = pd.DataFrame({'EURUSD_Close': prices_eur, 'GBPUSD_Close': prices_gbp})

# 1. Hồi quy OLS để tìm phần dư từ cặp chuỗi
X = sm.add_constant(df['GBPUSD_Close'])  # Thêm constant để hồi quy
ols_model = sm.OLS(df['EURUSD_Close'], X).fit()
residuals = ols_model.resid  # Lấy phần dư

# 2. Kiểm định CADF (kiểm tra tính dừng của phần dư)
cadf_test_result = adfuller(residuals)
print("CADF Test Statistic:", cadf_test_result[0])
print("p-value:", cadf_test_result[1])
print("Critical Values:", cadf_test_result[4])

# Kết luận
if cadf_test_result[1] < 0.05:
    print("Phần dư là chuỗi dừng (có đồng tích hợp giữa EURUSD và GBPUSD).")
else:
    print("Phần dư không phải chuỗi dừng (không có đồng tích hợp).")
```

#### Giải thích:
1. Hồi quy OLS:
    - Chạy hồi quy OLS giữa chuỗi `EURUSD_Close` và `GBPUSD_Close` để tính *residual*.

2. Kiểm định ADF với *residual* (CADF Test):
    - Kiểm tra tính dừng của chuỗi *residual*.
    - Nếu `p-value < 0.05`, bác bỏ giả thuyết không (chuỗi có gốc đơn) → Chuỗi là chuỗi dừng → Có *cointegration* giữa hai chuỗi thời gian.

#### Kết luận:
*CADF Test* là một bước quan trọng trong kiểm định *cointegration*. Nếu *residual* từ mô hình hồi quy là chuỗi dừng, thì hai chuỗi có mối quan hệ *cointegration* và có thể sử dụng trong chiến lược *pairs trading*.

---

## 1. Cointegration of More Than Two Time Series (Đồng Tích Hợp Hơn Hai Chuỗi Thời Gian)
Kiểm định *cointegration Engle–Granger* có một số hạn chế:

- Nó được thiết kế cho hai chuỗi thời gian (hoặc hai tài sản).
- Thậm chí trong trường hợp này, bước hồi quy một chuỗi thời gian theo chuỗi thời gian khác phụ thuộc vào thứ tự của các biến.

Mặc dù phương pháp này có thể được mở rộng tự nhiên cho nhiều hơn hai chuỗi tài sản, nhưng thứ tự sắp xếp các biến trở nên rất quan trọng.

#### Phương pháp thay thế:
- **Kiểm định *Johansen (Johansen, 1991, 1995)***: Dựa trên mô hình chuỗi thời gian đa biến *(multivariate time series modeling)*.

- Kiểm định này phù hợp với mô hình **VECM (Vector Error Correction Model)** cho $N$ tài sản.
- Mô hình này tạo ra một ma trận $Π$ chứa các *key* $N × N$ đặc trưng cho mối quan hệ *cointegration* giữa các chuỗi.
→ Bằng cách phân tích thứ hạng của ma trận này, ta có thể xác định số lượng mối quan hệ *cointegration* có trong dữ liệu.

#### Giải thích:
- *Engle-Granger Test*: Tốt cho hai chuỗi nhưng khó áp dụng cho nhiều chuỗi vì thứ tự các chuỗi có thể làm thay đổi kết quả.
- *Johansen Test*: Cho phép kiểm tra *cointegration* với nhiều chuỗi tài sản và không phụ thuộc vào thứ tự biến đầu vào.
Ví dụ: Nếu có ba tài sản A, B, C, kiểm định *Johansen* sẽ xác định có bao nhiêu cặp *cointegration* trong ba tài sản đó.

## 2. Are Cointegrated Pairs Persistent? (Cặp Đồng Tích Hợp Có Ổn Định Không?)
Có thể bạn nghĩ rằng sau khi một cặp *cointegration* được phát hiện và vượt qua các kiểm định cần thiết, công việc đã hoàn thành và chiến lược *pairs trading* sẽ mang lại lợi nhuận. Tuy nhiên, một câu hỏi cần đặt ra là liệu mối quan hệ *cointegration* này có ổn định theo thời gian hay không.

#### Thực tế:
- Không khó để tìm thấy các cặp *cointegration* trong một giai đoạn dữ liệu lịch sử nhất định, nhưng những cặp này có thể mất đi tính *cointegration* trong giai đoạn sau - *out-of-sample period* *(Chan, 2013)*.
- Nguyên nhân: Giá trị tài sản của một công ty có thể thay đổi nhanh chóng do các quyết định quản lý, sự cạnh tranh hoặc các tin tức tiêu cực ảnh hưởng đến một công ty nhưng không ảnh hưởng đến công ty khác.

Trên thực tế, các nghiên cứu thực nghiệm đã đưa ra bằng chứng không ủng hộ giả thuyết cho rằng *cointegration* là một đặc tính bền vững. *(Clegg, 2014)*. *Spread* của các cặp *cointegration* thường bị ảnh hưởng bởi các cú sốc dài hạn có thể làm mất đi tính *cointegration*.

**Giải pháp:**
- Xem xét các phiên bản *cointegration* thay đổi theo thời gian *(time-varying cointegration)*, chẳng hạn như sử dụng lọc *Kalman (Kalman Filtering)* để ước lượng mối quan hệ *cointegration* thay đổi dần theo thời gian.
- Có thể áp dụng các dạng *cointegration* linh hoạt hơn, chẳng hạn như khái niệm *cointegration* từng phần *(partial cointegration)*, cho phép chuỗi *spread* có chứa thành phần *random walk*.

#### Giải thích:
- **Cặp *cointegration* có ổn định không?:** Mối quan hệ *cointegration* có thể thay đổi và không ổn định do các yếu tố bên ngoài như tin tức, quản lý doanh nghiệp hoặc sự cạnh tranh trong thị trường.
- **Lọc Kalman:** Phương pháp giúp mô hình hóa sự thay đổi động của mối quan hệ *cointegration* giữa các chuỗi thời gian.

**Tóm tắt:**
- **Kiểm định *Johansen***: Cho phép kiểm định *cointegration* nhiều hơn hai chuỗi thời gian một cách chính xác và linh hoạt.
- **Tính ổn định của cặp *cointegration:*** Không phải lúc nào cũng bền vững theo thời gian; các sự kiện thị trường có thể phá vỡ mối quan hệ này. Sử dụng các công cụ như *Kalman Filtering* hoặc mô hình *cointegration* từng phần giúp khắc phục nhược điểm này.

#### Ví dụ code:
Kiểm định *johansen* cho một tập hợp ví dụ: `pairs = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", "NZDUSD"]`

```python
# Import các thư viện cần thiết
import numpy as np
import pandas as pd
from statsmodels.tsa.vector_ar.vecm import coint_johansen

# Tạo chuỗi dữ liệu giả lập cho các cặp tiền tệ
np.random.seed(42)
T = 200  # Số lượng điểm dữ liệu
pairs = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", "NZDUSD"]
prices_data = {}

# Giả lập dữ liệu giá đóng cửa cho mỗi cặp tiền tệ
for pair in pairs:
    initial_price = np.random.uniform(1.0, 2.0)  # Giá ban đầu ngẫu nhiên
    returns = np.random.normal(0, 0.01, T)  # Lợi nhuận ngẫu nhiên
    prices_data[pair] = initial_price * np.exp(np.cumsum(returns))  # Giá đóng cửa giả lập

# Tạo DataFrame chứa giá đóng cửa của tất cả các cặp tiền tệ
df_prices = pd.DataFrame(prices_data, index=pd.date_range(start='2022-01-01', periods=T))

# Chạy kiểm định Johansen cho tập hợp các cặp tiền tệ
johansen_test_result = coint_johansen(df_prices, det_order=0, k_ar_diff=1)

# In kết quả kiểm định Johansen
print("Eigenvalue Test Statistics:")
print(johansen_test_result.lr1)
print("\nCritical Values:")
print(johansen_test_result.cvt)

# In kết luận về số lượng đồng tích hợp
rank = sum(johansen_test_result.lr1 > johansen_test_result.cvt[:, 1])
print(f"\nSố lượng mối quan hệ đồng tích hợp: {rank}")
```
##### STDOUT/STDERR
![image](https://github.com/user-attachments/assets/3a89f701-5943-4fc3-914c-4710833f4c88)

#### Kết quả Kiểm định Johansen cho tập hợp các cặp tiền tệ:
- **Eigenvalue Test Statistics:** Đây là các giá trị thống kê kiểm định cho từng cặp giá trị riêng.
- **Critical Values:** Các giá trị tới hạn ở các mức ý nghĩa 10%, 5% và 1%.

#### Kết luận:
- Số lượng mối quan hệ *cointegration* được phát hiện là 0.
→ Không có mối quan hệ *cointegration* đáng kể giữa các chuỗi giá đóng cửa của các cặp tiền tệ trong tập hợp dữ liệu giả lập này.

#### Giải thích:
- Nếu một thống kê kiểm định lớn hơn giá trị tới hạn tại một mức ý nghĩa nhất định (ví dụ 5%), ta có thể bác bỏ giả thuyết không và kết luận rằng có tồn tại mối quan hệ *cointegration*.
- Trong trường hợp này, tất cả các giá trị thống kê đều không đủ lớn để vượt qua ngưỡng tới hạn, do đó không có cặp *cointegration* giữa các chuỗi.

Nếu bạn muốn thử nghiệm với dữ liệu thực tế hoặc tinh chỉnh số lượng bậc trễ (k__ar__diff) và các thông số khác, điều này có thể dẫn đến các kết quả khác nhau.​

---

***Bản quyền dịch thuật và diễn giải thuộc về justinnguyen92&copy; - [telegram](https://t.me/justinnguyen92)***

Giả sử chúng ta đã phát hiện được một cặp chuỗi thời gian *log-price* $y_{1t}$ và $y_{2t}$ có *cointegration* và đã tạo thành chuỗi *spread* $y_{1t} - \gamma y_{2t}$, tức là sử dụng danh mục hai tài sản $w = [1, -\gamma]^T$ với đòn bẩy:

$$\|w\| = 1 + \gamma$$

Để đảm bảo việc so sánh công bằng, cần chuẩn hóa đòn bẩy về mức 1. Khi đó, danh mục đầu tư với đòn bẩy chuẩn hóa sẽ là:

$$
w = \frac{1}{1 + \gamma} 
\begin{bmatrix} 
1 \\ 
-\gamma 
\end{bmatrix}
\tag{15.2}
$$

*Spread* chuẩn hóa sẽ là: $z_t = w^T y_t$

Lợi nhuận của danh mục đầu tư tại thời điểm $t$ (bỏ qua chi phí giao dịch) được tính là (xem Chương 6 để biết chi tiết về ký hiệu danh mục đầu tư - *portfolio notation*):

$$w^T (y_t - y_{t-1}) = z_t - z_{t-1}$$

Giả sử chúng ta chốt lời ở thời gian $t$ sau $k$ chu kỳ, *spread* hồi về mức trung bình và vị thế được đóng lại. Điều này dẫn đến mức chênh lệch tối thiểu là $|z_{t+k} - z_t| \geq s_0$, đây chính là lợi nhuận danh mục trong $k$ thời kỳ.

#### Mô tả quá trình giao dịch:
- **Trading *spread***: Xác định thời điểm mua hoặc bán *spread* và quyết định mức đầu tư (*sizing*).

- Một chuỗi tín hiệu $s_t$ được định nghĩa để biểu thị chiến lược:
  - Dương (+): Mua.
  - Bằng 0: Không mở vị thế.
  - Âm (−): Bán khống.

Giao dịch *spread* được tóm gọn thành việc quyết định khi nào nên mua hoặc bán khống *spread*, và đầu tư bao nhiêu (gọi là "*sizing"*). Điều này được thực hiện một cách thuận tiện bằng cách định nghĩa một chuỗi thời gian "tín hiệu" $s_1, s_2, s_3, \ldots$, trong đó $s_t$ biểu thị mức độ đầu tư (giá trị dương cho mua, bằng 0 khi không có vị thế, và giá trị âm cho bán khống), thường được giới hạn trong khoảng \(-1 \leq s_t \leq 1\) để kiểm soát đòn bẩy.

Chúng ta sẽ giả định rằng giá trị của tín hiệu tại thời điểm $t$, $s_t$, đã được quyết định dựa trên thông tin đến (và bao gồm cả) thời điểm $t$, nghĩa là, $\ldots, y_{t-2}, y_{t-1}, y_t$. Như vậy, sự kết hợp giữa *spread portfolio* (15.2) và tín hiệu $s_t$ tạo ra danh mục đầu tư thay đổi theo thời gian $s_t \times w$, với lợi nhuận tương ứng:

$$R_t^{\text{port}} = s_{t-1} \times w^T (y_t - y_{t-1}) = s_{t-1} \times (z_t - z_{t-1}),$$

- $s_{t-1}$: Tín hiệu giao dịch tại thời điểm $t-1$.
- $w^T (y_t - y_{t-1})$: Biến động *spread* của danh mục.

### Giải thích chi tiết:
1. **Đòn bẩy chuẩn hóa**:
   - Việc chuẩn hóa đòn bẩy về 1 giúp đảm bảo rằng mức độ rủi ro giữa các chiến lược có thể so sánh được.
   - Trong số danh mục $w = [1, -\gamma]$ cho biết khối lượng tài sản cần mua và bán tương ứng.

2. **Tín hiệu giao dịch**:
   - Chuỗi tín hiệu $s_t$ kiểm soát quyết định mở hoặc đóng vị thế:
     - $s_t = 1$: Mở vị thế mua *spread*.
     - $s_t = -1$: Mở vị thế bán *spread*.
     - $s_t = 0$: Không mở vị thế.

3. **Lợi nhuận danh mục**:
   - Lợi nhuận phụ thuộc vào sự thay đổi của *spread* trong khoảng thời gian từ $t-1$ đến $t$.
   - Khi *spread* hồi về trung bình (mean reversion), lợi nhuận được chốt dựa trên biến động *spread*.

### Ý nghĩa trong thực tế:
- Nếu *spread* lệch quá xa mức trung bình và có tín hiệu phù hợp ($s_t$), nhà giao dịch sẽ mở vị thế để khai thác lợi nhuận từ sự hồi tụ của *spread*.
- Phương pháp này nhấn mạnh tầm quan trọng của việc chuẩn hóa tỷ lệ giao dịch để tránh rủi ro quá mức và đảm bảo lợi nhuận ổn định.

---

# Trading Strategies
Để xây dựng một chiến lược giao dịch *spread*, điều cần thiết là xác định quy tắc cho tín hiệu định cỡ vị thế $s_t$. Vì vậy, một phương pháp thông dụng là sử dụng phiên bản chuẩn hóa của *spread*, gọi là **standard score (*z-score*)**:

```math
z_t^{\text{score}} = \frac{z_t - \mathbb{E}[z_t]}{\sqrt{\text{Var}(z_t)}},
```

- $\mathbb{E}[z_t]$: Kỳ vọng (trung bình) của *spread* $z_t$.
- $\text{Var}(z_t)$: Phương sai của $z_t$.

*Z-score* này có giá trị trung bình bằng 0 và phương sai bằng 1.

<span style="color:red">Tuy nhiên, trong thực tế, *z-score* không thể được sử dụng trực tiếp do mắc phải vấn đề *look-ahead bias* (thiên kiến biết trước) khi ước tính giá trị trung bình và phương sai trên toàn bộ dữ liệu. Một cách tiếp cận đơn giản là sử dụng một tập dữ liệu huấn luyện nhằm xác định trung bình và phương sai, sau đó áp dụng chúng cho dữ liệu kiểm tra trong tương lai.</span> Một cách tiếp cận tinh vi hơn là tính toán các giá trị này một cách thích ứng trên cửa sổ trượt *(rolling window)*, chẳng hạn bằng cách sử dụng **Bollinger Bands**.

*Bollinger Bands* là một công cụ giao dịch kỹ thuật được tạo ra bởi John Bollinger vào đầu những năm 1980. Công cụ này xuất phát từ nhu cầu cần các đại diện giao dịch linh hoạt từ việc quan sát thấy rằng độ biến động *(volatility)* có tính động theo thời gian.

- *Bollinger Bands* được tính toán dựa trên trung bình và độ lệch chuẩn trong một khoảng thời gian xác định trước *(rolling-window basis over some lookback window)*.
- Dải trên và dưới được tính là mức trung bình cộng hoặc trừ hai lần độ lệch chuẩn.

Trong bối cảnh *z-score*, *spread* có thể được chuẩn hóa một cách thích ứng bằng cách sử dụng các trung bình và phương sai được tính toán trên các khoảng thời gian trượt *(can be adaptively normalized with the rolling mean and rolling standard deviation)*.

### Giải thích chi tiết:
1. Z-score* (Standard Score):
   - *Z-score* chuẩn hóa giá trị *spread* để xác định vị trí tương đối của nó so với trung bình.
   - Nếu *z-score* lớn hơn một ngưỡng nhất định, ta có thể coi đó là tín hiệu để mở hoặc đóng vị thế trong chiến lược *pairs trading*.

2. Vấn đề Look-Ahead Bias:
   - *Look-ahead bias* xảy ra khi sử dụng thông tin từ tương lai trong quá trình tính toán, dẫn đến mô hình thiếu tính thực tế.
   - Giải pháp là sử dụng các "cửa sổ trượt" (*rolling window*) để cập nhật trung bình và phương sai liên tục.

3. Bollinger Bands:
   - *Bollinger Bands* giúp xác định mức độ phân kỳ của giá so với trung bình.
   - Dải trên và dưới cho biết mức biến động mà tại đó *spread* có thể bật ngược trở lại mức trung bình.

4. Chiến lược giao dịch với Bollinger Bands:
- Khi *spread* vượt qua dải trên → **Bán khống** (SHORT).
- Khi *spread* chạm dải dưới → **Mua vào** (LONG).
- Nếu *spread* nằm trong khoảng giữa → **Không mở vị thế**.

### Kết luận:
Chiến lược giao dịch *spread* dựa vào việc sử dụng *z-score* để xác định điểm vào và thoát lệnh. Tuy nhiên, việc sử dụng dữ liệu trong tương lai gây ra thiên kiến, vì vậy cần dùng các phương pháp động như Bollinger Bands để đảm bảo tính khách quan và thực tế. *Bollinger Bands* cho phép xác định các mức biến động hợp lý để thực hiện các giao dịch trong chiến lược *pairs trading*.

---

# "Linear Strategy" và "Thresholded Strategy"
Chúng ta hãy mô tả hai chiến lược giao dịch *spread* đơn giản nhất, đó là chiến lược tuyến tính (*linear strategy*) và chiến lược ngưỡng (*thresholded strategy*):  

### 1. Chiến lược tuyến tính (*Linear Strategy*):
Chiến lược này rất dễ hiểu và dựa trên ý tưởng đối lập: *mua khi giá thấp và bán khi giá cao*. *(Chan, 2013)*  
- Ban đầu, tín hiệu định cỡ vị thế $s_t$ có thể được định nghĩa đơn giản là giá trị âm của *z-score*:  $s_t = -z_t^{\text{score}}$

- Để *scale-in* và *scale-out* quy mô hoặc thậm chí tốt hơn, bao gồm một hệ số mở rộng quy mô như $s_t = - \frac{z_{\text{score}, t}}{s_0}$ trong đó $s_0$ biểu thị ngưỡng mà tín hiệu được đòn bẩy tối đa - *fully leveraged*

- Trong thực tế, để giới hạn đòn bẩy ở mức 1, ta giới hạn tín hiệu định cỡ vị thế trong khoảng $[-1, 1]$:  

```math
s_t = -\left[ \frac{z_t^{\text{score}}}{s_0} \right]_{-1}^{+1},
```

Trong đó, $[\cdot]_{a}^{b}$ giới hạn giá trị của biểu thức: nếu nhỏ hơn $a$ thì gán bằng $a$, nếu lớn hơn $b$ thì gán bằng $b$.

### 2. **Chiến lược ngưỡng (*Thresholded Strategy*):**  
Chiến lược này cũng tuân theo nguyên tắc đối lập mua thấp và bán cao, nhưng thay vì tuyến tính, nó là chiến lược "tất cả hoặc không" - *all-in or all-out sizing based* *(Vidyamurthy, 2004)* dựa trên các ngưỡng giá trị $s_0$:  
- Mua khi *z-score* thấp hơn $-s_0$.  
- Bán khống khi *z-score* lớn hơn $+s_0$.
- Đóng vị thế khi *z-score* trở lại $0$.  

Công thức tín hiệu định cỡ vị thế:  

```math
s_t =
\begin{cases} 
+1 & \text{if } z_t^{\text{score}} < -s_0, \\
0 & \text{after } z_t^{\text{score}} \text{ reverts to } 0, \\
-1 & \text{if } z_t^{\text{score}} > +s_0.
\end{cases}
```

### Giải thích chi tiết:
#### 1. Linear Strategy (Chiến lược tuyến tính):
   - **Nguyên tắc:** Tín hiệu định cỡ vị thế thay đổi tuyến tính theo giá trị của *z-score*.
   - Khi *spread* càng phân kỳ so với trung bình (*z-score* càng lớn hoặc nhỏ), quy mô vị thế càng lớn để tối đa hóa lợi nhuận khi *spread* hồi về mức trung bình.
   - Tuy nhiên, để tránh rủi ro quá mức, giá trị $s_t$ được giới hạn trong khoảng $[-1, 1]$, nghĩa là đòn bẩy tối đa là 1 (không vay thêm vốn).

#### 2. Thresholded Strategy (Chiến lược ngưỡng):
   - **Nguyên tắc:** Chỉ mở vị thế khi *z-score* vượt qua các ngưỡng $\pm s_0$.
   - Đây là chiến lược đơn giản nhưng hiệu quả trong việc tránh các tín hiệu nhiễu nhỏ.
   - Không thay đổi kích thước vị thế dần dần như chiến lược tuyến tính mà chỉ vào lệnh khi mức độ phân kỳ đủ lớn và đóng lệnh khi *spread* hồi tụ về 0.

### Tóm tắt:
- **Chiến lược tuyến tính (Linear):** Quy mô vị thế thay đổi dần dựa trên mức độ phân kỳ của *spread*.
- **Chiến lược ngưỡng (Thresholded):** Quy mô vị thế được quyết định bởi các ngưỡng cố định; chỉ vào lệnh khi phân kỳ lớn và đóng lệnh khi *spread* hồi tụ về 0.
- Hai chiến lược này đều dựa trên nguyên tắc chính của *pairs trading*: *mua thấp và bán cao để thu lợi từ sự hồi tụ về mức trung bình của *spread**.

---
Hình 15.13 và 15.14 minh họa chiến lược tuyến tính và chiến lược ngưỡng, lần lượt được xây dựng dựa trên một spread tổng hợp được tạo từ mô hình AR(1) với hệ số tự hồi quy là 0,7. Lưu ý sự khác biệt về bản chất của kích thước tín hiệu: *continuous* so với *on-off*. Các ngưỡng được chọn một cách tùy ý là $s_0 = 1$ và cần được tối ưu hóa phù hợp để tối đa hóa lợi nhuận (như được mô tả chi tiết trong phần tiếp theo). Trong thực tế, phiên bản *z-score rolling* nên được sử dụng để đảm bảo có thể triển khai mà không gặp lỗi *look-ahead bias*, chẳng hạn như dựa trên *Bollinger Bands (Chan, 2013)*. 

Figure 15.13: Illustration of pairs trading via the linear strategy on the spread.
![image](https://github.com/user-attachments/assets/1bff1890-c2a8-499b-98ab-9d6c9623f414)

Figure 15.14: Illustration of pairs trading via the thresholded strategy on the spread.
![image](https://github.com/user-attachments/assets/3d29796f-7c44-4c97-a442-120b0ab037df)

---

#### Ví dụ code: 
Chiến lược *Linear Strategy* với các mức *standard deviation* 1 - 2 - 3, `signal` khi `z-score` *cross* mức 2

```python
# ================================================================
# VÍ DỤ CHIẾN LƯỢC LINEAR STRATEGY VỚI Z-SCORE & STD
# ================================================================
# Import các thư viện cần thiết
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Giả lập dữ liệu chuỗi thời gian spread với mô hình AR(1)
np.random.seed(42)
T = 200  # Số lượng điểm dữ liệu
phi = 0.7  # Hệ số tự hồi quy
epsilon = np.random.normal(0, 1, T)
spread = np.zeros(T)
spread[0] = 0

for t in range(1, T):
    spread[t] = phi * spread[t - 1] + epsilon[t]  # AR(1)

# Tạo DataFrame chứa spread
df = pd.DataFrame({"spread": spread})

# Tính z-score (rolling mean và rolling std) với cửa sổ trượt 20 kỳ
window = 20
df['rolling_mean'] = df['spread'].rolling(window).mean()
df['rolling_std'] = df['spread'].rolling(window).std()
df['z_score'] = (df['spread'] - df['rolling_mean']) / df['rolling_std']

# Thay đổi chiến lược Linear Strategy để sử dụng các mức độ lệch chuẩn (standard deviation)
# Ngưỡng mới thay đổi theo mức 2 (cross mức 2 để kích hoạt tín hiệu)
upper_threshold = 2  # Ngưỡng trên (+2)
lower_threshold = -2  # Ngưỡng dưới (-2)

# Tín hiệu giao dịch: 
# +1 khi Z-score xuống dưới mức -2 (mua), -1 khi Z-score vượt qua mức +2 (bán khống)
df['signal'] = np.where(df['z_score'] <= lower_threshold, 1, 0)  # Mua vào khi z-score <= -2
df['signal'] = np.where(df['z_score'] >= upper_threshold, -1, df['signal'])  # Bán khống khi z-score >= +2

# Lợi nhuận chiến lược
df['position_change'] = df['signal'].diff().fillna(0)  # Thay đổi vị thế
df['returns'] = df['signal'].shift(1) * df['spread'].diff()  # Lợi nhuận từ spread
df['cumulative_returns'] = df['returns'].cumsum()  # Lợi nhuận tích lũy

# Vẽ biểu đồ z-score, tín hiệu giao dịch và lợi nhuận tích lũy
plt.figure(figsize=(15, 10))

# Biểu đồ Z-score
plt.subplot(3, 1, 1)
plt.plot(df.index, df['z_score'], label='Z-score', color='blue')
plt.axhline(upper_threshold, color='red', linestyle='--', label=f'Upper Threshold (+{upper_threshold})')
plt.axhline(lower_threshold, color='green', linestyle='--', label=f'Lower Threshold ({lower_threshold})')
plt.axhline(0, color='black', linestyle='--', label='Mean')
plt.title('Z-score with Standard Deviation Levels')
plt.legend()

# Biểu đồ Tín hiệu giao dịch
plt.subplot(3, 1, 2)
plt.plot(df.index, df['signal'], label='Signal', color='black')
plt.title('Signal for Linear Strategy with Thresholds')
plt.ylim([-1.5, 1.5])
plt.legend()

# Biểu đồ Lợi nhuận tích lũy
plt.subplot(3, 1, 3)
plt.plot(df.index, df['cumulative_returns'], label='Cumulative Returns', color='purple')
plt.title('Cumulative Returns from Modified Linear Strategy')
plt.legend()

plt.tight_layout()
plt.show()
```
![output (7)](https://github.com/user-attachments/assets/f4237a9e-9b71-4bb5-9ae0-41089682e732)

### Phân tích Biểu đồ Chiến lược Giao dịch với Ngưỡng *Standard Deviation*
1. **Biểu đồ `Z-score` và `Standard Deviation Levels`:**
   - **`Z-score` <span style="color:blue">(đường màu xanh)</span>:** Biểu diễn sự lệch của `spread` so với mức trung bình.
   - **Ngưỡng ±2 (đường đứt nét):**
     - <span style="color:red">Đường màu đỏ: Ngưỡng trên (+2)</span>.
     - <span style="color:green">Đường màu xanh lá: Ngưỡng dưới (-2)</span>.
   - Khi `Z-score` vượt qua các ngưỡng này, tín hiệu giao dịch được kích hoạt.

2. **Biểu đồ Tín hiệu Giao dịch:**
   - **+1 (mua vào):** Khi `Z-score` <= -2 (spread quá thấp so với mức trung bình).
   - **-1 (bán khống):** Khi `Z-score` >= +2 (spread quá cao so với mức trung bình).
   - **0 (không vị thế):** Khi `Z-score` nằm giữa các ngưỡng hoặc quay lại gần mức trung bình.

3. **Biểu đồ Lợi nhuận Tích lũy:**
   - Lợi nhuận tích lũy có xu hướng tăng dần khi các tín hiệu giao dịch được kích hoạt đúng thời điểm, chứng tỏ chiến lược hoạt động tốt trong việc khai thác sự hồi quy về trung bình của `spread`.

### Kết luận:
- **Chiến lược sử dụng mức lệch chuẩn ±2** giúp giảm thiểu các tín hiệu nhiễu nhỏ (khi `spread` dao động nhẹ quanh trung bình).
- Đây là cách tối ưu để vào lệnh khi có sự phân kỳ đáng kể và thoát lệnh khi spread hồi về trung bình, từ đó tối ưu hóa lợi nhuận và giảm rủi ro do tín hiệu sai lệch.

---

#### Ví dụ code: 
Chiến lược *Linear Strategy* với *Bollinger Bands*

```python
# ================================================================
# LINEAR STRATEGY + BOLLINGER BANDS
# Tính Bollinger Bands cho Z-score
bollinger_window = 20  # Cửa sổ tính toán Bollinger Bands
df['z_score_rolling_mean'] = df['z_score'].rolling(bollinger_window).mean()  # Trung bình động Z-score
df['z_score_rolling_std'] = df['z_score'].rolling(bollinger_window).std()  # Độ lệch chuẩn động Z-score
df['upper_band'] = df['z_score_rolling_mean'] + 2 * df['z_score_rolling_std']  # Dải trên (+2 std)
df['lower_band'] = df['z_score_rolling_mean'] - 2 * df['z_score_rolling_std']  # Dải dưới (-2 std)

# Tạo tín hiệu giao dịch dựa trên Bollinger Bands
df['signal_bollinger'] = 0  # Khởi tạo tín hiệu mặc định là 0 (không vị thế)
df['signal_bollinger'] = np.where(df['z_score'] >= df['upper_band'], -1, df['signal_bollinger'])  # Bán khi Z-score >= dải trên
df['signal_bollinger'] = np.where(df['z_score'] <= df['lower_band'], 1, df['signal_bollinger'])  # Mua khi Z-score <= dải dưới

# Tính lợi nhuận chiến lược
df['returns_bollinger'] = df['signal_bollinger'].shift(1) * df['spread'].diff()  # Lợi nhuận từ spread
df['cumulative_returns_bollinger'] = df['returns_bollinger'].cumsum()  # Lợi nhuận tích lũy

# Vẽ biểu đồ z-score, tín hiệu giao dịch và lợi nhuận tích lũy
plt.figure(figsize=(15, 10))

# Biểu đồ Z-score
plt.subplot(3, 1, 1)
plt.plot(df.index, df['z_score'], label='Z-score', color='blue')
plt.plot(df.index, df['upper_band'], label='Bollinger Upper Band (+2 std)', color='red', linestyle='--')
plt.plot(df.index, df['lower_band'], label='Bollinger Lower Band (-2 std)', color='green', linestyle='--')
plt.axhline(0, color='black', linestyle='--', label='Mean')
plt.title('Z-score with Bollinger Bands for Linear Strategy')
plt.legend()

# Biểu đồ tín hiệu giao dịch
plt.subplot(3, 1, 2)
plt.plot(df.index, df['signal_bollinger'], label='Signal', color='black')
plt.title('Trading Signals (Bollinger Bands)')
plt.ylim([-1.5, 1.5])
plt.axhline(0, color='grey', linestyle='--')
plt.legend()

# Biểu đồ lợi nhuận tích lũy
plt.subplot(3, 1, 3)
plt.plot(df.index, df['cumulative_returns_bollinger'], label='Cumulative Returns', color='purple')
plt.title('Cumulative Returns from Bollinger Bands Strategy')
plt.legend()

plt.tight_layout()
plt.show()
```

![output (8)](https://github.com/user-attachments/assets/bccb18a9-3d17-483c-896d-f9871cebc610)
![output (9)](https://github.com/user-attachments/assets/f25c647b-5711-40fe-a229-ab21df9330ec)

### Phân tích Biểu đồ Z-score với Bollinger Bands
1. ***Z-score* <span style="color:blue">(đường màu xanh)</span>:**
   - Biểu diễn sự lệch của spread so với trung bình động.
   - Khi `Z-score` vượt qua ngưỡng trên hoặc dưới, có thể xuất hiện tín hiệu giao dịch.

2. **Dải *Bollinger Bands*:**
   - **<span style="color:red">Dải trên (+2 độ lệch chuẩn, đường màu đỏ)</span>:** Biểu diễn mức độ phân kỳ mạnh về phía tăng.
   - **<span style="color:green">Dải dưới (-2 độ lệch chuẩn, đường màu xanh lá)</span>:** Biểu diễn mức độ phân kỳ mạnh về phía giảm.

3. **Đường trung bình (đường màu đen):**
   - Trung tâm của *Bollinger Bands*, đại diện cho trung bình động của `Z-score`.

### Nhận xét:
- Khi `Z-score` chạm hoặc vượt qua dải *Bollinger Bands*, tín hiệu giao dịch có thể kích hoạt.
- *Bollinger Bands* giúp xác định rõ vùng giá trị phân kỳ bất thường của `spread`, từ đó hỗ trợ việc ra quyết định mua hoặc bán trong chiến lược *Linear Strategy*.

### Phân tích Biểu đồ Chiến lược Giao dịch với *Bollinger Bands*
1. **Biểu đồ Tín hiệu Giao dịch (*Trading Signals*):**
   - **Tín hiệu +1 (mua vào):** Khi `Z-score` giảm xuống dưới dải dưới (-2 độ lệch chuẩn).
   - **Tín hiệu -1 (bán khống):** Khi `Z-score` vượt lên trên dải trên (+2 độ lệch chuẩn).
   - **Tín hiệu 0 (không vị thế):** Khi `Z-score` nằm trong khoảng giữa dải trên và dải dưới hoặc hồi về mức trung bình.

2. **Biểu đồ Lợi nhuận Tích lũy (*Cumulative Returns*):**
   - Đường lợi nhuận tích lũy cho thấy các lần vào lệnh đúng thời điểm đã mang lại lợi nhuận tích cực.
   - Chiến lược này tạo ra các bước nhảy lợi nhuận khi `spread` phân kỳ đáng kể và sau đó quay trở lại mức trung bình.

### Nhận xét:
- **Chiến lược *Bollinger Bands*:** Giúp tránh các tín hiệu nhiễu khi *spread* dao động nhẹ quanh mức trung bình.
- **Hiệu suất chiến lược:** Biểu đồ lợi nhuận tích lũy cho thấy lợi nhuận có xu hướng tăng trưởng đều khi chiến lược hoạt động tốt trong các tình huống hồi quy về trung bình.
- Để tăng độ chính xác, có thể thay đổi tham số của cửa sổ trượt và độ lệch chuẩn trong dải *Bollinger Bands* để phù hợp với dữ liệu thực tế hơn.

---

#### Ví dụ code: 
Chiến lược *Thresholded Strategy* và `z-score` *standard deviation* +-2

```python
# ===============================================
# VÍ DỤ CHIẾN LƯỢC THRESHOLDED VỚI Z-SCORE & STD
# ===============================================
# Import các thư viện cần thiết
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Giả lập dữ liệu chuỗi thời gian spread với mô hình AR(1)
np.random.seed(42)
T = 200  # Số lượng điểm dữ liệu
phi = 0.7  # Hệ số tự hồi quy
epsilon = np.random.normal(0, 1, T)
spread = np.zeros(T)
spread[0] = 0

for t in range(1, T):
    spread[t] = phi * spread[t - 1] + epsilon[t]  # AR(1)

# Tạo DataFrame chứa spread
df = pd.DataFrame({"spread": spread})

# Tính z-score (rolling mean và rolling std) với cửa sổ trượt 20 kỳ
window = 20
df['rolling_mean'] = df['spread'].rolling(window).mean()
df['rolling_std'] = df['spread'].rolling(window).std()
df['z_score'] = (df['spread'] - df['rolling_mean']) / df['rolling_std']

# Thay đổi chiến lược Linear Strategy để sử dụng các mức độ lệch chuẩn (standard deviation)
# Ngưỡng mới thay đổi theo mức 2 (cross mức 2 để kích hoạt tín hiệu)
upper_threshold = 2  # Ngưỡng trên (+2)
lower_threshold = -2  # Ngưỡng dưới (-2)

# Tín hiệu giao dịch Thresholded Strategy
df['signal'] = 0  # Mặc định không có vị thế
df['signal'] = np.where(df['z_score'] <= lower_threshold, 1, df['signal'])  # Mua khi z-score <= -2
df['signal'] = np.where(df['z_score'] >= upper_threshold, -1, df['signal'])  # Bán khống khi z-score >= +2

# Lợi nhuận chiến lược
df['returns'] = df['signal'].shift(1) * df['spread'].diff()  # Lợi nhuận từ spread
df['cumulative_returns'] = df['returns'].cumsum()  # Lợi nhuận tích lũy

# Vẽ biểu đồ z-score, tín hiệu giao dịch và lợi nhuận tích lũy
plt.figure(figsize=(15, 10))

# Biểu đồ Z-score
plt.subplot(3, 1, 1)
plt.plot(df.index, df['z_score'], label='Z-score', color='blue')
plt.axhline(upper_threshold, color='red', linestyle='--', label=f'Upper Threshold (+{upper_threshold})')
plt.axhline(lower_threshold, color='green', linestyle='--', label=f'Lower Threshold ({lower_threshold})')
plt.axhline(0, color='black', linestyle='--', label='Mean')
plt.title('Z-score with Thresholded Strategy')
plt.legend()

# Biểu đồ Tín hiệu giao dịch
plt.subplot(3, 1, 2)
plt.plot(df.index, df['signal'], label='Signal', color='black')
plt.title('Thresholded Strategy Signal')
plt.ylim([-1.5, 1.5])
plt.legend()

# Biểu đồ Lợi nhuận tích lũy
plt.subplot(3, 1, 3)
plt.plot(df.index, df['cumulative_returns'], label='Cumulative Returns', color='purple')
plt.title('Cumulative Returns from Thresholded Strategy')
plt.legend()

plt.tight_layout()
plt.show()
```

![output (10)](https://github.com/user-attachments/assets/a4700041-1d2f-479c-ad77-2e037baffcac)

### Phân tích Biểu đồ Chiến lược Giao dịch Thresholded Strategy với Ngưỡng ±2
1. Biểu đồ `Z-score` và ngưỡng ±2:
   - `Z-score` <span style="color:blue">(đường màu xanh)</span>: Biểu diễn mức độ phân kỳ của `spread` so với trung bình.
   - Ngưỡng trên và dưới:
      - <span style="color:red">Đường màu đỏ (+2)</span> → Nếu `Z-score` vượt qua ngưỡng này, kích hoạt bán khống.
      - <span style="color:green">Đường màu xanh lá (-2)</span> → Nếu `Z-score` xuống dưới ngưỡng này, kích hoạt mua vào.
   - Khi `Z-score` nằm giữa các ngưỡng, không có tín hiệu giao dịch.

2. Biểu đồ Tín hiệu Giao dịch:
   - Tín hiệu +1 (mua vào): Khi `Z-score` xuống dưới mức -2.
   - Tín hiệu -1 (bán khống): Khi `Z-score` vượt qua mức +2.
   - Tín hiệu 0: Khi `Z-score` nằm trong khoảng giữa hoặc quay lại gần trung bình.

3. Biểu đồ Lợi nhuận Tích lũy:
   - Lợi nhuận tích lũy tăng khi tín hiệu giao dịch được kích hoạt đúng thời điểm (`spread` hồi về trung bình).
   - Sự gia tăng rõ rệt chứng tỏ chiến lược khai thác hiệu quả sự hồi quy về trung bình của `spread`.

### Kết luận:
- ***Thresholded Strategy***: Chỉ vào lệnh khi sự phân kỳ đủ lớn (ngưỡng ±2), giúp giảm các tín hiệu nhiễu nhỏ.
- Lợi nhuận tích lũy: Chiến lược này đem lại kết quả tốt, với mức lợi nhuận tăng đều nhờ việc chốt lời khi *spread* hồi về mức trung bình.
- Đây là chiến lược phù hợp với dữ liệu có sự hồi quy về trung bình rõ ràng như trong ví dụ trên. ​

---

***Bản quyền dịch thuật và diễn giải thuộc về justinnguyen92&copy; - [telegram](https://t.me/justinnguyen92)***

# Optimizing the Threshold - Tối ưu hóa Threshold
Xem xét chiến lược *thresholded strategy* đơn giản, trong đó:
- **Mua:** Khi *Z-score* giảm xuống dưới ngưỡng $-s_0$.
- **Bán khống:** Khi *Z-score* vượt lên trên ngưỡng $+s_0$.
- **Đóng vị thế (unwinding):** Khi *Z-score* quay trở lại giá trị cân bằng (zero).

Lưu ý rằng, theo ngữ cảnh của *spread*, ngưỡng $s_0$ được định nghĩa là:

$$s_0 \times \sigma$$

**Trong đó:**
- $\sigma$: Độ lệch chuẩn của *spread*.

Việc lựa chọn giá trị ngưỡng $s_0$ là rất quan trọng vì nó xác định:
1. Tần suất vị thế được đóng (chốt lời).
2. Lợi nhuận tối thiểu đạt được trên mỗi giao dịch.

Tổng lợi nhuận bằng số lần giao dịch nhân với lợi nhuận của mỗi giao dịch. Khi vị thế được đóng sau $k$ kỳ, ý nghĩa của sự khác biệt *spread* $z_{t+k} - z_t$ phụ thuộc vào việc *spread* biểu thị ***log-prices*** hay ***prices***:
- ***Log-prices:*** Chênh lệch *spread* biểu thị *log-return* của *profit*.
- ***Prices:*** Chênh lệch *spread* biểu thị lợi nhuận tuyệt đối (*absolute profit* - được mở rộng cùng với *initial budget*).

Do đó, sau $N^{\text{trades}}$ giao dịch thành công, tổng lợi nhuận (chưa gộp lãi) có thể được tính là:

$$N^{\text{trades}} \times s_0 \sigma$$

(Lợi nhuận gộp lãi - *compounded profit* cũng có thể được sử dụng).

Phần tiếp theo sẽ xác định giá trị ngưỡng tối ưu $s_0$ để tối đa hóa tổng lợi nhuận trong cả hai cách tiếp cận tham số và phi tham số.

### Diễn giải chi tiết:
1. **Ngưỡng giao dịch ($s_0$):**
   - Ngưỡng $s_0$ được sử dụng để xác định mức độ phân kỳ cần thiết trước khi thực hiện giao dịch.
   - Ngưỡng này là thước đo độ nhạy của chiến lược:
     - **Ngưỡng nhỏ** → Giao dịch thường xuyên hơn, nhưng lợi nhuận mỗi giao dịch thấp.
     - **Ngưỡng lớn** → Giao dịch ít hơn, nhưng lợi nhuận mỗi giao dịch cao hơn.

2. **Ý nghĩa của *spread*:**
   - Nếu *spread* được đo bằng log-prices, chênh lệch *spread* đại diện cho lợi nhuận log (*log-return*).
   - Nếu *spread* được đo bằng prices, chênh lệch *spread* đại diện cho lợi nhuận tuyệt đối (*absolute profit*).

3. **Tổng lợi nhuận:**
   - Lợi nhuận tổng hợp là sản phẩm của:
     - **Số lần giao dịch thành công** ($N_{trades}$).
     - **Lợi nhuận tối thiểu của mỗi giao dịch** ($s_0 \cdot \sigma$).

4. **Mục tiêu:**
   - Xác định giá trị tối ưu của $s_0$ để cân bằng giữa tần suất giao dịch và lợi nhuận mỗi giao dịch nhằm tối đa hóa tổng lợi nhuận.

### Kết luận:
- Chiến lược *thresholded strategy* phụ thuộc vào việc lựa chọn ngưỡng $s_0$, giúp tối ưu hóa lợi nhuận dựa trên mức độ phân kỳ và hồi quy của *spread*.
- Trong thực tế, giá trị $s_0$ phải được điều chỉnh phù hợp với dữ liệu lịch sử và điều kiện thị trường cụ thể để đạt hiệu quả cao nhất.

## 1. Parametric Approach - Tiếp cận tham số
Giả sử *Z-score* tuân theo phân phối chuẩn - *standard normal distribution*:

```math
z_t^{\text{score}} \sim \mathcal{N}(0, 1).
```

Khi đó, xác suất *Z-score* lệch khỏi giá trị trung bình 0 với biên độ lớn hơn hoặc bằng $s_0$ là: $1 - \Phi(s_0)$, Trong đó $\Phi(\cdot)$ là Hàm phân phối tích lũy (CDF) của phân phối chuẩn.

Với chuỗi thời gian có $T$ giai đoạn, số sự kiện giao dịch khả thi (theo một hướng) có thể được xấp xỉ: $T \times \left(1 - \Phi(s_0)\right)$ với tổng lợi nhuận - *total profit* là: $T \times \left(1 - \Phi(s_0)\right) \times s_0$

Dưới mô hình tham số đơn giản này, ngưỡng tối ưu $s_0^*$ có thể được tìm thấy bằng cách:

$$s_0^* = \arg \max_{s_0} \, \left(1 - \Phi(s_0)\right) \times s_0$$

Hình 15.15 minh họa cách đánh giá tham số của lợi nhuận so với ngưỡng $s_0$ cho một chuỗi *spread* Gaussian tổng hợp.
![image](https://github.com/user-attachments/assets/b73faef1-f494-4142-a284-b47191dad55c)

### Diễn giải chi tiết:
#### 1. Giả định về *Z-score*:
   - *Z-score* được giả định tuân theo phân phối chuẩn chuẩn hóa $\mathcal{N}(0, 1)$, điều này phù hợp với thực tế vì *Z-score* là sự chuẩn hóa của *spread* dựa trên trung bình và phương sai.

#### 2. Xác suất giao dịch:
   - Xác suất *Z-score* vượt qua ngưỡng $s_0$ (trong một hướng, tức là chỉ giao dịch mua hoặc bán) là: $1 - \Phi(s_0)$
   - Do đó, số sự kiện giao dịch có thể xảy ra trong chuỗi thời gian $T$ là:

$$T \times (1 - \Phi(s_0))$$

#### 3. Lợi nhuận tổng thể:
   - Lợi nhuận mỗi giao dịch tối thiểu là $s_0$.
   - Lợi nhuận tổng thể (chưa gộp lãi) là:
     
$$T \times (1 - \Phi(s_0)) \times s_0$$

   - Công thức này thể hiện rằng lợi nhuận phụ thuộc vào ngưỡng $s_0$:
     - Ngưỡng $s_0$ lớn hơn → ít giao dịch nhưng lợi nhuận mỗi giao dịch cao hơn.
     - Ngưỡng $s_0$ nhỏ hơn → nhiều giao dịch nhưng lợi nhuận mỗi giao dịch thấp hơn.

#### 4. Ngưỡng tối ưu ($s_0^*$):
   - Ngưỡng tối ưu $s_0^*$ được xác định bằng cách tối đa hóa hàm lợi nhuận tổng thể:

$$s_0^* = \arg \max_{s_0} \left[(1 - \Phi(s_0)) \cdot s_0 \right]$$

### Kết luận:
- ***Parametric Approach:*** Cung cấp cách tiếp cận có hệ thống để tối ưu hóa ngưỡng giao dịch $s_0$, dựa trên giả định về phân phối của *Z-score*.
- **Ứng dụng thực tế:** Giá trị $s_0^*$ sẽ tối ưu hóa sự cân bằng giữa tần suất giao dịch và lợi nhuận mỗi giao dịch, giúp tối đa hóa tổng lợi nhuận.
- **Hạn chế:** Phương pháp này giả định phân phối chuẩn của *Z-score*, có thể không hoàn toàn đúng với dữ liệu thực tế.

## 2. Nonparametric Data-Driven Approach - Tiếp cận dữ liệu phi tham số
Một phương pháp thay thế cho cách tiếp cận tham số - *parametric approach* (dựa trên một mô hình có thể không chính xác) là phương pháp dựa trên dữ liệu phi tham số *nonparametric data-driven approach* <span style="color:red">tức là dựa trên dữ liệu mà không dựa vào bất kỳ giả định mô hình nào</span>. Ý tưởng chính là chỉ cần sử dụng dữ liệu sẵn có để thực nghiệm tính toán số lượng sự kiện giao dịch cho mỗi ngưỡng có thể.

Một cách tiếp cận thay thế cho phương pháp tham số (dựa trên mô hình có thể không chính xác) là phương pháp dựa trên dữ liệu, không dựa trên bất kỳ giả định mô hình nào. Ý tưởng là chỉ sử dụng dữ liệu sẵn có để đếm số lượng sự kiện có thể giao dịch cho mỗi ngưỡng khả thi.

Với $T$ quan sát của *z-score*, $z_t^{\text{score}}$ trong khoảng $t = 1, \ldots, T$, và $J$ giá trị ngưỡng được rời rạc hóa $s_{0,1}, \ldots, s_{0,J}$, ta có thể tính tần suất giao dịch thực nghiệm cho mỗi ngưỡng $s_{0j}$ (theo một hướng) như sau:

$$\bar{f}_j = \frac{1}{T} \sum_{t=1}^{T} \mathbf{1}\{z_t^{\text{score}} > s_{0,j}\},$$

Trong đó: $\mathbf{1}\{.\}$ là hàm chỉ báo, trả về giá trị 1 nếu điều kiện đúng và 0 nếu sai.

Thật không may, các giá trị thực nghiệm $\bar{f}_j$ có thể rất nhiễu - *noise*, điều này có thể ảnh hưởng đến việc đánh giá tổng lợi nhuận - *total profit*. Một cách để giảm nhiễu trong các giá trị $\bar{f} = (\bar{f}_1, \ldots, \bar{f}_j)$ là tận dụng thực tế rằng tần suất giao dịch nên là một hàm làm mượt của ngưỡng. Chúng ta có thể thu được một phiên bản mượt hơn bằng cách giải bài toán bình phương tối thiểu.


$$\min_f \sum_{j=1}^J (f_j - \bar{f_j})^2 + \lambda \sum_{j=1}^{J-1} (f_j - f_{j+1})^2$$

Trong đó:
- Thành phần đầu tiên đo lường sự khác biệt giữa giá trị $f_j$ nhiều và giá trị mượt.
- Thành phần thứ hai đảm bảo tính mượt, được kiểm soát bởi siêu tham số - *hyper-parameter*  $\lambda$.

Bài toán này có thể viết gọn hơn dưới dạng:

$$\min_f \|f - \bar{f}\|_2^2 + \lambda \|D f\|_2^2$$

Trong đó:
- $D$ là ma trận sai phân (*difference matrix*), được định nghĩa như sau:

```math
D =
\begin{bmatrix}
1 & -1 &  &  &  \\
  & 1  & -1 &  &  \\
  &    & \ddots & \ddots &  \\
  &    &        & 1 & -1
\end{bmatrix}
\in \mathbb{R}^{(J-1) \times J}.
```

Do đây là bài toán bình phương tối thiểu, lời giải có dạng đóng (*closed-form*):

$$f^* = (I + \lambda D^\top D)^{-1} \bar{f}$$

Cuối cùng, ngưỡng tối ưu có thể được tìm bằng cách tối đa hóa tổng lợi nhuận đã được làm mượt:

$$s_0^* = \arg \max_{s_{0j} \in \{s_{01}, s_{02}, \ldots, s_{0J}\}} s_{0j} \times f_j.$$

Hình 15.16 minh họa việc đánh giá phi tham số về lợi nhuận so với ngưỡng, cho thấy phiên bản dữ liệu mượt hơn và ít nhiễu gốc.
![image](https://github.com/user-attachments/assets/6e80b7fa-5c12-4b87-a470-ec0788d29991)

### Diễn giải chi tiết:
##### 1. Phương pháp phi tham số:
   - Không giả định *Z-score* tuân theo phân phối chuẩn, mà chỉ sử dụng dữ liệu thực nghiệm.
   - Tính toán tần suất giao dịch thực nghiệm $f_j$ cho mỗi ngưỡng $s_{0,j}$.

##### 2. Giảm nhiễu:
   - Các giá trị $f_j$ thực nghiệm có thể bị nhiễu (do số lượng giao dịch nhỏ hoặc sự biến động bất thường).
   - Sử dụng bài toán bình phương tối thiểu để mượt hóa $f_j$, đảm bảo tính liên tục giữa các ngưỡng.

#### 3. Bài toán mượt hóa:
   - Thành phần $\|f - \bar{f}\|_2^2$: Đo độ lệch giữa giá trị nhiễu và giá trị mượt.
   - Thành phần $\|D f\|_2^2$: Đảm bảo sự thay đổi giữa các giá trị $f_j$ liên tiếp là nhỏ, duy trì tính mượt mà.

#### 4. Ngưỡng tối ưu:
   - Ngưỡng tối ưu $s_0^*$ được xác định bằng cách tối đa hóa tổng lợi nhuận trên dữ liệu mượt.

### Kết luận:
- Phương pháp phi tham số không dựa vào giả định mô hình, giúp linh hoạt và phù hợp với dữ liệu thực nghiệm.
- Mượt hóa tần suất giao dịch $f_j$ giúp cải thiện đánh giá lợi nhuận và xác định ngưỡng giao dịch tối ưu $s_{0}^*$.
- Đây là cách tiếp cận mạnh mẽ khi dữ liệu nhiễu và không đáp ứng được các giả định mô hình của phương pháp tham số.

# Primer on the Kalman Filter
Mô hình không gian trạng thái *(State-space modeling)* cung cấp một *framework* thống nhất để xử lý nhiều loại vấn đề trong phân tích chuỗi thời gian. Nó có thể được coi là một mô hình phổ quát và linh hoạt, với một thuật toán rất hiệu quả là bộ lọc Kalman *(Kalman filter)*. Ý tưởng cơ bản là ước tính sự tiến hóa của hệ thống theo thời gian, được thúc đẩy bởi một loạt các giá trị chưa quan sát hoặc giá trị ẩn, mà chỉ có thể được đo lường gián tiếp thông qua các quan sát từ đầu ra của hệ thống. Mô hình này có thể được sử dụng để lọc, làm mượt và dự báo. Chi tiết hơn về *State-space modeling* và *Kalman filter* có thể được tìm thấy trong Mục 4.2 của Chương 4.

*Kalman filter*, được NASA sử dụng trong chương trình Apollo vào những năm 1960, hiện nay đã có rất nhiều ứng dụng công nghệ. Nó thường được sử dụng trong dẫn đường, định vị và điều khiển của các phương tiện như máy bay, tàu vũ trụ và tàu biển. Bộ lọc này cũng được ứng dụng rộng rãi trong phân tích chuỗi thời gian, xử lý tín hiệu và kinh tế lượng. Gần đây, nó đã trở thành một thành phần chính trong việc lập kế hoạch và kiểm soát robot, cũng như tối ưu hóa quỹ đạo.

*State-space modeling* và *Kalman filter* đã phát triển đầy đủ, với nhiều sách giáo khoa xuất sắc có sẵn như các tài liệu kinh điển của B. D. O. Anderson và Moore (1979), Durbin và Koopman (2012). Một số tài liệu tham khảo khác bao gồm Brockwell và Davis (2002), Shumway và Stoffer (2017), A. Harvey (1989), và đặc biệt trong chuỗi thời gian tài chính như Zivot et al. (2004), Tsay (2010), Lütkepohl (2007), và Koopman (2009).**

## Mô hình toán học của *Kalman filter*
Về mặt toán học, *Kalman filter* dựa trên *State-space modeling* tuyến tính Gaussian với thời gian rời rạc $t = 1, \dots, T$ *(Durbin và Koopman, 2012)*:

$$y_t = Z_t \alpha_t + \epsilon_t \quad (\text{phương trình quan sát}),$$

$$\alpha_{t+1} = T_t \alpha_t + \eta_t \quad (\text{phương trình trạng thái}),$$

**Trong đó:**
- $y_t$: Quan sát qua thời gian với Ma trận quan sát $Z_t$.
- $\alpha_t$: Trạng thái ẩn hoặc chưa quan sát được của hệ thống với Ma trận chuyển tiếp trạng thái $T_t$.
- $\epsilon_t$ và $\eta_t$: là các nhiễu *noise* là phân phối Gaussian với Ma trận $mean=0$ và Ma trận hiệp phương sai - *covariance* lần lượt mà $H$ và $Q$:

$$\epsilon_t \sim \mathcal{N}(0, H), \quad \eta_t \sim \mathcal{N}(0, Q).$$

- Trạng thái ban đầu $\alpha_1$ có thể được mô hình hóa như:

$$\alpha_1 \sim \mathcal{N}(\alpha_1, P_1).$$

Các phần mềm hiện đại luôn sẵn có *(python, R) (Helske, 2017; Holmes et al., 2012; Petris and Petrone, 2011; Tusell, 2011).*(66)

**Ghi chú:**
- Các tham số của *State-space modeling* ($Z_t, T_t, H, Q, \alpha_1, P_1$) có thể được người dùng cung cấp (nếu biết) hoặc được suy ra từ dữ liệu với các thuật toán tối đa hóa độ khả năng hợp lý *(maximum likelihood estimation)*. Một lần nữa, các phần mềm hiện nay có sẵn và hiệu quả cho việc lắp tham số này. *(Holmes et al., 2012)*.(67)

- Để chính xác hơn, bộ lọc Kalman là một thuật toán rất hiệu quả để mô tả tối ưu phân phối của trạng thái ẩn tại thời điểm $t$, $\alpha_t$, theo cách nhân quả. Cụ thể, $\alpha_{t|t-1}$ và $\alpha_{t|t}$ biểu thị giá trị kỳ vọng dựa trên các quan sát đến thời điểm $t-1$ và $t$, tương ứng. Các đại lượng này có thể được tính toán hiệu quả bằng thuật toán "chuyển tiếp" (forward pass) chạy từ $t = 1$ đến $t = T$ một cách đệ quy - *recursive way*, để thuật toán có thể hoạt động theo thời gian thực *(Durbin and Koopman, 2012)*.

#### Ý nghĩa và ứng dụng của *Kalman filter*:
1. **Tối ưu hóa phân phối trạng thái ẩn:**
   - *Kalman filter* là một thuật toán hiệu quả để mô tả tối ưu phân phối của trạng thái ẩn tại thời điểm $t$, $\alpha_t$, theo cách nhân quả.
   - Cụ thể:
     - $\alpha_{t+1|t}$: Trạng thái dự đoán tại thời điểm $t + 1$ dựa trên các quan sát từ $t$ trở về trước.
     - $\alpha_{t|t}$: Trạng thái ước tính tại thời điểm $t$.
   - Các giá trị này có thể được tính toán hiệu quả thông qua quy trình "đi tới" (forward pass) từ $t = 1$ đến $T$.

2. **Ứng dụng thực tế:**
   - *Kalman filter* không chỉ được sử dụng trong mô hình hóa chuỗi thời gian mà còn trong các bài toán điều khiển thời gian thực.

#### Kết luận:
- *State-space modeling* cung cấp một cách tiếp cận linh hoạt để xử lý chuỗi thời gian phức tạp.
- *Kalman filter* là một công cụ mạnh mẽ và hiệu quả để ước tính trạng thái ẩn của hệ thống, đặc biệt trong các ứng dụng thời gian thực như tài chính, kinh tế lượng, và kỹ thuật điều khiển.

---


## *Spread Modeling* thông qua *Kalman*

Trong bối cảnh mô hình hóa *spread*, chúng ta muốn mô hình hóa $y_{1t} \approx \mu_t + \gamma_t y_{2t}$, trong đó \mu_t và $\gamma_t$ thay đổi chậm theo thời gian. Điều này có thể thực hiện dễ dàng thông qua mô hình không gian trạng thái bằng cách xác định trạng thái ẩn là $\alpha_t = (\mu_t, \gamma_t)$, dẫn đến:

```math
y_{1t} = [1 \ y_{2t}] 
\begin{bmatrix}
\mu_t \\
\gamma_t
\end{bmatrix} 
+ \epsilon_t,
```

```math
\begin{bmatrix}
\mu_{t+1} \\
\gamma_{t+1}
\end{bmatrix} 
= 
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
\mu_t \\
\gamma_t
\end{bmatrix} 
+ 
\begin{bmatrix}
\eta_{1t} \\
\eta_{2t}
\end{bmatrix},
```
[15.3]

**Trong đó:**
- Tất cả các thành phần nhiễu đều độc lập và tuân theo phân phối: $\epsilon_t \sim \mathcal{N}(0, \sigma_\epsilon^2)$, $\eta_{\mu_t} \sim \mathcal{N}(0, \sigma_\mu^2),$ và $\eta_{\gamma_t} \sim \mathcal{N}(0, \sigma_\gamma^2).$

- Ma trận chuyển tiếp trạng thái là $T = I$, ma trận quan sát là $Z_t = [1 \ y_{2t}]$, và trạng thái ban đầu là:
  - $\mu_1 \sim \mathcal{N}(\bar{\mu}, \sigma_{\mu,1}^2),$
  - $\gamma_1 \sim \mathcal{N}(\bar{\gamma}, \sigma_{\gamma,1}^2)$.

*Spread* chuẩn hóa với đòn bảy = 1 (xem công thức 15.2), có thể được tính:

$$z_t = \frac{1}{1 + \gamma_{t|t-1}} \left( y_{1t} - \gamma_{t|t-1} y_{2t} - \mu_{t|t-1} \right),$$



Trong đó $\mu_{t|t-1}$ và $\gamma_{t|t-1}$ là các trạng thái ẩn được ước tính bởi thuật toán Kalman.

---

## Ước tính các Tham số của Mô hình
Các tham số mô hình $\sigma^2_\epsilon$, $\sigma^2_\mu$, $\sigma^2_\gamma$ (và trạng thái ban đầu - *initial states*) có thể được xác định bằng các phương pháp ước lượng đơn giản hoặc được tối ưu hóa từ dữ liệu (yêu cầu tính toán phức tạp hơn). Ví dụ, ta có thể sử dụng tập dữ liệu huấn luyện ban đầu với $T^{LS}$ mẫu để ước lượng $\mu$ và $\gamma$ thông qua phương pháp bình phương tối thiểu, $\mu^{LS}$ và $\gamma^{LS}$, từ đó thu được phần dư ước lượng $\epsilon_t^{LS}$. Sau đó, các công thức sau đây cung cấp một phương pháp ước lượng hiệu quả cho các tham số *State-space model*:

$$
\sigma^2_\epsilon = \text{Var} \left( \epsilon_t^{LS} \right),
$$

$$
\mu_1 \sim \mathcal{N} \left( \mu^{LS}, \frac{1}{T^{LS}} \text{Var} \left( \epsilon_t^{LS} \right) \right),
$$

$$
\gamma_1 \sim \mathcal{N} \left( \gamma^{LS}, \frac{1}{T^{LS}} \frac{\text{Var} \left( \epsilon_t^{LS} \right)}{\text{Var} \left( y_{2t} \right)} \right),
$$

$$
\sigma^2_\mu = \alpha \times \text{Var} \left( \epsilon_t^{LS} \right),
$$

$$
\sigma^2_\gamma = \alpha \times \frac{\text{Var} \left( \epsilon_t^{LS} \right)}{\text{Var} \left( y_{2t} \right)},
$$

trong đó, siêu tham số $\alpha$ xác định tỷ lệ biến động giữa các trạng thái ẩn thay đổi chậm theo thời gian và sự biến động của *spread*.

---

## Mở Rộng Mô Hình Không Gian Trạng Thái
*State-space model* của *spread* trong (15.3) có thể được mở rộng theo nhiều cách khác nhau để cải thiện hiệu suất. Một cách mở rộng đơn giản là mô hình hóa không chỉ tỷ lệ *hedge* mà còn cả động lượng hoặc vận tốc của nó. Điều này có thể được thực hiện bằng cách mở rộng trạng thái ẩn thành $\alpha_t = (\mu_t, \gamma_t, \dot{\gamma}_t)$, dẫn đến mô hình không gian trạng thái:

```math
y_{1t} = [1 \, y_{2t} \, 0]
\begin{bmatrix}
\mu_t \\ \gamma_t \\ \dot{\gamma}_t
\end{bmatrix}
+ \epsilon_t,
```

```math
\begin{bmatrix}
\mu_{t+1} \\ \gamma_{t+1} \\ \dot{\gamma}_{t+1}
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
\mu_t \\ \gamma_t \\ \dot{\gamma}_t
\end{bmatrix}
+ \eta_t.
\tag{15.4}
```

Mô hình này làm cho $\gamma_t$ ít nhiễu hơn và cung cấp một *spread* tốt hơn, như được chỉ ra trong các thí nghiệm số.

Một cách mở rộng khác của *state-space modeling* trong (15.3) dưới khái niệm *cointegration* một phần là mô hình hóa *spread* với một thành phần tự hồi quy *(Clegg and Krauss, 2018)*. Điều này có thể được thực hiện bằng cách định nghĩa trạng thái ẩn là $\alpha_t = (\mu_t, \gamma_t, \epsilon_t)$, dẫn đến:

```math
y_{1t} = [1 \, y_{2t} \, 1]
\begin{bmatrix}
\mu_t \\ \gamma_t \\ \epsilon_t
\end{bmatrix},
```

```math
\begin{bmatrix}
\mu_{t+1} \\ \gamma_{t+1} \\ \epsilon_{t+1}
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \rho
\end{bmatrix}
\begin{bmatrix}
\mu_t \\ \gamma_t \\ \epsilon_t
\end{bmatrix}
+ \eta_t.
\tag{15.5}
```

trong đó $\rho$ là một tham số cần được ước lượng với điều kiện $|\rho| < 1$ (hoặc được cố định ở một giá trị hợp lý như $\rho = 0.9$).


### Kết luận
- *State-space modeling* cung cấp một phương pháp linh hoạt và hiệu quả để mô hình hóa *spread* trong giao dịch cặp.
- Việc mở rộng mô hình với vận tốc hoặc thành phần tự hồi quy có thể cải thiện đáng kể hiệu suất dự báo và giao dịch.

---


