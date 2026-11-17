# カーブ形状のグラスサイドバー（Arastoo）

- 出典：Instagram @code.xr（Arastoo）のリール「Curved Sidebar UI」（2026-11-15投稿）
  - https://www.instagram.com/reel/Dfw4gEmz87N/
  - 内容は動画解析で確認。実装は React.js / CSS3 / HTML5、ソースコードは「Code」コメントで配布の形式
- 関連：notes/2026-11-08-glassy-sidebar-v7-arastoo.md（同じ作者のサイドバーだが、こちらはフローティング型ピル→ランチャーの3段階展開で別物）、notes/2026-11-02-collapsible-sidebar-upgrade.md（@designcodewithav の折りたたみサイドバー、別物）

## 中身

- 暗い波形の抽象背景の左端に立つ、半透明の細いサイドバー。上部アイコン「Expand」にホバー／クリックすると、バーがスムーズに横へ広がってフルメニューになる
- テーマは紫＆黒。グラスモーフィズムに「カーブ（曲面）」の造形を組み合わせ、境界には紫のグロー
- 展開後の構成（アプリ名は「LUMEN」）：
  - プロフィール欄（Nova PRO、ID 表示つき）
  - MENU：Bookings、Upcoming、Calendar、History、Services、Profile、Memberships、Earnings、Share & Grow、Analytics（入れ子ナビゲーション）
  - 「NOTICE」カード（クリスタルのグラフィック入り）
  - 最下部に Settings と Log out
- 画面下部には React のコードエディタが常時表示される、この作者のシリーズ共通の型（LineChart や PieChart の import が見える）

## 学び・所感

- 同じ作者の Glassy SideBar V7 が「ピル→ランチャー→ワークスペース」の段階展開だったのに対し、こちらは通常のドロワー式サイドバーの開閉に、カーブ形状とグロー境界で質感を足した作例。主役は展開方式ではなく「曲面ガラス」という造形
- プロフィール＋プラン表示（PRO）をサイドバー上部に置く構成は、SaaS 系ダッシュボードの定番レイアウト
- 新しい用語・技法の提示はないため、図鑑カードは追加せずノートのみ（同作者のダッシュボード／サイドバー変種の先例どおり）
