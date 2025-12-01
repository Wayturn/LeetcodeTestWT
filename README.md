# LeetCode 刷題攻略

## 🔥 1. HashMap 系列（最常用）
* **用途**：Two Sum 系、字數統計、差值、前綴和、找 complement、記錄看過什麼。
* **建議**：8～10 題（刷法：兩題 easy → 三題 medium → 一兩題 tricky）
* **重點**：HashMap 真的不用刷多，重點是 pattern 要熟。

### 代表題：
- Two Sum
- Subarray Sum Equals K
- Longest Substring Without Repeating Characters（HashMap + Sliding Window）
- Group Anagrams
- Valid Anagram
- 3Sum（HashMap + 排序思維）
- 4Sum（延伸即可，不強迫）

---

## 🔥 2. Two Pointers / Sliding Window 系列
* **說明**：一般後端工程師最常遇到的題目類型之一。
* **建議**：8～12 題（Sliding Window 一開始會卡一下，但一熟就一路通）

### 代表題：
- Longest Substring Without Repeating Characters（超必刷）
- Minimum Window Substring（經典大題）
- Two Sum II（排序後）
- 3Sum（真實考試超常出）
- Trapping Rain Water（高階，但很重要）
- Container With Most Water（pattern 很明顯）

---

## 🔥 3. Binary Search 系列
* **說明**：你不用刷很多，只要會辨識「這題根本不是找值，是找區間」。
* **建議**：5～7 題
* **重點**：這類型其實很看「邏輯乾不乾淨」，你問題解析能力夠就會做。

### 代表題：
- Binary Search（基礎）
- Search in Rotated Sorted Array（經典）
- Find Peak Element
- Find Minimum in Rotated Sorted Array

---

## 🔥 4. Linked List 系列
* **說明**：後端偶爾會遇到，但面試還是很常出。
* **建議**：5～7 題（不用多）
* **重點**：Linked list 全都是「指標思維」，五六題就能看懂 90%。

### 代表題：
- Reverse Linked List
- Merge Two Sorted Lists
- Remove N-th Node From End
- Linked List Cycle
- Add Two Numbers（Big hit）

---

## 🔥 5. Binary Tree / DFS / BFS 系列
* **說明**：這是你未來會需要的（FastAPI、後端、資料結構都會碰到）。
* **建議**：10 題左右
* **重點**：這一類的難度靠「遞迴直覺」，不是刷題量。

### 代表題：
- Maximum Depth of Binary Tree（DFS）
- Balanced Binary Tree
- Path Sum
- Binary Tree Level Order Traversal（BFS）
- Validate BST
- Lowest Common Ancestor（LCA 熱門）

---

## 🔥 6. Dynamic Programming（DP）系列
* **說明**：大魔王區。但後端工作面試其實不會考很深，只考常見幾題。
* **建議**：5～8 題（把 pattern 建起來，超過就沒必要強刷）
* **重點**：DP 的關鍵不在於題量，而在於「寫得出遞推式」。

### 代表題：
- Climbing Stairs（DP Hello World）
- House Robber
- House Robber II
- Maximum Subarray（其實是 DP）
- Longest Increasing Subsequence（LIS）
- Coin Change

---

## 🔥 7. Greedy 系列
* **說明**：很少面試考，但你做產品會用到邏輯。
* **建議**：3～5 題

### 代表題：
- Jump Game
- Jump Game II
- Gas Station

---

## 📌 整體統計：你要刷多少題？

| 類型 | 建議題數 |
| :--- | :--- |
| HashMap | 8–10 |
| Sliding Window | 8–12 |
| Two Pointers | 5–8 |
| Binary Search | 5–7 |
| Linked List | 5–7 |
| Tree / DFS / BFS | 10 |
| DP | 5–8 |
| Greedy | 3–5 |

➡ **總計**：大概 45～60 題 = 後端工程師「可面試」等級。

---

## 🔥 最推薦順序（從簡單 → 建直覺 → 再疊難度）

### 第 1 階段：HashMap 核心（最基礎的基礎）
這階段可以讓你完全熟悉：complement 思維、「看過什麼？」邏輯、dict 存 key/value 的 pattern。
* **順序**：
  1. Two Sum（DONE！）
  2. Valid Anagram
  3. Group Anagrams
  4. Two Sum II（變形題）
  5. Subarray Sum Equals K（HashMap 高配版）

### 第 2 階段：Sliding Window（你以後會超常用）
Sliding Window 是你未來工作最容易碰到的：字串處理、Token 過期、API 節流。
* **順序**：
  1. Longest Substring Without Repeating Characters（經典）
  2. Longest Repeating Character Replacement
  3. Minimum Window Substring（進階大題）
  4. Sliding Window Maximum

### 第 3 階段：Two Pointers（會讓你看題目更快）
這系列很好練習排序後的邏輯。
* **順序**：
  1. 3Sum
  2. Container With Most Water
  3. Trapping Rain Water（中高階但超值得）

### 第 4 階段：Binary Search（超常被問）
這是後端職缺面試必考。一定要懂「我不是找值，我是在找條件成立的邊界」。
* **順序**：
  1. Binary Search（基本）
  2. Search in Rotated Sorted Array
  3. Find Minimum in Rotated Sorted Array
  4. Find Peak Element

### 第 5 階段：Linked List（面試最容易出）
5 題就能搞定 90% 的 Linked List 題。
* **順序**：
  1. Reverse Linked List
  2. Merge Two Sorted Lists
  3. Linked List Cycle
  4. Remove N-th Node From End
  5. Add Two Numbers（中階）

### 第 6 階段：DFS / BFS（後端偶爾會問）
這類型讓你對資料結構更有感覺。
* **順序**：
  1. Maximum Depth of Binary Tree
  2. Binary Tree Level Order Traversal
  3. Path Sum
  4. Validate BST
  5. Lowest Common Ancestor（稍微難，但超常考）

### 第 7 階段：Dynamic Programming（5 題就夠）
這階段讓你熟悉遞推。只要抓到：狀態、過去影響未來、最佳化、重複子問題。
* **順序**：
  1. Climbing Stairs
  2. House Robber
  3. Maximum Subarray（DP disguised as greedy）
  4. Coin Change
  5. Longest Increasing Subsequence (LIS)

---

## 🎯 最後 → 把順序壓縮成一條路線

**🧩 全序列（從最容易 → 最難）**
`HashMap` → `Sliding Window` → `Two Pointers` → `Binary Search` → `Linked List` → `Tree(DFS/BFS)` → `DP`

這條順序的好處：
1. 你每個階段都能立即感受到「變強」
2. 不會卡關，也不會覺得刷題很痛苦
3. 工作面試最常考的題型都排前面
4. 很符合你「專案驅動、要看到成效」的習慣
