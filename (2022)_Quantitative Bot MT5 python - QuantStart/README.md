# Quantitative bot mt5 python
 Quantitative bot mt5 python

## Setup MT5 connect python is here:
This is socket connect for mt5 and python - use DARWINEX library

https://github.com/darwinex/dwxconnect/

https://github.com/darwinex/dwxconnect/blob/main/README.md

All resources in dwxconnect-main.zip

## Use Backtrader as framework backtest for python 
Have an error when install directly from pip: 

https://stackoverflow.com/questions/63471764/importerror-cannot-import-name-warnings-from-matplotlib-dates

Install Backtrader from here to pass the error: 

pip install git+https://github.com/mementum/backtrader.git@0fa63ef4a35dc53cc7320813f8b15480c8f85517#egg=backtrader

# Modelling
## Statistical Learning & Statistical Testing

Tại sao phải làm Statistical Testing?

Đối với algorithmic trading, các bài test thống kê chỉ hữu ích khi chúng tạo ra lợi nhuận khi được áp dụng cho các chiến lược trading. Như vậy có thể lập luận rằng nó có ý nghĩa hơn khi dùng đánh giá performance ở cấp độ giao dịch (strategy level) hơn là ở cấp độ time series. Vậy thì giá trị của việc tính toán các số liệu trên là gì khi chỉ có thể sử dụng ở cấp độ phân tích giao dịch (trade level analysis), đo lường risk/reward và đánh giá drawdown trong giao dịch?

<sup>As far as algorithmic trading is concerned the statistical tests outlined above are only as useful as the profits they generate when applied to trading strategies. Thus it could be argued that it makes more sense to evaluate performance at the strategy level rather than at time series level. What is the value of calculating the above metrics when it is possible to use trade level analysis, risk/reward measures and drawdown evaluations?</sup>

Đầu tiên, bất kỳ chiến lược giao dịch nào được thực hiện nào dựa trên đo lường time series statistical sẽ có một mẫu lớn hơn nhiều để làm việc. Điều này đơn giản là vì khi tính toán các bài statistical tests này mỗi bar của thông tin đang được sử dụng thay vì mỗi trade. Sẽ có ít round-trip trades hơn nhiều với bar và do đó, ý nghĩa thống kê của bất kỳ số đo trade-level nào sẽ sai lệch nhỏ hơn.

<sup>Firstly, any implemented trading strategy based on a time series statistical measure will have a far larger sample to work with. This is simply because when calculating these statistical tests each *bar* of information is being used rather than each *trade*. There will be far less roundtrip trades than bars and hence the statistical significance of any trade-level metrics will be far smaller.</sup>

Thứ hai, bất kỳ chiến lược nào được triển khai sẽ phụ thuộc vào các tham số nhất định, chẳng hạn như lookback periods cho rolling measures hoặc z-score measures để vào và thoát khỏi giao dịch trong mean-reversion setting. Do đó, strategy level metrics chỉ phù hợp với các tham số này trong khi các  statistical tests có giá trị đối với chính mẫu time series nội tại.

<sup>Secondly, any strategy implemented will depend upon certain parameters such as lookback periods for rolling measures or z-score measures for entering and exiting a trade in a mean-reversion setting. Hence strategy level metrics are only appropriate for *these parameters* while the statistical tests are valid for the underlying time series sample itself.</sup>

Trong công việc thực tế, cả hai bộ số liệu thống kê sẽ được tính toán. Các thư viện Statsmodels và Pandas giúp việc này cực kỳ đơn giản.

<sup>In practice both sets of statistics will be calculated. The Statsmodels and Pandas libraries make this extremely straightforward. The additional effort is actually rather minimal!</sup>

### Regression
## Linear regression

https://www.alpharithms.com/predicting-stock-prices-with-linear-regression-214618/

Aside: Giả định Linear Regression & Autocorrelation

Trước khi đi sâu hơn, chúng ta cần thảo luận về giới hạn kỹ thuật của Linear Regression. Linear Regression yêu cầu một loạt các giả định được thực hiện để có hiệu quả. Người ta có thể áp dụng một mô hình tuyến tính (linear model) mà không cần xác thực các giả định này nhưng không có khả năng có được những insight hữu ích.

Một trong những giả định này là các biến trong dữ liệu là độc lập (independent variables). Cụ thể, điều này chỉ ra rằng phần dư - residuals (chênh lệch giữa giá trị dự đoán - predicted value và giá trị quan sát được - observed value) cho bất kỳ biến đơn lẻ nào là không liên quan.

Đối với dữ liệu dạng Time Series, đây thường là một vấn đề vì các giá trị được quan sát của chúng ta có bản chất là theo chiều dọc—có nghĩa là chúng là các giá trị được quan sát cho cùng một thứ, được ghi lại theo trình tự. Điều này tạo ra một đặc tính gọi là tự tương quan (autocorrelation), mô tả cách một biến có liên hệ với chính nó như thế nào (liên quan đến chính nó.) (Chatterjee, 2012)

<sup>For Time Series data this is often a problem since our observed values are *longitudinal* in nature—meaning they are *observed values* for the same thing, recorded in sequence. This produces a characteristic called autocorrelation which describes how a variable is somehow related to itself (self-related.) (Chatterjee, 2012)</sup>

Phân tích Autocorrelation rất hữu ích trong việc xác định các xu hướng như tính thời vụ hoặc kiểu thời tiết. Tuy nhiên, khi nói đến các giá trị ngoại suy để dự đoán giá, đó là một vấn đề. Điều đáng nói ở đây là các giá trị ngày của chúng ta không phù hợp làm biến độc lập và chúng ta cần nghĩ ra một thứ khác và sử dụng giá trị đóng đã điều chỉnh làm biến độc lập. May mắn thay, có một số lựa chọn tuyệt vời ở đây.

<sup>*Autocorrelation analysis* is useful in identifying trends like seasonality or weather patterns. When it comes to extrapolating values for price prediction, however, it is problematic. The takeaway here is that our date values aren’t suitable as our *independent variable* and we need to come up with something else and use the adjusted close value as the independent variable</sup>

https://realpython.com/linear-regression-in-python/

https://www.geeksforgeeks.org/linear-regression-python-implementation/



