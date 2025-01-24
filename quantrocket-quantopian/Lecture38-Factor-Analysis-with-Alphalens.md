# Factor Analysis with Alphalens

Làm thế nào để chúng ta biết một yếu tố alpha có tốt hay không? Thật không may, không có một ngưỡng cụ thể nào để cho bạn biết liệu một yếu tố có thực sự hữu ích hay không. Thay vào đó, chúng ta cần so sánh một yếu tố cụ thể với các lựa chọn khác trước khi quyết định có sử dụng nó hay không. Mục tiêu cuối cùng của chúng ta trong việc xác định và chọn các yếu tố tốt nhất là sử dụng chúng để xếp hạng cổ phiếu trong chiến lược cổ phiếu long-short, đã được đề cập ở các bài giảng khác. Các yếu tố mà càng dự đoán độc lập, thì phương pháp xếp hạng và chiến lược tổng thể của chúng ta sẽ càng tốt hơn.

Điều chúng ta mong muốn khi so sánh các yếu tố là đảm bảo rằng tín hiệu được chọn thực sự có khả năng dự đoán **sự chuyển động tương đối của giá cả**. Chúng ta không muốn dự đoán số lượng tuyệt đối mà các tài sản trong *universe* của chúng ta sẽ tăng hay giảm. Chúng ta chỉ quan tâm rằng chúng ta có thể chọn các tài sản để mua sẽ tốt hơn các tài sản mà chúng ta bán. Trong chiến lược *long-short equity*, chúng ta nắm giữ một danh mục tài sản **LONG** và một danh mục tài sản **SHORT**, được xác định bởi các giá trị yếu tố liên quan đến từng tài sản trong *universe* của chúng ta. Nếu phương pháp xếp hạng của chúng ta có tính dự đoán, điều này có nghĩa là các tài sản trong danh mục trên cùng sẽ vượt trội hơn các tài sản trong danh mục dưới cùng. Miễn là sự chênh lệch này nhất quán theo thời gian, chiến lược của chúng ta sẽ có lợi nhuận dương.

Một yếu tố riêng lẻ có thể có nhiều thành phần chuyển động để đánh giá, nhưng lý tưởng là nó nên độc lập với các yếu tố khác mà bạn đã giao dịch để giữ cho danh mục đầu tư của bạn đa dạng. Chúng ta thảo luận lý do này trong bài giảng về Rủi Ro Tập Trung Vị Trí - *Position Concentration Risk*.

Trong bài giảng này, chúng ta sẽ trình bày chi tiết và giải thích các thống kê liên quan để đánh giá yếu tố alpha của bạn trước khi thử triển khai nó trong một thuật toán. Điều quan trọng cần nhớ là tất cả các số liệu được cung cấp ở đây là tương đối so với các yếu tố khác mà bạn có thể đang giao dịch hoặc đánh giá.

Hãy cùng xem xét một yếu tố và thử đánh giá tính khả thi của nó. Chúng ta sẽ tính toán các giá trị yếu tố bằng cách sử dụng Pipeline, vì vậy hãy đảm bảo rằng bạn đã xem qua hướng dẫn về Pipeline nếu chưa quen với cách Pipeline hoạt động.

```python
from zipline.research import run_pipeline, get_forward_returns
from zipline.pipeline import Pipeline, master, EquityPricing
from zipline.pipeline.factors import Returns, AverageDollarVolume
```

# Momentum

Ở đây, chúng ta sẽ sử dụng yếu tố **momentum** làm ví dụ. Các yếu tố momentum là một dạng rất phổ biến của yếu tố alpha và chúng xuất hiện ở nhiều hình thức và kích cỡ khác nhau. Tất cả đều cố gắng đạt được cùng một ý tưởng, rằng các chứng khoán đang di chuyển sẽ tiếp tục di chuyển. Các yếu tố momentum cố gắng định lượng xu hướng trong thị trường tài chính và "lướt trên làn sóng", có thể nói như vậy.

Giả sử rằng chúng ta nghi ngờ rằng một yếu tố momentum có thể dự đoán được lợi nhuận của cổ phiếu.

```python
momentum = Returns(window_length=252, exclude_window_length=21)
```

Yếu tố momentum này xem xét sự thay đổi giá trong suốt năm qua, tính đến một tháng trước.

# Judging a Factor with Alphalens

