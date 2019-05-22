# HW4 - ETF measurements comparison


## 小組成員
第12組
- R07723032 黃郁珺
- B06902033 黃奕鈞
- B06902106 宋岩叡


## ETF
共66檔ETF
XLB, IYM, IGE, VAW, PKB, XHB, ITB, GDX, XME, MXI, PYZ, SLX, RTM, UYM, SMN, FXZ, MOO, CUT, WOOD, HAP, PSAU, PAGG, FLM, GRES, GDXJ, CHIM, FTRI, FTAG, SBM, PSCM, SIL, COPX, LIT, GNR, REMX, GOEX, URA, NUGT, DUST, CROP, SOIL, GUNR, PICK, RING, SLVP, VEGI, SILJ, JNUG, JDST, FMAT, SGDM, GDXX, GDXS, HOML, SGDJ, NAIL, NANR, VOX, ERUS, IYZ, FCOM, IXP, XTL, WBIF, FONE, LTL


## Source
Yahoo finance

## 指標類型
* Sharpe ratio
* Omega
* Riskiness

計算方式： 下載ETF的5年歷史資料，利用rolling window的方式，以3年時間計算以上三指標（156 w or 36 m）

## 績效評比
以Omega月資料為範例

績效資料:
![績效](/pic/mOmega.png)

#### 不同指標結果

* Omega月資料排名
![Omega月資料排名](/pic/mOmega_rank.png)

以XLB此檔ETF作為範例畫出Omega月資料排名狀況
![Omega月資料排名圖表](/pic/mOmega_rank_plot.png)
Omega值與ASKSR值的排名狀況，可發現以兩者比率進行報酬排名的差異性大
![月資料排名比較圖表](/pic/mm_comparison.png)


週排名狀況
![Omega週資料排名圖表](/pic/mOmega_rank_plot.png)

可看出投資標的的排名變動幅度大

#### 週資料 vs. 月資料


## 投資策略
* 可藉由前一期的績效評比決定本期投資標的，如以績效最好的前10檔基金組成投組進行投資。但須每期調整，月資料較為合適
* 視長期表現最佳的ETF決定投資標的，也可以最好的幾檔基金作為投組。

而投資策略的共同問題皆為前一期報酬最高不一定代表本期報酬好，須特別留意