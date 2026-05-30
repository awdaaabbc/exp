# Output 文件夹说明

本目录包含所有实验的输出结果，包括模型权重、训练日志、配置文件、混淆矩阵和统计分析结果。

---

## 目录结构

```
output/
├── HGD/                          # HGD 数据集实验结果
├── bci_iv_2a/                    # BCI IV-2a 数据集实验结果
├── bci_iv_2a_500/                # BCI IV-2a 500Hz 采样率实验
├── bci_iv_2a_cltnet_500/         # BCI IV-2a CLTNet 对比实验
├── bci_iv_2b/                    # BCI IV-2b 数据集实验结果
├── openbmi/                      # OpenBMI 数据集实验结果
├── openbmi_baselines/            # OpenBMI 基线模型对比实验
├── confusion_matrices/           # 混淆矩阵可视化结果
── hgd_ablation/                 # HGD 消融实验结果
├── hgdttt/                       # HGD 测试实验结果
├── baseline_compare/             # 基线模型对比实验
├── tuning_temp/                  # 临时调参实验
├── tuning_temp_bci2b/            # BCI-2b 临时调参实验
└── model3_p_values_summary_all_datasets.txt  # 所有数据集 p 值汇总
```

---

## 详细说明

### 1. HGD/ - HGD 数据集实验

HGD（High Gamma Dataset）数据集包含 14 名受试者的运动想象 EEG 数据，4 分类任务。

#### Model3_Yuan/
原始 Model3 模型在 HGD 数据集上的训练结果。
- **结构**: `sub{1-14}/{timestamp}/`
- **内容**: `config.yaml`（配置文件）、`log_result_*.txt`（训练日志）、`model.pth`（模型权重）
- **受试者**: sub1 - sub14

#### Model3_withoutDynamic/
移除动态卷积模块的消融实验结果。
- **受试者**: sub1 - sub14

#### Model3_withoutFreq/
移除频带注意力模块的消融实验结果。
- **受试者**: sub1 - sub14

#### Model3_withoutLastStep/
移除最后一个时间步的消融实验结果。
- **受试者**: sub1 - sub14

#### hgd_model3_subject_results.md
HGD 数据集各受试者的实验结果汇总文档。

---

### 2. bci_iv_2a/ - BCI IV-2a 数据集实验

BCI Competition IV 2a 数据集，包含 9 名受试者，4 分类运动想象任务。

#### loso_experiment/
Leave-One-Subject-Out 交叉验证实验结果。
- **文件**: `results.txt`

#### sensitivity_experts_{1,2,4,5}/
不同专家数量的敏感性分析实验。

#### sensitivity_freq_{balanced,default,high_focus,low_focus}/
频带注意力不同配置的敏感性分析。

#### sensitivity_no_dynamic_conv/
移除动态卷积的敏感性分析。

#### 最佳日志/
最优实验配置的日志记录。

#### sensitivity_summary_freq.txt
频带敏感性分析汇总。

---

### 3. bci_iv_2a_500/ - BCI IV-2a 500Hz 实验

500Hz 采样率下的 CLTNet 模型实验结果。
- **结构**: `CLTNet/results.txt`

---

### 4. bci_iv_2a_cltnet_500/ - BCI IV-2a CLTNet 对比

CLTNet 基线模型在 BCI IV-2a 上的对比实验。
- **结构**: `CLTNet/results.txt`

---

### 5. bci_iv_2b/ - BCI IV-2b 数据集实验

BCI Competition IV 2b 数据集，包含 9 名受试者，2 分类运动想象任务。

#### Model3/
原始 Model3 模型训练结果。
- **结构**: `sub{1-9}/{timestamp}/`
- **内容**: `config.yaml`、`log_result.txt`

#### Model3_withoutDynamic/
移除动态卷积的消融实验。
- **受试者**: sub1 - sub9

#### Model3_withoutFreq/
移除频带注意力的消融实验。
- **受试者**: sub1 - sub9

#### Model3_withoutTCN/
移除 TCN 模块的消融实验。
- **受试者**: sub1 - sub9

---

### 6. openbmi/ - OpenBMI 数据集实验

OpenBMI 数据集，包含多个受试者的运动想象 EEG 数据，2 分类任务。

#### sub{1-18}/
各受试者的训练日志。
- **文件**: `log_result.txt`、`log_result_*.txt`

---

### 7. openbmi_baselines/ - OpenBMI 基线对比

OpenBMI 数据集上基线模型的对比实验结果。
- **结构**: `run_{timestamp}/summary.txt`
- **内容**: 各基线模型的汇总结果

---

### 8. confusion_matrices/ - 混淆矩阵

各数据集、模型、受试者的混淆矩阵可视化结果。

#### hgd/
HGD 数据集的混淆矩阵。
- **命名格式**: `hgd_sub{XX}_Model3.png` 和 `hgd_sub{XX}_Model3.txt`
- **内容**: 
  - `.png`: 混淆矩阵热力图
  - `.txt`: 包含 TP、TN、FP、FN 等详细指标

---

### 9. hgd_ablation/ - HGD 消融实验

HGD 数据集消融实验的详细结果。

#### Model3/
原始模型各受试者的训练配置。

#### summary_Model3.txt / summary_Model3_withoutDynamic.txt
消融实验结果汇总文件。

---

### 10. hgdttt/ - HGD 测试实验

HGD 数据集的测试和可视化结果。
- `ablation_comparison.png/txt`: 消融实验对比图和数据
- `hgd_0512_summary_*.md`: 实验结果汇总文档
- `model3_hgd_summary.txt`: Model3 在 HGD 上的汇总
- `summary_Model3*.txt`: 各模型的汇总结果

---

### 11. baseline_compare/ - 基线模型对比

基线模型对比实验的统计结果。
- **结构**: `run_{timestamp}/p_values.txt`
- **内容**: 各模型之间的 p 值统计

---

### 12. tuning_temp/ - 临时调参实验

临时参数调优实验的日志记录。
- **文件**: `log_result.txt`

---

### 13. tuning_temp_bci2b/ - BCI-2b 临时调参

BCI IV-2b 数据集的临时参数调优实验。
- **文件**: `log_result.txt`

---

### 14. model3_p_values_summary_all_datasets.txt

所有数据集上 Model3 模型的 p 值统计汇总文件，用于显著性检验。

---

## 文件说明

### config.yaml
每次实验的配置文件，包含：
- 超参数（学习率、batch size、epochs 等）
- 模型配置（通道数、类别数等）
- 设备配置（GPU/CPU）

### log_result_*.txt
训练日志文件，包含：
- 每个 epoch 的训练/测试损失和准确率
- Kappa 系数、F1 分数等指标
- 最佳准确率记录
- 训练时间和 ETA

### model.pth
训练保存的模型权重文件（已排除在 git 之外）。

### results.txt / summary.txt
实验结果汇总文件，包含各受试者的平均性能指标。

---

## 注意事项

1. **模型权重文件**（`.pth`）由于体积较大，已添加到 `.gitignore` 中，未上传至 GitHub。
2. 每个受试者的实验结果保存在独立的时间戳文件夹中，便于追溯实验历史。
3. 消融实验文件夹命名规则：`Model3_{移除的组件}`，如 `Model3_withoutDynamic` 表示移除动态卷积模块。
