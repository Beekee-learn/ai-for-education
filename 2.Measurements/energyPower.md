Energy and Power
---
In the charts that follow, we examine the power consumption during the inference process across various configurations. Notably, the --mlock and --no-mmap options appear to have a minimal effect on energy use.

Interestingly, it is observed that the 4-bit model uses less power than the 2-bit model. This reduction in energy consumption may be attributed to data transfers that potentially slow down the CPUs, leading to lower energy costs.

![energy_1](images/nrg_img1.png)
![energy_2](images/nrg_img2.png)
![energy_3](images/nrg_img3.png)
![energy_4](images/nrg_img4.png)
