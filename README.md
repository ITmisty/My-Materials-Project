Materials-Data-Explorer
利用 Python 與 Materials Project API 進行材料篩選與視覺化。

專案簡介
利用 `pymatgen` 串接 Materials Project 資料庫，自動化獲取材料的熱力學穩定性、能帶結構及空間群資訊，並進行初步的數據篩選。

技術棧 (Tech Stack)
- 程式語言: Python 3.14
- 核心庫: `mp-api`, `pymatgen`, `pandas`
- 視覺化: `py3Dmol` (3D 晶體模擬)

核心功能
1. 單一材料視覺化: 輸入 MP-ID 即可生成互動式 3D 晶格模型。
2. 批量性質對比: 一次抓取多元體系的材料性質（如 Li-Fe-O 系統）。
3. 穩定性篩選: 自動計算 $E_{above\_hull}$ 並標記穩定相。

實驗結果
以下為 Li-Fe-O 體系中穩定性前 5 名的材料數據：

| 化學式 | 能隙 (eV) | 密度 (g/cm³) | 穩定性 (E_hull) |
| :--- | :--- | :--- | :--- |
| LiFe5O8 | 0.00 | 4.29 | 0.000 |
| LiFeO2 | 2.10 | 4.35 | 0.000 |

晶體展示
以下為利用 `py3Dmol` 生成的互動式晶體模型截圖。利用 HTML 表格，我們可以整齊地比較不同的結構體系。

<table width="100%" cellspacing="0" cellpadding="5">
  <tr>
    <td align="center"><strong>純鋁 (Al) - FCC 結構</strong></td>
    <td align="center"><strong>氮化鎵 (GaN) - Wurtzite 結構</strong></td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <img src="Al_structure.png" alt="Aluminum Structure" width="100%">
    </td>
    <td align="center" valign="top">
      <img src="GaN_structure.png" alt="GaN Structure" width="100%">
    </td>
  </tr>
  <tr>
    <td align="center" valign="top">
      <p><em>Materials Project ID: mp-134</em></p>
    </td>
    <td align="center" valign="top">
      <p><em>Materials Project ID: mp-804</em></p>
    </td>
  </tr>
</table>