Để đánh giá liệu một yếu tố có khả thi hay không, chúng tôi đã tạo ra một *package* có tên là **Alphalens**. Mã nguồn của *package* này có sẵn trên [GitHub](https://github.com) nếu bạn muốn tìm hiểu chi tiết về cách nó hoạt động. Chúng tôi sử dụng Alphalens để tạo một "tear sheet" của một yếu tố, tương tự như cách chúng tôi sử dụng **pyfolio** để tạo một "tear sheet" để phân tích

```python
import alphalens as al
```

Alphalens sử dụng yếu tố của bạn và kiểm tra mức độ hữu ích của nó trong việc dự đoán giá trị tương đối thông qua một tập hợp các chỉ số khác nhau. Nó phân loại tất cả các cổ phiếu trong universe mà bạn đã chọn vào các phần vị (quantiles) khác nhau dựa trên thứ hạng của chúng theo yếu tố của bạn và phân tích lợi nhuận, hệ số thông tin (IC), tỷ lệ thay đổi của từng phần vị và cung cấp phân tích chi tiết về lợi nhuận và IC theo ngành (hoặc các khóa phân nhóm khác).

Trong suốt bài giảng này, chúng ta sẽ xem xét các phần chính của một "tear sheet" của Alphalens từng bước một và giải thích cách diễn giải các biểu đồ riêng lẻ khác nhau. Để làm điều này, chúng ta sẽ nêu rõ các bước trung gian từ việc định nghĩa pipeline đến tạo ra một "tear sheet". Ở cuối sổ ghi chú, chúng ta sẽ chỉ ra một cách dễ dàng hơn để bỏ qua các bước trung gian và tạo toàn bộ "tear sheet" cùng một lúc.

# Defining a universe

Như thường lệ, chúng ta cần định nghĩa universe của mình. Trong trường hợp này, chúng ta sử dụng một phiên bản đơn giản hóa của universe **TradableStocksUS**, không bao gồm bộ lọc Market Cap (để giảm sự phụ thuộc vào dữ liệu trong bài giảng này). Các quy tắc universe được chia thành một biến **initial_universe** gồm các trường thông tin chính của chứng khoán và một biến **screen** bao gồm tất cả các quy tắc khác. Việc định nghĩa một **initial_universe** giới hạn universe tính toán của pipeline, từ đó giúp nó chạy nhanh hơn so với việc đặt tất cả các quy tắc trong **screen**. Xem **Pipeline Tutorial** để biết thêm thông tin chi tiết về sự khác biệt giữa **initial_universe** và **screen**.

```python
initial_universe =  (
    # common stocks only
    master.SecuritiesMaster.usstock_SecurityType2.latest.eq("Common Stock")
    # primary share only
    & master.SecuritiesMaster.usstock_PrimaryShareSid.latest.isnull()
)

screen = (
    # dollar volume over $2.5M over trailing 200 days
    (AverageDollarVolume(window_length=200) >= 2.5e6)
    # price > $5
    & (EquityPricing.close.latest > 5)
    # no missing data for 200 days (exclude trading halts, IPOs, etc.)
    & EquityPricing.close.all_present(window_length=200)
    & (EquityPricing.volume.latest > 0).all(window_length=200)
)
```

# Getting Data

Bây giờ chúng ta sẽ lấy các giá trị cho yếu tố của mình đối với tất cả các cổ phiếu trong universe bằng cách sử dụng Pipeline. Chúng ta cũng muốn đảm bảo rằng mình có mã ngành (sector code) cho từng cổ phiếu riêng lẻ, vì vậy chúng ta thêm **Sector** như một yếu tố khác vào Pipeline. Lưu ý rằng việc chạy Pipeline có thể mất một khoảng thời gian.

```python
pipe = Pipeline(
    columns = {
        'momentum': momentum,
        'sector': master.SecuritiesMaster.usstock_Sector.latest
    },
    initial_universe=initial_universe,
    screen=screen
)

results = run_pipeline(pipe, start_date='2010-01-01', end_date='2011-01-01', bundle='usstock-learn-1d')
```

Cùng xem data mà chúng ta nhận được

```python
my_factor = results['momentum']
print(my_factor.head())
```

![alt text](image-3.png)

Biến **my_factor** của chúng ta chứa một **pandas Series** với giá trị yếu tố cho từng cổ phiếu trong universe tại mỗi thời điểm. 

Ở đây, chúng ta tạo một **Series** khác chứa thông tin về ngành (sector) cho từng cổ phiếu thay vì các giá trị yếu tố. Đây là dữ liệu phân loại mà chúng ta sẽ sử dụng như một tham số cho **Alphalens** sau này.

```python
sectors = results['sector']
```

# Alphalens Components

Bây giờ, khi chúng ta đã có các thành phần cơ bản cần thiết để phân tích yếu tố, chúng ta có thể bắt đầu làm việc với **Alphalens**. Lưu ý rằng chúng ta sẽ tách các thành phần riêng lẻ của gói, vì vậy đây không phải là quy trình làm việc điển hình khi sử dụng một "tear sheet" của Alphalens. Quy trình làm việc điển hình được trình bày ở cuối sổ ghi chú.

Đầu tiên, chúng ta tính toán lợi nhuận kỳ vọng (*forward returns*). Lợi nhuận kỳ vọng là lợi nhuận mà chúng ta sẽ nhận được nếu nắm giữ từng chứng khoán trong khoảng thời gian tính theo ngày, kết thúc tại ngày đã cho, được truyền qua tham số **periods**. Trong trường hợp này, chúng ta xem xét các khoảng thời gian 1, 5 và 10 ngày trong tương lai. Chúng ta có thể xem điều này như một bài *budget backtest*. "Tear sheet" không tính đến bất kỳ chi phí hoa hồng hay độ trượt giá nào; thay vào đó, nó chỉ xem xét các giá trị như thể chúng ta đã nắm giữ các cổ phiếu được chỉ định trong số ngày cụ thể đến ngày hiện tại.

```python
periods = [1, 5, 10]
forward_returns = get_forward_returns(my_factor, periods=periods, bundle="usstock-learn-1d")
```

Tiếp theo, chúng ta chuyển dữ liệu yếu tố và lợi nhuận kỳ vọng (*forward returns*) vào Alphalens:

```python
factor_data = al.utils.get_clean_factor(
    my_factor,
    forward_returns,
    groupby=sectors
)
```

![alt text](image-4.png)

Biến `factor_data` ở đây tương tự như biến `my_factor` ở trên. Nó có giá trị yếu tố cho từng cổ phiếu trong universe của chúng ta tại mỗi thời điểm. Hàm `Alphalens` của chúng ta ở đây cũng cung cấp một nhóm phân loại theo ngành đi kèm với giá trị yếu tố.

```
factor_data.head()
```

![alt text](image-5.png)

Như đã giải thích ở trên, lợi nhuận kỳ vọng (forward returns) là lợi nhuận mà chúng ta sẽ nhận được nếu nắm giữ từng chứng khoán trong số ngày được chỉ định, kết thúc vào ngày đã cho. Những lợi nhuận này cũng được phân chia theo ngành.

Hàm này cũng phân loại yếu tố của chúng ta vào các phần vị (quantiles) cho mỗi ngày, thay thế giá trị yếu tố bằng phần vị phù hợp vào một ngày nhất định. Vì chúng ta sẽ nắm giữ các nhóm cổ phiếu thuộc phần vị cao nhất và thấp nhất, chúng ta chỉ quan tâm đến yếu tố này khi nó liên quan đến sự dịch chuyển vào và ra khỏi các nhóm này.

**Alphalens** cung cấp bốn loại phân tích trên các yếu tố alpha:

- Phân bố Yếu tố (Factor Distribution)
- Lợi nhuận (Returns)
- Thông tin (Information)
- Tỷ lệ thay đổi (Turnover)

Mỗi chủ đề này được trình bày trong một "tear sheet" riêng biệt cũng như trong một "tear sheet" đầy đủ bao quát toàn bộ.

# Factor Distribution Table

Một "tear sheet" đầy đủ bắt đầu với một bảng thống kê mô tả sự phân bố của các giá trị yếu tố. Bảng này có thể được hiển thị riêng bằng đoạn mã sau:

```python
al.plotting.plot_factor_distribution_table(factor_data)
```

![alt text](image-6.png)

Bảng bao gồm một hàng cho mỗi phần vị (quantile) của yếu tố. Theo mặc định, các yếu tố được chia thành 5 phần vị có kích thước bằng nhau; điều này có thể được thay đổi bằng cách sử dụng tham số `quantiles` trong hàm `get_clean_factor` (hoặc sử dụng các hàm phổ biến hơn được trình bày sau trong sổ ghi chú).

Đối với mỗi phần vị, chúng ta sẽ thấy giá trị nhỏ nhất, lớn nhất, trung bình và độ lệch chuẩn của các giá trị yếu tố. Điều này cung cấp cho chúng ta một cái nhìn tổng quan về việc các giá trị yếu tố kết thúc ở phần vị nào.

Chúng ta cũng có thể xem tổng số lượng giá trị trong mỗi phần vị cho toàn bộ phân tích, số lượng trung bình hàng ngày trên mỗi phần vị và tỷ lệ phần trăm trên mỗi phần vị. Ở đây, vì chúng ta sử dụng phần vị có kích thước bằng nhau (tùy chọn mặc định), nên số lượng là giống nhau cho mỗi phần vị. Ngoài ra, chúng ta có thể chỉ định tham số `bins` cho hàm `get_clean_factor` (hoặc sử dụng các hàm phổ biến hơn được trình bày sau trong sổ ghi chú) thay vì `quantiles`. Việc sử dụng tham số `bins` sẽ tạo ra các phần vị có chiều rộng bằng nhau (được phân cách theo phạm vi tổng thể của các giá trị yếu tố) thay vì các phần vị có kích thước bằng nhau. Trong trường hợp đó, số lượng thường sẽ khác nhau giữa các phần vị.

# Returns Tear Sheet

Nếu chúng ta chỉ quan tâm đến lợi nhuận, chúng ta có thể tạo một "tear sheet" chỉ chứa phân tích lợi nhuận. Đoạn mã sau đây tạo ra tất cả các biểu đồ lợi nhuận của chúng ta sau khi đã lưu trữ dữ liệu lợi nhuận kỳ vọng (forward returns):

```python
al.tears.create_returns_tear_sheet(factor_data, by_group=True);
```

![alt text](image-7.png)

![alt text](image-8.png)

![alt text](image-9.png)

# Returns Tear Sheet Breakdown

### \( \alpha \) and \( \beta \) Point Estimates Table
"Tear sheet" tính toán \( \alpha \) và \( \beta \) của yếu tố của chúng ta so với thị trường. Các giá trị này được tính bằng cách tạo một hồi quy (regression) của lợi nhuận thị trường trong mỗi giai đoạn so với một danh mục yếu tố long-short và trích xuất các tham số. Các giá trị này biểu thị lợi nhuận vượt mức liên quan đến yếu tố của chúng ta và hệ số beta của thị trường, tương ứng.

### Returns Point Estimates Table
Các ước lượng điểm này cũng được tính toán mà không quan tâm đến việc phân nhóm theo ngành, vì vậy chúng cung cấp cho chúng ta một cái nhìn tổng quan về việc chênh lệch (spread) của chúng ta sẽ trông như thế nào nếu chúng ta giao dịch yếu tố này bằng một thuật toán *long-short equity* mà không xem xét lợi nhuận đến từ các ngành nào.

### Mean Relative Return by Factor Quantile
Yếu tố đã được phân vị (quantized factor) được sử dụng để tạo ra các nhóm riêng biệt, với lợi nhuận cho mỗi nhóm được tính toán theo từng khoảng thời gian ngày. Chúng ta nhận được thông tin này thông qua các biểu đồ cột và biểu đồ violin.

Những biểu đồ này cung cấp một tóm tắt đơn giản nhất về giá trị dự đoán của yếu tố. Đối với một yếu tố có tính dự đoán, chúng ta muốn thấy lợi nhuận trung bình tăng dần (hoặc giảm dần) một cách đơn điệu theo các phần vị từ trái sang phải.

Biểu đồ cột cung cấp lợi nhuận trung bình cho mỗi phần vị yếu tố, theo từng khung thời gian. Điều này mang lại cho chúng ta một tập hợp các ước lượng điểm để hiểu sơ bộ về cách giá trị yếu tố tương quan với lợi nhuận.

Sự khác biệt chính giữa biểu đồ cột và biểu đồ violin là biểu đồ violin cho thấy mật độ dữ liệu của chúng ta. Biểu đồ violin càng "mập", mật độ lợi nhuận ở vùng đó càng cao. Tại đây, chúng ta biểu diễn các biểu đồ violin cho lợi nhuận kỳ vọng trong 1, 5 và 10 ngày đối với từng phần vị.

### Factor-Weighted Long/Short Portfolio Cumulative Return

